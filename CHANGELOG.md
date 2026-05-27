# Changelog

All notable changes to Paprčkovi Svatba 2026 will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.3.2] — 2026-05-27

### Added
- **Hide-done toggle:** v1 — completed tasks hidden by default, toggle button in checklist header ([index.html](index.html))
- **Collapsed budget:** v1 — budget section default collapsed, expand on click, summary visible ([index.html](index.html))
- **v3music:** New version — v1 copy + background audio player with 2 tracks (DJ Ötzi, Hasselhoff), 3 synced controls ([v3music/index.html](v3music/index.html))
- **Deploy switch:** `DEPLOY_DEFAULT` file controls root `/` version, Actions auto-resets to `v1` ([DEPLOY_DEFAULT](DEPLOY_DEFAULT))

### Changed
- Deploy workflow: reads DEPLOY_DEFAULT, deploys selected version as `/`, resets after ([.github/workflows/deploy.yml](.github/workflows/deploy.yml))
- All docs synced: CLAUDE.md, README, walkthrough updated with v3music

## [1.3.1] — 2026-05-27

### Added
- **Guests section** between budget and timeline — fetches `data/guests.md` from GitHub Raw ([v2/index.html](v2/index.html))
- New guests: Jan Drah +1, Jirka Pok, Hozik P. +1 on Taťka's side ([data/guests.md](data/guests.md))
- `Docs/ARCHITEKTURA-APLIKACI.md` — UML architecture templates for v0/v1/v2 ([Docs/ARCHITEKTURA-APLIKACI.md](Docs/ARCHITEKTURA-APLIKACI.md))
- `Docs/MASTER-PROMPT.md` — interactive decision tree for AI agents ([Docs/MASTER-PROMPT.md](Docs/MASTER-PROMPT.md))

### Changed
- **Budget overhaul:** `data/budget.md` redesigned as 1 source of truth with Rezervováno/Zaplaceno/Zbývá columns ([data/budget.md](data/budget.md))
- **Koliba catering split:** task #7 → 7a (Pohoštění 11 100 Kč) + 7b (Poobědový budget 18 900 Kč) ([data/tasks.md](data/tasks.md))
- Cross-doc sync: all references bumped 36 → 37

### Fixed
- Excel PostToolUse hook: `sys.exit` bug fixed, hardcoded paths → relative ([.claude/settings.json](.claude/settings.json))
- Cross-doc sync: CLAUDE.md, copilot-instructions, v2/index.html all updated 36 → 37

### Removed
- `data/budget-items.md` — duplicate, superseded by `data/budget.md`

## [1.3.0] — 2026-05-26

### Added
- **37th task:** "Rozlučka se svobodou" (important, 0 Kč, Žanetka) ([data/tasks.md](data/tasks.md))
- **4 Continue checks:** tasks-md-data-integrity, people-rules, no-secrets-exposure, budget-hard-cap ([.continue/checks/](.continue/checks/))
- **Schůzka prstýnky** marked done (Mamka+Taťka+Žanetka, completed 2026-05-25)

### Changed
- People reassigned: Taťka 9→8, Žanetka 6→7, Děti 3→5 (hudba + fotokoutek → Děti)
- Docs fully synced: README, AGENTS, PRD, CLAUDE.md — 36→37 tasks, 13→14 important, 5→6 done

### Fixed
- Various header counts and budget tables updated for 37-task model

## [1.2.0] — 2026-05-24

### Added
- **v0 baseline:** `v0/index.html` — archival copy of Svatba_001 with dates corrected to Aug 29, 2026. 20 tasks, 81 500 Kč budget ([v0/index.html](v0/index.html))
- `scripts/rebuild_excel.py` — auto-generates budget Excel from tasks.md ([scripts/rebuild_excel.py](scripts/rebuild_excel.py))
- `scripts/_verify_tasks.py` — data integrity checker ([scripts/_verify_tasks.py](scripts/_verify_tasks.py))

### Changed
- **PRD expanded:** 20→36 tasks, 81.5K→100K budget, 5 people ([docs/PRD-svatba-paprckovi-2026.md](docs/PRD-svatba-paprckovi-2026.md))
- **Dáda merged into Mamka** (Dagmar Sobková) — 6→5 people, Mamka 17→18 tasks
- PRD timeline extended: missing task #36 (Schůzka prstýnky, May 25) added
- All docs synced to 36-task / 100K model

