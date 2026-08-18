#!/usr/bin/env python3
"""Update the PRD status line and a marker-driven stats + version-history
section from data/*.csv.

- The `> Status: active — ...` line is refreshed from current CSV stats.
- A `## 📊 Stav (auto-sync z data/*.csv)` section (stats block + version
  history table) is appended at the end of the PRD, created on first run.
  Version-history rows are appended only when the recorded stats change
  materially (semi-automatic per the approved design).

The CSV files remain the single source of truth — never modified here.

Modes:
  python update-prd.py            update (backup + write + show diff)
  python update-prd.py --check-only   exit 0 if in sync, 1 if not (no write)
  python update-prd.py --dry-run      preview the diff without writing
  python update-prd.py --ci-check     check-only with GitHub Actions output
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
PRD_PATH = os.path.join(REPO_ROOT, "docs", "PRD-svatba-paprckovi-2026.md")
BACKUP_PATH = os.path.join(REPO_ROOT, "docs", "PRD-svatba-paprckovi-2026.md.bak")

# Marker blocks appended/updated at the end of the PRD.
BLOCK_NAMES = ["PRD_STATS", "PRD_VERSION_HISTORY"]

# The status line is refreshed via this unique pattern (blockquote line).
STATUS_RE = re.compile(r"> Status: active — [^\n]*")


def _load_extract_stats():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "extract-stats.py")
    spec = importlib.util.spec_from_file_location("extract_stats", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _fmt(n: int) -> str:
    return f"{n:,}".replace(",", " ")


def _cz_date(iso_date: str) -> str:
    """2026-07-29 -> '29. 7. 2026' (Czech format)."""
    try:
        year, month, day = iso_date.split("-")
        return f"{int(day)}. {int(month)}. {year}"
    except ValueError:
        return iso_date


def _people_count(es) -> int:
    """Number of distinct assignees in tasks.csv (the 'X osob' figure)."""
    import csv as _csv

    tasks_path = os.path.join(REPO_ROOT, "data", "tasks.csv")
    people = set()
    with open(tasks_path, "r", encoding="utf-8") as f:
        for row in _csv.DictReader(f):
            if row.get("id") and row.get("assign"):
                for name in (a.strip() for a in row["assign"].split(",")):
                    if name:
                        people.add(name)
    return len(people)


def render_status_line(es) -> str:
    """Build the PRD status line from the current CSV-derived metrics.

    Args:
        es: Statistics helper module from ``scripts/extract-stats.py``.

    Returns:
        str: The markdown blockquote used at the top of the PRD.
    """
    t = es.get_task_stats()
    b = es.get_budget_stats()
    g = es.get_guest_stats()
    d = es.get_latest_dates()
    people = _people_count(es)
    return (
        f"> Status: active — {_cz_date(d['latest_changelog'])} "
        f"({t['total']} úkolů, {people} osob, {_fmt(b['planned_total'])} Kč, "
        f"{g['total']} hostů)"
    )


def render_blocks(es) -> dict:
    """Create the PRD sync blocks for stats and version history.

    The function returns a dictionary of markdown blocks used in the PRD.
    ``PRD_STATS`` is the short status summary and ``PRD_VERSION_HISTORY`` keeps
    an append-only history table of the important summary numbers.

    Args:
        es: Statistics helper module from ``scripts/extract-stats.py``.

    Returns:
        dict: Mapping of marker names to rendered markdown bodies.
    """
    t = es.get_task_stats()
    b = es.get_budget_stats()
    g = es.get_guest_stats()
    d = es.get_latest_dates()
    people = _people_count(es)
    date_str = _cz_date(d["latest_changelog"])

    stats_block = (
        f"✅ **{t['completed']}/{t['total']} splněno** · "
        f"💰 **{_fmt(b['planned_total'])} / {_fmt(b['cap'])} Kč naplánováno** "
        f"({_fmt(b['actual_total'])} Kč utraceno) · "
        f"🧑 **{g['total']} hostů** ({g['confirmed']} potvrzeno) · "
        f"👥 **{people} osob** · 📅 změny do {d['latest_changelog']}"
    )

    header = ["| Datum | Úkolů | Splněno | Plán (Kč) | Hostů | Osob |", "|---|---|---|---|---|---|"]
    current_row = f"| {date_str} | {t['total']} | {t['completed']} | {_fmt(b['planned_total'])} | {g['total']} | {people} |"

    history = read_version_history(PRD_PATH)
    history_lines = ["| " + " | ".join(row) + " |" for row in history]
    if not history:
        # First run: seed with the current state as the baseline row.
        rows = header + [current_row]
    else:
        last_row = history[-1][1:]  # [úkoly, splněno, plán, hostů, osob]
        changed = (
            str(t["total"]) != last_row[0]
            or str(t["completed"]) != last_row[1]
            or _fmt(b["planned_total"]) != last_row[2]
            or str(g["total"]) != last_row[3]
            or str(people) != last_row[4]
        )
        if changed:
            rows = header + history_lines + [current_row]
        else:
            rows = header + history_lines

    return {
        "PRD_STATS": stats_block,
        "PRD_VERSION_HISTORY": "\n".join(rows),
    }


def read_version_history(path: str):
    """Parse the version-history table from the PRD.

    Args:
        path: Absolute or repo-relative path to the PRD markdown file.

    Returns:
        list: Rows containing six cells: date, task count, completed count,
        planned budget, guest count, and people count.
    """
    content = _read_file(path)
    match = re.search(
        r"<!-- PRD_VERSION_HISTORY_START -->\n(.*?)\n<!-- PRD_VERSION_HISTORY_END -->",
        content, re.DOTALL,
    )
    if not match:
        return []
    lines = match.group(1).splitlines()
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        # Skip the markdown separator row (|---|---|...) and the header.
        if len(cells) == 6 and cells[0] != "Datum" and not all(re.fullmatch(r"-+", c) for c in cells):
            rows.append(cells)
    return rows


def _read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


_MARKER_RE = re.compile(
    r"<!-- (?P<name>[A-Z_]+)_START -->\n(?P<body>.*?)\n<!-- (?P=name)_END -->",
    re.DOTALL,
)


def _as_block(name: str, body: str) -> str:
    return f"<!-- {name}_START -->\n{body}\n<!-- {name}_END -->"


def apply_blocks(content: str, blocks: dict):
    """Apply the rendered PRD blocks to the document, creating missing sections.

    Args:
        content: Current markdown document.
        blocks: Mapping of marker names to markdown contents.

    Returns:
        tuple: ``(updated_content, changed_names, inserted_names)``.
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

    present = {m.group("name") for m in _MARKER_RE.finditer(new_content)}
    missing = [name for name in BLOCK_NAMES if name not in present]
    if missing:
        block_text = "\n\n".join(_as_block(n, blocks[n]) for n in missing)
        section = f"## 📊 Stav (auto-sync z data/*.csv)\n\n{block_text}\n"
        new_content = new_content.rstrip() + "\n\n" + section
        inserted.extend(missing)

    return new_content, changed, inserted


