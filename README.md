# 💒 Svatba Paprčkovi 2026

Plánovací aplikace — **29. srpna 2026, 11:15**
Git-backed architektura: data v MD souborech, appka je čte a renderuje.

## Odkazy

| Link | URL |
|------|-----|
| **Plánovač v1** | https://doma77git.github.io/PaprckoviSvatba2026/ |
| **Plánovač v2** | https://doma77git.github.io/PaprckoviSvatba2026/v2/ |
| **Data — úkoly** | https://github.com/doma77git/PaprckoviSvatba2026/blob/master/data/tasks.md |
| **Data — hosté** | https://github.com/doma77git/PaprckoviSvatba2026/blob/master/data/guests.md |
| **Data — rozpočet Excel** | https://github.com/doma77git/PaprckoviSvatba2026/blob/master/data/rozpocet-svatba-2026.xlsx |
| **Repozitář** | https://github.com/doma77git/PaprckoviSvatba2026 |
| **Dokumentace** | [PRD](docs/PRD-svatba-paprckovi-2026.md) |
| **Archivní verze (001!)** | https://doma77git.github.io/PaprckoviSvatba2026/Older_up2date/ |
| **WhatsApp** | _[doplň odkaz na skupinu]_ |

## Klíčové informace

- **Datum:** 29. srpna 2026, 11:15
- **Obřad:** Nová radnice Ostrava
- **Hostina:** Koliba U Zlatého Jarouše (U Miloše), Karasova 1130/23, 709 00 Ostrava
- **Rozpočet:** MAX 100 000 Kč (hard cap) · 36 úkolů · 6 osob
- **Nevěsta:** Mamka (Dagmar) | **Ženich:** Taťka
- **Svědci:** Kikinka (za nevěstu), Žanetka (za ženicha)
- **Organizátorka:** Žanetka
- **Děti (4 dcery):** Gabriela, Kristýnka, Natálka, Kačka — výzdoba, dort, focení
- **Dáda:** pomoc s prstýnky
- **Hotovo (5/36):** termín ✓, radnice ✓, děti ✓, svědci ✓, oddávající ✓

## Struktura

```
./
├── index.html              ← plánovač v1 (single-file, localStorage)
├── v2/index.html           ← plánovač v2 (git-backed, fetch MD z GitHubu)
├── data/
│   ├── tasks.md            ← 36 úkolů — autoritativní zdroj
│   ├── guests.md           ← seznam hostů
│   ├── rozpocet-svatba-2026.xlsx        ← auto-generovaný Excel (SUMIF)
│   └── manualrozpocet-svatba-2026.xlsx  ← manuální Excel (user edituje)
├── public/                 ← favicon, manifest, 404
├── .github/workflows/      ← auto-deploy na push do masteru
├── .claude/settings.json   ← hooks (PreToolUse, PostToolUse, Notification)
├── docs/                   ← PRD, design spec
├── README.md
├── CLAUDE.md
├── AGENTS.md
├── HISTORY.md
└── .gitignore
```

## Deployment

Push do `master` → GitHub Actions → `gh-pages`:
- `/` — v1 (produkce)
- `/v2/` — v2 (nová verze)

**Nepotřebuje npm, node, build.** Data v `data/*.md`, appky v `index.html` + `v2/index.html`.

## Progress

✅ 5/36 splněno · 💰 0/100 000 Kč utraceno · 📅 ~100 dní do svatby
🍽️ Koliba U Zlatého Jarouše: potvrzeno 21.5.2026 (Mamka + Žanetka u Miloše)
💍 Schůzka prstýnky: Dáda+Taťka+Žanetka 25.5.2026
📍 [Navigovat](https://maps.google.com/?q=Karasova+1130/23,+709+00+Ostrava)