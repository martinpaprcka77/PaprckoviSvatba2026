# PaprckoviSvatba2026 — AI Assistant Instructions

## Overview

Dual wedding planner — v1 (single-file) + v2 (git-backed). No build, no npm.
**Live v1:** https://doma77git.github.io/PaprckoviSvatba2026/
**Live v2:** https://doma77git.github.io/PaprckoviSvatba2026/v2/

## Active Project

### Svatba Paprckovi 2026
- **Wedding:** 29. srpna 2026, 11:15 — Nova radnice Ostrava + Koliba U Zlateho Jarouse (U Milose)
- **Budget:** MAX 100 000 Kc hard cap (mandatory 94 500 + important 5 000 + optional 500)
- **Tasks:** 37 (19 mandatory + 14 important + 4 optional) · 5 people
- **Source of truth:** `data/tasks.md` (tasks), `data/guests.md` (guests)
- **Repo:** https://github.com/doma77git/PaprckoviSvatba2026
- **Deploy:** Push to master -> GitHub Actions -> gh-pages (`/` + `/v2/`)

### Architecture
- v0: `v0/index.html` — archive baseline (Svatba_001, 20 tasks, Aug 29 date)
- v1: `index.html` — single-file, inline CSS/JS, localStorage (`svatba_state_v3`)
- v2: `v2/index.html` — fetches `data/*.md` from GitHub Raw, writes via GitHub API (AES-GCM PAT, PIN)
- Data: `data/tasks.md` (36 tasks), `data/guests.md` (guests by side)
- Excel: `data/rozpocet-svatba-2026.xlsx` (auto-gen SUMIF), `data/manualrozpocet-svatba-2026.xlsx` (user manual)

### People (5)
Mamka (nevesta), Tatka (zenich), Zanetka (organizatorka + svedkyne), Kikinka (svedkyne), Deti (4 dcery — vyzdoba/dort/foceni)

### Key Rules
- Budget 100 000 Kc hard cap — verify before every commit
- Never remove Deti from tasks — co-assign, never replace
- Names without hacek, no surnames: Mikesovi (not Mikesovi)
- Append-only notes in tasks.md
- PostToolUse hook auto-rebuilds Excel when tasks.md changed