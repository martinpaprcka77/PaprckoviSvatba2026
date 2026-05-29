# CLAUDE.md — Svatba Paprčkovi 2026

## Projekt

Wedding planner: 36 tasks, 5 people, 89.5K Kč budget (MAX 100K), Aug 29, 2026.

## Autoritativní zdroje

- **Tasks:** `data/tasks.md` (36 rows, assignments, budget per task)
- **Budget:** `data/budget.md` (položky + odhad)
- **Spec:** `docs/prd-svatba-paprckovi-2026.md` (requirements, dates, roles)
- **Guests:** `data/guests.md` (public seznam hostů)

## Web verze

- **v1** (production): `index.html` — offline-first, localStorage
- **v0** (archive): `v0/index.html` — baseline snapshot (20 tasks, 2026-05-24)
- **v3music** (experimental): `v3music/index.html` — v1 + karaoke audio/lyrics

## Klíčová pravidla

1. **Budget 100K hard cap** — žádné překročení
2. **Nikdy neodebírat Děti** z úkolů — co-assign, nikdy nenahrazovat
3. **Jména bez háčků** (Mikesovi, ne Mikešovi), bez příjmení; Děti výjimka
4. **Append-only poznámky** v tasks.md; oddělovač `; `
5. **MD = source of truth** — apps čtou, nikdy nepíšou
6. **Po editaci tasks.md:** aktualizovat header čísla, tabulku lidí, rozpočet

## Agenty — co vědět

- `data/tasks.md` je autoritativní
- Ověř rozpočet ≤ 100K vždy
- Linky lowercase (`docs/`, ne `Docs/`)
- Sync header čísla a tabulky v README po editaci
