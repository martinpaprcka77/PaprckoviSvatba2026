#!/bin/bash
# sync-docs.sh — orchestrate documentation sync (PRD) from data/*.csv.
# README je od 2026-09-07 statický (čistý přehled bez auto-sync markerů),
# takže se zde už nekontroluje — syncuje se jen docs/PRD-svatba-paprckovi-2026.md.
#
# Usage:
#   ./scripts/sync-docs.sh             update docs to match CSV (backup + diff)
#   ./scripts/sync-docs.sh --check-only  exit 0 if in sync, 1 if not (no write)
#   ./scripts/sync-docs.sh --dry-run     preview changes without writing
#   ./scripts/sync-docs.sh --ci-check    check-only with GitHub Actions output
#
# Exit codes: 0 = success / in sync, 1 = out of sync or update applied, 2 = usage.
set -u

MODE="${1:-}"

case "$MODE" in
  "" | --check-only | --dry-run | --ci-check) ;;
  *)
    echo "Usage: $0 [--check-only|--dry-run|--ci-check]" >&2
    exit 2
    ;;
esac

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
rc=0

PYTHONIOENCODING=utf-8 python "$SCRIPT_DIR/update-prd.py" $MODE || rc=1

exit $rc
