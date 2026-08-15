"""Tests for scripts/extract-stats.py against the real data/*.csv files.

Expected values are locked to the current CSV state (source of truth);
update them deliberately when the CSV data changes.
"""

import importlib.util
import os
import sys

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "extract-stats.py")
_spec = importlib.util.spec_from_file_location("extract_stats", _SCRIPT)
extract_stats = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(extract_stats)


def test_get_task_stats():
    stats = extract_stats.get_task_stats()
    assert stats["total"] == 33
    assert stats["completed"] == 11
    assert stats["by_category"] == {"mandatory": 17, "important": 12, "optional": 4}


def test_get_budget_stats():
    stats = extract_stats.get_budget_stats()
    assert stats["planned_total"] == 89_500
    assert stats["actual_total"] == 82_650
    assert stats["remaining"] == 6_850
    assert stats["reserve"] == 10_500
    assert stats["cap"] == 100_000
    assert stats["by_category"]["mandatory"] == {"planned": 84_500, "actual": 78_100}
    assert stats["by_category"]["important"] == {"planned": 4_500, "actual": 4_150}
    assert stats["by_category"]["optional"] == {"planned": 500, "actual": 400}


def test_get_guest_stats():
    stats = extract_stats.get_guest_stats()
    assert stats["total"] == 17
    assert stats["confirmed"] == 11
    assert stats["by_side"] == {"mamka": 3, "tatka": 4, "spolecni": 10}


def test_get_latest_dates():
    stats = extract_stats.get_latest_dates()
    assert stats["wedding_date"] == "2026-08-29"
    assert stats["latest_changelog"] == "2026-07-29"
    assert stats["latest_task_completion"] == "2026-07-15"


def test_get_version_info():
    stats = extract_stats.get_version_info()
    assert set(stats) == {"current_version", "commit_count"}
    assert isinstance(stats["commit_count"], int)
    assert stats["commit_count"] > 0


def test_missing_data_dir_returns_zeros(monkeypatch):
    monkeypatch.setattr(extract_stats, "DATA_DIR", os.path.join(_SCRIPT, "does-not-exist"))
    assert extract_stats.get_task_stats()["total"] == 0
    assert extract_stats.get_budget_stats()["planned_total"] == 0
    assert extract_stats.get_guest_stats()["total"] == 0
