# 💒 Dagmar + Martin Paprčkovi — Svatba 2026

Památková webová stránka svatby **Dagmar Sobkové a Martina Paprčky**, kteří se vzali **v sobotu 29. srpna 2026 v 11:15** na Nové radnici v Ostravě. Svatba proběhla; stránka je **poděkování + galerie fotek** s počítadlem „společného času" a interním plánovačem pro rodinu.

> **Production:** https://martinpaprcka77.github.io/PaprckoviSvatba2026/
> **Repo je veřejné** (`martinpaprcka77/PaprckoviSvatba2026`), Pages povoleno (build z GitHub Actions).

## 🧩 Stack a konvence

Statická webová aplikace ve stylu HTML/CSS/JavaScript bez build procesu. Primární zdroj dat je sada CSV v `data/`, kterou web čte pouze pro zobrazení; Python skripty v `scripts/` slouží ke statistikám a synchronizaci README/PRD.

- hlavní jazyk: HTML + CSS + JavaScript
- nástroje pro data/docs: Python 3 (`scripts/*.py`)
- testy: `python -m pytest scripts/tests/test_extract_stats.py -q`
- lokální vývoj: `python -m http.server 8080`
- žádný npm build ani bundler; rozhraní je servírováno jako statický obsah
- web je **read-only**, data se editují přes CSV → git → push → Pages

## ⚡ Stránky (publikované)

| Stránka | Odkaz | Stav |
|---|---|---|
| **Veřejná (poděkování + galerie)** | `/` (`index.html`) | publikovaná |
| **Plánovač (rodina, PIN)** | `/planner.html` | publikovaná |

Následující stránky jsou **archivované** — zůstávají v repu, ale `deploy.yml` je na web **nepublikuje** (vrací 404): `landing.html`, `karaoke.html`, `index_june.html`, `tests.html`.

## 🏗️ Architektura

```text
master
├── index.html              veřejná poděkovací stránka + galerie fotek (read-only)
├── planner.html            interní plánovač pro rodinu (PIN)
├── landing.html            ARCHIV (starý design) — nepublikuje se
├── karaoke.html            ARCHIV — nepublikuje se
├── index_june.html         ARCHIV — nepublikuje se
├── tests.html              ARCHIV — nepublikuje se
├── data/
│   ├── tasks.csv           autoritativní úkoly (vše 33/33 hotovo)
│   ├── budget.csv          autoritativní rozpočet
│   ├── guests.csv          hosté
│   ├── changelog.csv       historie rozhodnutí
│   └── sync.json           generovaný snapshot (čte index.js loader)
├── media/
│   └── fotky/              galerie svatebních fotek
├── public/                 favicon, manifest, 404
├── docs/                   technická dokumentace
├── .claude/                agentí skilly / settings (Claude Code)
├── .continue/              guardrail checky (Continue)
└── .github/workflows/      GitHub Pages deploy + sync validace
```

### Data flow

1. `data/*.csv` je **source of truth** (úkoly, rozpočet, hosté, changelog).
2. Web data pouze čte; aplikace CSV nepřepisuje.
3. `data/sync.json` je **odvozený snapshot** generovaný workflow `update-sync.yml` (node `.claude/update-sync.js`), který si prohlíží `js/sync-loader.js`.
4. Změna dat = editace CSV → commit → push na `master`.
5. GitHub Actions ověří sync (`sync-validation.yml`) a nasadí Pages (`deploy.yml`).

## 📊 Stav (auto-sync z data/*.csv)

<!-- TASK_STATS_START -->
✅ **33/33 splněno** · 💰 **89 500 / 100 000 Kč naplánováno** (82 650 Kč utraceno) · 🧑 **17 hostů** (11 potvrzeno) · 📅 změny do 2026-09-07
<!-- TASK_STATS_END -->

<!-- TASK_CATEGORIES_START -->
| Kategorie | Úkolů | Plán | Skutečnost |
|---|---|---|---|
| 🔴 Povinné | 17 | 84 500 Kč | 78 100 Kč |
| 🟡 Důležité | 12 | 4 500 Kč | 4 150 Kč |
| 🟢 Volitelné | 4 | 500 Kč | 400 Kč |
| **Celkem** | **33** | **89 500 Kč** | **82 650 Kč** |
<!-- TASK_CATEGORIES_END -->

