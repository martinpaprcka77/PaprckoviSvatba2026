# 🍀 SESSION MEMORY — Svatba Paprčkovi 2026

## Session Context
- **Datum:** Květen 2026
- **Cíl:** Vytvoření interaktivního HTML plánovače svatby
- **Výstup:** `PaprckoviSvatba2026app.html` + GitHub Pages deploy

## Co bylo vytvořeno

### Hlavní soubory
| Soubor | Popis |
|--------|-------|
| `C:\dev\PS7\PaprckoviSvatba2026app.html` | HLAVNÍ — finální verze, editable budget, MUST-DO widget |
| `C:\dev\PS7\index.html` | Kopie pro GitHub Pages |
| `C:\dev\PS7\svatba_app.html` | Starší verze s extra featury (countdown, person filtry, timeline) |
| `C:\dev\PS7\Scripts\Publish-Svatba.ps1` | Bootstrap — 1 příkazem publikuje gist |

## Parametry svatby
- **Název:** Svatba Paprčkovi 2026
- **Termín:** 15. června 2026 · 14:00–20:00
- **Místo:** Terasa + odpolední oslava
- **Kdo:** Mamka (nevěsta) + Taťka (ženich) — 29 let spolu
- **Rodina:** 4 dcery (15, 20+, 20+, 20+)
- **Fotograf:** Tátův kamarád (host + fotí)
- **DJ:** Z vlastních řad

## Struktura úkolů (20)
- **Povinné (8):** pronájem 15k, matrika 1.8k, svědci 0, prstýnky 20k, oblek 7k, catering 35k, šaty 14k, hosté 0
- **Důležité (7):** schůzka 0, pozvánky 1.8k, fotograf 2k, DJ 2.5k, technika 0, nápoje 0, dekorace 7k
- **Volitelné (5):** dort 3k, kytice 0, líčení 0, dárky 0, focení 0

## Rozpočet finální
- **Základ:** 107 300 Kč
- **Max (+20 %):** 128 760 Kč
- Viz tabulka v README.md nebo v app

## GitHub
- **Repo:** `github.com/doma77git/PaprckoviSvatba2026`
- **Live Pages:** `doma77git.github.io/PaprckoviSvatba2026/`
- **Branch master:** README + všechny zdrojáky
- **Branch gh-pages:** deploynutá appka
- **Git user:** doma77git (token v keyring)
- **gh CLI:** 2.92.0, autentikován

## Důležité příkazy
```powershell
# Publikovat jako gist
.\Scripts\Publish-Svatba.ps1

# Push změny
git add . && git commit -m "zprava" && git push origin master
git push origin gh-pages

# Zkontrolovat Pages
gh api repos/doma77git/PaprckoviSvatba2026/pages
```

## Co se řešilo
1. Vytvoření HTML checklistu s checkboxy a localStorage
2. Postupné přidávání budgetu, kategorií, person filtrů
3. Expertíza reálných českých cen (prstýnky 20k, catering 35k atd.)
4. Dvě verze: `svatba_app.html` (bohatší featury) a `PaprckoviSvatba2026app.html` (editable budget)
5. GitHub Pages deploy — gh-pages branch
6. Gist bootstrap script — Publish-Svatba.ps1
7. Problém: git commit s diakritikou v message (řešeno jednoduchými messages bez mezer)
8. Problém: Pages API vyžadovala existující gh-pages branch
