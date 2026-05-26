---
name: Task Data Integrity
description: Verify tasks.md internal consistency — counts, budget math, header sync
---

If `data/tasks.md` was not changed, no action is needed.

When `data/tasks.md` is in the diff, verify these invariants:

## Task count consistency

- Count all rows starting with `| 2026` in tasks.md. This count must match the header line `X úkolů` and the budget table's **Celkem** row.
- The header says e.g. `37 úkolů` — verify the count matches.

## Category task counts

Count tasks by category (`Kat.` column, index 4 in pipe-split):

- `mandatory` count must match the budget table's Povinné row
- `important` count must match the budget table's Důležité row
- `optional` count must match the budget table's Volitelné row

## Budget math per category

Sum `Plán (Kč)` column (index 5) per category:

- mandatory sum must match budget table (e.g. 94 500)
- important sum must match budget table (e.g. 5 000)
- optional sum must match budget table (e.g. 500)
- Total must be exactly 100 000 Kč

## People table consistency

The People table in tasks.md lists task counts per person. Verify:

- Count occurrences of each person in the `Kdo` column (index 3, comma-separated — a task with `Deti, Mamka` counts for both)
- Each person's count must match the People table
- Allowed people: Mamka, Taťka, Žanetka, Kikinka, Děti

## Task count note

The note under the People table says `*Součet > 36 — 3 úkoly mají více přiřazených osob.*`. Verify that the sum of People table counts equals Σ(počet osob na úkol) napříč všemi řádky. (Pozor: úkoly se 3 přiřazenými osobami přispívají +2 ke zvýšení, ne +1.)

## Done count

Count tasks with `[x]` in `Stav` column (index 6). Must match `Done: X/37` in CLAUDE.md if that line was also changed.

## Concrete verification

Run this on the current tasks.md and check the output:

```bash
python -c "
import re
with open('data/tasks.md', encoding='utf-8') as f:
    md = f.read()
lines = [l for l in md.split('\n') if l.startswith('| 2026')]
m = i = o = 0
mc = ic = oc = 0
for l in lines:
    parts = [p.strip() for p in l.split('|')]
    cat = parts[4]; price = int(parts[5]) if parts[5].isdigit() else 0
    if cat == 'mandatory': m += price; mc += 1
    elif cat == 'important': i += price; ic += 1
    elif cat == 'optional': o += price; oc += 1
total = m + i + o
print(f'Tasks: {len(lines)} | Mand: {mc}/{m} | Imp: {ic}/{i} | Opt: {oc}/{o} | Total: {total}')
print('OK' if total == 100000 and len(lines) == 37 else 'GAP')
"
```

If any count or sum is off, FAIL. List each mismatch with expected vs actual.
