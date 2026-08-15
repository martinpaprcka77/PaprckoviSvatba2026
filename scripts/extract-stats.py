#!/usr/bin/env python3
"""Extract statistics from the wedding planner CSV files.

CSV files in data/ are the single source of truth. This module parses them
and returns structured statistics for the documentation sync system
(README.md / PRD updaters). It never modifies the CSVs.
"""

import csv
import os
import subprocess
from typing import Any, Dict, List

# Hard budget cap, see docs/PRD and CLAUDE.md rule #1.
BUDGET_CAP = 100_000
WEDDING_DATE = "2026-08-29"

# Resolve the repo data directory relative to this file so the module works
# from any cwd (scripts/ lives one level below the repo root).
_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(_REPO_ROOT, "data")


def _read_csv(filename: str) -> List[Dict[str, str]]:
    """Read a CSV from DATA_DIR, skipping blank rows. UTF-8 aware."""
    path = os.path.join(DATA_DIR, filename)
    rows: List[Dict[str, str]] = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                # Skip blank lines: they yield a row with only the None key
                # and no named-column values. Rows whose quoted extra fields
                # land under the None key (e.g. budget.csv B002/B003) are kept.
                if not any(v for k, v in row.items() if k is not None):
                    continue
                rows.append(row)
    except FileNotFoundError:
        # Defensive: caller decides what zero-valued stats mean.
        pass
    return rows


def _int(value: str) -> int:
    """Parse an integer CSV cell defensively (empty / invalid -> 0)."""
    try:
        return int(str(value).strip() or 0)
    except ValueError:
        return 0


def get_task_stats() -> Dict[str, Any]:
    """Task statistics from tasks.csv (id,deadline,title,assign,category,status,note)."""
    stats: Dict[str, Any] = {
        "completed": 0,
        "total": 0,
        "by_category": {"mandatory": 0, "important": 0, "optional": 0},
    }
    for row in _read_csv("tasks.csv"):
        if not row.get("id"):
            continue
        stats["total"] += 1
        status = (row.get("status") or "").strip().lower()
        if status == "done":
            stats["completed"] += 1
        category = (row.get("category") or "").strip().lower()
        if category in stats["by_category"]:
            stats["by_category"][category] += 1
    return stats


def get_budget_stats() -> Dict[str, Any]:
    """Budget statistics from budget.csv (id,item,category,amount_plan,amount_actual,note)."""
    planned_total = 0
    actual_total = 0
    by_category: Dict[str, Dict[str, int]] = {
        "mandatory": {"planned": 0, "actual": 0},
        "important": {"planned": 0, "actual": 0},
        "optional": {"planned": 0, "actual": 0},
    }
    for row in _read_csv("budget.csv"):
        if not row.get("id"):
            continue
        planned = _int(row.get("amount_plan"))
        actual = _int(row.get("amount_actual"))
        planned_total += planned
        actual_total += actual
        category = (row.get("category") or "").strip().lower()
        if category in by_category:
            by_category[category]["planned"] += planned
            by_category[category]["actual"] += actual
    return {
        "planned_total": planned_total,
        "actual_total": actual_total,
        "remaining": planned_total - actual_total,
        "reserve": BUDGET_CAP - planned_total,
        "cap": BUDGET_CAP,
        "by_category": by_category,
    }


def get_guest_stats() -> Dict[str, Any]:
    """Guest statistics from guests.csv (id,name,side,count,confirmed,note).

    count is the number of people per row; totals are sums of count.
    """
    stats: Dict[str, Any] = {
        "total": 0,
        "confirmed": 0,
        "by_side": {"mamka": 0, "tatka": 0, "spolecni": 0},
    }
    for row in _read_csv("guests.csv"):
        if not row.get("id"):
            continue
        count = _int(row.get("count"))
        stats["total"] += count
        confirmed = (row.get("confirmed") or "").strip().lower()
        if confirmed == "confirmed":
            stats["confirmed"] += count
        side = (row.get("side") or "").strip().lower()
        if side in stats["by_side"]:
            stats["by_side"][side] += count
    return stats


def get_latest_dates() -> Dict[str, str]:
    """Latest dates from changelog.csv and done-task deadlines."""
    stats: Dict[str, str] = {
        "wedding_date": WEDDING_DATE,
        "latest_changelog": "",
        "latest_task_completion": "",
    }
    changelog_dates = [
        (row.get("date") or "").strip()
        for row in _read_csv("changelog.csv")
        if row.get("date")
    ]
    if changelog_dates:
        stats["latest_changelog"] = max(changelog_dates)

    completion_dates = [
        (row.get("deadline") or "").strip()
        for row in _read_csv("tasks.csv")
        if row.get("id")
        and (row.get("status") or "").strip().lower() == "done"
        and row.get("deadline")
    ]
    if completion_dates:
        stats["latest_task_completion"] = max(completion_dates)
    return stats


def get_version_info() -> Dict[str, Any]:
    """Version information from git (commit count + describe)."""
    stats: Dict[str, Any] = {"current_version": "dev", "commit_count": 0}
    try:
        result = subprocess.run(
            ["git", "rev-list", "--count", "HEAD"],
            capture_output=True, text=True, cwd=_REPO_ROOT,
        )
        if result.returncode == 0:
            stats["commit_count"] = int(result.stdout.strip())
        result = subprocess.run(
            ["git", "describe", "--tags", "--always"],
            capture_output=True, text=True, cwd=_REPO_ROOT,
        )
        if result.returncode == 0:
            stats["current_version"] = result.stdout.strip()
    except (FileNotFoundError, subprocess.SubprocessError, ValueError):
        pass
    return stats


if __name__ == "__main__":
    import json

    print(json.dumps({
        "tasks": get_task_stats(),
        "budget": get_budget_stats(),
        "guests": get_guest_stats(),
        "dates": get_latest_dates(),
        "version": get_version_info(),
    }, ensure_ascii=False, indent=2))
