# 💒 Svatba Paprčkovi 2026

Svatební plánovač — **29. srpna 2026, 11:15**
Read-only architektura: CSV soubory = source of truth, appka jen čte. Editace přes PC → git. Bez npm, bez backendu.

## ⚡ Rychlé odkazy

| Co | Kde |
|----|-----|
| **Veřejná stránka** (produkce) | https://martinpaprcka77.github.io/PaprckoviSvatba2026/ |
| **Plánovač** (PIN chráněno) | https://martinpaprcka77.github.io/PaprckoviSvatba2026/planner.html |
| **Archiv červen 2026** | https://martinpaprcka77.github.io/PaprckoviSvatba2026/index_june.html |
| **Úkoly** | [data/tasks.csv](data/tasks.csv) |
| **Hosté** | [data/guests.csv](data/guests.csv) |
| **Rozpočet** | [data/budget.csv](data/budget.csv) |
| **Historie rozhodnutí** | [data/changelog.csv](data/changelog.csv) |
| **Repozitář** | https://github.com/martinpaprcka77/PaprckoviSvatba2026 |

## 📊 Aktuální stav

```
✅ 6/36 splněno  ·  💰 89 500 / 100 000 Kč naplánováno
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
├── index.html              ← Veřejná stránka (romantický design, bez rozpočtu)
├── planner.html            ← Plánovač pro Žanetku (PIN chráněno, hint: rok narození JP)
├── index_june.html         ← Archiv — stav ke červnu 2026
├── data/
│   ├── tasks.csv           ← 36 úkolů — AUTORITATIVNÍ zdroj
│   ├── budget.csv          ← Rozpočet — AUTORITATIVNÍ zdroj
│   ├── guests.csv          ← Seznam hostů
│   └── changelog.csv       ← Historie rozhodnutí
├── docs/                   ← PRD, design spec, knowledge base
├── public/                 ← favicon, manifest, 404
├── media/                  ← Sweet Caroline MP3 (2 verze)
└── .github/workflows/      ← auto-deploy na push do masteru
```

### Data flow
1. Editace `data/*.csv` → commit + push
2. Appka fetchuje z GitHub Raw při každém otevření (no-cache)
3. **localStorage se při každém načtení přepisuje daty z CSV** — žádné lokální stavy
4. Auto-refresh každých 12 hodin (i když stránka zůstane otevřená)
5. Push do `master` → GitHub Actions → `gh-pages` → live (~1 min)

### Stránky
- **`/`** — Veřejná, romantická, iPhone-optimized. Checklist (splněné skryté), harmonogram, hosté. Odkaz na plánovač.
- **`/planner.html`** — PIN chráněno (hint: rok narození JP). Plná verze — vše včetně rozpočtu a changelogu.
- **`/index_june.html`** — Archivní snímek stavu ke červnu 2026.

## 🔒 Pravidla

1. **Budget 100 000 Kč hard cap** — změna ceny v `budget.csv` → vyrovnat jinde
2. **Nikdy neodebírat Děti** z úkolů — co-assign (`Děti, Mamka`), nikdy nenahrazovat
3. **Jména bez háčků, bez příjmení** — Mikesovi (ne Mikešovi), jen křestní / přezdívky
4. **Append-only poznámky** v tasks.csv; oddělovač `;`
5. **budget.csv je autoritativní** pro peníze — tasks.csv neobsahuje částky
6. **Appka je read-only** — CSV = source of truth, appka nikdy nikam nezapisuje
7. **Force refresh** — při každém otevření fetch čerstvých CSV, localStorage se přepisuje

## 🔧 Lokální vývoj

```bash
python -m http.server 8080   # http://localhost:8080/
```

## 📋 Editace dat

Všechna data se editují přímo na GitHubu nebo v git klientu. Nikdy přes appku.

| Soubor | Co editovat |
|--------|-------------|
| `data/tasks.csv` | Změna stavu (`open`→`done`), přidání poznámky, nový úkol |
| `data/budget.csv` | Skutečná cena (`amount_actual`), nová položka |
| `data/guests.csv` | Potvrzení hosta (`confirmed`), počet osob |
| `data/changelog.csv` | Přidat řádek po každém důležitém rozhodnutí |

### CSV schéma

**tasks.csv:** `id, deadline, title, assign, category, status, note`
- `category`: `mandatory` / `important` / `optional`
- `status`: `open` / `done`
- `note`: volný text, více hodnot odděleno `;`

**budget.csv:** `id, item, category, amount_plan, amount_actual, note`
- `amount_actual`: vyplnit až při skutečném zaplacení

**guests.csv:** `id, name, side, count, confirmed, note`
- `side`: `mamka` / `tatka` / `spolecni`

**changelog.csv:** `date, who, what, detail`

## 🚀 Deploy

Push do `master` → GitHub Actions → `gh-pages` → live (~1 min)

```bash
git add data/tasks.csv
git commit -m "tasks: T011 done — oznámení rozesláno"
git push
```

## 📜 Historie verzí

| Verze | Datum | Popis |
|-------|-------|-------|
| **1.0.0** | 2026-05-16 | Počáteční verze — single-file HTML; localStorage; 35 úkolů |
| **1.1.0** | 2026-05-21 | Git-backed data; MD soubory; dual deploy; Excel hooks |
| **1.2.0** | 2026-05-24 | v0 baseline; deploy fix; cleanup |
| **1.3.0** | 2026-05-26 | 37 úkolů; guests foundations |
| **1.3.1** | 2026-05-27 | Guests live; budget přepracován |
| **1.3.2** | 2026-05-27 | Hide-done toggle; collapsed budget; v3music |
| **2.0.0** | 2026-06-02 | CSV migrace; romantický design; planner.html; auto-refresh; žádný localStorage state |
