## 2026-05-26

- **37 úkolů:** Přidán úkol "Rozlučka se svobodou" (important, 0 Kč, Žanetka)
- **Sync všech docs:** README, AGENTS, PRD, CLAUDE.md — 36→37 úkolů, 13→14 important, 5→6 hotovo
- **Opravy:** Součet >36→37 v tasks.md, important 13→14 v CLAUDE.md
- **4 Continue checks:** tasks-md-data-integrity, people-rules, no-secrets-exposure, budget-hard-cap
- **People sync:** Taťka 9→8, Žanetka 6→7, Děti 3→5 (hudba+fotokoutek→Děti)

# HISTORY — Svatba Paprčkovi 2026

## 2026-05-26

- **Schůzka prstýnky (Mamka+Taťka+Žanetka) označena jako hotová** — proběhla 25. 5. 2026 ✓
- **37 úkolů:** Přidán úkol "Rozlučka se svobodou" (important, 0 Kč, Žanetka)
- **Sync všech docs:** README, AGENTS, PRD, CLAUDE.md — 36→37 úkolů, 13→14 important, 5→6 hotovo
- **4 Continue checks:** tasks-md-data-integrity, people-rules, no-secrets-exposure, budget-hard-cap
- **People sync:** Taťka 10→8, Žanetka 6→7, Děti 3→5 (hudba+fotokoutek→Děti)

## 2026-05-24 (večer/noc)

- **v0 baseline:** `v0/index.html` vytvořen z `Older/Svatba_001.html`. Všechna data posunuta z 15.6.→29.8.2026 (+75 dní). 20 úkolů, 81 500 Kč budget — čistý referenční bod před PRD expanzí na 36 úkolů. Push na GitHub + deploy přes Pages.
- **Docs sync:** 6 souborů aktualizováno — CLAUDE.md (20→36 úkolů, 81.5K→100K budget, people counts), data/budget.md (kompletní přepis 20→36 položek dle tasks.md), README/AGENTS/copilot-instructions (architektura rozšířena o v0/), Older_up2date/README.md (v3→v0 reference fix).
- **Deploy workflow fix:** `peaceiris/actions-gh-pages` (push do gh-pages větve) → `actions/deploy-pages` (nativní Actions deployment). Repo používá `build_type: workflow` — peaceiris push do gh-pages už nespouštěl deployment. v0/ vracelo 404 do opravy.
- **Stale workflow:** `pages-build-deployment` (GitHub auto-created) deaktivován — poslední běh 10:40 UTC před přepnutím na workflow typ. GitHub nedovolil ruční disable (built-in workflow).

## 2026-05-24 (odpoledne)

- **Docs cleanup:** 24 PAPROS/Brain leftover files removed (Architecture, CrossAgent, KnowledgeBase, Generated, Workflows, CommandReference, ProjectOverview, Roadmap_v2, PAPROS_history, AI_Instructions, SessionMemory). Repo 60→42 tracked files.
- **build_excel.py:** Vytvořen skript pro auto-generování Excelu z tasks.md. 3 listy (Všechny úkoly, Podle osoby, Rozpočet). Hook nyní funkční.
- **Excel hook fix:** `sys.exit(0 if not tasks.md else 0)` → `(sys.exit(0) if not tasks.md else None)` — původní kód vždy ukončil proces, Excel se nikdy negeneroval.
- **PRD timeline:** Doplněn chybějící task #36 (Schůzka prstýnky, 25.5.)
- **Deploy conflict:** Odstraněn redundantní `static.yml` (uploadoval celý repo root), `deploy.yml` zůstává (kurátované soubory).
- **Cross-doc sync:** Opraveny zastaralé počty — 6→5 osob (Older_up2date/README.md), budget 86.5/11.5/2k→94.5/5/0.5k, 35→36 tasků (wedding-data-instructions.md).
- **Git:** Orphan→sync s origin/master, user.email→noreply, .gitignore rozšířen o ralph-loop.
- **Úklid:** 14 PNG screenshotů, 2 .original.md backupů, run_v2.py, test_v2.py, .playwright-mcp/, :USERPROFILE/ — vše smazáno.

## 2026-05-24 (ráno/dopoledne)

- **Git history squash:** 117→1 commit (master), 82→1 commit (gh-pages). Clean repo.
- **Deep cross-check:** 7 discrepancies found → Mamka 16→17 (oddávající reassigned), then 17→18 (Dáda merged as Mamka alias). Děti assignee opravy v PRD, PRD 35→36 tasků
- **Dáda = Mamka = Dagmar Sobková** — sloučeno do 5 osob, Mamka 18 úkolů. Schůzka prstýnky Mamka+Taťka+Žanetka.
- **README přepsán:** přehlednější struktura, aktuální stav, milníky, pravidla, automatizace
- **Code review:** 6 stale Dáda references found & fixed in copilot-instructions.md + v1 index.html (persons filter, stats, task #36)

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