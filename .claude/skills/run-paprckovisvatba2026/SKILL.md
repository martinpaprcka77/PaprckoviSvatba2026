---
name: run-paprckovisvatba2026
description: Serve, run, and drive the Paprčkovi 2026 wedding-planner static site (index.html, planner.html). Use when asked to start the site, take a screenshot of it, log into the PIN-gated planner, or click through its tabs/checklist.
---

Static HTML/CSS/JS, no build step. "Running" it means serving the repo
root over HTTP and driving a headless Chromium against it with the
Playwright REPL at `.claude/skills/run-paprckovisvatba2026/driver.cjs`
(no `chromium-cli` binary in this environment, so this driver fills
that role — same command shape).

All paths below are relative to the repo root.

## Prerequisites

Playwright and its Chromium build are already present in this
environment (`/opt/pw-browsers`, global npm package). Nothing to
install. If starting from a machine that lacks them:

```bash
npm install -g playwright
npx playwright install --with-deps chromium
```

## Serve

```bash
python -m http.server 8080 &
echo $! > /tmp/svatba-http.pid
timeout 15 bash -c 'until curl -sf http://localhost:8080/index.html >/dev/null; do sleep 0.3; done'
```

Stop with `kill $(cat /tmp/svatba-http.pid)`.

## Run (agent path) — drive with the Playwright REPL

The driver needs Playwright resolved via `NODE_PATH` (it's a CommonJS
`require`, installed only in the global npm prefix here):

```bash
export NODE_PATH=$(npm root -g)
export BASE_URL=http://localhost:8080
export SHOTS_DIR=/tmp/svatba-shots
```

Pipe commands to it, one per line:

```bash
node .claude/skills/run-paprckovisvatba2026/driver.cjs <<'EOF'
nav /index.html
wait-for .hero-countdown
screenshot index
console-errors
quit
EOF
```

Screenshots land at `$SHOTS_DIR/<name>.png`. `console-errors` prints
every JS console error seen so far (as a JSON array) — check it's
`[]`, or only the known Google Fonts gotcha (see below), before
declaring success.

Commands the driver understands:

| command | what it does |
|---|---|
| `nav <path-or-url>` | `page.goto`; a bare path (`/planner.html`) resolves against `$BASE_URL` |
| `wait-for <selector>` | wait for a CSS selector to become visible (5s timeout) |
| `wait-text <text>` | wait for text to appear anywhere on the page |
| `click <selector>` | click |
| `fill <selector> <text>` | fill an input |
| `press <key>` | keyboard press (e.g. `Enter`) |
| `eval <js>` | `page.evaluate(js)`, prints the JSON result |
| `setls <key> <value>` | `localStorage.setItem(key, value)` — use to bypass the PIN gate (see below) |
| `screenshot [name]` | full-page PNG to `$SHOTS_DIR/<name>.png` |
| `console-errors` | prints all captured console errors as JSON |
| `sleep <ms>` | raw wait, avoid unless nothing else works |
| `quit` | closes the browser |

### Log into the PIN-gated planner

The PIN is hardcoded in `planner.html` (`const PIN = '1941';`) and
gates via a numeric keypad, not a text input, so `fill` doesn't apply
— click the digit buttons (`data-n` attribute) in sequence:

```bash
node .claude/skills/run-paprckovisvatba2026/driver.cjs <<'EOF'
nav /planner.html
wait-for .pin-btn
click .pin-btn[data-n="1"]
click .pin-btn[data-n="9"]
click .pin-btn[data-n="4"]
click .pin-btn[data-n="1"]
wait-for .tabs
screenshot planner-overview
click .tab[data-tab="budget"]
wait-for #tab-budget.active
screenshot planner-budget
console-errors
quit
EOF
```

Faster alternative that skips the click sequence entirely — the gate
just checks `localStorage.planner_auth_v1 === 'ok'`:

```
nav /planner.html
setls planner_auth_v1 ok
nav /planner.html
wait-for .tabs
```

Tab panes are `.tab[data-tab="overview|tasks|budget|guests|schedule|log"]`
/ `#tab-<name>`; a pane is ready when it has class `active`
(`wait-for #tab-budget.active`), which is also how you confirm a tab
switch actually rendered rather than just accepting the click.

## Run (human path)

```bash
python -m http.server 8080   # then open http://localhost:8080/ in a browser
```

Useless headless — only for a human with a display.

## Test

No test suite (`tests.html` exists but tests a retired markdown
parser, not the live `parseCSV` — see CLAUDE.md's "Known stale docs").
There is nothing to run beyond the driver smoke flow above.

## Gotchas

- **Google Fonts requests fail in this sandbox** with
  `net::ERR_CONNECTION_RESET` (blocked outbound to
  `fonts.googleapis.com`/`fonts.gstatic.com`). This shows up in
  `console-errors` on every page load. It's a fallback-font cosmetic
  issue, not a bug in the site — don't chase it, just don't mistake it
  for a real regression.
- **The PIN pad isn't a form input** — `fill`/`press` won't work on it;
  you must `click` the four digit buttons in order, or set
  `planner_auth_v1` in localStorage and reload (see above).
- **`driver.cjs` is CommonJS (`.cjs`), not ESM** — `require('playwright')`
  only resolves because `NODE_PATH=$(npm root -g)` is set; Node's ESM
  loader ignores `NODE_PATH` entirely, which is why this isn't a
  `.mjs` file with `import`.
- **Readline buffers all heredoc lines before any handler resolves** —
  the driver serializes commands through an explicit promise queue
  (see the `queue` variable in `driver.cjs`). Without it, a piped
  heredoc runs every command concurrently and `quit` can close the
  browser mid-`nav`.
- **All CSV data (`tasks.csv`, `budget.csv`, `guests.csv`,
  `changelog.csv`) is fetched live and cache-busted** — the server
  must actually be running and serving `data/` for the page to show
  real content instead of an empty shell.

## Troubleshooting

- **`Error [ERR_MODULE_NOT_FOUND]: Cannot find package 'playwright'`**:
  `NODE_PATH` wasn't exported before running `node driver.cjs`. Run
  `export NODE_PATH=$(npm root -g)` first.
- **`net::ERR_CONNECTION_RESET` in `console-errors`**: expected — see
  Gotchas above, it's the blocked Google Fonts request, not a broken
  page.
- **`page.goto: net::ERR_ABORTED`**: the driver's commands ran out of
  order (an earlier `quit` raced a `nav`). Make sure you're on the
  version of `driver.cjs` with the promise queue in `main()`.
