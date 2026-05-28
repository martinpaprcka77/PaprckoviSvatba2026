---
name: Budget Hard Cap
description: Enforce 100 000 Kc total budget with correct category targets
---

If `data/tasks.md` was not changed, no action is needed.

## Rules

The wedding budget has a **hard cap of 100 000 Kč**. Current allocation:

| Category | Tasks | Budget (Kč) |
|----------|-------|-------------|
| mandatory | 19 | 84 500 |
| important | 13 | 4 500 |
| optional | 4 | 500 |
| **Total** | **36** | **89 500** |

Buffer: 10 500 Kč (100 000 − 89 500)

## Verification

Run this check on the current tasks.md:

```bash
python -c "
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
issues = []
if total > 100000: issues.append(f'OVER HARD CAP: {total} > 100000')
if mc != 19: issues.append(f'Mandatory count {mc} != 19')
if ic != 13: issues.append(f'Important count {ic} != 13')
if oc != 4: issues.append(f'Optional count {oc} != 4')
if issues:
    for x in issues: print('FAIL:', x)
else:
    print(f'OK: {total} Kč across {len(lines)} tasks (cap 100 000, buffer {100000-total})')
"
```

## What to check in the diff

### Budget changes
- If any `Plán (Kč)` value changed: verify the category sum still matches its target
- If total budget would exceed 100 000 Kč: FAIL — must rebalance within the same category

### Category changes
- If a task's category changed: verify both old and new category sums still match targets
- The count per category must stay: 19/13/4

### Task additions/removals
- New tasks must fit within existing category budgets — price must be offset by reducing another task in the same category
- No task can be removed if it would break category task counts (19/13/4) without updating the targets

## What to flag

- Total budget > 100 000 Kč: FAIL
- Category sum doesn't match target: FAIL
- Category task count doesn't match target: FAIL
- Budget < 100 000 Kč: WARN (under budget is not an error, but the cap should be fully utilized per the spec)
