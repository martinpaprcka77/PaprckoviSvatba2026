# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Wedding planner for Svatba Paprčkovi 2026 (29 Aug 2026, Nová radnice Ostrava + Koliba U Zlatého Jarouše). Static HTML/CSS/JS, no build, no backend. Deployed to GitHub Pages on push to `master`.

## Architecture

`data/*.csv` is the single source of truth. Pages fetch it client-side with cache-busting (`fetch(..., {cache:'no-store'})` + a timestamp query param), parse it with a small hand-rolled CSV parser, and render — **read-only**, nothing ever writes back to the CSVs; edits are a direct CSV change + git commit/push. `localStorage` is used only for the `planner.html` PIN gate (`planner_auth_v1`) and a refresh timer — never for task/budget/guest state, which is always re-fetched.

**Pages:**
- `index.html` — public, no budget shown, countdown + checklist (done items hidden).
- `planner.html` — PIN-gated, full view: tasks, budget, guests, changelog.
- `index_june.html` — frozen archive snapshot; don't wire to live data.
- `karaoke.html` — standalone Sweet Caroline page (audio + synced lyrics).
- `tests.html` — **stale**: tests the old markdown parser, not the current `parseCSV`.

**Data files** (`data/`, CSV, header + one row per record):
- `tasks.csv`: `id,deadline,title,assign,category,status,note` — `category` ∈ `mandatory|important|optional`, `status` ∈ `open|done`, `assign` comma-separated for co-assigned tasks.
- `budget.csv`: `id,item,category,amount_plan,amount_actual,note` — money lives here, not in `tasks.csv`.
- `guests.csv`: `id,name,side,count,confirmed,note` — `side` ∈ `mamka|tatka|spolecni`.
- `changelog.csv`: `date,who,what,detail` — append a row after every meaningful decision.

**Deploy** (`.github/workflows/deploy.yml`): copies `index.html`, `planner.html`, `index_june.html`, `karaoke.html`, `data/`, `public/*`, `media/` to GitHub Pages. Retries the deploy step up to 3x on transient failures. New top-level pages/assets must be added to this workflow or they won't ship.

**Docs:** `docs/PRD-svatba-paprckovi-2026.md` is the requirements/spec document.

## Local development

```bash
python -m http.server 8080
```

No install, no build, no test command — verify in a browser.

## Key rules

1. **Budget hard cap: 100 000 Kč total** in `data/budget.csv` — sum `amount_plan` and confirm ≤ 100 000 after any edit.
2. **Never remove Děti from a task's `assign`** — co-assign (`Děti, Mamka`), never replace.
3. **Names: no háčky, no surnames** (`Mikesovi` not `Mikešovi`) — only `Mamka`, `Taťka`, `Žanetka`, `Kikinka`, `Děti`.
4. **`tasks.csv` notes are append-only** — separator `; `.
5. **CSV is authoritative** — edit + commit/push, never through the UI.
6. Deploy paths in `.github/workflows/deploy.yml` define what ships.

## Known stale docs

- `README.md` and `docs/PRD-*.md` carry a numeric snapshot that drifts every time `data/tasks.csv`/`data/budget.csv` changes. **Always recompute counts/totals from the CSV** rather than trusting hardcoded numbers in prose — update them when you touch task/budget data in the same session.
- `.github/copilot-instructions.md` and `.continue/checks/*.md` describe an older `data/*.md` + `doma77git`-owned setup — outdated, but the rules they encode (above) still hold. Fix opportunistically, not required.
