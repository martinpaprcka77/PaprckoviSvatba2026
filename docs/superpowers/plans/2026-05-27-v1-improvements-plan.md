# V1 Improvements + V3music Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add hide-completed toggle and collapsed budget to v1, create v3music with audio player, add deploy switch via DEPLOY_DEFAULT, update all cross-file docs.

**Architecture:** Surgical edits to v1 single-file HTML (536 lines). v3music is full copy of v1 + audio player module. Deploy switch is a one-line read file in Actions workflow. Docs get v3music + hide-done additions in version tables.

**Tech Stack:** HTML/CSS/JS single-file, localStorage, GitHub Actions (bash), MP3 via HTML5 `<audio>` element

---

## File Map

| File | Action | Responsibility |
|------|--------|---------------|
| `index.html` | Edit | Hide-done toggle + budget collapse |
| `v3music/index.html` | **Create** | Full copy of v1 + audio player (2 tracks, 3 synced controls) |
| `.github/workflows/deploy.yml` | Edit | Add v3music/ to deploy + DEPLOY_DEFAULT reader |
| `DEPLOY_DEFAULT` | **Create** | One-line text file: `v1` |
| `CLAUDE.md` | Edit | Add v3music to version table, update deploy section |
| `README.md` | Edit | Add v3music quick link |
| `walkthrough.md` | Edit | Add v3music to verze table + deploy section |
| `CHANGELOG.md` | Edit | Add `## [1.3.2] — 2026-05-27` entry |
| `media/Sweet_Caroline_Remix.mp3` | Git add | DJ Ötzi remix (4.4 MB) |
| `media/Sweet_Caroline_Hoff.mp3` | Git add | Hasselhoff cover (4.8 MB) |

**Skip from commit:** 7 other media files (.mp4, .m4a, original Sweet_Caroline) — 29 MB unnecessary.

---

### Task 1: Add hide-done toggle + budget collapse to v1 `index.html`

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add CSS for toggle, collapsed budget, and transition**

Insert into `<style>` block after the `.filters button.active` rule (line 87):

```css
/* Hide-done toggle */
.hide-done-toggle {
    display: inline-flex; align-items: center; gap: 4px;
    padding: 5px 12px; border-radius: 20px; border: 1.5px solid var(--border-dark);
    background: var(--bg-card); color: var(--text-muted); font-size: 0.74rem;
    font-weight: 600; cursor: pointer; font-family: inherit; transition: all 0.2s;
    white-space: nowrap; float: right;
}
.hide-done-toggle.active { background: var(--success); color: #fff; border-color: var(--success); }
.hide-done-toggle .dot {
    width: 8px; height: 8px; border-radius: 50%; display: inline-block;
    background: var(--text-muted); transition: background 0.2s;
}
.hide-done-toggle.active .dot { background: #fff; }

/* Budget collapse */
.budget-header {
    display: flex; justify-content: space-between; align-items: center;
    cursor: pointer; user-select: none;
}
.budget-header h2 { margin: 0; }
.budget-collapse-btn {
    font-size: 0.75rem; color: var(--text-muted); font-weight: 500;
    transition: transform 0.3s;
}
.budget-collapse-btn.open { transform: rotate(180deg); }
.budget-body { overflow: hidden; transition: max-height 0.35s ease; }
.budget-body.collapsed { max-height: 0 !important; }
.budget-summary { display: none; font-size: 0.85rem; padding: 8px 0; }
.budget-summary.visible { display: block; }
```

- [ ] **Step 2: Add hide-done toggle button in the checklist card, next to filters**

Replace the checklist card HTML (lines 154-161) with:

```html
    <!-- Checklist -->
    <div class="card">
        <h2>📋 Checklist</h2>
        <div style="display:flex;align-items:center;gap:6px;">
            <div class="filters" id="filters" style="margin-bottom:0;flex:1;"></div>
            <button class="hide-done-toggle active" id="hideDoneToggle" onclick="toggleHideDone()" title="Schovat hotové">
                👁 <span class="dot"></span>
            </button>
        </div>
        <div id="tasksContainer"></div>
        <div style="margin-top:12px; text-align:center;">
            <button class="btn btn-outline" onclick="resetAll()">🔄 Reset checkboxů</button>
        </div>
    </div>
```

