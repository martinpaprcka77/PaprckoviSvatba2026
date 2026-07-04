# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Wedding planner for Svatba Paprčkovi 2026 (29 Aug 2026, 11:15, Nová radnice Ostrava + Koliba U Zlatého Jarouše). Static, no-build, no-backend site: plain HTML/CSS/JS pages that fetch CSV data files at runtime. Deployed to GitHub Pages on every push to `master`.

## Architecture

**Data flow:** `data/*.csv` is the single source of truth. Every page fetches the CSVs client-side with cache-busting (`fetch('data/' + name + '?_=' + Date.now(), {cache:'no-store'})`), parses them with a small hand-rolled CSV parser (handles quoted fields with embedded commas), and renders. Pages are **read-only against the data** — nothing in the app writes back to the CSVs; edits happen by hand (or by an agent) editing the CSV files and pushing to git. The only client-side write is `localStorage` for two things: the PIN gate on `planner.html` (`planner_auth_v1`) and a countdown/UI refresh timer — never for task/budget/guest state, which is always re-fetched fresh.

**Pages (all top-level, no build step, no framework):**
- `index.html` — public page, romantic/guest-facing, no budget shown, countdown timer, checklist (done items hidden), links to `planner.html`.
- `planner.html` — PIN-gated (4-digit PIN check + localStorage flag) full view for organizers: tasks, budget, guests, changelog.
- `index_june.html` — frozen archive snapshot of state as of June 2026. Do not wire it up to live CSVs; it's meant to stay static.
- `karaoke.html` — standalone Sweet Caroline karaoke page (audio + synced lyrics), uses `media/*.mp3`.
- `tests.html` — **stale**: a manual test-runner page exercising `parseTasksMD` / `parseBudgetMD` / `parseGuestsMD` functions from an earlier markdown-based data format. The app now uses CSV (`parseCSV` in `index.html`/`planner.html`), so this suite doesn't cover the current parser. Don't treat it as passing/failing signal until it's ported to CSV.

**Data files (`data/`, CSV, header row + one row per record):**
- `tasks.csv`: `id, deadline, title, assign, category, status, note` — `category` ∈ `mandatory|important|optional`, `status` ∈ `open|done`, `assign` is comma-separated for co-assigned tasks (e.g. `Děti, Mamka`).
- `budget.csv`: `id, item, category, amount_plan, amount_actual, note` — `amount_actual` filled in only once actually paid; budget amounts live here, not in `tasks.csv`.
- `guests.csv`: `id, name, side, count, confirmed, note` — `side` ∈ `mamka|tatka|spolecni`.
- `changelog.csv`: `date, who, what, detail` — append a row after every meaningful decision.

**Deploy** (`.github/workflows/deploy.yml`): on push to `master`, copies `index.html`, `planner.html`, `index_june.html`, `karaoke.html`, `data/`, `public/*`, `media/` into a flat `deploy_out/` and publishes it to GitHub Pages. There is no npm/build tooling — new pages or assets must be added explicitly to this workflow's copy list or they won't ship.

**Docs:** `docs/PRD-svatba-paprckovi-2026.md` is the requirements/spec document (roles, day-of schedule, budget rationale).

## Local development

```bash
python -m http.server 8080   # http://localhost:8080/
```

No install, no build, no test command — verify changes by opening the page in a browser and checking the fetched CSV renders correctly. When editing JS that touches `parseCSV`/`fetchCSV`, sanity-check against `tests.html`'s intent even though it's currently testing the old parser (see above).

## Key rules

1. **Budget hard cap: 100 000 Kč total** across `data/budget.csv`. Before/after any budget edit, sum `amount_plan` across all rows and confirm it stays ≤ 100 000.
2. **Never remove Děti from a task's `assign`** — only co-assign (`Děti, Mamka`), never replace them.
3. **Names: no háčky, no surnames** — e.g. `Mikesovi` not `Mikešovi`. Only first names/nicknames (`Mamka`, `Taťka`, `Žanetka`, `Kikinka`, `Děti`) are valid `assign` values.
4. **`tasks.csv` notes are append-only** — when adding to `note`, append rather than overwrite, separated by `; `.
5. **CSV files are authoritative; the app never writes to them.** Any data change is a direct edit to the CSV + git commit/push, never through the UI.
6. Deploy paths in `.github/workflows/deploy.yml` are the definitive list of what ships — a new top-level HTML page/asset needs a line added there.

## Known stale docs — do not trust blindly

Several docs in this repo describe an earlier version of the project and are out of sync with the current CSV-based `data/` files and page set:
- `README.md` states 36 tasks / 19+13+4 category split; the current `data/tasks.csv` actually has 34 rows (17 mandatory / 13 important / 4 optional). Budget total (89 500 Kč) still matches. Recompute counts from the CSV rather than trusting hardcoded numbers in prose docs.
- `.github/copilot-instructions.md` references a `v2/` directory, `data/*.md` files, and repo owner `doma77git` — none of which exist in this repo anymore (data is CSV, owner is `martinpaprcka77`, no `v2/`).
- `.continue/checks/*.md` (budget/task/people-rules checks) are written against `data/tasks.md` (markdown table format) and won't match against the current `data/tasks.csv`; the underlying *rules* they encode (budget cap, Děti co-assign, no-hacek names) are still correct and mirrored above.

If you touch these files as part of unrelated work, feel free to correct obviously wrong facts, but fixing the full drift is out of scope unless asked.
