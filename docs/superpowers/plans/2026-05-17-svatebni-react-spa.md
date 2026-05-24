# Svatební React SPA — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Přepis svatebního webu Paprčkovi z vanilla HTML monolitu (1041 ř.) do React SPA — Vite + Tailwind + React Router.

**Architecture:** 2 routy — `/` veřejná landing page (6 narativních sekcí) a `/planovani` PIN-chráněný plánovač (dashboard, tasky, budget, počasí, sync). State přes 3 React Context providery, persistence localStorage + GitHub API.

**Tech Stack:** Vite 7, React 19, Tailwind CSS 4, React Router 7, Open-Meteo API, GitHub API

---

## File Structure

```
C:\dev\PS7\
├── index.html                    # Vite entry (root)
├── package.json
├── vite.config.js
├── public/
│   ├── manifest.json
│   └── favicon.svg
├── src/
│   ├── main.jsx                  # React root + BrowserRouter
│   ├── App.jsx                   # Layout + Routes
│   ├── index.css                 # Tailwind + custom props
│   ├── contexts/
│   │   ├── WeddingContext.jsx    # tasks, budget, guests
│   │   ├── UIContext.jsx         # dark mode, PIN
│   │   └── WeatherContext.jsx    # Open-Meteo
│   ├── data/
│   │   ├── tasks.js             # 35 tasks
│   │   └── guests.js            # guest list
│   ├── hooks/
│   │   ├── useCountdown.js
│   │   ├── useCloudSync.js
│   │   └── useScrollTop.js
│   ├── pages/
│   │   ├── LandingPage.jsx
│   │   └── PlanningPage.jsx
│   ├── components/
│   │   ├── layout/
│   │   │   ├── Header.jsx
│   │   │   └── ScrollToTop.jsx
│   │   ├── landing/
│   │   │   ├── HeroSection.jsx
│   │   │   ├── StoryTimeline.jsx
│   │   │   ├── VenueInfo.jsx
│   │   │   ├── GalleryGrid.jsx
│   │   │   ├── Lightbox.jsx
│   │   │   ├── RSVPSection.jsx
│   │   │   └── PlannerNavBanner.jsx
│   │   ├── planning/
│   │   │   ├── PinGate.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── WeatherCard.jsx
│   │   │   ├── TaskList.jsx
│   │   │   ├── TaskItem.jsx
│   │   │   ├── BudgetTracker.jsx
│   │   │   └── Settings.jsx
│   │   └── shared/
│   │       └── ProgressBar.jsx
│   └── lib/
│       ├── github-sync.js        # GitHub API helpers
│       └── weather.js            # Open-Meteo fetcher
└── .github/workflows/deploy.yml  # updated for Vite
```

---

### Task 1: Project scaffolding

**Files:**
- Create: `package.json`, `vite.config.js`, `index.html`, `src/main.jsx`, `src/index.css`

- [ ] **Step 1: Initialize package.json with all dependencies**

```json
{
  "name": "svatba-paprckovi",
  "private": true,
  "version": "4.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-router-dom": "^7.0.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.4.0",
    "@tailwindcss/vite": "^4.0.0",
    "tailwindcss": "^4.0.0",
    "vite": "^7.0.0"
  }
}
```

- [ ] **Step 2: Install dependencies**

Run: `cd C:/dev/PS7 && npm install`
Expected: packages installed, `node_modules/` created

- [ ] **Step 3: Create vite.config.js**

```js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [react(), tailwindcss()],
  base: '/PaprckoviSvatba2026/',
  build: { outDir: 'dist' }
});
```

- [ ] **Step 4: Create root index.html (Vite entry)**

Write: `C:\dev\PS7\index.html`

```html
<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="Svatba 2026">
  <meta name="theme-color" content="#8b3a3a">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
  <link rel="manifest" href="/PaprckoviSvatba2026/manifest.json">
  <title>💒 Svatba Paprčkovi 2026</title>
</head>
<body class="bg-[#faf7f2] text-[#2d2a24] font-[Cormorant_Garamond]">
  <div id="root"></div>
  <script type="module" src="/src/main.jsx"></script>
</body>
</html>
```

- [ ] **Step 5: Create src/index.css**

```css
@import "tailwindcss";

@theme {
  --color-wedding: #8b3a3a;
  --color-wedding-dark: #6b2e2e;
  --color-wedding-light: #c46a6a;
  --color-gold: #d4a017;
  --color-cream: #faf7f2;
  --color-warm: #2d2a24;
  --color-muted: #999;
  --color-card: #fff;
  --color-border: #e8e0d8;
  --font-wedding: 'Cormorant Garamond', Garamond, Georgia, serif;
}

[data-theme="dark"] {
  --color-cream: #1a1816;
  --color-card: #252220;
  --color-border: #3a3530;
  --color-warm: #e8e4dd;
  --color-muted: #8a8580;

  & body {
    background: linear-gradient(175deg, #1a1816 0%, #1f1c19 40%, #1a1715 100%);
  }
}

body {
  font-family: var(--font-wedding);
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

::selection {
  background: rgba(139, 58, 58, 0.2);
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

- [ ] **Step 6: Create src/main.jsx**

```jsx
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App';
import './index.css';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter basename="/PaprckoviSvatba2026">
      <App />
    </BrowserRouter>
  </StrictMode>
);
```

- [ ] **Step 7: Verify dev server starts**

Run: `cd C:/dev/PS7 && npm run dev`
Expected: Vite dev server starts, no errors, blank page renders

- [ ] **Step 8: Commit**

```bash
cd C:/dev/PS7
git add package.json package-lock.json vite.config.js index.html src/main.jsx src/index.css
git commit -m "scaffold: Vite + React + Tailwind + React Router setup"
```

---

### Task 2: Data files — extract from original app

**Files:**
- Create: `src/data/tasks.js`, `src/data/guests.js`

- [ ] **Step 1: Create src/data/tasks.js**

```js
export const WEDDING_DATE = new Date(2026, 7, 29);

export const CAT_ORDER = ['mandatory', 'important', 'optional'];

export const CAT_LABELS = {
  mandatory: '🔴 Povinné',
  important: '🟡 Důležité',
  optional: '🟢 Volitelné'
};

export const CAT_COLORS = {
  mandatory: '#c0392b',
  important: '#b8860b',
  optional: '#27ae60'
};