- [ ] **Step 3: Replace budget card HTML with collapsible version**

Replace lines 164-174:

```html
    <!-- Budget -->
    <div class="card">
        <div class="budget-header" onclick="toggleBudget()">
            <h2>💰 Rozpočet</h2>
            <span class="budget-collapse-btn" id="budgetCollapseBtn">▼</span>
        </div>
        <div class="budget-summary visible" id="budgetSummary">
            <span style="font-weight:700;">CELKEM: <span id="budgetSummaryTotal">0 Kč</span></span>
            <span style="color:var(--text-muted);margin-left:8px;font-size:0.8rem;">(klikni pro detail)</span>
        </div>
        <div class="budget-body collapsed" id="budgetBody" style="max-height:2000px;">
            <table class="budget-table">
                <thead><tr><td><strong>Položka</strong></td><td style="text-align:right"><strong>Odhad (Kč)</strong></td></tr></thead>
                <tbody id="budgetTableBody"></tbody>
                <tfoot>
                    <tr><td class="budget-total">CELKEM</td><td class="budget-total" id="totalBudgetVal">0 Kč</td></tr>
                    <tr><td class="budget-tolerance" colspan="2">Max tolerance 120%: <span id="maxToleranceVal">0 Kč</span></td></tr>
                </tfoot>
            </table>
        </div>
    </div>
```

- [ ] **Step 4: Add new JS constants and state variables after existing constants (after line 207)**

```js
const LS_HIDE_DONE = 'svatba_hide_done';
const LS_BUDGET_COLLAPSED = 'svatba_budget_collapsed';
let hideDone = true;      // default: hide completed tasks
let budgetCollapsed = true; // default: collapsed
```

- [ ] **Step 5: Add load/save functions for new state (after saveBudget, line 333)**

```js
function loadHideDone() {
    try {
        const v = localStorage.getItem(LS_HIDE_DONE);
        if (v !== null) hideDone = (v === 'true');
    } catch (e) {}
}
function saveHideDone() {
    try { localStorage.setItem(LS_HIDE_DONE, hideDone.toString()); } catch (e) {}
}
function loadBudgetCollapsed() {
    try {
        const v = localStorage.getItem(LS_BUDGET_COLLAPSED);
        if (v !== null) budgetCollapsed = (v === 'true');
    } catch (e) {}
}
function saveBudgetCollapsed() {
    try { localStorage.setItem(LS_BUDGET_COLLAPSED, budgetCollapsed.toString()); } catch (e) {}
}
```

- [ ] **Step 6: Modify loadState() to load new keys (line 317-327)**

Add at end of `loadState()`:

```js
loadHideDone();
loadBudgetCollapsed();
```

- [ ] **Step 7: Modify renderTasks() to respect hideDone (line 369-398)**

Replace the renderTasks function:

```js
function renderTasks() {
    let filtered = [...tasks];
    if (currentFilter === 'mandatory') filtered = filtered.filter(t => t.cat === 'mandatory');
    else if (currentFilter === 'important') filtered = filtered.filter(t => t.cat === 'important');
    else if (currentFilter === 'optional') filtered = filtered.filter(t => t.cat === 'optional');

    // Hide completed tasks when toggle is active
    if (hideDone) filtered = filtered.filter(t => !completed[t.key]);

    filtered.sort((a, b) => new Date(a.deadline) - new Date(b.deadline));

    const catLabel = { mandatory: 'POVINNÉ', important: 'DŮLEŽITÉ', optional: 'VOLITELNÉ' };
    const catBadge = { mandatory: 'badge-man', important: 'badge-imp', optional: 'badge-opt' };

    document.getElementById('tasksContainer').innerHTML = filtered.length
        ? filtered.map(t => {
            const isDone = completed[t.key] || false;
            return `
            <div class="task-item ${isDone ? 'done' : ''}">
                <div class="task-check ${isDone ? 'checked' : ''}" onclick="toggleTask('${t.key}')"></div>
                <div class="task-content">
                    <div class="task-name">${t.title}</div>
                    <div class="task-meta">
                        <span>📅 ${formatDate(t.deadline)}</span>
                        <span>👤 ${t.assign}</span>
                        <span class="badge ${catBadge[t.cat]}">${catLabel[t.cat]}</span>
                        ${t.price ? `<span>💰 ${t.price.toLocaleString('cs')} Kč</span>` : ''}
                    </div>
                </div>
            </div>`;
        }).join('')
        : '<div style="text-align:center;color:var(--text-muted);padding:16px;">Žádné úkoly'
          + (hideDone ? ' (hotové schovány)' : '') + '</div>';
}
```