### Fixed
- **Deploy workflow:** `peaceiris/actions-gh-pages` (push to gh-pages branch) → `actions/deploy-pages` (native Actions). v0/ was serving 404 before this fix ([.github/workflows/deploy.yml](.github/workflows/deploy.yml))
- Stale `pages-build-deployment` workflow deactivated
- Excel hook fixed: `sys.exit` always-exited bug prevented Excel generation
- Redundant `static.yml` removed (was uploading entire repo root)
- 6 stale Dáda references fixed in copilot-instructions + v1 index.html

### Removed
- 24 PAPROS/Brain leftover files (Architecture, CrossAgent, KnowledgeBase, etc.) — repo 60→42 tracked files
- 14 PNG screenshots, 2 `.original.md` backups, `run_v2.py`, `test_v2.py`, `.playwright-mcp/`

## [1.1.0] — 2026-05-21

### Added
- **V2 Architecture:** Git-backed data — MD files in `data/`, app fetches from GitHub Raw, write-back via GitHub API with PIN ([v2/index.html](v2/index.html))
- **Dual deploy:** `/` (v1 production), `/v2/` (v2 testing) — both served from gh-pages
- **Seznam hostů** section planned (v2 groundwork) ([data/guests.md](data/guests.md))
- **Autoritativní Excel:** `data/rozpocet-svatba-2026.xlsx` — SUMIF/COUNTIF formulas, conditional formatting, per-person sheet
- **Manuální Excel:** `data/manualrozpocet-svatba-2026.xlsx` — user-editable simpler format
- **Hooks:** PreToolUse (block .env/.git edits), PostToolUse (auto-rebuild Excel on tasks.md change), Notification (idle alert) ([.claude/settings.json](.claude/settings.json))
- **Task #36:** Schůzka prstýnky (Mamka+Taťka+Žanetka, 25.5.2026)

### Changed
- **Venue confirmed:** Koliba U Zlatého Jarouše (U Miloše), Karasova 1130/23, 709 00 Ostrava — visited in person by Mamka + Žanetka
- **Catering breakdown:** 30 people, soup 95 Kč/person, main 275 Kč/person, lunch = 11 100 Kč, drinks = remainder to 30K
- **Wedding dress budget:** plan 11 100 Kč → 12 000 Kč, max 15 000 Kč
- **People roles:** Děti got tasks back (výzdoba, dort, focení per PRD role)
- Names standardized: **Mikesovi** (not Mikešovi), no surnames

### Fixed
- 5 V2 bugs: duplicate condition, falsy `actualCosts` check, TextEncoder base64, extra date dot, done count via `doneSet.size`
- `CLAUDE.md` + `copilot-instructions` synced to current state (36 tasks, 6 people, v2 architecture)

## [1.0.0] — 2026-05-14 / 2026-05-16

### Added
- **Initial release:** Single-file HTML wedding planner app ([index.html](index.html))
- **PRD:** Product Requirements Document with 35 tasks, 100 000 Kč budget, 5 people ([docs/PRD-svatba-paprckovi-2026.md](docs/PRD-svatba-paprckovi-2026.md))
- **Data files:** `data/tasks.md` — authoritative task list in Markdown table format
- **Inline architecture:** CSS + JS in single HTML file, no build step, no npm
- **localStorage persistence:** check-state + budget edits (`svatba_done_v4`, `svatba_budget_v4`)
- iPhone-optimized responsive design

### Key Decisions
- **Wedding date:** 29. srpna 2026, 11:15 — Nová radnice Ostrava (confirmed May 16)
- **Budget:** 100 000 Kč hard cap (down from 200K/111.8K)
- **Organizer:** Žanetka (hlavní), Mamka + Taťka (support)
- **Witnesses:** Kikinka (nevěsta) + Žanetka (ženich)
- **People:** Mamka (nevěsta), Taťka (ženich), Žanetka, Kikinka, Děti (4 daughters)
- **GitHub repo:** `doma77git/PaprckoviSvatba2026`
- **Deploy:** GitHub Actions → gh-pages → https://doma77git.github.io/PaprckoviSvatba2026/

---

## Version History Summary

| Version | Date | Tasks | Budget | People | Architecture |
|---------|------|-------|--------|--------|-------------|
| **1.0.0** | 2026-05-16 | 35 | 100 000 Kč | 5 | v1 single-file, localStorage |
| **1.1.0** | 2026-05-21 | 36 | 100 000 Kč | 6→5 | v2 git-backed, dual deploy, Excel hooks |
| **1.2.0** | 2026-05-24 | 36 | 100 000 Kč | 5 | v0 baseline, squash cleanup, deploy fix |
| **1.3.0** | 2026-05-26 | 37 | 100 000 Kč | 5 | guests section foundations |
| **1.3.1** | 2026-05-27 | 37 | 100 000 Kč | 5 | guests live, budget overhaul |
