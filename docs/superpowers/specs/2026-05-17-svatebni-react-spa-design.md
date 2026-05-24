# Design spec: Svatební React SPA

**Date:** 2026-05-17
**Status:** approved
**Stack:** Vite + React 19 + Tailwind CSS 4 + React Router

## Overview

Přepis svatebního webu Paprčkovi z monolitu `index.html` (1041 řádků vanilla HTML/CSS/JS) do React SPA se dvěma routami — veřejná landing page pro hosty a PIN-chráněná plánovací sekce pro organizátory.

**Live URL:** https://doma77git.github.io/PaprckoviSvatba2026/
**Repo:** doma77git/PaprckoviSvatba2026

## Design system

| Token | Value |
|-------|-------|
| `--primary` | `#8b3a3a` bordó |
| `--gold` | `#d4a017` zlatá |
| `--bg` | `#faf7f2` warm cream |
| `--text` | `#2d2a24` tmavě hnědá |
| `--muted` | `#999` |
| Font headings | Cormorant Garamond (Google Fonts) |
| Font UI | System sans-serif stack |
| Border radius | 12px (large), 8px (small) |
| Tap target min | 44px |

Dark mode: invert background to `#1a1816`, cards to `#252220`, primary to `#c46a6a`.

Tailwind config rozšiřuje tyto tokeny jako custom colors + font family.

## Routes

### `/` — Landing Page (veřejná)

6 sekcí v narativním scroll-triggered formátu:

1. **Hero** — full-width, bordó gradient. Jména "Martin & Dagmar", příjmení "Paprčkovi", datum "29. srpna 2026", countdown. Fallback: gradient vždy funguje; fotka páru jako optional overlay.
2. **Náš příběh** — vertikální timeline s 6 milníky: Gabriela → Seznámení 1.5.1997 → Kristýnka → Natálka → Kačka → Svatba 29.8.2026. Zlatá linka, bordó finální bod.
3. **Kdy & Kde** — dvě karty: radnice (bordó left border, 11:15) + Zlatá koliba (zlatá left border, po obřadu). Pod nimi mini mapa (OpenStreetMap/Mapy.cz tile).
4. **Fotogalerie** — Bento grid (asymetrický, 5 fotek). Lazy loading. Lightbox na klik.
5. **RSVP** — formulář: jméno (required), počet osob (stepper +/-), zpráva (optional). Submit tlačítko. Data se ukládají do GitHubu stejným mechanismem jako stávající cloud sync. Pod formulářem seznam hostů (8 položek, ~14-20 lidí) s počty a `+?` indikátory.
6. **Navigace** — dark banner "Pro organizátory" s tlačítkem "Vstoupit" → přechod na `/planovani`.

### `/planovani` — Plánování (PIN-chráněná)

Jednoduchý PIN gate: při první návštěvě se zeptá na PIN (default "2026"), uloží do localStorage. Bez správného PIN přesměruje na `/`.

Komponenty (přenesené z existující appky):
- **Dashboard** — 4 karty (zbývá dní, splněno úkolů, rozpočet, progress bar)
- **WeatherCard** — Open-Meteo API, lokalita Ostrava
- **TaskList** — 35 úkolů, 4 kategorie (mandatory/important/optional/done), 4 assignees (Mamka, Taťka, Žanetka, Kikinka), checkbox + oslavné particle efekty
- **BudgetTracker** — položky rozpočtu, editovatelné, progress bar, hard cap 100 000 Kč
- **Settings** — dark mode toggle, cloud sync trigger, info

Všechny featury z původní appky zůstávají:
- Dark mode (data-theme atribut na `<html>`, localStorage persistence)
- Cloud sync (GitHub API — čtení/zápis `src/state.json`)
- PWA (manifest.json, apple-touch-icon, theme-color)
- Confetti při 100% splnění, particle efekty při jednotlivých checknutích
- Scroll-to-top tlačítko
- prefers-reduced-motion respektování

## Komponentový strom

```
App
├── Layout (Header, Footer)
├── LandingPage
│   ├── HeroSection
│   ├── StoryTimeline
│   ├── VenueInfo
│   ├── GalleryGrid
│   │   └── Lightbox
│   ├── RSVPSection
│   │   └── GuestList
│   └── PlannerNavBanner
└── PlanningPage
    ├── PinGate
    ├── Dashboard
    ├── WeatherCard
    ├── TaskList
    │   └── TaskItem (×35)
    ├── BudgetTracker
    │   └── BudgetItem (×N)
    └── Settings
```

## State management

React Context — 3 providery:
- **WeddingContext** — svatební data (tasks, budget, rsvp, guests)
- **UIContext** — dark mode, PIN state
- **WeatherContext** — Open-Meteo data, loading/error

Data persistence: localStorage + GitHub API sync (stejný mechanismus jako stávající appka).

## Migrační poznámky

- Stávající `src/index.html` zůstane jako reference během vývoje, před deployem se nahradí.
- `src/state.json` zůstává jako cloud sync storage — beze změny.
- `manifest.json` zůstává, upraví se paths pro Vite build output.
- `.github/workflows/deploy.yml` se upraví — `vite build` → `dist/` → gh-pages.
- GitHub Pages musí sloužit SPA fallback: `404.html` přesměrování (nebo hash router).

## Co se NEDĚLÁ

- Žádný backend/server
- Žádná databáze
- Žádný auth provider (OAuth, Firebase)
- Žádný CMS pro fotky
- Žádné email notifikace z RSVP
- Žádné animace nad rámec stávajících (particles, confetti)
- Žádné i18n (pouze čeština)

## Soubory k vytvoření/změně

| Soubor | Akce |
|--------|------|
| `package.json` | Nový — Vite + React + Tailwind + React Router |
| `vite.config.js` | Nový — base: '/PaprckoviSvatba2026/' |
| `tailwind.config.js` | Nový — custom theme |
| `index.html` | Nový — Vite entry point |
| `src/main.jsx` | Nový — React root + Router |
| `src/App.jsx` | Nový — Layout + Routes |
| `src/contexts/*.jsx` | Nové — 3 providery |
| `src/pages/LandingPage.jsx` | Nový |
| `src/pages/PlanningPage.jsx` | Nový |
| `src/components/**/*.jsx` | Nové — ~15 komponent |
| `src/data/tasks.js` | Nový — extrahované z původního HTML |
| `src/data/guests.js` | Nový |
| `.github/workflows/deploy.yml` | Upravit — Vite build |
| `src/index.html` (původní) | Archivovat / smazat před deployem |
