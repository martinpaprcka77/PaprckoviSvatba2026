# HISTORY — Svatba Paprčkovi 2026

## 2026-05-21 (večer)

- **CLAUDE.md + copilot-instructions** sesynchronizovány na aktuální stav (36 úkolů, 6 osob, v2 architektura)
- **Hooks nasazeny** — PreToolUse chrání .env/.git, PostToolUse přegeneruje Excel po změně tasks.md, Notification idle alert
- **Manuální Excel** přidán do `data/manualrozpocet-svatba-2026.xlsx` — uživatelův formát pro editaci budgetu
- **Úkol #36** — Schůzka prstýnky Dáda+Taťka+Žanetka (25.5.2026). Dáda přidán jako 6. osoba.

## 2026-05-21 (ráno/dopoledne)

- **Rozpad cateringu od Miloše:** 30 lidí, polévka 95 Kč/os, druhé 275 Kč/os, oběd = 11 100 Kč, pití+chlast = zbytek do 30k
- **Svatební šaty:** plán 11 100 Kč, budget cca 12 000 Kč, max 15 000 Kč
- **Autoritativní Excel** `data/rozpocet-svatba-2026.xlsx` vytvořen — SUMIF/COUNTIF vzorce, podmíněné formátování, přehled na osobu
- **v2 bugfixy:** 5 oprav (duplicitní podmínka, falsy check actualCosts, TextEncoder base64, extra tečka v datu, počet hotových přes doneSet.size)
- **V2 Architecture zprovozněna:** Git jako databáze — MD soubory v `data/`, appka fetchuje, write přes GitHub API s PINem
- **Dual deploy:** `/` produkce (v1), `/v2/` testovací (v2)
- **Místo konání upřesněno:** Koliba U Zlatého Jarouše (U Miloše), Karasova 1130/23, Ostrava
- **Mikešovi → Mikesovi** opraveno (bez háčku, bez příjmení)

## 2026-05-16

- Finální datum 29.8.2026, budget 100k hard cap, Nová radnice + Zlatá koliba
- Žanetka = hlavní organizátor, Kikinka + Žanetka = svědci
- Appka: 35 tasků, 100k budget, iPhone optimalizace, state v3
- Všechny rozpory vyřešeny, data sjednocena napříč appkou + Brainem

## 2026-05-14

- PRD vytvořen — 35 úkolů, 100 000 Kč, 5 osob
- Appka: single-file HTML, inline CSS/JS, localStorage
- Repo: doma77git/PaprckoviSvatba2026