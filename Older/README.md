# Older Versions — Archive

Svatební appky od úplného počátku (7. 5. 2026) do 19. 5. 2026.
Uchováno pro historii a porovnání. NEMAZAT.

## Časová osa

```
7.5.    Svatba_001.html          ← první verze, 20 úkolů, jednoduchá ✨ NEJLEPŠÍ
7.5.    deepseek_html_...html    ← DeepSeek varianta, 20 úkolů
8.5.    PuvodnuApp.html          ← první "plná" verze s budgetem
14.5.   SVatbaV42.html           ← masivní expanze, GitHub API, PIN
17.5.   LastSvatba.html          ← 38 úkolů, 146k budget (přestřeleno)
19.5.   svatba_planner_v2_...    ← 20 úkolů, 116k budget, PIN
21.5.   (current)                ← 36 úkolů, 100k hard cap, Excel, v1+v2
```

## Detailní srovnání

### Svatba_001.html ✨ — 21.8 KB, 7. 5. 2026
**První a nejjednodušší.** 20 úkolů, žádný budget tracking, žádné ceny.
- 8 mandatory, 7 important, 5 optional
- Collapsible sekce, filtr podle osoby, progress bar
- Lidé: "Nevěsta", "Táta (fotograf)", "4 dcery", "Pronajímatel", "Známý / rodina" — neformální, lidské
- **Proč je super:** Jednoduchost. Žádný budget, žádné Excel tabulky, prostě checklist. Rychle načte, rychle pochopí.

### deepseek_html_20260507_52376d.html — 24.5 KB, 7. 5. 2026
Sesterská verze k 001, generovaná DeepSeekem. Stejná struktura, 20 úkolů, mírně jiné názvy.
- Clean iOS design, zaoblené karty, progress bar
- Neformální jazyk: "Mamka + tatka", "dcery"

### PuvodnuApp.html — 30.1 KB, 8. 5. 2026
První verze s budgetem a statistikami. Přechod od checklistu k plnohodnotnému plánovači.
- localStorage, budget view, timeline, stats, filters, guests
- Nelze přesně naparsovat (nestandardní JS struktura)

### SVatbaV42.html — 54.5 KB, 14. 5. 2026
Masivní skok ve složitosti. GitHub API integrace, PIN lock.
- localStorage, GitHub API, PIN, budget, timeline, stats, filters, guests
- 55KB — největší ze všech verzí

### LastSvatba.html — 43.0 KB, 17. 5. 2026
38 úkolů, budget **146 000 Kč** — vysoko nad limitem.
- 18 mandatory, 13 important, 7 optional
- Jen 4 osoby: Mamka, Taťka, Kikinka, Žanetka (Děti chybí!)
- Toto je verze kde "Děti ztratily úkoly" — opraveno v PRD 21.5.

### svatba_planner_v2_ultimate.html — 52.5 KB, 19. 5. 2026
20 úkolů, 116 100 Kč budget. Návrat k menšímu počtu úkolů.
- Jen 3 osoby: Děti, Mamka, Taťka
- PIN lock, stats, budget view
- "v2 ultimate" — pokus o finální verzi

## Co se vzalo z které verze

| Feature | Původ |
|---------|-------|
| Checklist s progress barem | 001 |
| Collapsible sekce | 001 |
| Budget tracking | PuvodnuApp |
| Timeline / harmonogram | PuvodnuApp |
| Filtr podle osoby | 001 |
| GitHub API sync | SVatbaV42 |
| PIN lock | SVatbaV42 |
| 100k hard cap | PRD (14.5.) |
| Excel budget | 21.5. |
| Hooks (auto-commit, regen) | 21.5. |
| v1+v2 dual deploy | 21.5. |
| Děti zpátky v úkolech | 21.5. (oprava z LastSvatba) |

## Poučení

1. **001 je nejoblíbenější** — jednoduchost vítězí. 20 úkolů, žádný budget, čistý checklist.
2. **LastSvatba (146k) ukazuje riziko** — bez hard capu budget nekontrolovaně roste.
3. **55KB verze jsou moc těžké** — 001 má 22KB a funguje líp.
4. **Děti se ztratily ve verzi 17.5.** — nutnost pravidla "nikdy neodebírat Děti".
5. **Evoluce od checklistu k systému** — 001 byl checklist, 21.5. je plnohodnotný systém s Excelem, hooks, git-backed architekturou.