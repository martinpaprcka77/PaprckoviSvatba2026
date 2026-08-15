# 💒 Svatba Paprčkovi 2026

Svatební plánovač pro **29. srpna 2026, 11:15**, Nová radnice Ostrava → Koliba U Zlatého Jarouše.

> **Production:** https://martinpaprcka77.github.io/PaprckoviSvatba2026/

## ⚡ Stránky

| Stránka | Odkaz |
|---|---|
| **Veřejná** | `/` |
| **Landing / nový design** | `/landing.html` |
| **Plánovač** | `/planner.html` |
| **Karaoke** | `/karaoke.html` |
| **Archiv červen 2026** | `/index_june.html` |

## 🏗️ Architektura

```text
master
├── index.html              veřejná stránka
├── landing.html            landing page
├── planner.html            interní plánovač
├── karaoke.html            karaoke
├── index_june.html         archiv
├── data/
│   ├── tasks.csv           autoritativní úkoly
│   ├── budget.csv          autoritativní rozpočet
│   ├── guests.csv          hosté
│   └── changelog.csv       historie rozhodnutí
├── media/                  média
├── public/                 favicon, manifest, 404
├── docs/                   technická dokumentace
└── .github/workflows/      GitHub Pages deploy
```

### Data flow

1. `data/*.csv` je **source of truth**.
2. Web data pouze čte; aplikace CSV nepřepisuje.
3. Změna dat = editace CSV → commit → push na `master`.
4. GitHub Actions sestaví Pages artifact a nasadí jej na GitHub Pages.
5. Runtime data se načítají z repozitáře při otevření aplikace.

## 📊 Stav (auto-sync z data/*.csv)

<!-- TASK_STATS_START -->
✅ **11/33 splněno** · 💰 **89 500 / 100 000 Kč naplánováno** (82 650 Kč utraceno) · 🧑 **21 hostů** (15 potvrzeno) · 📅 změny do 2026-08-16
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
- hosté celkem: **21**
- potvrzeno: **15**
<!-- GUESTS_END -->

<!-- COMPLETED_TASKS_START -->
**Hotovo (11):** Termín konfirmace — potvrzení data na matrice · Návštěva radnice — podání žádosti · Informování dětí — oznámení všem 4 dcerám · Svědci domluveni — Kikinka + Žanetka · Domluva oddávajícího — 11:15 Nová radnice · Schůzka prstýnky — Mamka+Taťka+Žanetka · Zlatá koliba — finální počet osob pro catering · Oblek a sako — výběr a nákup · Prstýnky — nákup a úprava · Svatební oznámení — rozeslání hostům + RSVP · Svatební šaty — výběr; nákup; úpravy
<!-- COMPLETED_TASKS_END -->

<!-- OPEN_TASKS_START -->
**Otevřeno (22):** Rozlučka se svobodou — organizace · Finální seznam hostů — potvrzení pro catering · Svatební cesta a dovolená — termín; ubytování; program · Doplňky — boty; šperky · Dárky pro svědky · Dekorace a květiny na radnici · První tanec — nácvik · Svatební dort — objednat a vyzvednout · Oddací list; podpisy; doklady · Doprava radnice → Zlatá koliba · Dekorace Zlaté koliby — výzdoba sálu · Fotokoutek / selfie zóna — příprava · Dárky na přivítanou pro hosty · Hry pro hosty and zábava · Hudba a playlist · Drobnosti pro hosty — guestbook + favory · Proslovy svědků — příprava · Líčení; nehty; vlasy · Střih a úprava · Confetti a prskavky · Fotograf — mobil; kamera; koordinace · Změna příjmení — matrika po svatbě
<!-- OPEN_TASKS_END -->

## 🔧 Lokální vývoj

Bez npm a bez backendu:

```bash
python -m http.server 8080
```

Potom otevři `http://localhost:8080/`.

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

- **Obřad:** 29. 8. 2026 v 11:15, Nová radnice Ostrava
- **Hostina:** Koliba U Zlatého Jarouše (U Miloše), Karasova 1130/23, 709 00 Ostrava

## 🚀 GitHub Pages

Deploy je definován v `.github/workflows/deploy.yml`.

Workflow:

```text
push master
   ↓
checkout
   ↓
prepare deploy_out
   ↓
upload Pages artifact
   ↓
deploy-pages
   ↓
GitHub Pages
```

Workflow je spustitelný také ručně přes **Actions → Deploy to GitHub Pages → Run workflow**.

Deploy obsahuje pouze runtime web, data, média a public assets; vývojové adresáře jako `docs/`, `.github/`, `.claude/` a `.continue/` se do Pages neposílají.

## 🩺 Repo repair checklist

- [x] GitHub Pages workflow používá moderní Pages artifact/deploy actions.
- [x] Deploy má explicitní `contents: read`, `pages: write`, `id-token: write` permissions.
- [x] Workflow lze spustit push-em i ručně (`workflow_dispatch`).
- [x] `landing.html`, `planner.html` a `karaoke.html` jsou součástí deploye.
- [x] `public/`, `data/` a `media/` se kopírují do výsledného webu.
- [x] Repo dokumentace se do veřejného Pages artifactu nekopíruje.
- [x] README odkazy jsou relativní, takže repo lze přesunout bez přepisování interních cest.
- [x] Čísla rozpočtu byla přepočtena z aktuálního `budget.csv`.

## 🔒 Pravidla projektu

1. `data/*.csv` = source of truth.
2. Appka je read-only.
3. Budget hard cap = 100 000 Kč.
4. Aktuální stav v dokumentaci nepřepisovat ručně bez kontroly CSV.
5. Každou důležitou změnu dat commitnout s popisnou zprávou.

## 📜 Historie

| Verze | Datum | Popis |
|---|---|---|
| **1.0.0** | 2026-05-16 | Počáteční single-file verze |
| **1.1.0** | 2026-05-21 | Git-backed data, dual deploy |
| **2.0.0** | 2026-06-02 | CSV migrace, romantický design, planner |
| **2.1.x** | 2026-07 | Reálný progres a úpravy svatebního plánu |
| **2.2.0** | 2026-08-08 | Repo/Pages repair, kompletní Pages deploy a README cleanup |