<!-- GUESTS_START -->
- hosté celkem: **17**
- potvrzeno: **11**
<!-- GUESTS_END -->

<!-- COMPLETED_TASKS_START -->
**Hotovo (33):** Termín konfirmace — potvrzení data na matrice · Návštěva radnice — podání žádosti · Informování dětí — oznámení všem 4 dcerám · Svědci domluveni — Kikinka + Žanetka · Domluva oddávajícího — 11:15 Nová radnice · Schůzka prstýnky — Mamka+Taťka+Žanetka · Zlatá koliba — finální počet osob pro catering · Oblek a sako — výběr a nákup · Prstýnky — nákup a úprava · Rozlučka se svobodou — organizace · Svatební oznámení — rozeslání hostům + RSVP · Finální seznam hostů — potvrzení pro catering · Svatební šaty — výběr; nákup; úpravy · Svatební cesta a dovolená — termín; ubytování; program · Doplňky — boty; šperky · Dárky pro svědky · Dekorace a květiny na radnici · První tanec — nácvik · Svatební dort — objednat a vyzvednout · Oddací list; podpisy; doklady · Doprava radnice → Zlatá koliba · Dekorace Zlaté koliby — výzdoba sálu · Fotokoutek / selfie zóna — příprava · Dárky na přivítanou pro hosty · Hry pro hosty a zábava · Hudba a playlist · Drobnosti pro hosty — guestbook + favory · Proslovy svědků — příprava · Líčení; nehty; vlasy · Střih a úprava · Confetti a prskavky · Fotograf — mobil; kamera; koordinace · Změna příjmení — matrika po svatbě
<!-- COMPLETED_TASKS_END -->

<!-- OPEN_TASKS_START -->
**Otevřeno (0):** 
<!-- OPEN_TASKS_END -->

## 🔧 Lokální vývoj a ověření

Bez npm, bez build systému a bez backendu:

```bash
python -m http.server 8080
```

Potom otevři `http://localhost:8080/` (veřejná stránka) nebo `/planner.html` (plánovač pro rodinu). Archivní stránky (`landing.html`, `karaoke.html`, `index_june.html`, `tests.html`) se lokálně otevřou, ale produkčně se nepublikují.

Pro ověření dat a dokumentace použij:

```bash
python -m pytest scripts/tests/test_extract_stats.py -q
python scripts/update-readme.py --check-only
python scripts/update-prd.py --check-only
```

## 📋 Editace dat

| Soubor | Účel |
|---|---|
| `data/tasks.csv` | stav a poznámky k úkolům |
| `data/budget.csv` | plánované a skutečné částky |
| `data/guests.csv` | hosté a potvrzení |
| `data/changelog.csv` | důležitá rozhodnutí |

**Pravidlo:** nejdříve změnit CSV, potom commit/push. README ani HTML nejsou zdrojem pravdy pro aktuální čísla.

## 💰 Rozpočet

Hard cap je **100 000 Kč**. Aktuální data v `budget.csv` dávají:

<!-- BUDGET_START -->
- plán: **89 500 Kč**
- skutečnost: **82 650 Kč**
- rezerva proti limitu podle plánu: **10 500 Kč**
<!-- BUDGET_END -->

Rozpočet se vždy počítá z CSV, nikoli z ručně napsaných čísel v README.

## 💒 Termín a místa

- **Obřad:** sobota 29. 8. 2026 v 11:15, Nová radnice Ostrava (proběhlo)
- **Hostina:** Koliba U Zlatého Jarouše (U Miloše), Karasova 1130/23, 709 00 Ostrava

## 🖼️ Veřejná stránka (index.html)

Po svatbě je `index.html` poděkováním pro hosty a památkou:
- Hero se jmény **Dagmar + Martin Paprčkovi** a watermarkem **„JUST MARRIED"**.
- **Počítadlo „společného času"** (od 29. 8. 2026 v 11:15) s vtipnou tovární cedulí „Dnů bez incidentu" a tlačítkem **MASTER STOP** (incident se zaznamená do dočasného čítače, hlavní počítadlo se neresetuje).
- **Galerie „Fotky z našeho dne"** — 5 fotek z `media/fotky/`, hlavní foto-4 nahoře; kliknutím se fotka otevře ve **skutečném fullscreen**.
- Patička s datem/časem svatby a místem.

