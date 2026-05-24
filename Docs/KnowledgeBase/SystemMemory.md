# 🧠 PAPROS 2026 — System Memory & Reference

Kompletní mapa paměti, promptů, obsahu, todů, skills a dokumentace.

---

## 🧬 MEMORY — Kam se ukládá paměť

### 1. DeepSeek notes (AI persistence)
```powershell
C:\Users\spravce\.deepseek\notes.txt
```
AI sem ukládá trvalé poznámky napříč sessionmi. Obsahuje:
- Historie rozhodnutí
- Klíčové parametry projektů
- Troubleshooting tips
- Odkazy na repa a live URL

### 2. MEMO soubor (workspace JSON)
```powershell
C:\dev\PS7\MEMO
```
JSON s metadaty o session (id, title, message_count, total_tokens, model, mode).
Slouží k obnovení kontextu při nové session.

### 3. Session memory (projektová)
```powershell
Docs\Svatba2026_SessionMemory.md
```
Dokumentace konkrétní session — co se dělalo, jaké problémy se řešily.

### 4. DeepSeek session store
```powershell
C:\Users\spravce\.deepseek\sessions\
```
Uložené session pro obnovení (`deepseek resume` / `deepseek fork`).

### 5. Audit log
```powershell
C:\Users\spravce\.deepseek\audit.log
```
Všechny tool cally a akce.

### 6. Composer history
```powershell
C:\Users\spravce\.deepseek\composer_history.txt
```
Historie promptů a odpovědí.

---

## 🤖 PROMPT — Kam se ukládá prompt konfigurace

### Prompt definitions
```powershell
Profiles\Prompts\Default.ps1    # Standardní prompt
Profiles\Prompts\Minimal.ps1    # Minimalistický
Profiles\Prompts\Dev.ps1        # Vývojářský
```

Přepínání:
```powershell
Set-PAPROSPrompt -Type Default
Set-PAPROSPrompt -Type Minimal
Set-PAPROSPrompt -Type Dev
# Nebo přes portal: portal → Prompt Menu
```

### Custom.Prompt.ps1
```powershell
Profiles\Custom.Prompt.ps1
```
Vlastní prompt načítaný při startu session.

### Global.Profile.ps1 (hlavní loader)
```powershell
Profiles\Global.Profile.ps1
```
- Nastaví PS7Root, PSModulePath
- Načte PAPROS moduly
- Spustí Start-Session
- Zobrazí banner

---

## 📦 CONTENT — Veškerý obsah workspace

### Kořen
| Soubor | Účel |
|--------|-------|
| `README.md` | Hlavní dokumentace workspace |
| `CLAUDE.md` | Instrukce pro AI asistenty |
| `Config.json` | Konfigurace prostředí |
| `codebase-map.html` | Vizuální mapa projektu |
| `MEMO` | Session metadata JSON |

### Docs/ — 20 markdown souborů
| Cesta | Obsah |
|-------|-------|
| `index.md` | Master index dokumentace |
| `CommandReference.md` | Všechny příkazy a aliasy |
| `AI_Instructions.md` | Instrukce pro AI |
| `ProjectOverview.md` | Přehled projektu |
| `PAPROS_history.md` | Historie vývoje |
| `Roadmap_v2.md` | Plán do budoucna |
| `Svatba2026_SessionMemory.md` | Session memory svatby |
| `KnowledgeBase/index.md` | Systémový manuál |
| `KnowledgeBase/DeepSeek.md` | DeepSeek CLI/TUI reference |
| `KnowledgeBase/AgentMemory.md` | Agentní paměť |
| `KnowledgeBase/CanonicalRules.md` | Pravidla a konvence |
| `Architecture/Architecture.md` | Architektura |
| `Architecture/System_Analysis.md` | Analýza systému |
| `CrossAgent/README.md` | Cross-agent workspace guide |
| `CrossAgent/Handoff.md` | Předávání mezi agenty |
| `CrossAgent/KnownRisks.md` | Známá rizika |
| `CrossAgent/MicrosoftCopilot.md` | Copilot kontext |
| `CrossAgent/Progress.md` | Progress cleanupů |
| `Workflows/Workflows.md` | Standardní workflow |
| `Generated/Curation/Inventory.md` | Inventář souborů |

### DotSources/ — 4 skripty
| Soubor | Funkce |
|--------|--------|
| `Init.ps1` | Bootstrapper, vytvoří adresáře |
| `Agent.ps1` | AGIL, plan, status, aliasy |
| `Skills.ps1` | Všechny skill funkce (15+) |
| `Sourcer.ps1` | Import-AllScripts fallback |

### Scripts/ — 13 skriptů
CheckHealth, AutoBootstrap, Create-Gist-And-Init, Fix*, Invoke*, New*, Summarize*, Verify*, **Publish-Svatba**

### Modules/ — 4 moduly
PAPROS.Core, PAPROS.Portal, PAPROS.Intelligence, PAPROS.Snapshot

### Projekty
```powershell
Projects\        # Spuštěním: init-task "Název"
```
Aktuálně: prázdné (všechny projekty v kořeni).

---

## ✅ TODO — Správa úkolů

### Způsoby:
| Metoda | Příkaz |
|--------|--------|
| **Plán** | `plan "Název"` → vytvoří `Docs\Plans\yyyyMMdd_Nazev.md` |
| **Checklist v session** | checklist_write / checklist_update |
| **Init task** | `init-task "Název"` → vytvoří projekt + plán + git |
| **Session memory** | Ručně v `Docs\*_SessionMemory.md` |
| **Notes** | AI ukládá do notes.txt |

