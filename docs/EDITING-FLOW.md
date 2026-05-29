# 📝 Editing Flow — Jak editovat data

> **Quick Start:** Edituj `data/tasks.md` → commit → push → data jsou live za ~10 sekund.

## Architecture

```
Your PC (editor)
    ↓ (edit file)
data/tasks.md (git)
    ↓ (git commit)
GitHub master
    ↓ (GitHub Raw API)
App fetches data
    ↓ (parse + render)
Live on https://doma77git.github.io/...
```

**Key:** App čte z GitHub Raw, **nikoliv** z gh-pages branch. Data=Live.

---

## Step-by-Step Editing

### 1️⃣ Edit locally

Open `data/tasks.md` in your editor (VS Code, Sublime, vim, notepad):

```markdown
| Termín | Úkol | Kdo | Kat. | Plán (Kč) | Skutečnost (Kč) | Stav | Timestamp | Poznámka |
|--------|------|-----|------|-----------|-----------------|------|-----------|----------|
| 2026-07-10 | Svatební oznámení | Mamka | mandatory | 1500 | _ | [ ] | _ | Rozeší se v červenci |
```

**Change:** Mark task as done → `[ ]` to `[x]`

```markdown
| 2026-07-10 | Svatební oznámení | Mamka | mandatory | 1500 | _ | [x] | 2026-07-10T14:30 | ✅ Odesláno |
```

### 2️⃣ Commit & Push

```bash
cd C:\projects\PaprckoviSvatba2026
git add data/tasks.md
git commit -m "Mark 'Svatební oznámení' as done"
git push origin master
```

Or in Git UI (VS Code Source Control):
- Stage `data/tasks.md`
- Write message: "Mark 'Svatební oznámení' as done"
- Click "Commit"
- Click "Push"

### 3️⃣ App fetches data

App has this in JavaScript:

```javascript
const DATA_URL = 'https://raw.githubusercontent.com/doma77git/PaprckoviSvatba2026/master/data/tasks.md';

async function fetchData() {
    const res = await fetch(DATA_URL, { cache: 'no-cache' });
    tasks = parseTasksMD(await res.text());
    renderTasks();
}
```

When you open the app, it **force-fetches** from GitHub Raw. No cache.

### 4️⃣ Live in ~10 seconds

After push, GitHub takes ~1-2 sec to update Raw. App takes ~5-8 sec to fetch and render.

**Total:** 10-15 seconds from push to live.

---

## What Can You Edit?

| File | What | Rules |
|------|------|-------|
| `data/tasks.md` | ✅ ALL | Mark done, update deadline, add note |
| `data/budget.md` | ✅ Prices only | Change "Odhad (Kč)" column |
| `data/guests.md` | ✅ ALL | Names, counts, food, confirmation |
| `index.html` | ⚠️ Code change | Only if you understand JavaScript |

---

## Editing Rules

### ✅ DO

- ✅ Append notes with `; ` separator: `Hotovo ; Odesláno v květnu`
- ✅ Update timestamps when status changes: `2026-07-10T14:30`
- ✅ Keep Czech names (no special chars): `Mamka` not `Mámka`
- ✅ Update header counts after changes: `| 36 | ... | 89 500 |`
- ✅ Commit with clear message: `Mark 'Item' as done`

### ❌ DON'T

- ❌ Don't delete rows — just mark as done or add note
- ❌ Don't change column order (parser expects fixed columns)
- ❌ Don't use special characters in names: use `Mikesovi` not `Mikešovi`
- ❌ Don't commit `index.html` unless you know what you're doing
- ❌ Don't break the markdown table structure

---

## Common Tasks

### Mark task as done

**File:** `data/tasks.md`

**Find:** `[ ]` (incomplete)  
**Replace with:** `[x]` (done)  
**Add timestamp:** `2026-07-10T14:30` (optional)

```diff
- | 2026-07-10 | Svatební oznámení | Mamka | mandatory | 1500 | _ | [ ] | _ | — |
+ | 2026-07-10 | Svatební oznámení | Mamka | mandatory | 1500 | _ | [x] | 2026-07-10T14:30 | ✅ Odesláno |
```

### Update actual cost (spent money)

**File:** `data/tasks.md`

**Column:** "Skutečnost (Kč)"

```diff
- | 2026-07-15 | Svatební šaty | Mamka | mandatory | 12000 | _ | [x] | ... | — |
+ | 2026-07-15 | Svatební šaty | Mamka | mandatory | 12000 | 11500 | [x] | ... | Koupeny za 11.5K |
```

### Change guest count

**File:** `data/guests.md`

```diff
- | Luki | 2 | _ | Ano | _ |
+ | Luki | 3 | — | Ano | Ano |
```

### Update budget price

**File:** `data/budget.md`

```diff
- | 7 | Zlatá koliba | M | 30000 | Viz rozpad ↓ |
+ | 7 | Zlatá koliba | M | 31000 | Zdražena o 1000 |
```

---

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| App shows **old data** | Browser cache | Hard refresh: `Ctrl+Shift+R` |
| App shows **error** | GitHub API down | Wait 30 sec, refresh |
| Changes **won't push** | No internet | Check WiFi / VPN |
| Markdown looks **broken** | Table syntax wrong | Check `\|` separators |
| Timestamp format **wrong** | Invalid ISO format | Use `2026-07-10T14:30` |

---

## Data Flow Diagram

```
┌─────────────────────────────────────────────┐
│ You Edit data/tasks.md on Your PC           │
└──────────┬──────────────────────────────────┘
           │
           ↓
┌─────────────────────────────────────────────┐
│ git add data/tasks.md                       │
│ git commit -m "Update task"                 │
│ git push origin master                      │
└──────────┬──────────────────────────────────┘
           │ (1-2 sec)
           ↓
┌─────────────────────────────────────────────┐
│ GitHub Updates Raw File                     │
│ https://raw.githubusercontent.com/.../      │
│   master/data/tasks.md                      │
└──────────┬──────────────────────────────────┘
           │ (5-8 sec)
           ↓
┌─────────────────────────────────────────────┐
│ App Fetches & Parses                        │
│ fetchData() → parseTasksMD()                │
│ → renderTasks()                             │
└──────────┬──────────────────────────────────┘
           │ (instant)
           ↓
┌─────────────────────────────────────────────┐
│ Live on https://doma77git.github.io/        │
│ PaprckoviSvatba2026/                        │
└─────────────────────────────────────────────┘
```

---

## Offline Editing

If **no internet**, you can still edit locally:

1. Edit `data/tasks.md` offline
2. Commit locally: `git commit -m "..."`
3. When online: `git push origin master`
4. App updates automatically

**No action needed from you** — app will fetch when you next open it.

---

## Who Can Edit?

| Role | Can Edit | How |
|------|----------|-----|
| **Mamka** | ✅ All tasks | Via local git |
| **Taťka** | ✅ All tasks | Via local git |
| **Žanetka** | ✅ Her tasks | Via local git |
| **Kikinka** | ✅ Her tasks | Via local git |
| **Děti** | ✅ Their tasks | Via local git |

**GitHub:** All users need git access to the repo (ask Martinpaprcka77).

---

## Next Steps

1. **Clone repo:** `git clone https://github.com/doma77git/PaprckoviSvatba2026.git`
2. **Open editor:** VS Code → open folder
3. **Edit data files:** `data/tasks.md`, `data/budget.md`, `data/guests.md`
4. **Commit & push:** via Git UI or terminal
5. **Verify:** Open app, check changes (5-15 sec)

**Questions?** Ask Martinpaprcka77.
