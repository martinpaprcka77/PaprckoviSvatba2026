---
name: Budget Hard Cap
description: Enforce 100 000 Kc total budget with correct category targets
---

If `data/tasks.md` was not changed, no action is needed.

## Rules

The wedding budget has a **hard cap of 100 000 Kč** with fixed category allocations:

| Category | Tasks | Budget (Kč) |
|----------|-------|-------------|
| mandatory | 19 | 94 500 |
| important | 14 | 5 000 |
| optional | 4 | 500 |
| **Total** | **37** | **100 000** |

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
if total != 100000: issues.append(f'Total {total} != 100000')
if mc != 19: issues.append(f'Mandatory count {mc} != 19')
if ic != 14: issues.append(f'Important count {ic} != 14')
if oc != 4: issues.append(f'Optional count {oc} != 4')
if m != 94500: issues.append(f'Mandatory sum {m} != 94500')
if i != 5000: issues.append(f'Important sum {i} != 5000')
if o != 500: issues.append(f'Optional sum {o} != 500')
if issues:
    for x in issues: print('FAIL:', x)
else:
    print('OK: Budget 100 000 Kc across 37 tasks')
"
```

## What to check in the diff

### Budget changes
- If any `Plán (Kč)` value changed: verify the category sum still matches its target
- If total budget would exceed 100 000 Kč: FAIL — must rebalance within the same category

### Category changes
- If a task's category changed: verify both old and new category sums still match targets
- The count per category must stay: 19/14/4

### Task additions/removals
- New tasks must fit within existing category budgets — price must be offset by reducing another task in the same category
- No task can be removed if it would break category task counts (19/14/4) without updating the targets

## What to flag

- Total budget > 100 000 Kč: FAIL
- Category sum doesn't match target: FAIL
- Category task count doesn't match target: FAIL
- Budget < 100 000 Kč: WARN (under budget is not an error, but the cap should be fully utilized per the spec)