export const TASKS = [
  { id: 1, cat: 'mandatory', title: 'Termín — konfirmace termínu', assign: 'Mamka', deadline: '29.5.2026', dl: '2026-05-29', price: 0, tl: '2026-05', note: '✅ Hotovo — termín potvrzen' },
  { id: 2, cat: 'mandatory', title: 'Návštěva radnice (Nová radnice Ostrava)', assign: 'Mamka', deadline: '11.5.2026', dl: '2026-05-11', price: 0, tl: '2026-05', note: '✅ Hotovo — minulé pondělí 11.5.2026' },
  { id: 3, cat: 'mandatory', title: 'Informování dětí o termínu', assign: 'Mamka', deadline: '29.5.2026', dl: '2026-05-29', price: 0, tl: '2026-05', note: '✅ Hotovo — proběhlo' },
  { id: 4, cat: 'mandatory', title: 'Svědci — domluvení (Kikinka + Žanetka)', assign: 'Mamka', deadline: '15.5.2026', dl: '2026-05-15', price: 0, tl: '2026-05', note: '✅ Hotovo — domluveno 15.5.2026' },
  { id: 5, cat: 'mandatory', title: 'Obřad — domluva oddávajícího (11:15 Nová radnice)', assign: 'Kikinka', deadline: '30.6.2026', dl: '2026-06-30', price: 0, tl: '2026-06', note: '📅 Schůzka v pondělí — proběhne' },
  { id: 6, cat: 'mandatory', title: 'Obřad — dekorace a květiny na radnici', assign: 'Kikinka', deadline: '15.8.2026', dl: '2026-08-15', price: 3000, tl: '2026-08', note: '' },
  { id: 7, cat: 'mandatory', title: 'Obřad — doprava (radnice → Zlatá koliba)', assign: 'Taťka', deadline: '20.8.2026', dl: '2026-08-20', price: 3000, tl: '2026-08', note: '' },
  { id: 8, cat: 'mandatory', title: 'Hostina — Zlatá koliba (U Miloše) menu + catering', assign: 'Žanetka', deadline: '15.7.2026', dl: '2026-07-15', price: 30000, tl: '2026-07', note: '✅ Potvrzeno — Miloš' },
  { id: 9, cat: 'mandatory', title: 'Hostina — nápoje a bar', assign: 'Žanetka', deadline: '1.8.2026', dl: '2026-08-01', price: 6000, tl: '2026-08', note: 'odhad' },
  { id: 10, cat: 'mandatory', title: 'Hostina — svatební dort', assign: 'Mamka', deadline: '20.8.2026', dl: '2026-08-20', price: 3000, tl: '2026-08', note: '' },
  { id: 11, cat: 'mandatory', title: 'Právní — oddací list, podpisy a doklady', assign: 'Kikinka', deadline: '20.8.2026', dl: '2026-08-20', price: 0, tl: '2026-08', note: '' },
  { id: 12, cat: 'mandatory', title: 'Právní — změna příjmení (Mamka)', assign: 'Mamka', deadline: '5.9.2026', dl: '2026-09-05', price: 0, tl: '2026-09', note: 'po svatbě' },
  { id: 13, cat: 'mandatory', title: 'Oblečení — svatební šaty (Mamka)', assign: 'Mamka', deadline: '15.7.2026', dl: '2026-07-15', price: 12000, tl: '2026-07', note: '' },
  { id: 14, cat: 'mandatory', title: 'Oblečení — oblek a sako (Taťka)', assign: 'Taťka', deadline: '15.7.2026', dl: '2026-07-15', price: 8000, tl: '2026-07', note: '' },
  { id: 15, cat: 'mandatory', title: 'Oblečení — doplňky (boty, šperky)', assign: 'Mamka', deadline: '1.8.2026', dl: '2026-08-01', price: 3000, tl: '2026-08', note: '' },
  { id: 16, cat: 'mandatory', title: 'Prstýnky — nákup a úprava', assign: 'Taťka', deadline: '15.7.2026', dl: '2026-07-15', price: 12000, tl: '2026-07', note: '' },
  { id: 17, cat: 'mandatory', title: 'Hosté — finální seznam hostů', assign: 'Mamka', deadline: '15.7.2026', dl: '2026-07-15', price: 0, tl: '2026-07', note: '' },
  { id: 18, cat: 'mandatory', title: 'Hosté — svatební oznámení', assign: 'Mamka', deadline: '10.7.2026', dl: '2026-07-10', price: 1500, tl: '2026-07', note: '' },
  { id: 19, cat: 'mandatory', title: 'Hosté — ubytování pro hosty', assign: 'Žanetka', deadline: '1.8.2026', dl: '2026-08-01', price: 5000, tl: '2026-08', note: 'odhad' },
  { id: 20, cat: 'important', title: 'Výzdoba — Zlatá koliba dekorace místnosti', assign: 'Žanetka', deadline: '15.8.2026', dl: '2026-08-15', price: 2000, tl: '2026-08', note: '' },
  { id: 21, cat: 'important', title: 'Výzdoba — fotokoutek / selfie zóna', assign: 'Taťka', deadline: '20.8.2026', dl: '2026-08-20', price: 2000, tl: '2026-08', note: '' },
  { id: 22, cat: 'important', title: 'Výzdoba — uvítací cedule, místa k sezení', assign: 'Mamka', deadline: '20.8.2026', dl: '2026-08-20', price: 500, tl: '2026-08', note: '' },
  { id: 23, cat: 'important', title: 'Dárky — pro svědky (Kikinka, Žanetka)', assign: 'Mamka', deadline: '10.8.2026', dl: '2026-08-10', price: 1500, tl: '2026-08', note: '' },
  { id: 24, cat: 'important', title: 'Dárky — pro rodiče a poděkování', assign: 'Taťka', deadline: '15.8.2026', dl: '2026-08-15', price: 1000, tl: '2026-08', note: '' },
  { id: 25, cat: 'important', title: 'Dárky — na přivítanou pro hosty', assign: 'Mamka', deadline: '20.8.2026', dl: '2026-08-20', price: 1000, tl: '2026-08', note: '' },
  { id: 26, cat: 'important', title: 'Program — první tanec (nácvik)', assign: 'Mamka', deadline: '15.8.2026', dl: '2026-08-15', price: 0, tl: '2026-08', note: '' },
  { id: 27, cat: 'important', title: 'Program — hry pro hosty a zábava', assign: 'Žanetka', deadline: '20.8.2026', dl: '2026-08-20', price: 500, tl: '2026-08', note: '' },
  { id: 28, cat: 'important', title: 'Program — svatební playlist / hudba', assign: 'Taťka', deadline: '20.8.2026', dl: '2026-08-20', price: 0, tl: '2026-08', note: '' },
  { id: 29, cat: 'important', title: 'Program — proslovy (svědci, rodiče)', assign: 'Kikinka', deadline: '25.8.2026', dl: '2026-08-25', price: 0, tl: '2026-08', note: '' },
  { id: 30, cat: 'important', title: 'Wellness — nehty, vlasy, líčení (Mamka)', assign: 'Mamka', deadline: '25.8.2026', dl: '2026-08-25', price: 2500, tl: '2026-08', note: '' },
  { id: 31, cat: 'important', title: 'Wellness — střih a úprava (Taťka)', assign: 'Taťka', deadline: '25.8.2026', dl: '2026-08-25', price: 500, tl: '2026-08', note: '' },
  { id: 32, cat: 'optional', title: 'Doplňky — drobnosti pro hosty (guestbook + favory)', assign: 'Mamka', deadline: '20.8.2026', dl: '2026-08-20', price: 1000, tl: '2026-08', note: '' },
  { id: 33, cat: 'optional', title: 'Doplňky — confetti a prskavky', assign: 'Žanetka', deadline: '25.8.2026', dl: '2026-08-25', price: 500, tl: '2026-08', note: '' },
  { id: 34, cat: 'optional', title: 'Doplňky — fotograf / dokumentace', assign: 'Kikinka', deadline: '25.8.2026', dl: '2026-08-25', price: 0, tl: '2026-08', note: '' },
  { id: 35, cat: 'optional', title: 'Svatební cesta — termín, ubytování a program', assign: 'Taťka', deadline: '15.7.2026', dl: '2026-07-15', price: 500, tl: '2026-07', note: '' }
];
```

- [ ] **Step 2: Create src/data/guests.js**

```js
export const GUESTS = [
  { name: 'Děti', count: 4, confirmed: null },
  { name: 'Mikeškovi', count: '2+2', confirmed: null },
  { name: 'Luki', count: '?', confirmed: null },
  { name: 'Peťa Z', count: '?', confirmed: null },
  { name: 'Peťa T', count: '?', confirmed: null },
  { name: 'Andrej', count: '?', confirmed: null },
  { name: 'Milada S', count: 1, confirmed: null },
  { name: 'Markéta S', count: '?', confirmed: null }
];
```

- [ ] **Step 3: Commit**

```bash
cd C:/dev/PS7 && git add src/data/ && git commit -m "data: extract 35 tasks + 8 guests from original app"
```

---

### Task 3: Core contexts — state management

**Files:**
- Create: `src/contexts/WeddingContext.jsx`, `src/contexts/UIContext.jsx`, `src/contexts/WeatherContext.jsx`
- Create: `src/lib/weather.js`

- [ ] **Step 1: Create src/lib/weather.js**

```js
const LAT = 49.82;
const LON = 18.26;

const ICONS = {
  0: '☀️', 1: '🌤️', 2: '⛅', 3: '☁️',
  45: '🌫️', 51: '🌦️', 61: '🌧️', 71: '❄️',
  80: '🌦️', 95: '⛈️'
};

export async function fetchWeather() {
  try {
    const res = await fetch(
      `https://api.open-meteo.com/v1/forecast?latitude=${LAT}&longitude=${LON}&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=auto`
    );
    const d = await res.json();
    if (!d.daily) throw new Error('no data');
    return {
      date: d.daily.time[0],
      max: d.daily.temperature_2m_max[0],
      min: d.daily.temperature_2m_min[0],
      icon: ICONS[d.daily.weathercode[0]] || '🌤️'
    };
  } catch {
    return null;
  }
}
```

- [ ] **Step 2: Create src/contexts/UIContext.jsx**

```jsx
import { createContext, useContext, useState, useEffect, useCallback } from 'react';

const UIContext = createContext(null);

export function UIProvider({ children }) {
  const [darkMode, setDarkMode] = useState(() => {
    const saved = localStorage.getItem('weddingState');
    return saved ? JSON.parse(saved).darkMode || false : false;
  });
  const [pin, setPin] = useState(() => localStorage.getItem('familyPin') || '2026');
  const [pinVerified, setPinVerified] = useState(false);
  const [toast, setToast] = useState(null);

  useEffect(() => {
    document.documentElement.toggleAttribute('data-theme', darkMode);
  }, [darkMode]);

  const toggleDarkMode = useCallback(() => setDarkMode(d => !d), []);

  const showToast = useCallback((msg, duration = 3000) => {
    setToast(msg);
    if (duration) setTimeout(() => setToast(null), duration);
  }, []);

  const verifyPin = useCallback((input) => {
    if (input === pin) { setPinVerified(true); return true; }
    return false;
  }, [pin]);

  return (
    <UIContext.Provider value={{ darkMode, toggleDarkMode, pin, setPin, pinVerified, verifyPin, toast, showToast }}>
      {children}
    </UIContext.Provider>
  );
}

export const useUI = () => useContext(UIContext);
```

- [ ] **Step 3: Create src/contexts/WeatherContext.jsx**

```jsx
import { createContext, useContext, useState, useEffect } from 'react';
import { fetchWeather } from '../lib/weather';

const WeatherContext = createContext(null);

export function WeatherProvider({ children }) {
  const [weather, setWeather] = useState(null);

  useEffect(() => {
    fetchWeather().then(setWeather);
  }, []);

  return (
    <WeatherContext.Provider value={weather}>
      {children}
    </WeatherContext.Provider>
  );
}

export const useWeather = () => useContext(WeatherContext);
```

- [ ] **Step 4: Create src/contexts/WeddingContext.jsx**

```jsx
import { createContext, useContext, useState, useCallback, useEffect } from 'react';
import { TASKS } from '../data/tasks';

const WeddingContext = createContext(null);

const STORAGE_KEY = 'weddingState';

function loadState() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) {
      const s = JSON.parse(raw);
      if (!s.showDone) s.showDone = { mandatory: false, important: false, optional: false };
      if (s.darkMode === undefined) s.darkMode = false;
      if (!s.version || s.version < 2) {
        s.done = [1, 2, 3, 4];
        s.budget = {};
        s.version = 2;
      }
      return s;
    }
  } catch {}
  return defaultState();
}

function defaultState() {
  return {
    version: 2,
    done: [],
    budget: {},
    view: 'tasks',
    filter: 'pending',
    sort: 'deadline',
    search: '',
    personFilter: '',
    showDone: { mandatory: false, important: false, optional: false },
    darkMode: false
  };
}

export function WeddingProvider({ children }) {
  const [state, setState] = useState(loadState);

  // Initialize budget entries for each task
  useEffect(() => {
    setState(prev => {
      const budget = { ...prev.budget };
      let changed = false;
      TASKS.forEach(t => {
        if (budget[t.id] === undefined) { budget[t.id] = t.price; changed = true; }
      });
      return changed ? { ...prev, budget } : prev;
    });
  }, []);

  const save = useCallback((next) => {
    setState(next);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
  }, []);

  const toggleTask = useCallback((id) => {
    setState(prev => {
      const idx = prev.done.indexOf(id);
      const done = idx > -1 ? prev.done.filter(i => i !== id) : [...prev.done, id];
      const next = { ...prev, done };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
      return next;
    });
    return state.done.indexOf(id) === -1; // true if just checked
  }, [state.done]);

  const setBudget = useCallback((id, value) => {
    setState(prev => {
      const budget = { ...prev.budget, [id]: value };
      const next = { ...prev, budget };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
      return next;
    });
  }, []);

  const setView = useCallback((view) => {
    setState(prev => {
      const next = { ...prev, view };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
      return next;
    });
  }, []);

  const applyCloudState = useCallback((cloudData) => {
    setState(prev => {
      const next = { ...prev };
      if (cloudData.done) next.done = cloudData.done;
      if (cloudData.budget) {
        next.budget = { ...prev.budget };
        Object.keys(cloudData.budget).forEach(k => {
          next.budget[Number(k)] = cloudData.budget[k];
        });
      }
      localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
      return next;
    });
  }, []);

  return (
    <WeddingContext.Provider value={{ state, toggleTask, setBudget, setView, save, applyCloudState }}>
      {children}
    </WeddingContext.Provider>
  );
}