- [ ] **Step 8: Add toggleHideDone function (after toggleTask, line 489)**

```js
function toggleHideDone() {
    hideDone = !hideDone;
    saveHideDone();
    updateHideDoneUI();
    renderTasks();
    renderMandatorySummary();
    showToast(hideDone ? '👁 Hotové schovány' : '👁 Zobrazuji i hotové');
}
function updateHideDoneUI() {
    const btn = document.getElementById('hideDoneToggle');
    if (hideDone) btn.classList.add('active');
    else btn.classList.remove('active');
}
```

- [ ] **Step 9: Add toggleBudget function + budget collapse logic (after updateHideDoneUI)**

```js
function toggleBudget() {
    budgetCollapsed = !budgetCollapsed;
    saveBudgetCollapsed();
    updateBudgetUI();
}
function updateBudgetUI() {
    const body = document.getElementById('budgetBody');
    const btn = document.getElementById('budgetCollapseBtn');
    const summary = document.getElementById('budgetSummary');
    if (budgetCollapsed) {
        body.classList.add('collapsed');
        btn.classList.remove('open');
        summary.classList.add('visible');
    } else {
        body.classList.remove('collapsed');
        btn.classList.add('open');
        summary.classList.remove('visible');
    }
}
```

- [ ] **Step 10: Modify renderBudget() to use new element IDs and update summary**

Replace `renderBudget()` body to use `budgetTableBody` ID and update summary:

```js
function renderBudget() {
    const tbody = document.getElementById('budgetTableBody');
    tbody.innerHTML = '';
    budgetItems.forEach((item, i) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${item.name}</td>`;
        const td = document.createElement('td');
        td.style.textAlign = 'right';
        const input = document.createElement('input');
        input.type = 'number'; input.value = item.cost; input.step = '500';
        input.addEventListener('change', () => {
            budgetItems[i].cost = parseInt(input.value) || 0;
            updateBudgetTotal(); saveBudget();
        });
        td.appendChild(input); tr.appendChild(td);
        tbody.appendChild(tr);
    });
    updateBudgetTotal();
    // Apply initial collapse state
    updateBudgetUI();
}
```

- [ ] **Step 11: Modify updateBudgetTotal() to also update the summary element**

Add after the existing `updateBudgetTotal()` body:

```js
function updateBudgetTotal() {
    const total = budgetItems.reduce((s, i) => s + i.cost, 0);
    const max = Math.round(total * 1.2);
    document.getElementById('totalBudgetVal').textContent = total.toLocaleString('cs') + ' Kč';
    document.getElementById('maxToleranceVal').textContent = max.toLocaleString('cs') + ' Kč';
    const el = document.getElementById('totalBudgetVal');
    el.style.color = total > 100000 ? 'var(--danger)' : 'var(--success)';
    // Collapsed summary
    const summaryEl = document.getElementById('budgetSummaryTotal');
    if (summaryEl) {
        summaryEl.textContent = total.toLocaleString('cs') + ' Kč';
        summaryEl.style.color = total > 100000 ? 'var(--danger)' : 'var(--success)';
    }
}
```

- [ ] **Step 12: Add updateHideDoneUI() and updateBudgetUI() calls to init()**

At the end of `init()`, before the final `init()` call (line 531), add:

```js
    updateHideDoneUI();
    // updateBudgetUI() already called inside renderBudget()
```

And modify the `init()` call order so that `updateHideDoneUI()` runs after the DOM is ready:

```js
    // ...existing renderBudget() call (which now calls updateBudgetUI)...
    updateHideDoneUI();
