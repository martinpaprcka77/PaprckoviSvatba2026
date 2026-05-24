# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Dual wedding planner — v1 (single-file) + v2 (git-backed). No build, no npm.
Live: https://doma77git.github.io/PaprckoviSvatba2026/

## Architecture — Data-Driven, Git-Backed

```
data/tasks.md          ← AUTHORITATIVE task list (36 tasks, 100 000 Kc)
data/guests.md         ← guest list by side
data/rozpocet-svatba-2026.xlsx    ← auto-generated Excel (SUMIF formulas)
data/manualrozpocet-svatba-2026.xlsx ← user manual budget Excel
docs/PRD-svatba-paprckovi-2026.md  ← authoritative spec (PRD rules)

v1: index.html          ← single-file, inline CSS/JS, localStorage
v2: v2/index.html       ← fetches MD from GitHub, PIN-unlocked write via API
```

**v1:** Inline `const TASKS = [...]` in index.html, `localStorage` state.
**v2:** Fetches `data/tasks.md` + `data/guests.md` from GitHub Raw. Write-back via GitHub API (AES-GCM encrypted PAT, SHA-256 PIN hash). Completed tasks auto-removed from DOM.
**Dual deploy:** `/` (v1 production), `/v2/` (v2 testing).

### Data Flow
1. Edit `data/tasks.md` or `data/guests.md` -> commit + push
2. v2 app fetches latest from GitHub automatically
3. Auto-generated Excel rebuilt by PostToolUse hook when tasks.md changes
4. Manual Excel edited by user independently
5. Push to `master` -> GitHub Actions -> `gh-pages` -> live

## Current State

- **Tasks:** 36 (19 mandatory + 13 important + 4 optional)
- **Budget:** 100 000 Kc (mandatory 94 500 + important 5 000 + optional 500)
- **People:** 6 — Mamka, Tatka, Zanetka, Kikinka, Deti, Dada
- **Done:** 5/36 (IDs 1-5, auto-initialized on first visit)
- **Storage key v1:** `svatba_state_v3`
- **Wedding:** 29. srpna 2026, 11:15 — Nova radnice Ostrava
- **Venue:** Koliba U Zlateho Jarouse (U Milose), Karasova 1130/23, 709 00 Ostrava

## People

| Kdo | Role | Tasks |
|-----|------|-------|
| **Mamka** | Nevesta | 16 |
| **Tatka** | Zenich | 9 |
| **Zanetka** | Hlavni organizatorka, svedkyne zenicha | 6 |
| **Kikinka** | Svedkyne nevesty | 3 |
| **Deti** | 4 dcery: Gabriela, Kristynka, Natalka, Kacka — vyzdoba, dort, foceni | 3 |
| **Dada** | Pomoc s prstynky | 1 |

## Budget — NON-NEGOTIABLE

- **MAX 100 000 Kc — hard cap.** Any price increase must find offsetting cuts.
- Category targets: mandatory 94 500 · important 5 000 · optional 500
- After any price edit: verify total <= 100 000 Kc before commit
- Excel `rozpocet-svatba-2026.xlsx` has conditional formatting — CELKEM turns red at >100k
- Important category grew from 12->13 tasks (added schuzka prstynky, 0 Kc)

## Key Rules

1. **Never remove Deti** from tasks — co-assign (`Deti, Mamka`), never replace
2. **Names without hacek** in data: Mikesovi (not Mikesovi with hacek)
3. **No surnames** — first names / nicknames only
4. **Append-only** notes in tasks.md; use `; ` separator
5. **Excel auto-regen** — PostToolUse hook rebuilds `rozpocet-svatba-2026.xlsx` when tasks.md edited
6. After editing tasks.md: update header count, people table, budget table — all three

## Task Data Structure (tasks.md)

```
| Termin | Ukol | Kdo | Kat. | Plan (Kc) | Skutecnost (Kc) | Stav | Timestamp | Poznamka |
```
- `Kdo` comma-separated: `Deti, Mamka`
- `Kat.`: `mandatory` | `important` | `optional`
- `Stav`: `[x]` done (with timestamp) or `[ ]` open
- `_` = empty/not yet filled

## Excel Files

| File | Purpose | Edit via |
|------|---------|----------|
| `data/rozpocet-svatba-2026.xlsx` | Auto-generated — all 36 tasks, SUMIF budget, per-person sheet | Rebuilt automatically |
| `data/manualrozpocet-svatba-2026.xlsx` | User manual budget — simpler format, mandatory items | User edits directly |

## Hooks (`.claude/settings.json`)

| Hook | What |
|------|------|
| **PreToolUse** (Edit|Write) | Blocks edits to `.env`, `package-lock.json`, `.git/` |
| **PostToolUse** (Edit|Write) | Rebuilds `rozpocet-svatba-2026.xlsx` when tasks.md changes |
| **Notification** (idle_prompt) | Desktop popup when Claude awaits input |

## Deployment

- Push to `master` -> `.github/workflows/deploy.yml` -> `gh-pages`
- `/` = v1, `/v2/` = v2
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
print(f'Tasks: {len(lines)} (target: 36) | Budget: {total:,} Kc (target: 100000)')
print(f'Mand: {m:,} | Imp: {i:,} | Opt: {o:,}')
print('OK' if total == 100000 and len(lines) == 36 else 'GAP — fix before commit')
"
```