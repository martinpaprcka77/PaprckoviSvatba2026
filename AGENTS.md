# AGENTS.md

This file provides guidance to AI coding assistants working in this repository.

## Overview
Dual wedding planner — v1 (single-file) + v2 (git-backed). No build, no npm.
Live: https://doma77git.github.io/PaprckoviSvatba2026/

## Architecture
- **v0:** `v0/index.html` — archive baseline (Svatba_001, 20 tasks, Aug 29 date)
- **v1:** `index.html` — single-file, inline CSS/JS, localStorage (`svatba_state_v3`)
- **v2:** `v2/index.html` — fetches `data/tasks.md` + `data/guests.md` from GitHub Raw, writes via GitHub API (AES-GCM PAT, PIN)
- **Data:** `data/tasks.md` (37 tasks, authoritative), `data/guests.md` (guest list)
- **Excel:** `data/rozpocet-svatba-2026.xlsx` (auto-gen SUMIF), `data/manualrozpocet-svatba-2026.xlsx` (user manual)
- **Hooks:** `.claude/settings.json` (PreToolUse block .env/.git, PostToolUse rebuild Excel, Notification idle)

## Current State
- 37 tasks (19 mandatory + 14 important + 4 optional)
- 100 000 Kc budget (mandatory 94 500 + important 5 000 + optional 500)
- 5 people: Mamka, Tatka, Zanetka, Kikinka, Deti
- 6/37 done (termín, radnice, deti informovany, svedci, oddavajici, schuzka prstynky)
- Wedding: 29. srpna 2026, Nova radnice Ostrava + Koliba U Zlateho Jarouse

## Rules
1. Budget 100 000 Kc hard cap — verify before commit
2. Never remove Deti from tasks — co-assign, never replace
3. Names without hacek, no surnames: Mikesovi (not Mikesovi)
4. After editing tasks.md: update header count, people table, budget table
5. PRD is authoritative spec: `docs/PRD-svatba-paprckovi-2026.md`

## Deploy
Push to `master` -> GitHub Actions -> `gh-pages` (`/` + `/v2/`)

## Verify
```bash
python -c "
with open('data/tasks.md', encoding='utf-8') as f: md = f.read()
lines = [l for l in md.split('\n') if l.startswith('| 2026')]
m = i = o = 0
for l in lines:
    parts = [p.strip() for p in l.split('|')]
    cat = parts[4]; price = int(parts[5]) if parts[5].isdigit() else 0
    if cat == 'mandatory': m += price
    elif cat == 'important': i += price
    elif cat == 'optional': o += price
print(f'Tasks: {len(lines)}/37 | Budget: {m+i+o}/100000 | OK' if (m+i+o)==100000 and len(lines)==37 else 'GAP')
"
```