import re
with open('data/tasks.md', encoding='utf-8') as f:
    md = f.read()
lines = [l for l in md.split('\n') if l.startswith('| 2026')]
m = i = o = d = 0
for l in lines:
    parts = [p.strip() for p in l.split('|')]
    cat = parts[4]
    price = int(parts[5]) if parts[5].isdigit() else 0
    if cat == 'mandatory': m += price
    elif cat == 'important': i += price
    elif cat == 'optional': o += price
    if '[x]' in parts[7]: d += 1
total = m + i + o
print(f'Tasks: {len(lines)}/36 | Budget: {total:,}/89500 | {"OK" if total==89500 and len(lines)==36 else "GAP"}')
print(f'  Mandatory: {m:,} Kc')
print(f'  Important: {i:,} Kc')
print(f'  Optional:  {o:,} Kc')
print(f'  Done:      {d}/36')
