# Older_up2date — Archivní verze s opravami

Původní HTML soubory z `../Older/` upravené:
- Opraveny názvy: tatka→Taťka, Dcery→Děti, mamka→Mamka
- Přidán archivní banner s odkazem na originál
- Opraveno datum svatby (Červen→Srpen, 29.8.2026)
- Title prefix `📦 ARCHIV`

## Co bylo opraveno

| Soubor | Původní název | Opravy |
|--------|--------------|--------|
| Svatba_001.html | "Svatební plánovač \| Červen 2026" | → 29.8.2026, Taťka/Mamka/Děti |
| deepseek_*.html | "Svatba mamky a tatky" | → Mamky a Taťky, Dcery→Děti |
| PuvodnuApp.html | "Svatba mamky a tatky" | → Mamky a Taťky, Dcery→Děti |
| SVatbaV42.html | OK | Jen banner |
| LastSvatba.html | OK | Jen banner |
| svatba_planner_v2_ultimate.html | OK | Jen banner |

## Co NEBYLO změněno

- **Struktura úkolů** — počet, názvy, kategorie zůstávají původní
- **Design a CSS** — zachován původní vzhled každé verze
- **Bugy a chyby** — neopravováno (chybí budget v 001, 146k v LastSvatba jsou záměrně zachovány jako ukázka evoluce)

## Doporučení pro další vývoj

### 1. Svatba_001.html jako zaklad pro v0 (archivni baseline)
22KB, 20 úkolů, čistý design. Když se k tomu přidá:
- Budget bar (z LastSvatba)
- Filtr podle osoby (z PuvodnuApp)
- GitHub sync (z SVatbaV42, ale zjednodušený)

Vznikne ideální kombinace — jednoduchost 001 + funkčnost v2.

### 2. Hard cap na budget je kritický
Verze 17.5. (146k) a 19.5. (116k) ukazují, že bez Excelu a pravidla "100k max"
se budget nekontrolovaně nafukuje. Excel s podmíněným formátováním (aktuální
`rozpocet-svatba-2026.xlsx`) tento problém řeší.

### 3. Neztratit lidi
Ve verzi 17.5. (LastSvatba) Děti úplně zmizely z přiřazení úkolů — jen 4 osoby.
Verze 19.5. má jen 3 osoby. Aktuální stav (5 osob) je správný.
Pravidlo "nikdy neodebírat Děti" v CLAUDE.md je nutné.

### 4. Velikost souboru = indikátor složitosti
```
001:         22 KB — ideální
DeepSeek:    25 KB — OK
PuvodnuApp:  30 KB — OK
LastSvatba:  43 KB — začíná být těžké
v2_ultimate: 53 KB — moc
SVatbaV42:   55 KB — nejtěžší
```

Optimální velikost pro single-file appku je 20-30 KB.
Nad 40 KB už to chce rozdělit (data zvlášť, appka zvlášť) — což je aktuální architektura.

### 5. Co si vzít z každé verze

| Verze | Co je dobré | Co je špatně |
|-------|------------|--------------|
| 001 | Jednoduchost, rychlost, čistý design | Chybí budget, nekonzistentní jména |
| DeepSeek | iOS styling, barevné karty | Stejné jako 001, nic navíc |
| PuvodnuApp | Budget tracking, stats, filtr osob | Větší, složitější |
| SVatbaV42 | GitHub API, PIN, hodně features | 55KB, moc složité na údržbu |
| LastSvatba | 38 úkolů (kompletní) | 146k budget (moc), chybí Děti |
| v2_ultimate | Clean design, PIN, stats | 116k budget (moc), jen 3 osoby |

### 6. Deployment

Všechny verze jsou dostupné na:
- `../Older_up2date/` — opravene verze (tento adresar)
- `../Older/` — puvodni neupravene originaly
- `../v0/` — archivni baseline (Svatba_001, 20 ukolu, 29.8.)
- `../` — aktualni produkcni verze (v1)
- `../v2/` — aktualni v2 (git-backed)

Pro porovnání s Mamkou a Žanetkou otevřít `index.html` v tomto adresáři —
je tam přehledná stránka se všemi verzemi a doporučeními.