# Technical Walkthrough — Svatba Paprčkovi 2026

> **Aktuální stav (květen 2026):** 37 úkolů, 19 mandatory + 14 important + 4 optional, 5 osob, budget 100 000 Kč, 6/37 hotovo.
> Živě: [https://doma77git.github.io/PaprckoviSvatba2026/](https://doma77git.github.io/PaprckoviSvatba2026/)

Tento dokument popisuje architekturu, deployment a data flow svatebního plánovače **Svatba Paprčkovi 2026**.

---

## 1. Architektura — Data-Driven, Git-Backed

Aplikace je plně statická — žádný backend, žádný build, žádné npm. Data žijí v Markdown souborech v repu, appky je fetchnou z GitHub Raw a vyrenderují.

### Tři verze

| Verze | URL | Účel | Data |
|-------|-----|------|------|
| **v0** | `/v0/` | Archivní baseline | Inline (20 úkolů, 81 500 Kč) |
| **v1** | `/` (přepínatelné DEPLOY_DEFAULT) | Produkce | Fetchuje `data/tasks.md` z GitHub Raw, localStorage pro check-state + budget |
| **v2** | `/v2/` | Testovací | Fetchuje `data/tasks.md` + `data/guests.md` z GitHub Raw, write-back přes API |
| **v3music** | `/v3music/` | v1 + audio | Kopie v1 + 2 skladby (DJ Ötzi, Hasselhoff), 3 ovladače, refrén skip |

### Data Flow

```
Editace tasks.md / guests.md → commit + push → GitHub Actions → gh-pages → live
                                              ↕
                              PostToolUse hook → přegeneruje Excel
```

1. **Editace:** Markdown soubory v `data/` (`tasks.md`, `guests.md`, `budget.md`)
2. **Commit + push** do `master`
3. **GitHub Actions** (`deploy.yml`) nasadí na `gh-pages`
4. **Appky** při načtení fetchnou z GitHub Raw (CDN)
5. **PostToolUse hook** automaticky přegeneruje Excel při změně `tasks.md`

---

## 2. Verze v Detailu

### v0 — Archivní Baseline

- Umístění: [`v0/index.html`](v0/index.html)
- Vytvořeno 2026-05-24 z `Older/Svatba_001.html`
- 20 úkolů, 81 500 Kč budget
- Všechna data posunuta z 15. 6. → 29. 8. 2026 (+75 dní)
- Slouží jako čistý referenční bod před PRD expanzí na 36/37 úkolů

### v1 — Produkce (Single-File)

- Umístění: [`index.html`](index.html)
- **Fetch-based:** načítá `data/tasks.md` z GitHub Raw při startu
- **localStorage:** pouze check-state (`svatba_done_v4`) + editable budget (`svatba_budget_v4`)
- **iOS-first design:** Google Fonts (Outfit + Playfair Display), SVG progress gauge, swipeable mandatory feed, glassmorphic tab bar, dark mode, PWA manifest
- **Budget guardrails:** 100 000 Kč hard cap, real-time validation, cost-reduction suggestions při překročení
- **State úložiště:** v4 klíče (migrováno z v3)

### v2 — Testovací (Git-Backed)

- Umístění: [`v2/index.html`](v2/index.html)
- **Fetchuje** `data/tasks.md` + `data/guests.md` z GitHub Raw
- **Write-back** přes GitHub API s rodinným PINem:
  - PAT šifrovaný AES-GCM v localStorage
  - PIN hash SHA-256 (dobrovolný, neotravuje)
  - Timestamp validace: `[x]` + timestamp = validní dokončení
- **Completed tasks** auto-removed z DOM (lze zobrazit)
- **Seznam hostů** mezi rozpočtem a harmonogramem
- **Nová sekce:** guests section fetching `data/guests.md`

---

## 3. Data Files

| Soubor | Účel | Editace |
|--------|------|---------|
| [`data/tasks.md`](data/tasks.md) | Autoritativní tabulka 37 úkolů | PC → git |
| [`data/guests.md`](data/guests.md) | Seznam hostů podle stran | PC → git |
| [`data/budget.md`](data/budget.md) | 1 source of truth pro rozpočet (s Rezervováno/Zaplaceno/Zbývá) | PC → git |
| [`data/rozpocet-svatba-2026.xlsx`](data/rozpocet-svatba-2026.xlsx) | Auto-generovaný Excel (SUMIF/COUNTIF, podmíněné formátování) | Automaticky |
| [`data/manualrozpocet-svatba-2026.xlsx`](data/manualrozpocet-svatba-2026.xlsx) | Manuální budget Excel | Uživatel přímo |
| [`docs/PRD-svatba-paprckovi-2026.md`](docs/PRD-svatba-paprckovi-2026.md) | Product Requirements Document (autoritativní spec) | PC → git |

### Struktura tasks.md

```
| Termín | Úkol | Kdo | Kat. | Plán (Kč) | Skutečnost (Kč) | Stav | Timestamp | Poznámka |
```

- `Kdo`: čárkou odděleno (`Mamka, Děti`)
- `Kat.`: `mandatory` / `important` / `optional`
- `Stav`: `[x]` (s timestampem) nebo `[ ]`
- `_` = nevyplněno

---

## 4. Aktuální Stav

### Úkoly (37)

| Kategorie | Počet | Rozpočet | Hotovo |
|-----------|-------|----------|--------|
| 🔴 Povinné (mandatory) | 19 | 94 500 Kč | 5 |
| 🟡 Důležité (important) | 14 | 5 000 Kč | 1 |
| 🟢 Volitelné (optional) | 4 | 500 Kč | 0 |
| **Celkem** | **37** | **100 000 Kč** | **6/37** |

### Lidé (5)

| Kdo | Role | Úkolů |
|-----|------|-------|
| **Mamka** | Nevěsta (Dagmar Sobková) | 18 |
| **Taťka** | Ženich | 8 |
| **Žanetka** | Hlavní organizátorka, svědkyně ženicha | 7 |
| **Kikinka** | Svědkyně nevěsty | 3 |
| **Děti** | 4 dcery: Gabriela, Kristýnka, Natálka, Kačka | 5 |

### Hotovo

- ✅ Termín konfirmace (2026-05-20)
- ✅ Návštěva radnice (2026-05-20)
- ✅ Informování dětí (2026-05-20)
- ✅ Svědci domluveni (2026-05-20)
- ✅ Oddávající domluven (2026-05-15)
- ✅ Schůzka prstýnky (2026-05-25)

---

## 5. Deployment

- **GitHub repo:** `doma77git/PaprckoviSvatba2026`
- **Branch:** `master` → GitHub Actions → `gh-pages`
- **Workflow:** [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) — kurátovaný upload (pouze relevantní soubory)
- **Live:**
  - [v1 produkce](https://doma77git.github.io/PaprckoviSvatba2026/)
  - [v2 testovací](https://doma77git.github.io/PaprckoviSvatba2026/v2/)
  - [v3music](https://doma77git.github.io/PaprckoviSvatba2026/v3music/)
  - [v0 archiv](https://doma77git.github.io/PaprckoviSvatba2026/v0/)
  - [Archivní verze](https://doma77git.github.io/PaprckoviSvatba2026/Older_up2date/)

### Git History

- Historie squashnuta 2026-05-24: master 117→1 commit, gh-pages 82→1 commit
- Tag `live` na milestone verzi

---

## 6. Automatizace (Hooks)

| Hook | Co dělá |
|------|---------|
| **PreToolUse** (Edit\|Write) | Blokuje editace `.env`, `package-lock.json`, `.git/` |
| **PostToolUse** (Edit\|Write) | Přegeneruje `rozpocet-svatba-2026.xlsx` při změně `tasks.md` |
| **Notification** (idle_prompt) | Desktop popup když Reasonix/Claude čeká na input |
| **GitHub Actions** | Auto-deploy na push do masteru |

### Ověření integrity

```bash
python scripts/_verify_tasks.py
# nebo
python -c "
import re
with open('data/tasks.md', encoding='utf-8') as f:
    md = f.read()
lines = [l for l in md.split('\n') if l.startswith('| 2026')]
m = i = o = 0
for l in lines:
    parts = [p.strip() for p in l.split('|')]
    cat = parts[4]; price = int(parts[5]) if parts[5].isdigit() else 0
    if cat == 'mandatory': m += price
    elif cat == 'important': i += price
    elif cat == 'optional': o += price
total = m + i + o
print(f'Tasks: {len(lines)} (target: 37) | Budget: {total:,} Kc (target: 100000)')
print(f'Mand: {m:,} | Imp: {i:,} | Opt: {o:,}')
print('OK' if total == 100000 and len(lines) == 37 else 'GAP')
"
```

---

## 7. iOS UI Features (v1 + v2)

Obě verze sdílejí premium iOS-first design:

- **Typography:** Outfit (UI) + Playfair Display (headings)
- **Dark mode:** Automatický dle systémového nastavení
- **SVG progress gauge:** Animovaný kruhový indikátor
- **Swipeable mandatory feed:** Horizontální carousel pro urgentní úkoly
- **Glassmorphic bottom nav:** `backdrop-filter: blur(20px)`, safe-area padding
- **PWA ready:** Manifest, apple-touch-icon, standalone display
- **Budget guardrails:** Live validace, hard cap červeně, cost-reduction návrhy
- **Touch targets:** 44px minimum, scale(0.97) haptic feedback

---

## 8. Klíčová Pravidla

1. **Budget 100 000 Kč hard cap** — změna ceny → vyrovnat jinde
2. **Nikdy neodebírat Děti** z úkolů — co-assign (`Děti, Mamka`), nikdy nenahrazovat
3. **Jména v datech bez háčků, bez příjmení** — Mikesovi (ne Mikešovi); Děti je výjimka (správná čeština)
4. **Append-only poznámky** v tasks.md; oddělovač `; `
5. **Po editaci tasks.md:** aktualizovat header počty, people tabulku, budget tabulku
6. **PRD je autoritativní spec** — `docs/PRD-svatba-paprckovi-2026.md`

---

## 9. Verze — Historie

| Verze | Datum | Úkolů | Budget | Architektura |
|-------|-------|-------|--------|-------------|
| 1.0.0 | 2026-05-16 | 35 | 100 000 Kč | v1 single-file, localStorage, iOS-first UI |
| 1.1.0 | 2026-05-21 | 36 | 100 000 Kč | v2 git-backed, PIN sync, dual deploy, Excel hooks |
| 1.2.0 | 2026-05-24 | 36 | 100 000 Kč | v0 baseline, git squash, Dáda→Mamka merge, deploy fix |
| 1.3.0 | 2026-05-26 | 37 | 100 000 Kč | Rozlučka přidána, guests groundwork |
| 1.3.1 | 2026-05-27 | 37 | 100 000 Kč | Guests live, budget.md 1SoT, Koliba split |

Podrobný changelog: [`CHANGELOG.md`](CHANGELOG.md)
Historický deník: [`HISTORY.md`](HISTORY.md)