def main():
    """Sync the PRD status and metrics blocks from the current data files."""
    parser = argparse.ArgumentParser(description="Sync PRD status/stats from data/*.csv")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check-only", action="store_true", help="exit 0/1, do not write")
    mode.add_argument("--dry-run", action="store_true", help="show diff, do not write")
    mode.add_argument("--ci-check", action="store_true", help="check-only with GH output")
    args = parser.parse_args()

    es = _load_extract_stats()
    content = _read_file(PRD_PATH)

    issues = []

    # 1) Status line.
    expected_status = render_status_line(es)
    status_match = STATUS_RE.search(content)
    status_ok = status_match and status_match.group(0) == expected_status
    if not status_ok:
        issues.append("status line")
        if status_match:
            content = STATUS_RE.sub(expected_status, content, count=1)
        else:
            content = content.replace(
                "> Product Requirements Document — 14. 5. 2026",
                "> Product Requirements Document — 14. 5. 2026\n" + expected_status,
                1,
            )

    # 2) Stats block + version history.
    blocks = render_blocks(es)
    new_content, changed, inserted = apply_blocks(content, blocks)
    if changed or inserted:
        issues.extend(changed)
        issues.extend(f"{name} (inserted)" for name in inserted)

    in_sync = not issues

    if in_sync:
        print("PRD: v souladu (in sync)")
        return 0

    diff = difflib.unified_diff(
        _read_file(PRD_PATH).splitlines(), new_content.splitlines(),
        fromfile="PRD.md", tofile="PRD.md (synced)",
        lineterm="", n=1,
    )
    diff_text = "\n".join(diff)

    if args.check_only or args.ci_check:
        prefix = "::error file=docs/PRD-svatba-paprckovi-2026.md::" if args.ci_check else ""
        print(f"{prefix}PRD je mimo sync: {', '.join(issues)}")
        print(diff_text)
        return 1

    if not args.dry_run:
        shutil.copyfile(PRD_PATH, BACKUP_PATH)
        with open(PRD_PATH, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"PRD: zapsáno (záloha: {os.path.basename(BACKUP_PATH)})")
    else:
        print("PRD: dry-run, nic nezapsáno")
    print(diff_text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