Data pro galerii/fotky se nenačítají z CSV — je to statický obsah. Hosté a harmonogram už na veřejné stránce nejsou (zůstaly v `planner.html`).

## 🚀 GitHub Pages

Deploy je definován v `.github/workflows/deploy.yml`; publikuje pouze **`index.html`** a **`planner.html`** (plus `data/`, `media/`, `public/`). Archivní HTML se na web nekopírují.

Workflow:

```text
push master
   ↓
checkout
   ↓
prepare deploy_out  (index.html + planner.html + data/ + media/ + public/)
   ↓
upload Pages artifact
   ↓
deploy-pages
   ↓
GitHub Pages
```

Workflow je spustitelný také ručně přes **Actions → Deploy to GitHub Pages → Run workflow**.

Deploy obsahuje pouze runtime web, data, média a public assets; vývojové adresáře jako `docs/`, `.github/`, `.claude/` a `.continue/` se do Pages neposílají.

> **Poznámka k Pages:** repo je veřejné a Pages povolené s buildem z GitHub Actions. Na free účtu Pages fungují jen na veřejných repozitářích — pokud repo znovu zprivatizuješ, Pages přestanou fungovat.

## 🩺 Repo repair checklist

- [x] GitHub Pages workflow používá moderní Pages artifact/deploy actions.
- [x] Deploy má explicitní `contents: read`, `pages: write`, `id-token: write` permissions.
- [x] Workflow lze spustit push-em i ručně (`workflow_dispatch`).
- [x] Publikují se jen **`index.html`** a **`planner.html`**; archivní HTML (`landing.html`, `karaoke.html`, `index_june.html`, `tests.html`) se na web neposílají.
- [x] `public/`, `data/` a `media/` (vč. `media/fotky/`) se kopírují do výsledného webu.
- [x] Repo dokumentace se do veřejného Pages artifactu nekopíruje.
- [x] README odkazy jsou relativní, takže repo lze přesunout bez přepisování interních cest.
- [x] Čísla rozpočtu byla přepočtena z aktuálního `budget.csv`.

## 🔒 Pravidla projektu

1. `data/*.csv` = source of truth.
2. Appka je read-only.
3. Budget hard cap = 100 000 Kč (svatba proběhla — rozpočet uzavřen).
4. Aktuální stav v dokumentaci nepřepisovat ručně bez kontroly CSV.
5. Každou důležitou změnu dat commitnout s popisnou zprávou.
6. Archivní stránky (`landing`, `karaoke`, `index_june`, `tests`) NEpublikovat na web — v `deploy.yml` je záměrně nekopírujeme.

## 📝 Changelog dokumentace

- 2026-09-07: dokumentace převedena do stavu **po svatbě** — repo veřejné, Pages povolené, veřejná stránka je poděkování + galerie fotek, archivní stránky se nepublikují.
- 2026-08-18: doplněn přehled o aktuálním stacku (HTML/CSS/JS + Python helper skripty), aktualizovány pokyny pro lokální běh a testování a vysvětleny validace README/PRD.
- 2026-08-18: přidány stručné JSDoc a Python docstrings pro veřejné funkce bez změny logiky.

## 📜 Historie

| Verze | Datum | Popis |
|---|---|---|
| **1.0.0** | 2026-05-16 | Počáteční single-file verze |
| **1.1.0** | 2026-05-21 | Git-backed data, dual deploy |
| **2.0.0** | 2026-06-02 | CSV migrace, romantický design, planner |
| **2.1.x** | 2026-07 | Reálný progres a úpravy svatebního plánu |
| **2.2.0** | 2026-08-08 | Repo/Pages repair, kompletní Pages deploy a README cleanup |
| **2.2.1** | 2026-08-18 | Aktualizace dokumentace, JSDoc a Python docstrings |
| **3.0.0** | 2026-09-07 | Svatba proběhla: úkoly 33/33 done, poděkovací landing + galerie fotek, repo veřejné, archivace stránek |
