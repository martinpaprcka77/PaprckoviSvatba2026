# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Dual wedding planner — v1 (single-file) + v2 (git-backed). No build, no npm.
Live: https://doma77git.github.io/PaprckoviSvatba2026/

## Architecture — Data-Driven, Git-Backed

```
data/tasks.md          ← AUTHORITATIVE task list (37 tasks, 100 000 Kc)
data/guests.md         ← guest list by side
data/budget.md         ← standalone budget doc (checklist format, derived from tasks.md)
data/rozpocet-svatba-2026.xlsx    ← auto-generated Excel (SUMIF formulas)
data/manualrozpocet-svatba-2026.xlsx ← user manual budget Excel
docs/PRD-svatba-paprckovi-2026.md  ← authoritative spec (PRD rules)

v0: v0/index.html       ← v0 archive (20 tasks, Aug 29 date, Svatba_001 baseline)
v1: index.html          ← fetch-based, reads tasks.md from GitHub Raw, localStorage for state only
v2: v2/index.html       ← fetches MD from GitHub, PIN-unlocked write via API
v3music: v3music/index.html ← v1 + audio player (2 tracks, 3 synced controls), deploy switch
```

**v1:** Svatba_001-style — simple checklist + editable budget table. Fetches `data/tasks.md` from GitHub Raw. localStorage for check state + budget edits only.
**v2:** Fetches `data/tasks.md` + `data/guests.md` from GitHub Raw. Write-back via GitHub API (AES-GCM encrypted PAT, SHA-256 PIN hash). Completed tasks auto-removed from DOM.
**Dual deploy:** `/` (v1 production, přepínatelné přes `DEPLOY_DEFAULT`), `/v2/` (v2 testing), `/v3music/` (v1+audio).

### Data Flow
1. Edit `data/tasks.md` or `data/guests.md` -> commit + push
2. v1 + v2 apps fetch latest from GitHub automatically on load
3. Auto-generated Excel rebuilt by PostToolUse hook when tasks.md changes
4. Manual Excel edited by user independently
5. Push to `master` -> GitHub Actions -> `gh-pages` -> live

## Current State

- **Tasks:** 36 (19 mandatory + 13 important + 4 optional)
- **Budget:** 100 000 Kc — aktuálně 89 500 Kc (mandatory 84 500 + important 4 500 + optional 500)
- **People:** 5 — Mamka, Tatka, Zanetka, Kikinka, Děti
- **Done:** 6/36 (termín, radnice, děti, svědci, oddávající, schůzka prstýnky)
- **Storage keys v1:** `svatba_done_v4`, `svatba_budget_v4` (localStorage, check-state + editable budget only)
- **Wedding:** 29. srpna 2026, 11:15 — Nova radnice Ostrava
- **Venue:** Koliba U Zlateho Jarouse (U Milose), Karasova 1130/23, 709 00 Ostrava

## People

| Kdo | Role | Tasks |
|-----|------|-------|
| **Mamka** | Nevesta | 18 |
| **Tatka** | Zenich | 7 |
| **Zanetka** | Hlavni organizatorka, svedkyne zenicha | 7 |
| **Kikinka** | Svedkyne nevesty | 3 |
| **Děti** | 4 dcery: Gabriela, Kristynka, Natalka, Kacka — vyzdoba, dort, foceni, hudba, foto | 5 |

## Budget

- **100 000 Kc — hard cap.** Mandatory 84 500 + important 4 500 + optional 500 = 89 500 Kc.
- Category targets: mandatory 19 tasks / 84 500 · important 13 tasks / 4 500 · optional 4 tasks / 500
- Autoritativní zdroj: `data/tasks.md` (rozpočet včetně rozpisu)
- Excel: `data/rozpocet-svatba-2026.xlsx` (auto-generated, SUMIF/COUNTIF, podmíněné formátování)
- CELKEM > 100 000 Kc = červená v appce
## Key Rules

1. **Never remove Děti** from tasks — co-assign (`Děti, Mamka`), never replace
2. **Names without hacek** in data: Mikesovi (not Mikesovi with hacek)
3. **No surnames** — first names / nicknames only
4. **Append-only** notes in tasks.md; use `; ` separator
5. **Excel auto-regen** — PostToolUse hook rebuilds `rozpocet-svatba-2026.xlsx` when tasks.md edited
6. After editing tasks.md: update header count, people table, budget table — all three

## Task Data Structure (tasks.md)

```
| Termin | Ukol | Kdo | Kat. | Plan (Kc) | Skutecnost (Kc) | Stav | Timestamp | Poznamka |
```
- `Kdo` comma-separated: `Děti, Mamka` (with diacritic — správná čeština)
- `Kat.`: `mandatory` | `important` | `optional`
- `Stav`: `[x]` done (with timestamp) or `[ ]` open
- `_` = empty/not yet filled

## Excel Files

| File | Purpose | Edit via |
|------|---------|----------|
| `data/rozpocet-svatba-2026.xlsx` | Auto-generated — all 37 tasks, SUMIF budget, per-person sheet | Rebuilt automatically |
| `data/manualrozpocet-svatba-2026.xlsx` | User manual budget — simpler format, mandatory items | User edits directly |

## Hooks (`.claude/settings.json`)

| Hook | What |
|------|------|
| **PreToolUse** (Edit|Write) | Blocks edits to `.env`, `package-lock.json`, `.git/` |
| **PostToolUse** (Edit|Write) | Rebuilds `rozpocet-svatba-2026.xlsx` when tasks.md changes |
| **Notification** (idle_prompt) | Desktop popup when Claude awaits input |

## Deployment

- Push to `master` -> `.github/workflows/deploy.yml` -> `gh-pages`
- `/` = v1 (default), `/v2/` = v2, `/v3music/` = v1+audio, přepínání přes `DEPLOY_DEFAULT`
- Repo: `doma77git/PaprckoviSvatba2026`

## Verify Data Integrity

```bash
python -c "
import re
with open('data/tasks.md', encoding='utf-8') as f:
    md = f.read()
lines = [l for l in md.split('\n') if l.startswith('| 2026')]
m = i = o = 0
for l in lines:
    parts = [p.strip() for p in l.split('|')]
    cat = parts[4]; price = int(parts[5]) if parts[5].isdigit() else 0
    if cat == 'mandatory': m += price
    elif cat == 'important': i += price
    elif cat == 'optional': o += price
total = m + i + o
print(f'Tasks: {len(lines)} (target: 36) | Budget: {total:,} Kc (target: 89500)')
print(f'Mand: {m:,} | Imp: {i:,} | Opt: {o:,}')
print('OK' if total == 89500 and len(lines) == 36 else 'GAP — fix before commit')
"
```