### Příklady:
```powershell
# Vytvořit plán
plan "Doladit rozpočet svatby"

# Vytvořit projekt
init-task "Můj nový projekt"

# Zkontrolovat stav
awareness
test-all
```

---

## ⚡ SKILLS — Všechny dostupné

### Built-in (z DotSources/Skills.ps1)

| Skill | Alias | Popis |
|-------|-------|-------|
| `Get-Skills` | `show-skills` | Seznam skills |
| `Search-Skills` | — | Hledání v skills |
| `Initialize-Task` | `init-task` | Vytvoří projekt |
| `Search-Code` | `grep` | Hledání v kódu |
| `Backup-Environment` | `backup` | Záloha prostředí |
| `Test-Environment` | `test-all` | Diagnostika |
| `Watch-Logs` | `watch` | Live logy |
| `Get-GitSummary` | `gs` | Git přehled |
| `Optimize-Script` | `optimize` | Optimalizace skriptu |
| `Deploy-Script` | `deploy` | Nasazení skriptu |
| `Invoke-VisualizeCodebase` | `viz` | Vizuální mapa |
| `Invoke-ReviewScript` | `review` | Code review |
| `Publish-Svatba` | `svatba`, `publish-svatba` | Publikuje svatební appku jako gist |
| `Get-SvatbaPages` | `svatba-status` | Stav GitHub Pages |

### Z Agent.ps1
| Skill | Alias | Popis |
|-------|-------|-------|
| `Show-Docs` | `docs` | Zobrazí Docs |
| `Install-AGBlock` | — | Bezpečný zápis souborů |
| `Get-AgentStatus` | `status` | Status agenta |
| `Start-Plan` | `plan` | Vytvoří plán |

### Přidání nového skillu
```powershell
# 1. Přidat funkci do DotSources\Skills.ps1
# 2. Přidat alias na konec souboru
# 3. Reloadnout modul:
Remove-Module PAPROS.Core -Force
Import-Module PAPROS.Core -Force
```

---

## 📋 MD SOUBORY — Kompletní mapa

```
📁 C:\dev\PS7\
├── 📄 README.md              # Hlavní dokumentace workspace
├── 📄 CLAUDE.md              # AI instrukce (pravidla, architektura)
├── 📁 Docs\
│   ├── 📄 index.md           # Master index dokumentace
│   ├── 📄 AI_Instructions.md # Instrukce pro AI agenty
│   ├── 📄 CommandReference.md# Reference příkazů
│   ├── 📄 PAPROS_history.md  # Historie vývoje
│   ├── 📄 ProjectOverview.md # Přehled projektu
│   ├── 📄 Roadmap_v2.md      # Roadmapa
│   ├── 📄 Svatba2026_SessionMemory.md # Paměť session svatby
│   ├── 📁 KnowledgeBase\
│   │   ├── 📄 index.md       # Systémový manuál
│   │   ├── 📄 DeepSeek.md    # DeepSeek CLI/TUI reference
│   │   ├── 📄 AgentMemory.md # Paměť agenta
│   │   └── 📄 CanonicalRules.md # Pravidla
│   ├── 📁 Architecture\
│   │   ├── 📄 Architecture.md
│   │   └── 📄 System_Analysis.md
│   ├── 📁 CrossAgent\
│   │   ├── 📄 README.md
│   │   ├── 📄 Handoff.md
│   │   ├── 📄 KnownRisks.md
│   │   ├── 📄 MicrosoftCopilot.md
│   │   └── 📄 Progress.md
│   ├── 📁 Plans\             # Plány úkolů (yyyyMMdd_Nazev.md)
│   ├── 📁 Workflows\
│   │   └── 📄 Workflows.md
│   └── 📁 Generated\
│       └── 📁 Curation\
│           └── 📄 Inventory.md
```

---

## 🔄 Module Load Chain (jak se vše načítá)

```
PowerShell start
  └─ $PROFILE
       └─ Global.Profile.ps1
            ├─ Nastaví PS7Root, PSModulePath
            ├─ Zobrazí banner
            ├─ Import-Module PAPROS.Core
            │    ├─ Načte Config.json → $Global:PAPROSConfig
            │    ├─ Načte Identity.json → $Global:AgentIdentity
            │    ├─ Dot-source: Init.ps1    (bootstrapper)
            │    ├─ Dot-source: Agent.ps1   (AGIL, plan, aliasy)
            │    ├─ Dot-source: Skills.ps1  (všechny skills)
            │    └─ Dot-source: Sourcer.ps1 (fallback)
            ├─ Import-Module PAPROS.Portal
            │    └─ Show-Portal, Show-HelpMenu, atd.
            └─ Start-Session
                 ├─ Repair-Environment
                 ├─ OneDrive Safety Check
                 └─ Throttled Diagnostics (1×/hod)
```

---

## 🔗 Rychlé odkazy

```powershell
🌐 Live Pages: https://doma77git.github.io/PaprckoviSvatba2026/
📦 GitHub:     https://github.com/doma77git/PaprckoviSvatba2026
📄 Notes AI:   C:\Users\spravce\.deepseek\notes.txt
📄 MEMO:       C:\dev\PS7\MEMO
📄 README:     C:\dev\PS7\README.md
📄 CLAUDE.md:  C:\dev\PS7\CLAUDE.md
📁 Docs:       C:\dev\PS7\Docs\
⚡ Portal:     portal (alias pro Show-Portal)
```

---

*PAPROS 2026 — PowerShell Automation and Profile Orchestration System*
*Poslední aktualizace: Květen 2026*
