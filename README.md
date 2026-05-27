# 💒 Svatba Paprčkovi 2026

Svatební plánovač — **29. srpna 2026, 11:15**
Git-backed architektura: data v MD souborech, appka je čte a renderuje. Bez npm, bez backendu.

## ⚡ Rychlé odkazy

| Co | Kde |
|----|-----|
| **Plánovač v1** (produkce) | https://doma77git.github.io/PaprckoviSvatba2026/ |
| **Plánovač v2** (testovací) | https://doma77git.github.io/PaprckoviSvatba2026/v2/ |
| **v3music (v1+audio)** | https://doma77git.github.io/PaprckoviSvatba2026/v3music/ |
| **v0 (archivní baseline)** | https://doma77git.github.io/PaprckoviSvatba2026/v0/ |
| **Úkoly** | [data/tasks.md](data/tasks.md) |
| **Hosté** | [data/guests.md](data/guests.md) |
| **Rozpočet Excel** | [data/rozpocet-svatba-2026.xlsx](data/rozpocet-svatba-2026.xlsx) |
| **Manuální Excel** | [data/manualrozpocet-svatba-2026.xlsx](data/manualrozpocet-svatba-2026.xlsx) |
| **PRD (specifikace)** | [docs/PRD-svatba-paprckovi-2026.md](docs/PRD-svatba-paprckovi-2026.md) |
| **Repozitář** | https://github.com/doma77git/PaprckoviSvatba2026 |
| **Archivní verze** | https://doma77git.github.io/PaprckoviSvatba2026/Older_up2date/ |

## 📊 Aktuální stav

```
✅ 6/37 splněno  ·  💰 0/100 000 Kč utraceno
```

| Kategorie | Úkolů | Plán |
|-----------|-------|------|
| 🔴 Povinné (mandatory) | 19 | 94 500 Kč |
| 🟡 Důležité (important) | 14 | 5 000 Kč |
| 🟢 Volitelné (optional) | 4 | 500 Kč |
| **Celkem** | **37** | **100 000 Kč** |

**Hotovo (6):** termín ✓ · radnice ✓ · děti ✓ · svědci ✓ · oddávající ✓ · schůzka prstýnky ✓

## 👥 Lidé

| Kdo | Role | Úkolů |
|-----|------|--------|
| **Mamka** | Nevěsta | 18 |
| **Taťka** | Ženich | 8 |
| **Žanetka** | Hlavní organizátorka, svědkyně ženicha | 7 |
| **Kikinka** | Svědkyně nevěsty | 3 |
| **Děti** | 4 dcery: Gabriela, Kristýnka, Natálka, Kačka — výzdoba, dort, focení, hudba, foto | 5 |

## 📅 Klíčové milníky

| Kdy | Co |
|-----|-----|
| ~~29. 5. 2025~~ | ✅ Termín, radnice, děti, svědci |
| ~~15. 5. 2026~~ | ✅ Oddávající domluven |
| **25. 5. 2026** | 💍 Schůzka prstýnky (Mamka+Taťka+Žanetka) |
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
./
├── index.html              ← v1 (single-file, localStorage, inline data)
├── v0/index.html           ← v0 archive (Svatba_001 baseline, 20 tasks, Aug 29)
├── v2/index.html           ← v2 (fetches MD z GitHubu, PIN write)
├── data/
│   ├── tasks.md            ← 37 úkolů — AUTORITATIVNÍ zdroj
│   ├── guests.md           ← seznam hostů
│   ├── rozpocet-svatba-2026.xlsx        ← auto-gen Excel (SUMIF vzorce)
│   └── manualrozpocet-svatba-2026.xlsx  ← manuální Excel
├── docs/                   ← PRD, design spec, knowledge base
├── public/                 ← favicon, manifest, 404
├── Older/                  ← archivní verze (001–v42)
├── Older_up2date/          ← opravené archivní verze
└── .github/workflows/      ← auto-deploy na push do masteru
```

### Data flow
1. Editace `data/tasks.md` / `data/guests.md` → commit + push
2. v2 appka automaticky fetchuje z GitHub Raw
3. PostToolUse hook přegeneruje `rozpocet-svatba-2026.xlsx`
4. Push do `master` → GitHub Actions → `gh-pages` → live

### Dual deploy
- **`/v0/`** — archivní baseline (Svatba_001, 20 úkolů, 29.8.)
- **`/`** — v1 produkce (stabilní, offline-first, localStorage)
- **`/v2/`** — v2 testovací (git-backed, PIN sync, live data)

## 🔒 Pravidla

1. **Budget 100 000 Kč hard cap** — jakákoliv změna ceny musí být vyrovnána jinde
2. **Nikdy neodebírat Děti** z úkolů — co-assign (`Děti, Mamka`), nikdy nenahrazovat
3. **Jména bez háčků, bez příjmení** — Mikesovi (ne Mikešovi), jen křestní / přezdívky
4. **Append-only poznámky** v tasks.md; oddělovač `; `
5. **Po editaci tasks.md:** aktualizovat header, people tabulku, budget tabulku
6. **PRD je autoritativní spec** — `docs/PRD-svatba-paprckovi-2026.md`

## 🔧 Automatizace

| Hook | Co dělá |
|------|---------|
| **PreToolUse** | Blokuje editace `.env`, `package-lock.json`, `.git/` |
| **PostToolUse** | Přegeneruje Excel po změně tasks.md |
| **Notification** | Desktop notifikace při čekání na input |
| **GitHub Actions** | Auto-deploy na push do masteru |
