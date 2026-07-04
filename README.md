# 💒 Svatba Paprčkovi 2026

Svatební plánovač — **29. srpna 2026, 11:15**, Nová radnice Ostrava → Koliba U Zlatého Jarouše.
Read-only: CSV soubory v `data/` = zdroj pravdy, appka jen čte, editace přes git. Bez npm, bez backendu. Technické detaily (architektura, CSV schéma, pravidla) viz [`.claude/CLAUDE.md`](.claude/CLAUDE.md).

## ⚡ Rychlé odkazy

| Co | Kde |
|----|-----|
| **Veřejná stránka** | https://martinpaprcka77.github.io/PaprckoviSvatba2026/ |
| **Landing page** (nový design) | https://martinpaprcka77.github.io/PaprckoviSvatba2026/landing.html |
| **Plánovač** (PIN chráněno) | https://martinpaprcka77.github.io/PaprckoviSvatba2026/planner.html |
| **Archiv červen 2026** | https://martinpaprcka77.github.io/PaprckoviSvatba2026/index_june.html |
| **Úkoly / Rozpočet / Hosté / Log** | [tasks.csv](data/tasks.csv) · [budget.csv](data/budget.csv) · [guests.csv](data/guests.csv) · [changelog.csv](data/changelog.csv) |
| **Repozitář** | https://github.com/martinpaprcka77/PaprckoviSvatba2026 |

## 📊 Aktuální stav

> Snímek k 5. 7. 2026 — po každé větší editaci `data/*.csv` přepočítej z CSV, ne z paměti.

```
✅ 8/28 splněno  ·  💰 80 500 / 100 000 Kč naplánováno
```

| Kategorie | Úkolů | Plán |
|-----------|-------|------|
| 🔴 Povinné | 16 | 76 500 Kč |
| 🟡 Důležité | 10 | 4 000 Kč |
| 🟢 Volitelné | 2 | 0 Kč |
| **Celkem** | **28** | **80 500 Kč** |

**Hotovo:** termín · radnice · děti · svědci · oddávající · schůzka prstýnky · prstýnky vyzvednuty · svatební šaty
**Rozpracováno:** svatební oznámení — tisk hotovo, zbývá rozeslat + RSVP
**Zrušeno:** dárky pro svědky · dárky na přivítanou · guestbook+favory · proslovy svědků · confetti · ubytování pro hosty · dekorace na radnici

## 👥 Lidé

| Kdo | Role | Úkolů |
|-----|------|--------|
| **Mamka** | Nevěsta | 15 |
| **Taťka** | Ženich | 4 |
| **Žanetka** | Hlavní organizátorka, svědkyně ženicha | 3 |
| **Kikinka** | Svědkyně nevěsty | 1 |
| **Děti** | 4 dcery: Gabriela, Kristýnka, Natálka, Kačka | 5 |

## 📅 Klíčové milníky

| Kdy | Co |
|-----|-----|
| ~~29. 5. 2025~~ | ✅ Termín, radnice, děti, svědci |
| ~~15. 5. 2026~~ | ✅ Oddávající domluven |
| ~~25. 5. 2026~~ | ✅ Schůzka prstýnky |
| ~~3. 7. 2026~~ | ✅ Prstýnky vyzvednuty |
| ~~4. 7. 2026~~ | ✅ Svatební šaty hotovo |
| 10. 7. 2026 | Svatební oznámení |
| 15. 7. 2026 | Koliba catering, oblek, hosté |
| 24. 7. 2026 | Rozlučka se svobodou |
| 1. 8. 2026 | Doplňky, ubytování |
| 10.–20. 8. 2026 | Výzdoba, program |
| 25. 8. 2026 | Poslední úpravy |
| **29. 8. 2026** | **💒 SVATBA 🎉** |

## 🏛️ Místo

- **Obřad:** 11:15, Nová radnice Ostrava
- **Hostina:** Koliba U Zlatého Jarouše (U Miloše), Karasova 1130/23, 709 00 Ostrava
- [📍 Navigovat](https://maps.google.com/?q=Karasova+1130/23,+709+00+Ostrava)

## 🔧 Vývoj a editace dat

```bash
python -m http.server 8080   # http://localhost:8080/
```

Data se editují přímo v `data/*.csv` + git commit/push (nikdy přes appku) → push na `master` → GitHub Actions → live za ~1 min.

## 📜 Historie verzí

| Verze | Datum | Popis |
|-------|-------|-------|
| **1.0.0** | 2026-05-16 | Počáteční verze — single-file HTML, localStorage |
| **1.1.0** | 2026-05-21 | Git-backed data, MD soubory, dual deploy |
| **1.2.0** | 2026-05-24 | v0 baseline, deploy fix |
| **1.3.x** | 2026-05-26/27 | Hosté a rozpočet přepracovány |
| **2.0.0** | 2026-06-02 | CSV migrace, romantický design, planner.html |
| **2.1.0** | 2026-07-04 | Reálný progres; zrušeno 5 úkolů |
| **2.2.0** | 2026-07-05 | Zrušeno ubytování + dekorace radnice; oznámení tisk hotovo |
