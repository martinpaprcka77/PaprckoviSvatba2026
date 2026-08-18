#!/usr/bin/env python3
"""Update the marker-driven statistic sections of README.md from data/*.csv.

Only content between `<!-- NAME_START -->` / `<!-- NAME_END -->` markers is
touched; everything else in README.md is preserved. The CSV files stay the
single source of truth — this script never modifies them.

Modes:
  python update-readme.py            update docs (backup + write + show diff)
  python update-readme.py --check-only   exit 0 if in sync, 1 if not (no write)
  python update-readme.py --dry-run      preview the diff without writing
  python update-readme.py --ci-check     check-only with GitHub Actions output
"""

import argparse
import csv
import difflib
import importlib.util
import os
import re
import shutil
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
BACKUP_PATH = os.path.join(REPO_ROOT, "README.md.bak")

# Marker blocks handled by this updater, in README display order.
BLOCK_NAMES = [
    "TASK_STATS",
    "TASK_CATEGORIES",
    "BUDGET",
    "GUESTS",
    "COMPLETED_TASKS",
    "OPEN_TASKS",
]

_CATEGORY_LABELS = {
    "mandatory": "🔴 Povinné",
    "important": "🟡 Důležité",
    "optional": "🟢 Volitelné",
}


def _load_extract_stats():
    """Import the hyphenated sibling module scripts/extract-stats.py."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "extract-stats.py")
    spec = importlib.util.spec_from_file_location("extract_stats", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _fmt(n: int) -> str:
    """Czech-style thousands separator: 89500 -> '89 500'."""
    return f"{n:,}".replace(",", " ")


def _read_tasks():
    """Tasks sorted by id for deterministic title lists."""
    path = os.path.join(REPO_ROOT, "data", "tasks.csv")
    tasks = []
    with open(path, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("id"):
                tasks.append(row)
    tasks.sort(key=lambda t: t["id"])
    return tasks


def render_blocks(es, tasks):
    """Render the current README stat content for every marker block.

    The README tracks a small set of summary blocks (task counts, guest totals,
    planned spending, and current task titles). This helper converts live CSV
    stats into the exact markdown fragment used by each marker block.

    Args:
        es: The extracted statistics module exposing summary helpers.
        tasks: Ordered task rows read from ``data/tasks.csv``.

    Returns:
        dict: Mapping of marker names to markdown block bodies.
    """
    t = es.get_task_stats()
    b = es.get_budget_stats()
    g = es.get_guest_stats()
    d = es.get_latest_dates()

    blocks = {}

    blocks["TASK_STATS"] = (
        f"✅ **{t['completed']}/{t['total']} splněno** · "
        f"💰 **{_fmt(b['planned_total'])} / {_fmt(b['cap'])} Kč naplánováno** "
        f"({_fmt(b['actual_total'])} Kč utraceno) · "
        f"🧑 **{g['total']} hostů** ({g['confirmed']} potvrzeno) · "
        f"📅 změny do {d['latest_changelog']}"
    )

    rows = ["| Kategorie | Úkolů | Plán | Skutečnost |", "|---|---|---|---|"]
    for key, label in _CATEGORY_LABELS.items():
        rows.append(
            f"| {label} | {t['by_category'][key]} | "
            f"{_fmt(b['by_category'][key]['planned'])} Kč | "
            f"{_fmt(b['by_category'][key]['actual'])} Kč |"
        )
    rows.append(
        f"| **Celkem** | **{t['total']}** | **{_fmt(b['planned_total'])} Kč** | "
        f"**{_fmt(b['actual_total'])} Kč** |"
    )
    blocks["TASK_CATEGORIES"] = "\n".join(rows)

    blocks["BUDGET"] = "\n".join(
        [
            f"- plán: **{_fmt(b['planned_total'])} Kč**",
            f"- skutečnost: **{_fmt(b['actual_total'])} Kč**",
            f"- rezerva proti limitu podle plánu: **{_fmt(b['reserve'])} Kč**",
        ]
    )

    blocks["GUESTS"] = "\n".join(
        [
            f"- hosté celkem: **{g['total']}**",
            f"- potvrzeno: **{g['confirmed']}**",
        ]
    )

    def titles(status):
        return [t2["title"].strip() for t2 in tasks if t2["status"].strip().lower() == status]

    done, open_ = titles("done"), titles("open")
    blocks["COMPLETED_TASKS"] = f"**Hotovo ({len(done)}):** " + " · ".join(done)
    blocks["OPEN_TASKS"] = f"**Otevřeno ({len(open_)}):** " + " · ".join(open_)

    return blocks


_MARKER_RE = re.compile(
    r"<!-- (?P<name>[A-Z_]+)_START -->\n(?P<body>.*?)\n<!-- (?P=name)_END -->",
    re.DOTALL,
)


def _as_block(name: str, body: str) -> str:
    return f"<!-- {name}_START -->\n{body}\n<!-- {name}_END -->"


def apply_blocks(content: str, blocks) -> tuple:
    """Replace or insert marker blocks inside ``README.md``.

    The updater only edits content between ``<!-- NAME_START -->`` and
    ``<!-- NAME_END -->`` markers, leaving the rest of the README untouched.

    Args:
        content: Full README markdown text.
        blocks: Mapping of marker names to replacement bodies.

    Returns:
        tuple: ``(new_content, changed_names, inserted_names)``.
    """
    changed = []
    inserted = []

    def replace(match):
        name = match.group("name")
        if name not in blocks:
            return match.group(0)
        new_block = _as_block(name, blocks[name])
        if new_block != match.group(0):
            changed.append(name)
        return new_block

    new_content = _MARKER_RE.sub(replace, content)

    # Insert missing blocks (first-time setup) before the first existing
    # marker block, or at the end of the file if none exist yet.
    present = {m.group("name") for m in _MARKER_RE.finditer(new_content)}
    missing = [name for name in BLOCK_NAMES if name not in present]
    if missing:
        block_text = "\n\n".join(_as_block(n, blocks[n]) for n in missing)
        first = _MARKER_RE.search(new_content)
        if first:
            anchor = first.group(0)
            new_content = new_content.replace(anchor, block_text + "\n\n" + anchor, 1)
        else:
            new_content = new_content.rstrip() + "\n\n" + block_text + "\n"
        inserted.extend(missing)

    return new_content, changed, inserted


def main():
    """Sync the README marker blocks from the current CSV data sets.

    The script can run in write, preview, or check-only modes. It validates the
    README against the source-of-truth CSV files and exits with a non-zero code
    when the markers are out of sync.
    """
    parser = argparse.ArgumentParser(description="Sync README.md stats from data/*.csv")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check-only", action="store_true", help="exit 0/1, do not write")
    mode.add_argument("--dry-run", action="store_true", help="show diff, do not write")
    mode.add_argument("--ci-check", action="store_true", help="check-only with GH output")
    args = parser.parse_args()

    es = _load_extract_stats()
    blocks = render_blocks(es, _read_tasks())

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    new_content, changed, inserted = apply_blocks(content, blocks)
    in_sync = not changed and not inserted

    if in_sync:
        print("README.md: v souladu (in sync)")
        return 0

    diff = difflib.unified_diff(
        content.splitlines(), new_content.splitlines(),
        fromfile="README.md", tofile="README.md (synced)",
        lineterm="", n=1,
    )
    diff_text = "\n".join(diff)

    if args.check_only or args.ci_check:
        prefix = "::error file=README.md::" if args.ci_check else ""
        print(f"{prefix}README.md je mimo sync: změněny bloky {', '.join(changed + inserted)}")
        print(diff_text)
        return 1

    if not args.dry_run:
        # Backup + write only when there is something to change.
        shutil.copyfile(README_PATH, BACKUP_PATH)
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"README.md: zapsáno (záloha: {os.path.basename(BACKUP_PATH)})")
    else:
        print("README.md: dry-run, nic nezapsáno")
    print(diff_text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