export const useWedding = () => useContext(WeddingContext);
```

- [ ] **Step 5: Verify contexts compile**

Run: `cd C:/dev/PS7 && npm run build`
Expected: Build succeeds (may warn about no App.jsx yet, that's fine)

- [ ] **Step 6: Commit**

```bash
cd C:/dev/PS7 && git add src/contexts/ src/lib/ && git commit -m "feat: state contexts — Wedding, UI, Weather + Open-Meteo fetcher"
```

---

### Task 4: Shared components + Layout

**Files:**
- Create: `src/components/shared/ProgressBar.jsx`, `src/components/shared/Toast.jsx`, `src/components/layout/ScrollToTop.jsx`
- Create: `src/hooks/useCountdown.js`

- [ ] **Step 1: Create src/hooks/useCountdown.js**

```js
import { useState, useEffect } from 'react';
import { WEDDING_DATE } from '../data/tasks';

export function useCountdown() {
  const [text, setText] = useState('');

  useEffect(() => {
    function tick() {
      const diff = WEDDING_DATE - new Date();
      if (diff <= 0) { setText('🎉 Svatba proběhla!'); return; }
      const d = Math.floor(diff / 86400000);
      const h = Math.floor((diff % 86400000) / 3600000);
      const m = Math.floor((diff % 3600000) / 60000);
      setText(`⏳ ${d}d ${h}h ${m}m do svatby`);
    }
    tick();
    const id = setInterval(tick, 60000);
    return () => clearInterval(id);
  }, []);

  return text;
}
```

- [ ] **Step 2: Create src/components/shared/ProgressBar.jsx**

```jsx
export default function ProgressBar({ value, max, label, colorClass = 'bg-[var(--color-wedding)]' }) {
  const pct = max ? Math.round((value / max) * 100) : 0;
  return (
    <div className="px-4 py-2 max-w-[600px] mx-auto">
      <div className="flex justify-between text-[.72rem] text-[var(--color-muted)] mb-1">
        <span>{label || `${value}/${max}`}</span>
        <span>{pct}%</span>
      </div>
      <div className="h-[10px] bg-[var(--color-border)] rounded-[10px] overflow-hidden">
        <div
          className={`h-full rounded-[10px] transition-[width] duration-500 ${colorClass}`}
          style={{
            width: `${pct}%`,
            background: 'linear-gradient(90deg, var(--color-wedding-dark), var(--color-wedding), var(--color-wedding-light))'
          }}
        />
      </div>
    </div>
  );
}
```

- [ ] **Step 3: Create src/components/shared/Toast.jsx**

```jsx
import { useUI } from '../../contexts/UIContext';

export default function Toast() {
  const { toast } = useUI();
  if (!toast) return null;
  return (
    <div className="fixed top-4 left-1/2 -translate-x-1/2 z-[400] bg-[#2d2a24] text-white px-5 py-2.5 rounded-full text-[.78rem] shadow-lg animate-pulse">
      {toast}
    </div>
  );
}
```

- [ ] **Step 4: Create src/components/layout/ScrollToTop.jsx**

```jsx
import { useState, useEffect } from 'react';

export default function ScrollToTop() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    function onScroll() { setVisible(window.scrollY > 300); }
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  return (
    <button
      onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
      className={`fixed z-[99] bottom-[90px] right-4 w-[44px] h-[44px] rounded-full border-0 bg-[var(--color-wedding)] text-white text-lg cursor-pointer shadow-lg flex items-center justify-center transition-all duration-200 ${visible ? 'opacity-100 translate-y-0 pointer-events-auto' : 'opacity-0 translate-y-2.5 pointer-events-none'}`}
      aria-label="Nahoru"
      style={{ paddingBottom: 'env(safe-area-inset-bottom, 10px)' }}
    >
      ↑
    </button>
  );
}
```

- [ ] **Step 5: Commit**

```bash
cd C:/dev/PS7 && git add src/hooks/ src/components/shared/ src/components/layout/ && git commit -m "feat: shared components — ProgressBar, Toast, ScrollToTop + useCountdown"
```

---

### Task 5: Landing — HeroSection + StoryTimeline

**Files:**
- Create: `src/components/landing/HeroSection.jsx`, `src/components/landing/StoryTimeline.jsx`

- [ ] **Step 1: Create HeroSection.jsx**

```jsx
import { useCountdown } from '../../hooks/useCountdown';

export default function HeroSection() {
  const countdown = useCountdown();

  return (
    <section className="relative overflow-hidden text-center text-white"
      style={{ background: 'linear-gradient(135deg, #5c1e1e, #8b3a3a, #6b2e2e)', paddingTop: 'max(60px, env(safe-area-inset-top, 0) + 40px)', paddingBottom: '48px' }}>
      <div className="absolute -top-[30px] -right-[30px] text-[160px] opacity-[.06] rotate-[-15deg] pointer-events-none">💍</div>
      <div className="absolute inset-0 pointer-events-none"
        style={{ background: 'radial-gradient(ellipse at 30% 20%, rgba(255,255,255,.06) 0%, transparent 70%)' }} />

      <div className="relative z-[1] px-6">
        <div className="text-[.7rem] uppercase tracking-[3px] opacity-70 mb-2">Svatba</div>
        <h1 className="text-[clamp(1.6rem,5vw,2rem)] font-bold tracking-[-.5px] mb-0.5">Martin &amp; Dagmar</h1>
        <div className="italic text-[clamp(.8rem,2.5vw,.9rem)] opacity-80 mb-4">Paprčkovi</div>

        <div className="inline-block bg-white/20 rounded-[20px] px-4 py-1.5 text-[clamp(.7rem,2vw,.8rem)] mb-3">
          29. srpna 2026
        </div>

        <div className="inline-block bg-white/20 rounded-[24px] px-5 py-2 text-[clamp(.9rem,3vw,1.1rem)] font-bold animate-pulse">
          {countdown}
        </div>
      </div>
    </section>
  );
}
```

- [ ] **Step 2: Create StoryTimeline.jsx**

```jsx
const MILESTONES = [
  { date: null, label: '👶 Dcera', title: 'Gabriela', desc: 'před seznámením', color: '#c46a6a' },
  { date: '1. května 1997', label: '💕', title: 'První setkání', desc: 'Martin a Dagmar se poznali', color: '#d4a017' },
  { date: null, label: '👶 Dcera', title: 'Kristýnka', desc: '', color: '#c46a6a' },
  { date: null, label: '👶 Dcera', title: 'Natálka', desc: '', color: '#c46a6a' },
  { date: null, label: '👶 Dcera', title: 'Kačka', desc: '', color: '#c46a6a' },
  { date: '29. srpna 2026', label: '💒', title: 'Svatba!', desc: 'Nová radnice Ostrava · 11:15', color: '#8b3a3a' }
];

export default function StoryTimeline() {
  return (
    <section className="px-4 py-8 max-w-[600px] mx-auto">
      <div className="text-center mb-5">
        <div className="text-[.65rem] uppercase tracking-[2px] text-[var(--color-muted)]">Náš příběh</div>
        <h2 className="text-[1.2rem] font-semibold text-[var(--color-warm)] mt-1">Jak to všechno začalo</h2>
      </div>

      <div className="relative pl-6 border-l-2 border-[var(--color-gold)]">
        {MILESTONES.map((m, i) => {
          const isLast = i === MILESTONES.length - 1;
          return (
            <div key={i} className="relative mb-3.5" style={isLast ? { marginBottom: 0 } : {}}>
              <div className="absolute top-0.5"
                style={{
                  left: '-29px',
                  width: isLast ? '12px' : '10px',
                  height: isLast ? '12px' : '10px',
                  background: m.color,
                  borderRadius: '50%',
                  border: '2px solid #faf7f2',
                  boxShadow: isLast ? '0 0 0 4px rgba(139,58,58,.2)' : 'none'
                }} />
              <div className="text-[.6rem] uppercase tracking-[1px] font-semibold" style={{ color: m.color }}>{m.label}</div>
              {m.date && <div className="text-[.65rem] text-[var(--color-muted)]">{m.date}</div>}
              <div className="text-[.78rem] font-semibold text-[var(--color-warm)]">{m.title}</div>
              {m.desc && <div className="text-[.65rem] text-[var(--color-muted)]">{m.desc}</div>}
            </div>
          );
        })}
      </div>
    </section>
  );
}
```

- [ ] **Step 3: Commit**

```bash
cd C:/dev/PS7 && git add src/components/landing/HeroSection.jsx src/components/landing/StoryTimeline.jsx && git commit -m "feat: landing — HeroSection + StoryTimeline"
```

---

### Task 6: Landing — VenueInfo + GalleryGrid + Lightbox

**Files:**
- Create: `src/components/landing/VenueInfo.jsx`, `src/components/landing/GalleryGrid.jsx`, `src/components/landing/Lightbox.jsx`

- [ ] **Step 1: Create VenueInfo.jsx**

```jsx
export default function VenueInfo() {
  return (
    <section className="px-4 py-6 max-w-[600px] mx-auto">
      <div className="text-center mb-4">
        <div className="text-[.65rem] uppercase tracking-[2px] text-[var(--color-muted)]">Kdy & Kde</div>
      </div>

      <div className="flex flex-col gap-2.5">
        <div className="bg-[var(--color-card)] rounded-xl p-4 shadow-sm border-l-4 border-[var(--color-wedding)]"
          style={{ boxShadow: '0 1px 4px rgba(0,0,0,.06)' }}>
          <div className="text-[.85rem] font-bold text-[var(--color-wedding)] mb-1">💒 Obřad — 11:15</div>
          <div className="text-[.75rem] font-semibold text-[var(--color-warm)]">Nová radnice Ostrava</div>
          <div className="text-[.68rem] text-[var(--color-muted)]">Prokešovo náměstí 8, Ostrava</div>
        </div>

        <div className="bg-[var(--color-card)] rounded-xl p-4 shadow-sm border-l-4 border-[var(--color-gold)]"
          style={{ boxShadow: '0 1px 4px rgba(0,0,0,.06)' }}>
          <div className="text-[.85rem] font-bold text-[var(--color-gold)] mb-1">🍽️ Hostina — po obřadu</div>
          <div className="text-[.75rem] font-semibold text-[var(--color-warm)]">Zlatá koliba, U Miloše</div>
          <div className="text-[.68rem] text-[var(--color-muted)]">Adresa bude doplněna</div>
        </div>
      </div>

      <div className="mt-3 h-[120px] bg-[var(--color-border)] rounded-lg flex items-center justify-center text-[.7rem] text-[var(--color-muted)]">
        🗺️ Mapa bude doplněna
      </div>
    </section>
  );
}
```

- [ ] **Step 2: Create Lightbox.jsx**

```jsx
import { useEffect } from 'react';

