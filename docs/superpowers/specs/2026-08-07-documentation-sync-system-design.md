# Documentation Synchronization System Design

**Date**: 2026-08-07  
**Project**: Svatba Paprčkovi 2026 Wedding Planner  
**Status**: Approved  

## Context and Problem Statement

The wedding planner uses CSV files in `data/` as the single source of truth, with documentation files (README.md, PRD-svatba-paprckovi-2026.md) that need to reflect current data. Currently, manual updates lead to inconsistencies where documentation shows outdated statistics, dates, or task completion status compared to the actual CSV data.

Common inconsistencies observed:
- Progress statistics (e.g., "10/27 splněno") not matching actual completed tasks count
- Budget totals in docs not matching sum of `amount_plan` in budget.csv
- Date mismatches (e.g., wedding date, completed task dates)
- "Hotovo"/"Rozpracováno"/"Zrušeno" lists not reflecting current task statuses
- Version history not updated after significant changes

## Goals

1. **Consistency**: Documentation automatically reflects current CSV data state
2. **Prevention**: Prevent committing inconsistent states via pre-commit checks
3. **Detection**: Catch inconsistencies that slip through via CI validation
4. **Manual Override**: Provide easy manual sync for ad-hoc updates
5. **Transparency**: Clear error messages showing exactly what's inconsistent
6. **Safety**: Non-destructive operations with backups and dry-run capabilities

## Non-Goals

- Modifying CSV data through documentation (CSV remains source of truth)
- Complex versioning system beyond basic change tracking
- Real-time synchronization (updates happen on commit/manual trigger)
- Multi-language support (documentation remains Czech)

## System Architecture

```
�┌─────────────────�┐    � ┌──────────────────�┐    � ┌────────────────────�┐
│   CSV Data      │    │ Documentation    │    │   Sync System      │
│ (tasks.csv,     │───�▶│ (README.md,      │    │                    │
│ budget.csv,     │    │  PRD.md,         │    │  � ┌─────────────�┐    │
│ guests.csv,     │    │  changelog.csv)  │    │  │ extract-stats │    │
│ changelog.csv)  │    │                  │    │  │   update-   │    │
�└─────────────────�┘    └──────────────────�┘    │  │   readme    │    │
                                                 │  │   update-   │    │
                                                 │  │     prd     │    │
                                                 │  └─────────────�┘    │
                                                 └────────────────────�┘
                                                       ▲
                                                       │
     � ┌────────────────────�┐    � ┌────────────────────�┐    │
     │ Pre-commit Hook    │    │ GitHub Action      │    │
     │ (.git/hooks/       │    │ (.github/workflows│    │
     │  pre-commit)       │    │  /sync-validation.yml)│
     └────────────────────�┘    └────────────────────�┘    │
                                                       │
     � ┌────────────────────�┐                            │
     │ Local Sync Script  │�◄──────────────────────────�┘
     │ (scripts/sync-docs.sh)                       │
     └────────────────────�┘
```

## Component Design

### 1. Data Extraction Layer (`scripts/extract-stats.py`)

**Responsibility**: Parse CSV files and calculate current statistics

**Functions**:
- `get_task_stats()` → Returns: `{completed: int, total: int, by_category: {"mandatory": int, "important": int, "optional": int}}`
- `get_budget_stats()` → Returns: `{planned_total: int, actual_total: int, remaining: int}`
- `get_guest_stats()` → Returns: `{total: int, confirmed: int, by_side: {"mamka": int, "tatka": int, "spolecni": int}}`
- `get_latest_dates()` → Returns: `{wedding_date: str, latest_changelog: str, latest_task_completion: str}`
- `get_version_info()` → Returns: `{current_version: str, commit_count: int}`

**Implementation Notes**:
- Uses Python's built-in `csv` module for proper quote handling
- Handles UTF-8 encoding and Czech characters
- Includes defensive programming for missing/malformed data
- Returns structured data (dict) for easy consumption by other modules

### 2. Documentation Update Layer

#### A. README Updater (`scripts/update-readme.py`)
**Responsibility**: Update statistics and status sections in README.md

**Update Targets** (using unique comment markers):
```html
<!-- TASK_STATS_START -->
��✅ 10/27 splněno  ·  �� 💰 80 500 / 100 000 Kč naplánováno (10 000 Kč utraceno)
<!-- TASK_STATS_END -->

<!-- TASK_CATEGORIES_START -->
| Kategorie | Úkolů | Plán |
|-----------|-------|------|
| �� 🔴 Povinné | 15 | 76 500 Kč |
| �� 🟡 Důležité | 10 | 4 000 Kč |
| �� 🟢 Volitelné | 2 | 0 Kč |
| **Celkem** | **27** | **80 500 Kč** |
<!-- TASK_CATEGORIES_END -->

<!-- COMPLETED_TASKS_START -->
**Hotovo:** termín · radnice · děti · svědci · oddávající · schůzka prstýnky · prstýnky vyzvednuty · svatební šaty · oblek a sako · rozlučka se svobodou
<!-- COMPLETED_TASKS_END -->

<!-- IN_PROGRESS_START -->
**Rozpracováno:** svatební oznámení — tisk hotovo, zbývá rozeslat + RSVP
<!-- IN_PROGRESS_END -->

<!-- CANCELLED_START -->
**Zrušeno:** dárky pro svědky · dárky na přivítanou · guestbook+favory · proslovy svědků · confetti · ubytování pro hosty · dekorace na radnici
<!-- CANCELLED_END -->
```

**Process**:
1. Read current README.md
2. For each section:
   - Find content between markers
   - Generate new content from current stats
   - Replace if different
3. Add markers if missing (first-time setup)
4. Create `.bak` backup before writing
5. Return diff of changes made

