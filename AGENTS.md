# AGENTS.md

This file provides guidance to AI coding assistants working in this repository.

## Overview
Wedding planner app — v1 + v2 + v3music (read-only MD). No build, no npm.
Live: https://doma77git.github.io/PaprckoviSvatba2026/

## Architecture
- **v0:** `v0/index.html` — archive baseline (Svatba_001, 20 tasks, Aug 29 date)
- **v1:** `index.html` — single-file, inline CSS/JS, localStorage (`svatba_state_v3`)
- **v2:** `v2/index.html` — fetches `data/tasks.md` + `data/guests.md` from GitHub Raw, read-only
- **v3music:** `v3music/index.html` — v1 + audio player (2 tracks), karaoke word-by-word lyrics
- **testplay:** `testplay.html` — isolated karaoke banner test page
- **Data:** `data/tasks.md` (36 tasks, authoritative), `data/guests.md` (3 guest sides)
- **Budget:** `data/budget.md` (derived from tasks.md), `data/rozpocet-svatba-2026.xlsx` (auto-gen)
- **Media:** `media/` — 2× Sweet Caroline (DJ Ötzi Remix + Hasselhoff) in MP3/M4A/MP4
- **Excel:** `scripts/rebuild_excel.py` — regenerates `rozpocet-svatba-2026.xlsx` from tasks.md

## Local Dev
```bash
python -m http.server 8080          # http://localhost:8080/
python scripts/rebuild_excel.py     # regenerate Excel after tasks.md changes
node -e "..."                       # see Verify section below
```

## Current State
- **36 tasks** (19 mandatory + 13 important + 4 optional)
- **Budget:** 100 000 Kc hard cap — currently 89 500 (84 500 + 4 500 + 500)
- **5 people:** Mamka, Tatka, Zanetka, Kikinka, Deti
- **6/36 done:** termín, radnice, děti, svědci, oddávající, schůzka prstýnky
- **Guests:** ~25 across 3 sides (Mamka, Taťka, Společní)
- **Wedding:** 29. srpna 2026, 11:15 — Nová radnice Ostrava + Koliba U Zlatého Jarouše
- **Repo:** doma77git/PaprckoviSvatba2026

## Audio (v3music)
- 2 tracks: **DJ Ötzi — Party Remix** + **David Hasselhoff**
- Both start from refrain, auto-switch to next track on end (cycle)
- Karaoke: word-by-word gold highlighting, click banner to expand full lyrics
- Lyrics per track: `LYRICS_OTZI` / `LYRICS_HOFF` arrays with per-line timestamps
- MP3 paths: `../media/` from v3music (media/ is at repo root, one level up on Pages)
- Controls: floating ▶ button (bottom-right), header button, 2 track selector buttons

## Rules
1. Budget 100 000 Kc hard cap — verify before every commit
2. Never remove Deti from tasks — co-assign (`Deti, Mamka`), never replace
3. Names without hacek, no surnames: Mikesovi (not Mikesovi)
4. After editing tasks.md: update header count, people table, budget table
5. PRD is authoritative spec: `docs/PRD-svatba-paprckovi-2026.md`
6. App is read-only — MD files are sources of truth, app never writes
7. Force refresh on open — always fetch latest MD, reset `completed = {}` from MD
8. Guest list: 3 sides (Mamka, Taťka, Společní) — v2 parser must handle all three

## Deploy
Push to `master` → GitHub Actions → `gh-pages`
Deploys: `/` (v1), `/v2/` (v2), `/v3music/` (v3music), `/media/` (MP3 files)

## Gotchas
- **Windows + Git Bash:** use `grep`/`ls`/`find`, NOT PowerShell cmdlets (`Select-String`, `Get-ChildItem` — fail in bash)
- **Commit messages with `()`:** use heredoc `git commit -m "$(cat <<'EOF' ... EOF)"` — bash parses parentheses
- **`../media/` paths:** media/ is at repo root; from v3music/ or testplay.html use `../media/file.mp3`
- **Audio autoplay:** browsers block `audio.play()` without user gesture — Playwright headless will fail on play
- **GitHub Pages deploy:** push to master → Actions → gh-pages (~1 min). Check: `gh run list --limit 1`
- **Playwright:** `npm i --save-dev playwright` (no global install needed). Clean up `node_modules/` after

## Verify
```bash
python -c "
with open('data/tasks.md', encoding='utf-8') as f: md = f.read()
lines = [l for l in md.split('\n') if l.startswith('| 2026')]
m = i = o = 0; mc = ic = oc = 0
for l in lines:
    parts = [p.strip() for p in l.split('|')]
    cat = parts[4]; price = int(parts[5]) if parts[5].isdigit() else 0
    if cat == 'mandatory': m += price; mc += 1
    elif cat == 'important': i += price; ic += 1
    elif cat == 'optional': o += price; oc += 1
total = m + i + o
print(f'Tasks: {len(lines)}/36 | Cat: {mc}/{ic}/{oc} | Budget: {total} (cap 100000)')
print('OK' if total <= 100000 and len(lines) == 36 else 'GAP — fix before commit')
"
```

## Key Files
| File | Role |
|------|------|
| `data/tasks.md` | Source of truth — tasks, budget, people counts |
| `data/guests.md` | Source of truth — guest list (Mamka/Taťka/Společní) |
| `data/budget.md` | Budget breakdown derived from tasks.md |
| `docs/PRD-svatba-paprckovi-2026.md` | Authoritative spec — full wedding details |
| `index.html` | v1 production app |
| `v2/index.html` | v2 read-only MD app |
| `v3music/index.html` | v1 + audio + karaoke |
| `testplay.html` | Standalone karaoke banner test |
| `scripts/rebuild_excel.py` | Excel regenerator |
| `.github/workflows/deploy.yml` | GitHub Pages deploy |