```

- [ ] **Step 13: Add toggleHideDone as window-level handler (inline onclick needs global scope)**

Since `toggleHideDone()` is called from inline `onclick` in HTML, it must be a global. All functions in this file are already global (no module scope). The function defined in Step 8 is already global. No extra step needed — just ensure the function name matches `onclick="toggleHideDone()"`.

- [ ] **Step 14: Commit**

```bash
git add index.html
git commit -m "feat: hide-done toggle + collapsed budget in v1"
```

---

### Task 2: Create v3music — full copy of v1 with audio player

**Files:**
- Create: `v3music/index.html`

- [ ] **Step 1: Create v3music directory and copy v1**

```bash
mkdir -p v3music
cp index.html v3music/index.html
```

- [ ] **Step 2: In v3music/index.html, add audio player CSS to the <style> block**

After the `.btn-danger` rule (line 119), add:

```css
/* Audio player */
.audio-panel {
    position: fixed; bottom: 80px; right: 16px; z-index: 90;
    background: var(--bg-card); border: 1px solid var(--border);
    border-radius: 16px; padding: 10px 14px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    display: flex; flex-direction: column; gap: 6px; align-items: center;
    font-size: 0.75rem; transition: opacity 0.3s;
}
.audio-panel.hidden { opacity: 0; pointer-events: none; }
.audio-row { display: flex; align-items: center; gap: 8px; }
.audio-btn {
    width: 40px; height: 40px; border-radius: 50%; border: none;
    cursor: pointer; font-size: 1.1rem; display: flex; align-items: center;
    justify-content: center; transition: all 0.2s;
    background: var(--primary); color: #fff;
}
.audio-btn.playing { background: var(--success); }
.audio-btn-sm {
    padding: 4px 10px; border-radius: 12px; border: 1px solid var(--border);
    background: var(--bg); color: var(--text-muted); font-size: 0.7rem;
    cursor: pointer; font-family: inherit;
}
.audio-btn-sm.active-track { background: var(--primary); color: #fff; border-color: var(--primary); }
.audio-track-label { font-size: 0.7rem; color: var(--text-muted); max-width: 120px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.header-audio-btn {
    display: inline-flex; align-items: center; gap: 4px;
    padding: 4px 10px; border-radius: 12px; background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.25); color: #fff;
    font-size: 0.72rem; cursor: pointer; font-family: inherit;
    margin-top: 8px; transition: background 0.2s;
}
.header-audio-btn:hover { background: rgba(255,255,255,0.25); }
```

- [ ] **Step 3: Add header audio button to the header div**

Replace the header div (lines 132-137) to include the audio play button:

```html
<div class="header">
    <h1>💍 Svatba Paprčkovi 2026</h1>
    <div class="sub">29. srpna 2026 · Nová radnice Ostrava · Koliba U Zlatého Jarouše</div>
    <div class="countdown" id="countdown">--</div>
    <div class="countdown-label" id="countdownLabel">dní do svatby</div>
    <button class="header-audio-btn" id="headerAudioBtn" onclick="toggleAudio()">
        🎵 Přehrát
    </button>
</div>
```

- [ ] **Step 4: Add floating audio panel + floating play button before closing `</div>` of `.container`**

After the footer div (before `</div>` on line 199), add:

```html
    <!-- Floating audio button -->
    <button class="audio-btn" id="floatingAudioBtn" onclick="toggleAudio()" style="position:fixed;bottom:20px;right:16px;z-index:100;box-shadow:0 4px 16px rgba(0,0,0,0.25);" title="Přehrát / Pozastavit">▶</button>

    <!-- Audio track selector panel -->
    <div class="audio-panel hidden" id="audioPanel">
        <div class="audio-row">
            <button class="audio-btn-sm active-track" data-track="0" onclick="switchTrack(0)">DJ Ötzi</button>
            <button class="audio-btn-sm" data-track="1" onclick="switchTrack(1)">Hasselhoff</button>
        </div>
        <div class="audio-track-label" id="audioTrackLabel">DJ Ötzi — Sweet Caroline</div>
    </div>
```

- [ ] **Step 5: Add <audio> element before `<script>`**

Before the `<script>` tag on line 203, add:

```html
<audio id="bgAudio" preload="auto" loop style="display:none;"></audio>
```

- [ ] **Step 6: Add audio JS constants and state (after existing LS key constants, line 208)**

```js
const LS_AUDIO_PLAYING = 'svatba_audio_playing';
const LS_AUDIO_TRACK = 'svatba_audio_track';
const LS_AUDIO_TIME = 'svatba_audio_time';
const AUDIO_TRACKS = [
    { name: 'DJ Ötzi — Sweet Caroline (Party Remix)', src: 'media/Sweet_Caroline_Remix.mp3', refrain: 65 },
    { name: 'David Hasselhoff — Sweet Caroline', src: 'media/Sweet_Caroline_Hoff.mp3', refrain: 68 }
];
let currentTrack = 0;
let audioPlaying = false;
```

- [ ] **Step 7: Add audio load/save functions (after loadState/saveDone area, line 333)**

```js
function loadAudioState() {
    try {
        const t = localStorage.getItem(LS_AUDIO_TRACK);
        if (t !== null) currentTrack = parseInt(t) || 0;
        const p = localStorage.getItem(LS_AUDIO_PLAYING);
        if (p !== null) audioPlaying = (p === 'true');
        const tm = localStorage.getItem(LS_AUDIO_TIME);
        if (tm !== null) {
            const audio = document.getElementById('bgAudio');
            audio.currentTime = parseFloat(tm) || 0;
        }
    } catch (e) {}
}
function saveAudioState() {
    try {
        const audio = document.getElementById('bgAudio');
        localStorage.setItem(LS_AUDIO_TRACK, currentTrack.toString());
        localStorage.setItem(LS_AUDIO_PLAYING, audioPlaying.toString());
        if (audio && !audio.paused) localStorage.setItem(LS_AUDIO_TIME, audio.currentTime.toString());
    } catch (e) {}
}
```

- [ ] **Step 8: Add audio control functions (before init)**

```js
function initAudio() {
    const audio = document.getElementById('bgAudio');
    audio.src = AUDIO_TRACKS[currentTrack].src;
    audio.load();
    loadAudioState();
    updateAudioUI();
}

function toggleAudio() {
    const audio = document.getElementById('bgAudio');
    if (!audio.src || audio.src === window.location.href) {
        audio.src = AUDIO_TRACKS[currentTrack].src;
        audio.load();
    }
    if (audio.paused) {
        // If this is first play, jump to refrain
        if (audio.currentTime < 1) {
            audio.currentTime = AUDIO_TRACKS[currentTrack].refrain;
        }
        audio.play().then(() => {
            audioPlaying = true;
            updateAudioUI();
            saveAudioState();
        }).catch(e => { console.error('Audio play failed:', e); });
    } else {
        audio.pause();
        audioPlaying = false;
        updateAudioUI();
        saveAudioState();
    }
}

function switchTrack(idx) {
    currentTrack = idx;
    const audio = document.getElementById('bgAudio');
    const wasPlaying = !audio.paused;
    audio.src = AUDIO_TRACKS[idx].src;
    audio.load();
    audio.currentTime = AUDIO_TRACKS[idx].refrain;
    if (wasPlaying) {
        audio.play().then(() => {
            audioPlaying = true;
            updateAudioUI();
            saveAudioState();
        }).catch(e => {});
    } else {
        audioPlaying = false;
        updateAudioUI();
        saveAudioState();
    }
}

function updateAudioUI() {
    const audio = document.getElementById('bgAudio');
    const headerBtn = document.getElementById('headerAudioBtn');
    const floatBtn = document.getElementById('floatingAudioBtn');
    const panel = document.getElementById('audioPanel');
    const label = document.getElementById('audioTrackLabel');

    // Header button
    headerBtn.textContent = audioPlaying ? '🔊 Hraje' : '🎵 Přehrát';

    // Floating button
    floatBtn.textContent = audioPlaying ? '⏸' : '▶';
    floatBtn.classList.toggle('playing', audioPlaying);

    // Track label
    label.textContent = AUDIO_TRACKS[currentTrack].name;

    // Track buttons
    panel.querySelectorAll('.audio-btn-sm').forEach((btn, i) => {
        btn.classList.toggle('active-track', i === currentTrack);
    });
}

// First-tap autoplay: start audio on first user interaction
let audioStarted = false;
function onFirstInteraction() {
    if (audioStarted) return;
    audioStarted = true;
    const audio = document.getElementById('bgAudio');
    if (!audio.src || audio.src === window.location.href) {
        audio.src = AUDIO_TRACKS[currentTrack].src;
        audio.load();
    }
    audio.currentTime = AUDIO_TRACKS[currentTrack].refrain;
    audio.play().then(() => {
        audioPlaying = true;
        updateAudioUI();
        saveAudioState();
    }).catch(e => {});
    // Remove listeners after first fire
    document.removeEventListener('click', onFirstInteraction);
    document.removeEventListener('touchstart', onFirstInteraction);
}
```

- [ ] **Step 9: Register first-tap listeners and init audio in init()**

Add at the end of `init()`, before the final `init()` call:

```js
    initAudio();
    document.addEventListener('click', onFirstInteraction);
    document.addEventListener('touchstart', onFirstInteraction);
```

- [ ] **Step 10: Save audio time periodically and on unload**

Add in `init()` or at script bottom:

```js
    // Save audio position every 5 seconds
    setInterval(saveAudioState, 5000);
    window.addEventListener('beforeunload', saveAudioState);
```

- [ ] **Step 11: Commit**

```bash
git add v3music/index.html
git commit -m "feat: v3music — v1 copy + audio player (DJ Ötzi + Hasselhoff)"
```

---

### Task 3: Add media files to git

**Files:**
- Git add: `media/Sweet_Caroline_Remix.mp3`, `media/Sweet_Caroline_Hoff.mp3`

- [ ] **Step 1: Add only the 2 needed MP3 files to git**

```bash
git add media/Sweet_Caroline_Remix.mp3 media/Sweet_Caroline_Hoff.mp3
```

- [ ] **Step 2: Verify .gitignore does NOT block media/**

Check that no pattern in `.gitignore` matches `media/*.mp3`. Current `.gitignore` has: `node_modules/`, `chat_export_*.md`, `.superpowers/`, `.deepseek/`, `dist/`, `.vite/`, `.vscode/`, `$null`, `%SystemDrive%/`, `package*.json`, `*.lock`. None of these block `media/`. No change needed.

- [ ] **Step 3: Commit**

```bash
git commit -m "feat: add Sweet Caroline MP3s for v3music player"
```

---

### Task 4: Deploy switch — DEPLOY_DEFAULT + Actions update

**Files:**
- Create: `DEPLOY_DEFAULT`
- Modify: `.github/workflows/deploy.yml`

- [ ] **Step 1: Create DEPLOY_DEFAULT file**

Write `v1` (no trailing newline):

```bash
echo -n "v1" > DEPLOY_DEFAULT
```

- [ ] **Step 2: Update deploy.yml to read DEPLOY_DEFAULT and deploy v3music**

Replace `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [master]

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/checkout@v4
      - name: Prepare deploy files
        run: |
          DEPLOY_DEFAULT=$(cat DEPLOY_DEFAULT 2>/dev/null || echo "v1")
          echo "Deploy default: $DEPLOY_DEFAULT"
          mkdir deploy_out
          # Copy the selected default version's index.html as root /
          if [ "$DEPLOY_DEFAULT" = "v3music" ]; then
            cp v3music/index.html deploy_out/
          else
            cp index.html deploy_out/
          fi
          cp -r public/* deploy_out/ 2>/dev/null || true
          cp -r v0 deploy_out/ 2>/dev/null || true
          cp -r v2 deploy_out/ 2>/dev/null || true
          cp -r v3music deploy_out/ 2>/dev/null || true
          cp -r Older deploy_out/ 2>/dev/null || true
          cp -r Older_up2date deploy_out/ 2>/dev/null || true
      - name: Reset DEPLOY_DEFAULT to v1
        run: |
          echo -n "v1" > DEPLOY_DEFAULT
          git config user.name "github-actions"
          git config user.email "github-actions@github.com"
          git add DEPLOY_DEFAULT
          git commit -m "reset DEPLOY_DEFAULT to v1" || true
          git push origin master || true
      - uses: actions/configure-pages@v4
      - uses: actions/upload-pages-artifact@v3
        with:
          path: ./deploy_out
      - uses: actions/deploy-pages@v4
        id: deployment
```

- [ ] **Step 3: Commit**

```bash
git add DEPLOY_DEFAULT .github/workflows/deploy.yml
git commit -m "feat: deploy switch — DEPLOY_DEFAULT controls which version is /"
```

---

### Task 5: Update cross-file documentation

**Files:**
- Modify: `CLAUDE.md`, `README.md`, `walkthrough.md`, `CHANGELOG.md`

- [ ] **Step 1: Update CLAUDE.md — version table + deploy**

Add v3music to the version architecture table (line ~18-27). Replace the triple-version summary:

```markdown
v0: v0/index.html       ← v0 archive (20 tasks, Aug 29 date, Svatba_001 baseline)
v1: index.html          ← fetch-based, reads tasks.md from GitHub Raw, localStorage for state only
v2: v2/index.html       ← fetches MD from GitHub, PIN-unlocked write via API
v3music: v3music/index.html ← v1 + audio player (2 tracks, 3 synced controls), deploy switch
```

Update deploy line (~line 100):

```markdown
- `/` = v1 (default production), `/v2/` = v2, `/v3music/` = v1+audio
- `DEPLOY_DEFAULT` file controls which version serves as `/` (Actions reads it, resets to v1 after)
```

- [ ] **Step 2: Update README.md — quick links table**

Add v3music row after v2 row (line 11):

```markdown
| **v3music (v1+audio)** | https://doma77git.github.io/PaprckoviSvatba2026/v3music/ |
```

- [ ] **Step 3: Update walkthrough.md — version table + deploy**

Add v3music to the "Tři verze" table (line 16-20):

```markdown
| **v3music** | `/v3music/` | v1 + audio přehrávač | Kopie v1 + 2 skladby (DJ Ötzi, Hasselhoff), 3 ovladače |
```

Add v3music to deploy live links (line 132-136), add after v2 line:

```markdown
  - [v3music](https://doma77git.github.io/PaprckoviSvatba2026/v3music/)
```

- [ ] **Step 4: Update CHANGELOG.md — add 1.3.2 entry**

Insert after the `## [Unreleased]` section (line 8), before `## [1.3.1]`:

```markdown
## [1.3.2] — 2026-05-27

### Added
- **Hide-done toggle:** v1 — completed tasks hidden by default, toggle button in checklist header ([index.html](index.html))
- **Collapsed budget:** v1 — budget section default collapsed, expand on click, summary visible ([index.html](index.html))
- **v3music:** New version — v1 copy + background audio player with 2 tracks (DJ Ötzi, Hasselhoff), 3 synced controls ([v3music/index.html](v3music/index.html))
- **Deploy switch:** `DEPLOY_DEFAULT` file controls root `/` version, Actions auto-resets to `v1` ([DEPLOY_DEFAULT](DEPLOY_DEFAULT))

### Changed
- Deploy workflow: reads DEPLOY_DEFAULT, deploys selected version as `/`, resets after ([.github/workflows/deploy.yml](.github/workflows/deploy.yml))
- All docs synced: CLAUDE.md, README, walkthrough updated with v3music

```

- [ ] **Step 5: Commit**

```bash
git add CLAUDE.md README.md walkthrough.md CHANGELOG.md
git commit -m "docs: sync v1 improvements + v3music across all docs"
```

---

### Task 6: Final verification

- [ ] **Step 1: Verify git status is clean**

```bash
git status
```
Expected: only untracked files should be the extra 7 media files (not needed for commit) and `.claude/ralph-loop.local.md`, `.reasonix/truncated-results/`.

- [ ] **Step 2: Verify file structure**

```bash
ls -la index.html v3music/index.html DEPLOY_DEFAULT .github/workflows/deploy.yml
```
Expected: all 4 files exist.

- [ ] **Step 3: Run data integrity check**

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
print(f'Tasks: {len(lines)} (target: 37) | Budget: {total:,} Kc (target: 100000)')
print(f'Mand: {m:,} | Imp: {i:,} | Opt: {o:,}')
print('OK' if total == 100000 and len(lines) == 37 else 'GAP — fix before commit')
"
```
Expected: `Tasks: 37 (target: 37) | Budget: 100,000 Kc (target: 100000)` and `OK`

- [ ] **Step 4: Check all cross-references in updated docs**

```bash
grep -n "v3music" CLAUDE.md README.md walkthrough.md CHANGELOG.md
```
Expected: at least one match in each file.

- [ ] **Step 5: Final commit if any verification fixes**

```bash
git status
# If clean, done. If fixes needed:
git add -A  # only if small doc fixes
git commit -m "chore: verification fixes"
```
