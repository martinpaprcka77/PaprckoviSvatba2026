## PAPROS 2026: Standard Workflows & Practices

### 🌐 **Universal GG — Git/Gist/Pages**
```
gg commit "msg"   →  git add -A + commit + push
gg push           →  git push
gg pull           →  git pull --ff-only
gg pages          →  git push master:gh-pages (deploy wedding app)
gg gist file      →  gh gist create --public
gg status         →  git status + recent log
```

### 🧠 **Tracker — State Engine**
```
tracker           →  display Data/State/state.json
update-state      →  scan goals, plans, commits, skills, projects → save
```
Auto-runs via post-commit hook after every `git commit`.

### 💾 **Memory & Knowledge**
```
mem-init          →  create Data/Intelligence/memory.json
mem-add Topic Detail →  append to memory.json + SystemMemory.md + notes.txt
mem-size          →  show file size and entry count
```

### 🩺 **Self-Check**
```
bootstrap         →  verify all dirs, files, modules, git, gh CLI
bootstrap -Fix    →  auto-create missing dirs/files
```
Run after clone or when something feels broken.

### 💒 **Wedding App — Svatba Paprčkovi 2026**
```
gg pages          →  deploy to doma77git.github.io/PaprckoviSvatba2026/
svatba            →  publish HTML as public Gist
svatba-status     →  check GitHub Pages build status
launch-svatba     →  interactive menu (open pages, publish, test)
```

### 📅 **Planning**
```
plan "Task Name"  →  create plan in Docs/Plans/yyyyMMdd_Task.md
init-task "Name"  →  create project + git + scaffold
```

### 🔄 **Sync Workflow**
1. `gg status` — check current state
2. `gg pull` — get latest from remote
3. `gg commit "message"` — add + commit + push (auto-triggers update-state)
4. `gg pages` — deploy to GitHub Pages (if wedding app)

### 🔧 **Health & Inventory**
```
bootstrap   →  quick self-check (dirs, files, modules)
test-all    →  full environment health check (CheckHealth.ps1)
```

### 🔐 **Backup & Recovery**
```
backup                →  zip core environment
gg gist file.html     →  create public Gist (quick share)
```
