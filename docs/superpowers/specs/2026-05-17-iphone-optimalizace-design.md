# iPhone Optimalizace — Svatba Paprčkovi 2026

**Datum:** 2026-05-17
**Cíl:** Zlepšit čitelnost, layout a výkon na iPhone 14/15/16 (Safari)
**Rozsah:** CSS + JS úpravy v `src/index.html`, single-file zachován

---

## 1. Fluidní typografie (mírný clamp)

HTML base se nemění (16px). Jednotlivé elementy používají `clamp()` pro plynulé škálování mezi 320–430px šířkou viewportu.

| Element | Původní | Nové |
|---------|---------|------|
| Header h1 | `1.7rem` (27px) | `clamp(1.5rem, 5vw, 2rem)` (24–34px) |
| `.sub` | `0.82rem` (13px) | `clamp(0.75rem, 2.5vw, 0.9rem)` (12–15px) |
| `.dashboard-card .number` | `1.6rem` (26px) | `clamp(1.4rem, 4.5vw, 1.8rem)` (22–31px) |
| `.dashboard-card .label` | `0.62rem` (10px) | `clamp(0.65rem, 2vw, 0.72rem)` (10–12px) |
| `.task-card .title` | `0.84rem` (13px) | `clamp(0.82rem, 3vw, 0.95rem)` (13–16px) |
| `.meta` | `0.65rem` (10px) | `clamp(0.68rem, 2.2vw, 0.76rem)` (11–13px) |
| `.badge` | `0.6rem` (10px) | `clamp(0.62rem, 2vw, 0.7rem)` (10–12px) |
| Urgency label | `0.55rem` (9px) | `clamp(0.6rem, 1.8vw, 0.65rem)` (10–11px) |
| `.section-title` | `0.9rem` (14px) | `clamp(0.85rem, 2.8vw, 0.95rem)` (14–16px) |
| `.section-title .count` | `0.65rem` (10px) | `clamp(0.62rem, 1.8vw, 0.7rem)` (10–12px) |
| Nav button font | `0.6rem` (10px) | `clamp(0.62rem, 1.8vw, 0.68rem)` (10–11px) |
| Nav icon | `1.2rem` (19px) | `clamp(1.1rem, 3.5vw, 1.3rem)` (18–22px) |

**Minimální garantovaná velikost:** nic pod 10px (teď nejmenší 8–9px).

---

## 2. Layout fixy

### 2.1 Budget řádky — stackovaný flex místo gridu

**Problém:** `grid-template-columns: 1fr 65px 70px 26px` — 161px fixní, na 320px šířce zbývá na název ~110px.
**Fix:** Dvouřádkový flex layout — řádek 1: název + cena, řádek 2: input + checkbox + "odhad" label.

```css
.budget-row {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 8px 12px;
}
.budget-row .top-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.budget-row .bottom-row {
  display: flex;
  align-items: center;
  gap: 8px;
}
```

### 2.2 Task karty — odstranit max-height ořez

**Problém:** `max-height: 280px` může oříznout delší názvy. Animace completion (`max-height: 0`) zůstává.
**Fix:** Odebrat `max-height` z normálního stavu, ponechat pouze pro `.done` animaci. Zvětšit checkbox na 24px.

```css
.task-card {
  /* max-height: 280px — REMOVED */
  ...
}
.task-card .checkbox {
  width: 24px; height: 24px;  /* bylo 22px */
}
```

### 2.3 Header — zjednodušení

**Problém:** Animace `background-size: 400%` způsobuje GPU repaint. Dva řádky subtextu + date-badge jsou redundantní.
**Fix:** Odebrat animaci pozadí. Sloučit sub a date-badge do jednoho řádku. Zvětšit countdown jako hlavní vizuální prvek.

```css
.header {
  background: linear-gradient(135deg, #5c1e1e, var(--red-dark), var(--red));
  /* animation: headerShift — REMOVED */
}
.header h1 { font-size: clamp(1.5rem, 5vw, 2rem); }
```

Countdown zůstává, date-badge a sub sloučeny do jednoho informačního řádku pod nadpisem.

### 2.4 Touch targety — minimum 44px everywhere

Všechny interaktivní prvky musí mít `min-height` ≥ 44px (již nastaveno přes `--tap-min: 44px`, ověřit konzistenci). Checkboxy zvětšeny na 24×24px (teď 22×22px).

---

## 3. Výkonnostní optimalizace

### 3.1 Lazy rendering views

**Problém:** `renderAll()` překresluje všech 5 views (tasks, budget, timeline, settings, stats) při každé změně stavu.
**Fix:** Renderovat jen aktuálně viditelnou view + header/dashboard (vždy viditelné).

```js
function renderAll() {
  updateCountdown();
  renderStats();           // vždy — header + dashboard
  renderCurrentView();     // jen aktivní view
  updateNav();             // nav state
}

function renderCurrentView() {
  switch (state.view) {
    case 'tasks': renderTasksUI(); break;
    case 'budget': renderBudgetUI(); break;
    case 'timeline': renderTimelineUI(); break;
    case 'settings': renderSettingsUI(); break;
  }
}
```

### 3.2 Odebrat drahý backdrop-filter z karet

**Problém:** `backdrop-filter: blur()` na každé task-card, dashboard-card a weather-card způsobuje drahé GPU operace při scrollování.
**Fix:** Nahradit `backdrop-filter` jednoduchou poloprůhlednou barvou pozadí. Efekt je na iPhonu minimálně viditelný, ale výkonnostní dopad velký.

```css
/* Před */
.dashboard-card {
  background: rgba(255,255,255,.65);
  backdrop-filter: blur(12px);
}
/* Po */
.dashboard-card {
  background: rgba(255,255,255,.92);
  /* backdrop-filter: blur — REMOVED */
}
```

### 3.3 Animace — will-change a paint reduction

- Header: odebrat `animation: headerShift` (background-position animace) — řešeno v 2.3
- Přidat `will-change: transform` na karty pro plynulejší hover animace
- `content-visibility: auto` na `.view` kontejnery pro skip rendering skrytých views

```css
.view { content-visibility: auto; }
.view.active { content-visibility: visible; }
.task-card { will-change: transform; }
```

### 3.4 Odebrat nepotřebné iOS-Safari hacky

`overscroll-behavior: none` brání "pull to refresh" a "swipe back" — může působit proti-nativně. Ponechat jen na root elementu, odebrat z `body`.

---

## 4. Co se nemění

- Single-file struktura (`index.html` obsahuje vše)
- Data model (TASKS, state, localStorage)
- Cloud sync logika (GitHub API)
- Weather API
- Tmavý režim
- 4-view navigace (Tasks, Budget, Timeline, Settings)
- GitHub Pages deployment

---

## 5. Success kritéria

1. **Čitelnost:** Nejmenší text ≥ 10px na šířce 320px+. Žádný text pod 10px.
2. **Layout:** Budget tabulka se nerozbije na šířce 320px. Task názvy nejsou oříznuté.
3. **Výkon:** `renderAll()` volá max 2 render funkce místo 7. Žádný `backdrop-filter: blur()`.
4. **Touch:** Všechny interaktivní prvky ≥ 44px výška, checkboxy ≥ 24×24px.
5. **Zpětná kompatibilita:** Aplikace funguje identicky na desktopu.
