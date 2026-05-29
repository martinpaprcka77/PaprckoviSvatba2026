# 💒 Svatba Paprčkovi 2026

Svatební plánovač — **29. srpna 2026, 11:15**
Read-only architektura: MD soubory = source of truth, appka jen čte. Editace přes PC → git. Bez npm, bez backendu.

## ⚡ Rychlé odkazy

| Co | Kde |
|----|-----|
| **Plánovač v1** (produkce) | https://doma77git.github.io/PaprckoviSvatba2026/ |
| **v3music (v1+audio)** | https://doma77git.github.io/PaprckoviSvatba2026/v3music/ |
| **v0 (archivní baseline)** | https://doma77git.github.io/PaprckoviSvatba2026/v0/ |
| **Úkoly** | [data/tasks.md](data/tasks.md) |
| **Hosté** | [data/guests.md](data/guests.md) |
| **Rozpočet Excel** | [data/rozpocet-svatba-2026.xlsx](data/rozpocet-svatba-2026.xlsx) |
| **Manuální Excel** | [data/manualrozpocet-svatba-2026.xlsx](data/manualrozpocet-svatba-2026.xlsx) |
| **PRD (specifikace)** | [docs/PRD-svatba-paprckovi-2026.md](docs/PRD-svatba-paprckovi-2026.md) |
| **Repozitář** | https://github.com/doma77git/PaprckoviSvatba2026 |
| **Archiv** | [`archive/`](archive/) |

## 📊 Aktuální stav

```
✅ 6/36 splněno  ·  💰 0/89 500 Kč utraceno
```

| Kategorie | Úkolů | Plán |
|-----------|-------|------|
| 🔴 Povinné (mandatory) | 19 | 84 500 Kč |
| 🟡 Důležité (important) | 13 | 4 500 Kč |
| 🟢 Volitelné (optional) | 4 | 500 Kč |
| **Celkem** | **36** | **89 500 Kč** |

**Hotovo (6):** termín ✓ · radnice ✓ · děti ✓ · svědci ✓ · oddávající ✓ · schůzka prstýnky ✓

## 👥 Lidé

| Kdo | Role | Úkolů |
|-----|------|--------|
| **Mamka** | Nevěsta | 18 |
| **Taťka** | Ženich | 7 |
| **Žanetka** | Hlavní organizátorka, svědkyně ženicha | 7 |
| **Kikinka** | Svědkyně nevěsty | 3 |
| **Děti** | 4 dcery: Gabriela, Kristýnka, Natálka, Kačka — výzdoba, dort, focení, hudba, foto | 5 |

## 📅 Klíčové milníky

| Kdy | Co |
|-----|-----|
| ~~29. 5. 2025~~ | ✅ Termín, radnice, děti, svědci |
| ~~15. 5. 2026~~ | ✅ Oddávající domluven |
| ~~25. 5. 2026~~ | ✅ Schůzka prstýnky (Mamka+Taťka+Žanetka) |
| 10. 7. 2026 | Svatební oznámení |
| 15. 7. 2026 | Koliba catering, šaty, oblek, prstýnky, hosté |
| 1. 8. 2026 | Nápoje, doplňky, ubytování |
| 10.–20. 8. 2026 | Výzdoba, dárky, program |
| 25. 8. 2026 | Poslední úpravy |
| **29. 8. 2026** | **💒 SVATBA 🎉** |

## 🏛️ Místo

- **Obřad:** 11:15, Nová radnice Ostrava
- **Hostina:** Koliba U Zlatého Jarouše (U Miloše), Karasova 1130/23, 709 00 Ostrava
- **Potvrzeno:** 21. 5. 2026 (Mamka + Žanetka osobně u Miloše)
- [📍 Navigovat](https://maps.google.com/?q=Karasova+1130/23,+709+00+Ostrava)

## 🏗️ Architektura

```
master (PRODUCTION) ──────────────────────────────────────
├── index.html              ← v1 (single-file, localStorage) — PRODUCTION
├── data/
│   ├── tasks.md            ← 36 úkolů — AUTORITATIVNÍ zdroj
│   ├── budget.md           ← rozpočet
│   ├── guests.md           ← seznam hostů
├── docs/                   ← PRD, design spec, knowledge base
├── public/                 ← favicon, manifest, 404
└── .github/workflows/      ← auto-deploy na push do masteru

experiment/audio ──────────────────────────────────────────
└── index.html              ← v1 + karaoke audio + lyrics (WIP)

experiment/timeline ───────────────────────────────────────
└── index.html              ← v1 + harmonogram + timeline view (WIP)
```

### Data flow
1. Editace `data/tasks.md` / `data/guests.md` → commit + push
2. Appka fetchuje z GitHub Raw (force refresh při otevření, maže starý localStorage)
3. Push do `master` → GitHub Actions → `gh-pages` → live

### Web verze
- **`/`** — v1 PRODUCTION (offline-first, localStorage, 667 řádků)
- **`experiment/audio`** — Audio + karaoke (feature branch, WIP)
- **`experiment/timeline`** — Harmonogram svatebního dne (feature branch, WIP)

### Historické verze
- **Git tags** — `v0-2026-05-24`, `v1-2026-05-15` (archiv jako git history, ne folders)

## 🔒 Pravidla

1. **Budget 100 000 Kč hard cap** (aktuálně 89 500 Kč) — změna ceny → vyrovnat jinde
2. **Nikdy neodebírat Děti** z úkolů — co-assign (`Děti, Mamka`), nikdy nenahrazovat
3. **Jména bez háčků, bez příjmení** — Mikesovi (ne Mikešovi), jen křestní / přezdívky
4. **Append-only poznámky** v tasks.md; oddělovač `; `
5. **Po editaci tasks.md:** aktualizovat header, people tabulku, budget tabulku
6. **PRD je autoritativní spec** — `docs/PRD-svatba-paprckovi-2026.md`
7. **Appka je read-only** — MD = source of truth, appka nikdy nikam nezapisuje
8. **Force refresh** — při otevření vždy fetch aktuálních MD, localStorage se maže

## 🔧 Automatizace

| Co | Jak |
|----|-----|
| **Budget Excel** | `scripts/rebuild_excel.py` — přegeneruje z tasks.md |
| **GitHub Actions** | Auto-deploy na push do masteru |
