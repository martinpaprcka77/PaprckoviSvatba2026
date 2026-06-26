# CLAUDE.md — Svatba Paprčkovi 2026

## Projekt

Wedding planner: 34 tasks, 5 people, 89.5K Kč budget (MAX 100K), Aug 29, 2026.

## Autoritativní zdroje

- **Tasks:** `data/tasks.csv` (34 rows, assignments; částky NE)
- **Budget:** `data/budget.csv` (položky + odhad — autoritativní pro peníze)
- **Spec:** `docs/PRD-svatba-paprckovi-2026.md` (requirements, dates, roles)
- **Guests:** `data/guests.csv` (public seznam hostů)

## Web verze

- **index.html** (production): veřejná stránka — read-only, fetch CSV
- **planner.html**: plánovač pro organizátory (PIN), plná verze vč. rozpočtu
- **index_june.html** (archive): snímek stavu ke červnu 2026
- **karaoke.html**: Sweet Caroline slovo po slovu + audio

## Klíčová pravidla

1. **Budget 100K hard cap** — žádné překročení
2. **Nikdy neodebírat Děti** z úkolů — co-assign, nikdy nenahrazovat
3. **Jména bez háčků** (Mikesovi, ne Mikešovi), bez příjmení; Děti výjimka
4. **Append-only poznámky** v tasks.csv; oddělovač `; `
5. **CSV = source of truth** — apps čtou, nikdy nepíšou
6. **Po editaci tasks.csv:** aktualizovat header čísla, tabulku lidí, rozpočet

## Agenty — co vědět

- `data/tasks.csv` je autoritativní
- Ověř rozpočet ≤ 100K vždy
- Linky lowercase (`docs/`, ne `Docs/`)
- Sync header čísla a tabulky v README po editaci