#### B. PRD Updater (`scripts/update-prd.py`)
**Responsibility**: Update "Current status" section and version history in PRD-svatba-paprckovi-2026.md

**Update Targets**:
- Current status block (mirrors README format but PRD-specific)
- Version history table (auto-add entry on significant changes)
- Any statistics tables

**Version History Logic**:
- Compares current state to last recorded version in table
- If meaningful difference (task completion change >0, budget change >1000 Kč, etc.)
- Adds new entry with current date and summary of changes

### 3. Synchronization Scripts

#### A. Main Sync Script (`scripts/sync-docs.sh`)
**Usage**:
- `./scripts/sync-docs.sh` → Update docs to match CSV (shows diff)
- `./scripts/sync-docs.sh --check-only` → Report if sync needed
- `./scripts/sync-docs.sh --ci-check` → CI-friendly output (for GitHub Actions)
- `./scripts/sync-docs.sh --dry-run` → Preview changes without writing

**Operation Mode**:
1. **Check-only mode**: 
   - Extract current stats from CSV
   - Extract current stats from docs (by parsing marked sections)
   - Compare and report mismatches
   - Exit code 0 if match, 1 if mismatch
   
2. **Update mode** (default):
   - Same as check, but if mismatch:
     - Create backups (`README.md.bak`, `PRD.md.bak`)
     - Update documentation with current stats
     - Show unified diff of changes
     - Exit code 0

3. **CI mode** (`--ci-check`):
   - Same as check-only but outputs in GitHub Actions error format
   - On failure: Sets action as failed with detailed annotations

#### B. Pre-commit Hook (`.git/hooks/pre-commit`)
**Implementation**: Symlink to `scripts/sync-docs.sh --check-only`
- Runs automatically before `git commit`
- Prevents commit if documentation is out of sync
- Shows clear error message with instructions to run sync script
- Bypassed only with `git commit --no-verify` (not recommended)

#### C. Installation Script (`scripts/install-hooks.sh`)
**Responsibility**: Set up development environment
- Creates symlink for pre-commit hook
- Verifies required tools (bash, python3)
- Optional: Installs in development mode

#### D. GitHub Action (`.github/workflows/sync-validation.yml`)
```yaml
name: Documentation Synchronization Validation
on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  validate-sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Validate documentation sync
        run: |
          chmod +x ./scripts/sync-docs.sh
          ./scripts/sync-docs.sh --ci-check
```

## File Structure

```
docs/
├── superpowers/
│   └── specs/
│       └── 2026-08-07-documentation-sync-system-design.md  # This file
├── snapshot-2026-08-07.md                 # Optional: auto-generated snapshots
├── README.md                              # Auto-updated by sync system
�└── PRD-svatba-paprckovi-2026.md           # Auto-updated by sync system

scripts/
├── sync-docs.sh                           # Main synchronization script
├── sync-pre-commit.sh                     # Symlink to sync-docs.sh --hook
├── extract-stats.py                       # CSV parsing and stats extraction
├── update-readme.py                       # README.md update logic
├── update-prd.py                          # PRD.md update logic
�└── install-hooks.sh                       # Environment setup script

.github/
�└── workflows/
    └── sync-validation.yml                # CI validation workflow
```

## Trade-offs Considered

### 1. Update Strategy: Aggressive vs Conservative
- **Aggressive** (auto-update docs on mismatch): Risk of overwriting manual doc improvements
- **Conservative** (fail and require manual fix): Safer but more friction
- **Chosen**: Conservative in pre-commit/CI (prevent bad state), aggressive in manual sync (user-initiated)

### 2. Implementation Language: Bash vs Python
- **Bash**: Simpler for file operations, git hooks
- **Python**: Better for CSV parsing, complex logic
- **Chosen**: Hybrid - bash orchestration with Python modules for core logic

### 3. Marker Approach: Regex vs Line Numbers
- **Line Numbers**: Fragile, breaks if surrounding content changes
- **Regex Markers**: Robust to surrounding content changes, requires adding markers
- **Chosen**: Unique HTML-style comment markers for resilience

### 4. Version History: Automatic vs Manual
- **Automatic**: Always up-to-date but may create noisy entries
- **Manual**: Precise but relies on human memory
- **Chosen**: Semi-automatic - suggests entries based on detectable changes, user approves via commit

## Open Questions

1. **Snapshot Frequency**: Should we auto-generate daily/weekly snapshot files in `docs/snapshots/?`
   - *Pros*: Historical record, easy to diff over time
   - *Cons*: Storage overhead, potential for forgotten files
   - *Tentative*: Not included in v1, can be added later via `scripts/generate-snapshot.sh`

2. **Changelog Automation**: Should significant CSV changes auto-add to changelog.csv?
   - *Pros*: Complete audit trail
   - *Cons*: Blurs line between data and metadata, potential for noisy entries
   - *Decision*: Keep changelog as strictly human-edited decision log per current practice

3. **Error Severity**: Should certain inconsistencies (e.g., minor wording differences) be warnings not errors?
   - *Decision*: Treat all marker-section mismatches as errors to ensure consistency; non-marker areas unaffected

## Approval

This design has been reviewed and approved for implementation. The synchronization system will ensure documentation accuracy while maintaining the CSV-as-source-of-truth architecture.

**Approved by**: [User/Team]  
**Approval Date**: 2026-08-07  

## Next Steps

1. Implement the design by creating the specified files
2. Write unit tests for extract-stats.py (test CSV parsing edge cases)
3. Test sync-docs.sh with various inconsistency scenarios
4. Install pre-commit hook in development environment
5. Add GitHub action to repository
6. Create initial synchronization to establish baseline consistency