export default function Lightbox({ src, alt, onClose }) {
  useEffect(() => {
    function onKey(e) { if (e.key === 'Escape') onClose(); }
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [onClose]);

  return (
    <div className="fixed inset-0 z-[200] bg-black/90 flex items-center justify-center p-4"
      onClick={onClose}>
      <button className="absolute top-4 right-4 text-white text-2xl w-[44px] h-[44px] flex items-center justify-center"
        onClick={onClose} aria-label="Zavřít">✕</button>
      <img src={src} alt={alt} className="max-w-full max-h-[90vh] rounded-lg"
        onClick={e => e.stopPropagation()} />
    </div>
  );
}
```

- [ ] **Step 3: Create GalleryGrid.jsx**

```jsx
import { useState } from 'react';
import Lightbox from './Lightbox';

const PLACEHOLDERS = [
  { label: 'Společné', grid: 'row-span-2' },
  { label: 'Foto', grid: '' },
  { label: 'Rodina', grid: 'row-span-2' },
  { label: 'Foto', grid: '' },
  { label: 'Děti', grid: '' },
];

export default function GalleryGrid() {
  const [lightbox, setLightbox] = useState(null);
  // TODO: replace with real photos when available
  const hasPhotos = false;

  return (
    <section className="px-4 py-6 max-w-[600px] mx-auto">
      <div className="text-center mb-3">
        <div className="text-[.65rem] uppercase tracking-[2px] text-[var(--color-muted)]">Fotogalerie</div>
      </div>

      <div className="grid grid-cols-[1.3fr_1fr] grid-rows-[120px_100px_120px] gap-1.5">
        {PLACEHOLDERS.map((p, i) => (
          <div key={i}
            className={`bg-[var(--color-border)] rounded-lg flex items-center justify-center text-[.65rem] text-[var(--color-muted)] cursor-pointer hover:opacity-80 transition-opacity ${p.grid}`}
            onClick={() => hasPhotos && setLightbox({ src: `photos/${i + 1}.jpg`, alt: p.label })}>
            📷 {p.label}
          </div>
        ))}
      </div>

      {!hasPhotos && (
        <p className="text-center text-[.65rem] text-[var(--color-muted)] mt-2">
          Fotky budou přidány později
        </p>
      )}

      {lightbox && <Lightbox {...lightbox} onClose={() => setLightbox(null)} />}
    </section>
  );
}
```

- [ ] **Step 4: Commit**

```bash
cd C:/dev/PS7 && git add src/components/landing/ && git commit -m "feat: landing — VenueInfo, GalleryGrid, Lightbox"
```

---

### Task 7: Landing — RSVPSection + PlannerNavBanner

**Files:**
- Create: `src/components/landing/RSVPSection.jsx`, `src/components/landing/PlannerNavBanner.jsx`

- [ ] **Step 1: Create RSVPSection.jsx**

```jsx
import { useState } from 'react';
import { GUESTS } from '../../data/guests';

export default function RSVPSection() {
  const [name, setName] = useState('');
  const [count, setCount] = useState(1);
  const [message, setMessage] = useState('');
  const [sent, setSent] = useState(false);

  function submit(e) {
    e.preventDefault();
    // RSVP data stored in localStorage for now, can be extended to GitHub sync
    const rsvp = { name, count, message, timestamp: Date.now() };
    const existing = JSON.parse(localStorage.getItem('weddingRsvp') || '[]');
    localStorage.setItem('weddingRsvp', JSON.stringify([...existing, rsvp]));
    setSent(true);
  }

  if (sent) {
    return (
      <section className="px-4 py-8 max-w-[600px] mx-auto text-center">
        <div className="text-3xl mb-3">❤️</div>
        <h3 className="text-lg font-semibold text-[var(--color-warm)]">Děkujeme!</h3>
        <p className="text-[.75rem] text-[var(--color-muted)] mt-1">Těšíme se na vás</p>
      </section>
    );
  }

  return (
    <section className="px-4 py-6 max-w-[600px] mx-auto">
      <div className="text-center mb-4">
        <div className="text-[.65rem] uppercase tracking-[2px] text-[var(--color-muted)]">Potvrzení účasti</div>
        <h2 className="text-[1.2rem] font-semibold text-[var(--color-warm)] mt-1">Přijdete?</h2>
        <p className="text-[.7rem] text-[var(--color-muted)]">Dejte nám vědět do 1. srpna 2026</p>
      </div>

      <form onSubmit={submit} className="flex flex-col gap-2.5">
        <input
          required
          type="text"
          placeholder="Vaše jméno"
          value={name}
          onChange={e => setName(e.target.value)}
          className="p-3 border border-[var(--color-border)] rounded-lg text-[.78rem] bg-[var(--color-card)] font-[inherit]"
        />
        <div className="flex gap-2 items-center">
          <span className="text-[.75rem] text-[var(--color-warm)]">Počet osob:</span>
          <div className="flex">
            <button type="button" onClick={() => setCount(c => Math.max(1, c - 1))}
              className="px-3.5 py-2 border border-[var(--color-border)] bg-[var(--color-card)] rounded-l-lg text-[.8rem] min-h-[44px]">−</button>
            <div className="px-4 py-2 border-t border-b border-[var(--color-border)] bg-[var(--color-card)] text-[.8rem] min-w-[36px] text-center">{count}</div>
            <button type="button" onClick={() => setCount(c => c + 1)}
              className="px-3.5 py-2 border border-[var(--color-border)] bg-[var(--color-card)] rounded-r-lg text-[.8rem] min-h-[44px]">+</button>
          </div>
        </div>
        <textarea
          placeholder="Zpráva (nepovinné)"
          value={message}
          onChange={e => setMessage(e.target.value)}
          rows={2}
          className="p-3 border border-[var(--color-border)] rounded-lg text-[.78rem] bg-[var(--color-card)] font-[inherit] resize-none"
        />
        <button type="submit"
          className="w-full bg-[var(--color-wedding)] text-white border-0 py-3.5 rounded-lg font-semibold text-[.82rem] cursor-pointer hover:bg-[var(--color-wedding-dark)] transition-colors min-h-[44px]"
          style={{ fontFamily: 'inherit' }}>
          Potvrdit účast
        </button>
      </form>

      {/* Guest list */}
      <div className="mt-5 pt-4 border-t border-[var(--color-border)]">
        <div className="text-[.7rem] uppercase tracking-[1px] text-[var(--color-muted)] mb-2.5">
          Hosté <span className="font-normal">({GUESTS.length} skupin)</span>
        </div>
        <div className="grid grid-cols-2 gap-1.5 text-[.68rem] text-[var(--color-warm)]">
          {GUESTS.map((g, i) => (
            <div key={i} className="flex justify-between px-2 py-1.5 bg-[var(--color-card)] rounded-md">
              <span>{g.name}</span>
              <span className="text-[var(--color-muted)]">{g.count}</span>
            </div>
          ))}
        </div>
        <div className="text-right text-[.65rem] text-[var(--color-gold)] mt-2 font-semibold">
          ~14–20 hostů
        </div>
      </div>
    </section>
  );
}
```

- [ ] **Step 2: Create PlannerNavBanner.jsx**

```jsx
import { Link } from 'react-router-dom';

export default function PlannerNavBanner() {
  return (
    <section className="px-4 py-5 text-center text-white"
      style={{ background: 'linear-gradient(135deg, #5c1e1e, #8b3a3a)' }}>
      <div className="text-[.7rem] uppercase tracking-[2px] opacity-70 mb-1.5">Pro organizátory</div>
      <div className="text-[1rem] font-semibold mb-1">Plánování svatby</div>
      <div className="text-[.7rem] opacity-70 mb-3">Tasky · Rozpočet · Počasí</div>
      <Link to="/planovani"
        className="inline-block px-7 py-2.5 bg-white/15 border border-white/30 rounded-[24px] text-white font-semibold text-[.78rem] no-underline hover:bg-white/25 transition-colors">
        🔒 Vstoupit
      </Link>
    </section>
  );
}
```

- [ ] **Step 3: Commit**

```bash
cd C:/dev/PS7 && git add src/components/landing/ && git commit -m "feat: landing — RSVPSection + PlannerNavBanner"
```

---

### Task 8: LandingPage — compose all sections

**Files:**
- Create: `src/pages/LandingPage.jsx`

- [ ] **Step 1: Create LandingPage.jsx**

```jsx
import HeroSection from '../components/landing/HeroSection';
import StoryTimeline from '../components/landing/StoryTimeline';
import VenueInfo from '../components/landing/VenueInfo';
import GalleryGrid from '../components/landing/GalleryGrid';
import RSVPSection from '../components/landing/RSVPSection';
import PlannerNavBanner from '../components/landing/PlannerNavBanner';

export default function LandingPage() {
  return (
    <main>
      <HeroSection />
      <StoryTimeline />
      <VenueInfo />
      <GalleryGrid />
      <RSVPSection />
      <PlannerNavBanner />
    </main>
  );
}
```

- [ ] **Step 2: Commit**

```bash
cd C:/dev/PS7 && git add src/pages/LandingPage.jsx && git commit -m "feat: LandingPage — compose all 6 sections"
```

---

### Task 9: Planning — PinGate + Dashboard + WeatherCard

**Files:**
- Create: `src/components/planning/PinGate.jsx`, `src/components/planning/Dashboard.jsx`, `src/components/planning/WeatherCard.jsx`

- [ ] **Step 1: Create PinGate.jsx**

```jsx
import { useState } from 'react';
import { useUI } from '../../contexts/UIContext';

export default function PinGate({ children }) {
  const { pinVerified, verifyPin } = useUI();
  const [input, setInput] = useState('');
  const [error, setError] = useState(false);

  if (pinVerified) return children;

  function submit(e) {
    e.preventDefault();
    if (verifyPin(input)) {
      setError(false);
    } else {
      setError(true);
      setInput('');
    }
  }

  return (
    <div className="min-h-[60vh] flex items-center justify-center px-4">
      <form onSubmit={submit} className="text-center max-w-[300px] w-full">
        <div className="text-4xl mb-4">🔒</div>
        <h2 className="text-[1.2rem] font-semibold text-[var(--color-warm)] mb-1">Plánování</h2>
        <p className="text-[.7rem] text-[var(--color-muted)] mb-4">Zadej rodinný PIN pro vstup</p>
        <input
          type="password"
          inputMode="numeric"
          maxLength={6}
          value={input}
          onChange={e => { setInput(e.target.value); setError(false); }}
          placeholder="PIN"
          autoFocus
          className="w-full p-3 border rounded-lg text-center text-lg tracking-[4px] font-[inherit] mb-2"
          style={{ borderColor: error ? 'var(--color-wedding)' : 'var(--color-border)' }}
        />
        {error && <p className="text-[.7rem] text-[var(--color-wedding)] mb-2">Nesprávný PIN</p>}
        <button type="submit"
          className="w-full bg-[var(--color-wedding)] text-white border-0 py-3 rounded-lg font-semibold text-[.82rem] cursor-pointer min-h-[44px]"
          style={{ fontFamily: 'inherit' }}>
          Vstoupit
        </button>
      </form>
    </div>
  );
}
```

- [ ] **Step 2: Create WeatherCard.jsx**

```jsx
import { useWeather } from '../../contexts/WeatherContext';

export default function WeatherCard() {
  const weather = useWeather();

  return (
    <div className="mx-4 mt-2 p-3.5 rounded-xl flex items-center gap-2.5 text-[.78rem] max-w-[600px]"
      style={{
        background: 'rgba(255,255,255,.88)',
        boxShadow: '0 1px 3px rgba(0,0,0,.04), 0 3px 10px rgba(0,0,0,.05)',
        border: '1px solid rgba(255,255,255,.35)'
      }}>
      {weather ? (
        <>
          <span className="text-[1.5rem] flex-shrink-0">{weather.icon}</span>
          <span className="font-semibold flex-1">{weather.max}°C / {weather.min}°C</span>
          <span className="text-[.7rem] text-[var(--color-muted)]">{weather.date}</span>
        </>
      ) : (
        <span className="text-[.7rem] text-[var(--color-muted)]">🌤️ Načítám počasí...</span>
      )}
    </div>
  );
}
```

- [ ] **Step 3: Create Dashboard.jsx**

```jsx
import { useWedding } from '../../contexts/WeddingContext';
import { TASKS } from '../../data/tasks';
import ProgressBar from '../shared/ProgressBar';

export default function Dashboard() {
  const { state } = useWedding();
  const total = TASKS.length;
  const done = state.done.length;
  const mTasks = TASKS.filter(t => t.cat === 'mandatory');
  const mDone = mTasks.filter(t => state.done.includes(t.id)).length;

  const tBudget = TASKS.filter(t => t.price > 0);
  const totalBudget = tBudget.reduce((s, t) => s + t.price, 0);
  const paid = tBudget.filter(t => state.done.includes(t.id)).reduce((s, t) => s + t.price, 0);

  function fmt(n) { return n ? n.toLocaleString('cs-CZ') : '0'; }

  return (
    <div className="max-w-[600px] mx-auto">
      <div className="grid grid-cols-2 gap-2 px-4 pt-2.5">
        {[
          { n: done, l: 'hotovo' },
          { n: total - done, l: 'zbývá' },
          { n: Math.round(done / total * 100) + '%', l: 'hotovo' }
        ].map((d, i) => (
          <div key={i} className="bg-[var(--color-card)] rounded-xl p-3.5 text-center shadow-sm border border-white/40"
            style={{ boxShadow: '0 1px 3px rgba(0,0,0,.05), 0 4px 14px rgba(0,0,0,.07)' }}>
            <div className="text-[clamp(1.4rem,4.5vw,1.8rem)] font-bold text-[var(--color-wedding)]">{d.n}</div>
            <div className="text-[clamp(.65rem,2vw,.72rem)] text-[var(--color-muted)] uppercase tracking-[.4px] mt-0.5">{d.l}</div>
          </div>
        ))}
      </div>

      <ProgressBar value={done} max={total} label={`${done}/${total} úkolů`} />

      {/* Mandatory widget */}
      <div className="mx-4 mb-2.5 bg-[var(--color-card)] rounded-xl p-3 shadow-sm border-l-4 border-[#c0392b]">
        <h3 className="text-[.78rem] text-[#c0392b] mb-1.5">🔴 Povinné <span className="font-normal text-[#666]">{mDone}/{mTasks.length}</span></h3>
        {mTasks.map(t => {
          const d = state.done.includes(t.id);
          return (
            <div key={t.id} className={`flex items-center gap-2 py-1.5 border-b border-[var(--color-border)] text-[.75rem] min-h-[44px] ${d ? 'opacity-0 max-h-0 py-0 border-0 pointer-events-none overflow-hidden' : ''}`}>
              <div className={`flex-shrink-0 w-[22px] h-[22px] rounded-[5px] border-2 flex items-center justify-center text-[11px] ${d ? 'bg-[var(--color-wedding)] border-[var(--color-wedding)] text-white' : 'border-[#d5ccc4] bg-white'}`}>
                {d ? '✓' : ''}
              </div>
              <span className="flex-1 min-w-0">{t.title}</span>
              <span className="text-[#999] text-[.68rem]">📅 {t.deadline}</span>
            </div>
          );
        })}
      </div>

      {/* Budget summary */}
      <div className="mx-4 bg-[var(--color-card)] rounded-xl p-3 shadow-sm">
        <h3 className="text-[.78rem] text-[var(--color-wedding)] mb-1.5">💰 Rozpočet</h3>
        <div className="flex justify-between text-[.72rem] py-0.5"><span>Celkem</span><span className="font-bold">{fmt(totalBudget)}&thinsp;Kč</span></div>
        <div className="flex justify-between text-[.72rem] py-0.5"><span>Uhrazeno</span><span className="font-bold text-[#27ae60]">{fmt(paid)}&thinsp;Kč</span></div>
      </div>
    </div>
  );
}
```

- [ ] **Step 4: Commit**

```bash
cd C:/dev/PS7 && git add src/components/planning/ && git commit -m "feat: planning — PinGate, Dashboard, WeatherCard"
```

---

### Task 10: Planning — TaskList + TaskItem + particles

**Files:**
- Create: `src/components/planning/TaskList.jsx`, `src/components/planning/TaskItem.jsx`

- [ ] **Step 1: Create TaskItem.jsx**

```jsx
import { useCallback } from 'react';
import { CAT_LABELS, CAT_COLORS } from '../../data/tasks';

function daysUntil(dl) {
  const t = new Date(dl + 'T12:00:00');
  return Math.round((t - Date.now()) / 86400000);
}

function fmt(n) {
  if (!n) return '0';
  return Math.abs(n).toLocaleString('cs-CZ');
}

export default function TaskItem({ task, done, onToggle }) {
  const uc = daysUntil(task.dl);
  const isOverdue = !done && uc < 0;
  const urgencyLabel = uc < 0 ? '⚠️ ' + Math.abs(uc) + 'd' : uc === 0 ? '🔴 dnes' : uc <= 14 ? '🔵 ' + uc + 'd' : '';

  const handleToggle = useCallback((e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    onToggle(task.id, { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 });
  }, [task.id, onToggle]);

  return (
    <div
      onClick={handleToggle}
      className={`rounded-lg p-3 cursor-pointer transition-all border-l-4 min-h-[44px] ${done ? 'opacity-50 grayscale' : ''}`}
      style={{ borderLeftColor: isOverdue ? '#c0392b' : CAT_COLORS[task.cat] }}>
      <div className="flex items-start gap-2">
        <div
          className={`flex-shrink-0 w-[22px] h-[22px] rounded-[5px] border-2 flex items-center justify-center text-[11px] mt-0.5 ${done ? 'bg-[var(--color-wedding)] border-[var(--color-wedding)] text-white' : 'border-[#d5ccc4] bg-white'}`}
          onClick={e => { e.stopPropagation(); handleToggle(e); }}>
          {done ? '✓' : ''}
        </div>
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-1 text-[.78rem] text-[var(--color-warm)]">
            {done && '✅ '}
            {task.title}
            {urgencyLabel && (
              <span className={`text-[.65rem] font-semibold ml-1 ${isOverdue ? 'text-[#c0392b] animate-pulse' : 'text-[#2196F3]'}`}>
                {urgencyLabel}
              </span>
            )}
          </div>
          <div className="flex flex-wrap gap-1 mt-1">
            <span className="text-[.6rem] px-1.5 py-0.5 rounded text-[var(--color-muted)] bg-gray-100">
              {CAT_LABELS[task.cat]}
            </span>
            <span className="text-[.6rem] px-1.5 py-0.5 rounded text-[var(--color-muted)] bg-gray-100">
              👤 {task.assign}
            </span>
            <span className="text-[.6rem] px-1.5 py-0.5 rounded text-[var(--color-muted)] bg-gray-100">
              📅 {task.deadline}
            </span>
            {task.price ? (
              <span className="text-[.6rem] px-1.5 py-0.5 rounded bg-green-50 text-[#27ae60]">
                💰 {fmt(task.price)}
              </span>
            ) : null}
          </div>
        </div>
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Create TaskList.jsx with particles and chime**

```jsx
import { useState, useCallback } from 'react';
import { useWedding } from '../../contexts/WeddingContext';
import { TASKS, CAT_ORDER, CAT_LABELS } from '../../data/tasks';
import TaskItem from './TaskItem';

function spawnParticles(pos) {
  const container = document.getElementById('particles');
  if (!container) return;
  const emojis = ['🎉', '🎊', '✨', '💒', '❤️', '🥂'];
  for (let i = 0; i < 6; i++) {
    const p = document.createElement('span');
    p.className = 'particle';
    p.textContent = emojis[i];
    p.style.left = (pos.x + (Math.random() - 0.5) * 80) + 'px';
    p.style.top = (pos.y + (Math.random() - 0.5) * 40) + 'px';
    p.style.animationDelay = (Math.random() * 0.15) + 's';
    container.appendChild(p);
    setTimeout(() => p.remove(), 1000);
  }
}

function spawnConfetti() {
  const container = document.getElementById('particles');
  if (!container) return;
  const emojis = ['🎉', '🎊', '🥂', '🍾', '💒', '✨', '💍', '🌸', '🎶', '❤️'];
  for (let i = 0; i < 35; i++) {
    const p = document.createElement('span');
    p.className = 'particle';
    p.textContent = emojis[Math.floor(Math.random() * emojis.length)];
    p.style.left = Math.random() * window.innerWidth + 'px';
    p.style.top = '-20px';
    p.style.animation = 'particleUp 1.5s ease-out forwards';
    p.style.fontSize = (1 + Math.random()) + 'rem';
    p.style.animationDelay = (Math.random() * 0.4) + 's';
    container.appendChild(p);
    setTimeout(() => p.remove(), 2000);
  }
}

function playChime() {
  try {
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    [660, 880].forEach((freq, i) => {
      const o = audioCtx.createOscillator();
      const g = audioCtx.createGain();
      o.connect(g); g.connect(audioCtx.destination);
      o.type = 'sine';
      o.frequency.setValueAtTime(freq, audioCtx.currentTime + i * 0.08);
      g.gain.setValueAtTime(0.3, audioCtx.currentTime + i * 0.08);
      g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + i * 0.08 + 0.15);
      o.start(audioCtx.currentTime + i * 0.08);
      o.stop(audioCtx.currentTime + i * 0.08 + 0.15);
    });
  } catch {}
}

export default function TaskList() {
  const { state, toggleTask } = useWedding();
  const [filter, setFilter] = useState(state.filter || 'pending');
  const [sort, setSort] = useState(state.sort || 'deadline');
  const [personFilter, setPersonFilter] = useState(state.personFilter || '');
  const [search, setSearch] = useState(state.search || '');
  const [showDone, setShowDone] = useState(state.showDone || { mandatory: false, important: false, optional: false });

  const people = [...new Set(TASKS.map(t => t.assign))];

  const handleToggle = useCallback((id, pos) => {
    const justChecked = toggleTask(id);
    if (justChecked) {
      playChime();
      spawnParticles(pos);
      if (state.done.length + 1 === TASKS.length) {
        setTimeout(spawnConfetti, 400);
      }
    }
  }, [toggleTask, state.done.length]);

  // Filter and sort
  let filtered = TASKS.filter(t => {
    if (filter === 'pending') { if (state.done.includes(t.id)) return false; }
    else if (filter !== 'all' && t.cat !== filter) return false;
    if (personFilter && t.assign !== personFilter) return false;
    if (search) return t.title.toLowerCase().includes(search.toLowerCase()) || t.assign.toLowerCase().includes(search.toLowerCase());
    return true;
  });

  if (sort === 'deadline') {
    filtered.sort((a, b) => (state.done.includes(b.id) ? 0 : 1) - (state.done.includes(a.id) ? 0 : 1) || a.dl.localeCompare(b.dl));
  } else if (sort === 'category') {
    filtered.sort((a, b) => CAT_ORDER.indexOf(a.cat) - CAT_ORDER.indexOf(b.cat) || a.dl.localeCompare(b.dl));
  } else if (sort === 'assign') {
    filtered.sort((a, b) => a.assign.localeCompare(b.assign) || a.dl.localeCompare(b.dl));
  }

  const groups = { mandatory: [], important: [], optional: [] };
  filtered.forEach(t => groups[t.cat].push(t));

  return (
    <div className="max-w-[600px] mx-auto pb-4">
      <div className="px-4 pt-3 flex gap-1.5 items-center">
        <input
          type="search"
          placeholder="🔍 Hledat úkol..."
          value={search}
          onChange={e => setSearch(e.target.value)}
          className="flex-1 p-2 border border-[var(--color-border)] rounded-lg text-[.78rem] bg-[var(--color-card)] font-[inherit] min-w-0"
          style={{ WebkitAppearance: 'none' }}
        />
        {['deadline', 'category', 'assign'].map(s => (
          <button key={s}
            onClick={() => setSort(s)}
            className={`p-2 min-h-[44px] min-w-[44px] rounded-lg border text-[1rem] ${sort === s ? 'bg-[var(--color-wedding)] text-white border-[var(--color-wedding)]' : 'bg-[var(--color-card)] border-[var(--color-border)]'}`}>
            {s === 'deadline' ? '📅' : s === 'category' ? '📂' : '👤'}
          </button>
        ))}
      </div>

      <div className="flex gap-1 px-4 mt-2 flex-wrap">
        {[
          { key: 'pending', label: '📋 K vyřízení' },
          { key: 'all', label: '🔍 Vše' },
          { key: 'mandatory', label: '🔴 Povinné' },
          { key: 'important', label: '🟡 Důležité' },
          { key: 'optional', label: '🟢 Volitelné' }
        ].map(f => (
          <button key={f.key}
            onClick={() => setFilter(f.key)}
            className={`px-2.5 py-1 rounded-full text-[.68rem] font-[inherit] cursor-pointer border-0 ${filter === f.key ? 'bg-[var(--color-wedding)] text-white' : 'bg-gray-100 text-[var(--color-muted)]'}`}>
            {f.label}
          </button>
        ))}
      </div>

      <div className="flex gap-1 px-4 mt-1.5 flex-wrap">
        <button
          onClick={() => setPersonFilter('')}
          className={`px-2.5 py-1 rounded-full text-[.68rem] border-0 cursor-pointer ${!personFilter ? 'bg-[var(--color-wedding)] text-white' : 'bg-gray-100 text-[var(--color-muted)]'}`}>
          👥 Všichni
        </button>
        {people.map(p => (
          <button key={p}
            onClick={() => setPersonFilter(p)}
            className={`px-2.5 py-1 rounded-full text-[.68rem] border-0 cursor-pointer ${personFilter === p ? 'bg-[var(--color-wedding)] text-white' : 'bg-gray-100 text-[var(--color-muted)]'}`}>
            {p}
          </button>
        ))}
      </div>

      <div className="px-4 mt-4">
        {CAT_ORDER.map(cat => {
          const items = groups[cat];
          if (!items.length) return null;
          const dc = items.filter(t => state.done.includes(t.id)).length;
          const hasDone = items.some(t => state.done.includes(t.id));

          return (
            <div key={cat} className="mb-3">
              <div className="flex items-center gap-2 mb-1.5">
                <span className="text-[.75rem] font-semibold">{CAT_LABELS[cat]}</span>
                <span className="text-[.65rem] text-[var(--color-muted)] bg-[rgba(139,58,58,.08)] px-2.5 py-0.5 rounded-[10px]">{dc}/{items.length}</span>
              </div>
              {items.map(t => (
                <TaskItem key={t.id} task={t} done={state.done.includes(t.id)} onToggle={handleToggle} />
              ))}
              {hasDone && (
                <button
                  onClick={() => setShowDone(s => ({ ...s, [cat]: !s[cat] }))}
                  className="text-[.68rem] text-[var(--color-wedding)] bg-transparent border-0 cursor-pointer py-1.5 font-[inherit]">
                  {showDone[cat] ? '🔽 Skrýt hotové' : `🔼 Zobrazit hotové (${dc})`}
                </button>
              )}
            </div>
          );
        })}

        {!filtered.length && (
          <div className="text-center py-8 text-[var(--color-muted)] text-[.8rem]">
            {search ? '🔍 Nic nenalezeno' : filter === 'pending' ? '🎉 Všechno hotovo!' : '🍀 Žádné úkoly'}
          </div>
        )}
      </div>
    </div>
  );
}
```

- [ ] **Step 3: Commit**

```bash
cd C:/dev/PS7 && git add src/components/planning/ && git commit -m "feat: planning — TaskList + TaskItem with particles and chime"
```

---

### Task 11: Planning — BudgetTracker + Settings

**Files:**
- Create: `src/components/planning/BudgetTracker.jsx`, `src/components/planning/Settings.jsx`
- Create: `src/hooks/useCloudSync.js`, `src/lib/github-sync.js`

- [ ] **Step 1: Create BudgetTracker.jsx**

```jsx
import { useWedding } from '../../contexts/WeddingContext';
import { TASKS, CAT_ORDER, CAT_LABELS } from '../../data/tasks';

function fmt(n) {
  if (!n) return '0';
  return Math.abs(n).toLocaleString('cs-CZ');
}

export default function BudgetTracker() {
  const { state, toggleTask, setBudget } = useWedding();
  const LIMIT = 100000;

  const spent = TASKS.reduce((s, t) => s + (state.budget[t.id] !== undefined ? state.budget[t.id] : t.price), 0);
  const overBudget = spent > LIMIT;

  const cats = {
    mandatory: TASKS.filter(t => t.cat === 'mandatory' && t.price > 0),
    important: TASKS.filter(t => t.cat === 'important' && t.price > 0),
    optional: TASKS.filter(t => t.cat === 'optional' && t.price > 0)
  };
  const icons = { mandatory: '🔴', important: '🟡', optional: '🟢' };

  return (
    <div className="max-w-[600px] mx-auto px-4 pb-4">
      <div className="mb-2.5">
        <div className="flex justify-between text-[.8rem] mb-1">
          <span>💰 Rozpočet celkem</span>
          <span style={{ color: overBudget ? '#c0392b' : '#27ae60' }}>{fmt(spent)} / {fmt(LIMIT)} Kč</span>
        </div>
        <div className="h-[10px] bg-[var(--color-border)] rounded-[10px] overflow-hidden">
          <div
            className="h-full rounded-[10px] transition-[width] duration-500"
            style={{
              width: `${Math.min(100, spent / LIMIT * 100)}%`,
              background: overBudget ? '#c0392b' : 'linear-gradient(90deg, var(--color-wedding-dark), var(--color-wedding), var(--color-wedding-light))'
            }}
          />
        </div>
      </div>

      {CAT_ORDER.map(cat => {
        const items = cats[cat];
        if (!items.length) return null;
        const catTotal = items.reduce((s, t) => s + (state.budget[t.id] || t.price), 0);
        const paid = items.filter(t => state.done.includes(t.id)).reduce((s, t) => s + (state.budget[t.id] || t.price), 0);

        return (
          <details key={cat} className="mb-2" open>
            <summary className="cursor-pointer text-[.78rem] font-semibold py-2 text-[var(--color-warm)]">
              {icons[cat]} {CAT_LABELS[cat]} — {fmt(catTotal)} Kč
            </summary>
            <div className="pl-2">
              {items.map(t => {
                const price = state.budget[t.id] !== undefined ? state.budget[t.id] : t.price;
                const done = state.done.includes(t.id);
                return (
                  <div key={t.id} className={`flex flex-col py-2 border-b border-[var(--color-border)] ${done ? 'opacity-50' : ''}`}>
                    <div className="flex justify-between text-[.75rem]">
                      <span>{t.title}</span>
                      <span className="font-semibold">{fmt(price)}&thinsp;Kč</span>
                    </div>
                    <div className="flex gap-2 items-center mt-1">
                      <input
                        type="number"
                        value={price}
                        onChange={e => setBudget(t.id, parseInt(e.target.value) || 0)}
                        min="0" step="100"
                        className="flex-1 p-1.5 border border-[var(--color-border)] rounded-md text-[.72rem] bg-[var(--color-card)] font-[inherit]"
                      />
                      <label className="flex items-center gap-1 text-[.68rem] text-[var(--color-muted)]">
                        <input type="checkbox" checked={done} onChange={() => toggleTask(t.id)} className="w-4 h-4" />
                        Hotovo
                      </label>
                    </div>
                  </div>
                );
              })}
              <div className="flex justify-between text-[.68rem] mt-1.5 text-[var(--color-muted)]">
                <span>Uhrazeno: {fmt(paid)} Kč</span>
                <span>Zbývá: {fmt(Math.abs(catTotal - paid))} Kč</span>
              </div>
            </div>
          </details>
        );
      })}
    </div>
  );
}
```

- [ ] **Step 2: Create src/lib/github-sync.js**

```js
const CLOUD = {
  owner: 'doma77git',
  repo: 'PaprckoviSvatba2026',
  branch: 'master',
  get api() {
    return `https://api.github.com/repos/${this.owner}/${this.repo}/contents/state.json?ref=${this.branch}`;
  }
};

export async function pushToCloud(state, token) {
  const getRes = await fetch(CLOUD.api, {
    headers: { Authorization: 'Bearer ' + token }
  });
  const existing = await getRes.json();
  const payload = {
    message: 'Sync from wedding app',
    content: btoa(unescape(encodeURIComponent(JSON.stringify({
      done: state.done,
      budget: state.budget,
      syncTs: Date.now().toString()
    }))))
  };
  if (existing.sha) payload.sha = existing.sha;
  const putRes = await fetch(CLOUD.api, {
    method: 'PUT',
    headers: {
      Authorization: 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  });
  return putRes.ok;
}

export async function pullFromCloud(token) {
  const getRes = await fetch(CLOUD.api, {
    headers: { Authorization: 'Bearer ' + token }
  });
  if (!getRes.ok) throw new Error('fetch failed');
  const data = await getRes.json();
  return JSON.parse(decodeURIComponent(escape(atob(data.content))));
}
```

- [ ] **Step 3: Create src/hooks/useCloudSync.js**

```js
import { useCallback } from 'react';
import { useWedding } from '../contexts/WeddingContext';
import { useUI } from '../contexts/UIContext';
import { pushToCloud, pullFromCloud } from '../lib/github-sync';

export function useCloudSync() {
  const { state, applyCloudState } = useWedding();
  const { showToast } = useUI();

  const push = useCallback(async () => {
    const token = localStorage.getItem('ghToken');
    if (!token) { showToast('🔑 Chybí token — vlož ho v Info'); return; }
    const ok = await pushToCloud(state, token);
    if (ok) {
      localStorage.setItem('weddingSyncTs', Date.now().toString());
      showToast('📡 Uloženo do cloudu');
    } else {
      showToast('⚠️ Chyba při ukládání');
    }
  }, [state, showToast]);

  const pull = useCallback(async () => {
    const token = localStorage.getItem('ghToken');
    if (!token) { showToast('🔑 Chybí token'); return; }
    try {
      const data = await pullFromCloud(token);
      applyCloudState(data);
      localStorage.setItem('weddingSyncTs', Date.now().toString());
      showToast('📡 Načteno z cloudu');
    } catch {
      showToast('⚠️ Chyba při načítání');
    }
  }, [applyCloudState, showToast]);

  return { push, pull };
}
```

- [ ] **Step 4: Create Settings.jsx**

```jsx
import { useUI } from '../../contexts/UIContext';
import { useCloudSync } from '../../hooks/useCloudSync';

export default function Settings() {
  const { darkMode, toggleDarkMode, pin, setPin, showToast } = useUI();
  const { push, pull } = useCloudSync();

  return (
    <div className="max-w-[600px] mx-auto px-4 pb-4">
      <h3 className="text-[1rem] font-semibold text-[var(--color-warm)] mb-4">⚙️ Info & Nastavení</h3>

      <div className="flex flex-col gap-3">
        <label className="flex items-center justify-between p-3 bg-[var(--color-card)] rounded-lg min-h-[44px]">
          <span className="text-[.78rem]">🌙 Tmavý režim</span>
          <input type="checkbox" checked={darkMode} onChange={toggleDarkMode}
            className="w-5 h-5 accent-[var(--color-wedding)]" />
        </label>

        <label className="flex flex-col gap-1 p-3 bg-[var(--color-card)] rounded-lg">
          <span className="text-[.78rem]">🔑 GitHub token</span>
          <input
            type="text"
            placeholder="ghp_..."
            defaultValue={localStorage.getItem('ghToken') || ''}
            onChange={e => localStorage.setItem('ghToken', e.target.value)}
            className="p-2 border border-[var(--color-border)] rounded-md text-[.72rem] bg-white font-mono"
          />
        </label>

        <label className="flex flex-col gap-1 p-3 bg-[var(--color-card)] rounded-lg">
          <span className="text-[.78rem]">🔐 Rodinný PIN</span>
          <input
            type="password"
            placeholder="Zadej PIN"
            defaultValue={pin}
            onChange={e => setPin(e.target.value)}
            className="p-2 border border-[var(--color-border)] rounded-md text-[.72rem] bg-white"
          />
        </label>

        <div className="p-3 bg-[var(--color-card)] rounded-lg">
          <span className="text-[.78rem] block mb-2">📡 Cloud sync</span>
          <div className="flex gap-1.5 flex-wrap">
            <button onClick={push}
              className="px-4 py-2 bg-[var(--color-wedding)] text-white border-0 rounded-[20px] text-[.72rem] cursor-pointer font-[inherit] hover:bg-[var(--color-wedding-dark)]">📤 Uložit do cloudu</button>
            <button onClick={pull}
              className="px-4 py-2 bg-[var(--color-wedding)] text-white border-0 rounded-[20px] text-[.72rem] cursor-pointer font-[inherit] hover:bg-[var(--color-wedding-dark)]">📥 Načíst z cloudu</button>
          </div>
        </div>

        <button
          onClick={() => { if (confirm('Opravdu resetovat?')) { localStorage.removeItem('weddingState'); window.location.reload(); } }}
          className="p-3 rounded-lg border border-[#c0392b] bg-transparent text-[#c0392b] text-[.72rem] cursor-pointer font-[inherit] min-h-[44px] hover:bg-red-50">
          🗑️ Resetovat vše
        </button>

        <div className="text-[.68rem] text-[var(--color-muted)] mt-2">
          <p>💒 Svatba Paprčkovi — plánovač úkolů</p>
          <p>Datum: 29. srpna 2026</p>
          <p>Obřad: 11:15 Nová radnice Ostrava</p>
          <p>Hostina: U Miloše, Zlatá koliba</p>
          <p>Verze 4.0</p>
          <p className="mt-1.5">Postaveno s ❤️ pomocí Claude + DeepSeek</p>
        </div>
      </div>
    </div>
  );
}
```

- [ ] **Step 5: Commit**

```bash
cd C:/dev/PS7 && git add src/components/planning/BudgetTracker.jsx src/components/planning/Settings.jsx src/hooks/useCloudSync.js src/lib/ && git commit -m "feat: planning — BudgetTracker, Settings, cloud sync"
```

---

### Task 12: PlanningPage — compose + bottom nav

**Files:**
- Create: `src/pages/PlanningPage.jsx`

- [ ] **Step 1: Create src/components/planning/TimelineView.jsx**

```jsx
import { useWedding } from '../../contexts/WeddingContext';
import { TASKS } from '../../data/tasks';

const MONTH_NAMES = {
  '2026-05': 'Květen', '2026-06': 'Červen',
  '2026-07': 'Červenec', '2026-08': 'Srpen', '2026-09': 'Září'
};

export default function TimelineView() {
  const { state } = useWedding();
  const grouped = {};
  TASKS.forEach(t => {
    const mm = t.tl.substring(0, 7);
    if (!grouped[mm]) grouped[mm] = [];
    grouped[mm].push(t);
  });

  return (
    <div className="max-w-[600px] mx-auto px-4 pb-4">
      {Object.keys(grouped).sort().map(mm => (
        <div key={mm} className="mb-4">
          <h3 className="text-[.9rem] font-semibold text-[var(--color-wedding)] mb-2 pl-3 border-l-2 border-[var(--color-wedding)]">
            {MONTH_NAMES[mm] || mm}
          </h3>
          {grouped[mm].map(t => {
            const done = state.done.includes(t.id);
            return (
              <div key={t.id} className={`flex items-start gap-3 py-2 border-b border-[var(--color-border)] text-[.75rem] ${done ? 'opacity-50' : ''}`}>
                <div className="text-[.65rem] text-[var(--color-muted)] min-w-[70px]">{t.deadline}</div>
                <div className="flex-1">
                  <div className="text-[var(--color-warm)]">{done ? '✅ ' : ''}{t.title}</div>
                  <div className="text-[.65rem] text-[#888]">👤 {t.assign}</div>
                </div>
              </div>
            );
          })}
        </div>
      ))}
    </div>
  );
}
```

- [ ] **Step 2: Create PlanningPage.jsx**

```jsx
import { useWedding } from '../contexts/WeddingContext';
import PinGate from '../components/planning/PinGate';
import Dashboard from '../components/planning/Dashboard';
import WeatherCard from '../components/planning/WeatherCard';
import TaskList from '../components/planning/TaskList';
import BudgetTracker from '../components/planning/BudgetTracker';
import TimelineView from '../components/planning/TimelineView';
import Settings from '../components/planning/Settings';

const VIEWS = {
  tasks: { label: '📋 Úkoly', component: TaskList },
  budget: { label: '💰 Budget', component: BudgetTracker },
  timeline: { label: '📅 Časová osa', component: TimelineView },
  settings: { label: '⚙️ Info', component: Settings }
};

export default function PlanningPage() {
  const { state, setView } = useWedding();
  const view = state.view || 'tasks';
  const ViewComponent = VIEWS[view]?.component || VIEWS.tasks.component;

  return (
    <PinGate>
      <div style={{ paddingBottom: 'calc(80px + env(safe-area-inset-bottom, 10px))' }}>
        <Dashboard />
        <WeatherCard />
        <ViewComponent />
      </div>

      {/* Bottom nav */}
      <nav className="fixed bottom-0 left-0 right-0 z-[100] bg-[var(--color-card)] border-t border-[var(--color-border)] flex justify-around py-1"
        style={{ paddingBottom: 'env(safe-area-inset-bottom, 4px)' }}>
        {Object.entries(VIEWS).map(([key, v]) => (
          <button
            key={key}
            onClick={() => setView(key)}
            className={`flex flex-col items-center gap-0.5 py-1.5 px-3 border-0 bg-transparent cursor-pointer font-[inherit] min-w-[60px] min-h-[52px] ${view === key ? 'text-[var(--color-wedding)]' : 'text-[var(--color-muted)]'}`}>
            <span className="text-[1.1rem]">{v.label.split(' ')[0]}</span>
            <span className="text-[.6rem] font-semibold">{v.label.split(' ')[1] || v.label.split(' ')[0]}</span>
          </button>
        ))}
      </nav>
    </PinGate>
  );
}
```

- [ ] **Step 3: Commit**

```bash
cd C:/dev/PS7 && git add src/pages/PlanningPage.jsx src/components/planning/TimelineView.jsx && git commit -m "feat: PlanningPage + TimelineView — compose with bottom nav"
```

---

### Task 13: App.jsx — Router + Layout + particles container

**Files:**
- Create: `src/App.jsx`

- [ ] **Step 1: Create App.jsx**

```jsx
import { Routes, Route } from 'react-router-dom';
import { UIProvider } from './contexts/UIContext';
import { WeddingProvider } from './contexts/WeddingContext';
import { WeatherProvider } from './contexts/WeatherContext';
import LandingPage from './pages/LandingPage';
import PlanningPage from './pages/PlanningPage';
import ScrollToTop from './components/layout/ScrollToTop';
import Toast from './components/shared/Toast';

export default function App() {
  return (
    <UIProvider>
      <WeddingProvider>
        <WeatherProvider>
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/planovani" element={<PlanningPage />} />
          </Routes>

          <ScrollToTop />
          <Toast />

          {/* Particle container for celebration effects */}
          <div id="particles" className="fixed inset-0 pointer-events-none z-[300]" />

          {/* Particle styles */}
          <style>{`
            .particle {
              position: absolute;
              font-size: 1.4rem;
              animation: particleUp .8s ease-out forwards;
              pointer-events: none;
            }
            @keyframes particleUp {
              0% { opacity: 1; transform: translateY(0) scale(1); }
              100% { opacity: 0; transform: translateY(-80px) scale(.4); }
            }
          `}</style>
        </WeatherProvider>
      </WeddingProvider>
    </UIProvider>
  );
}
```

- [ ] **Step 2: Verify build**

Run: `cd C:/dev/PS7 && npm run build`
Expected: Build succeeds, `dist/` directory created

- [ ] **Step 3: Verify dev server**

Run: `cd C:/dev/PS7 && npm run dev`
Expected: Dev server starts, all routes render, no console errors

- [ ] **Step 4: Commit**

```bash
cd C:/dev/PS7 && git add src/App.jsx && git commit -m "feat: App.jsx — Router + Layout + providers + particles"
```

---

### Task 14: PWA + deploy workflow update

**Files:**
- Create: `public/manifest.json`, `public/favicon.svg`
- Modify: `.github/workflows/deploy.yml`

- [ ] **Step 1: Create public/manifest.json**

```json
{
  "name": "Svatba Paprčkovi 2026",
  "short_name": "Svatba 2026",
  "start_url": "/PaprckoviSvatba2026/",
  "display": "standalone",
  "background_color": "#faf7f2",
  "theme_color": "#8b3a3a",
  "icons": [{
    "src": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 180 180'%3E%3Crect width='180' height='180' rx='36' fill='%238b3a3a'/%3E%3Ctext x='90' y='130' text-anchor='middle' font-size='120'%3E💒%3C/text%3E%3C/svg%3E",
    "sizes": "180x180",
    "type": "image/svg+xml"
  }]
}
```

- [ ] **Step 2: Create public/favicon.svg**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <rect width="100" height="100" rx="20" fill="#8b3a3a"/>
  <text x="50" y="72" text-anchor="middle" font-size="70">💒</text>
</svg>
```

- [ ] **Step 3: Check and update .github/workflows/deploy.yml**

Read the existing workflow first, then replace with Vite-based deploy:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [master]

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - run: npm ci
      - run: npm run build
      - name: Deploy to gh-pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```

- [ ] **Step 4: Add SPA fallback 404.html**

Create `public/404.html`:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Redirecting...</title>
  <script>
    sessionStorage.redirect = location.href;
  </script>
  <meta http-equiv="refresh" content="0;URL='/PaprckoviSvatba2026/'">
</head>
<body>Přesměrování...</body>
</html>
```

- [ ] **Step 5: Copy original index.html for reference**

```bash
cd C:/dev/PS7 && cp src/index.html src/index.original.html
```

- [ ] **Step 6: Verify full build**

Run: `cd C:/dev/PS7 && npm run build`
Expected: Clean build in `dist/`, all assets optimized

- [ ] **Step 7: Commit**

```bash
cd C:/dev/PS7 && git add public/ .github/workflows/deploy.yml src/index.original.html && git commit -m "config: PWA manifest, favicon, Vite deploy workflow, archive original HTML"
```

---

### Task 15: Final integration — verification and cleanup

- [ ] **Step 1: Verify dev server serves both routes**

Run: `cd C:/dev/PS7 && npm run dev`
Open: `http://localhost:5173/PaprckoviSvatba2026/`
Check: Landing page renders all 6 sections
Check: Navigate to `/planovani` — PIN gate shows
Check: Enter PIN "2026" — planning page renders
Check: Dashboard cards show correct numbers
Check: Task check/uncheck works with particles
Check: Budget tracker works
Check: Dark mode toggle
Check: `/planovani` redirects or shows 404 on direct access (GitHub Pages limitation noted)

- [ ] **Step 2: Check all features from original app**

Checklist:
- [ ] Countdown timer works (updates every 60s)
- [ ] Dashboard shows: hotovo, zbývá, %
- [ ] Progress bar updates on task toggle
- [ ] TaskList: filter by status, category, person, search, sort
- [ ] TaskItem: check/uncheck, urgency badge, overdue style
- [ ] BudgetTracker: edit prices, check done, total/limit bar
- [ ] WeatherCard: shows Ostrava weather from Open-Meteo
- [ ] Dark mode: toggle persists in localStorage
- [ ] Cloud sync: push/pull works (needs GitHub token in Info)
- [ ] Particles on task check
- [ ] Confetti when all tasks done
- [ ] ScrollToTop button visible after scroll
- [ ] PWA manifest loads correctly
- [ ] Responsive: 375px, 768px, 1024px
- [ ] prefers-reduced-motion: animations disabled
- [ ] Landing: RSVP form submits and shows thank you
- [ ] Landing: timeline renders all 6 milestones
- [ ] Landing: venue cards render with correct info
- [ ] Landing: gallery grid renders (placeholder state)

- [ ] **Step 3: Fix any issues found in verification**

- [ ] **Step 4: Test production build**

Run: `cd C:/dev/PS7 && npm run build && npm run preview`
Verify: Built app works in preview mode

- [ ] **Step 5: Final commit**

```bash
cd C:/dev/PS7 && git add -A && git status
# Review changes, ensure no secrets/node_modules committed
git commit -m "feat: complete React SPA — landing + planning, all features migrated"
```

- [ ] **Step 6: Push and deploy**

```bash
cd C:/dev/PS7 && git push
```
After push: watch GitHub Actions for successful deploy
Verify: `https://doma77git.github.io/PaprckoviSvatba2026/` shows new React app

---

## Verification checklist (pre-merge)

Run through these on the live site:
1. `/` loads landing page with all 6 sections
2. Countdown shows correct days to wedding
3. `/planovani` shows PIN gate
4. PIN "2026" unlocks planning page
5. Task check creates particle effect
6. All 35 tasks → confetti burst
7. Budget tracker: edit price, changes persist on reload
8. Dark mode toggle persists on reload
9. Mobile: 375px viewport looks correct, tap targets ≥44px
10. PWA: "Add to Home Screen" prompt works
