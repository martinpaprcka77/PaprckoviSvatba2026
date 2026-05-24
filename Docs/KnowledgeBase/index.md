# 📘 PAPROS 2026: System Manual

Welcome to the definitive guide for your Agentic Workstation.

## 🏛️ Core Architecture
The system is built on a **Modular Consolidation** pattern.
- **Root**: `C:\DEV\PS7`
- **Module**: `PAPROS.Core` (Self-healing loader)
- **Workflows**: `Plan -> Init -> Code -> Deploy`

### 🏗️ The "Bases" System
To ensure high modularity and maintainability, PAPROS 2026 uses a "Bases" architecture:
- **Prompts Base** (`.\Profiles\Prompts\`): Modular UI themes.
- **Portal Base** (`.\Modules\PAPROS.Portal\`): Decoupled UI logic.
- **Knowledge Base** (`.\Docs\KnowledgeBase\`): Structured system documentation.
- **Architecture Base** (`.\Docs\Architecture\`): System analysis and roadmap.

## 🕹️ Interactive Portal (`portal`)
The portal is your command center. Use it to:
- **Help Menu**: Access AI instructions and manuals.
- **Prompt Menu**: Switch between **Default**, **Minimal**, and **Dev** themes.
- **Dev Menu**: Run automations like `init-task` and `backup`.

## 🤖 AI Interaction (`AI_Instructions.md`)
We have dedicated instructions for:
- **Antigravity**: Environment maintenance and architecture.
- **Copilot**: On-the-fly code generation.
- **Claude Code**: High-quality modular script building.

## 🤖 DeepSeek CLI & TUI
Podrobná reference v [DeepSeek.md](DeepSeek.md). Zkratka:

- `deepseek "dotaz"` — CLI, jednorázový dotaz
- `deepseek run` — interaktivní chat v terminálu
- `deepseek-tui` — plnohodnotné terminálové UI s nástroji
- `deepseek review` — code review nad git diffem
- `deepseek doctor` — diagnostika
- `deepseek models` — seznam modelů

## 🧠 System Memory
Kompletní reference všech paměťových umístění, promptů, skills a dokumentace v [SystemMemory.md](SystemMemory.md).

## 🛠️ Essential Skills
- **`init-task "Name"`**: The one-shot project generator.
- **`deploy .\file.ps1`**: Promotes a script to a permanent skill.
- **`backup`**: Encapsulates your core config for safety.
- **`grep "Query"`**: Searches all project code instantly.

## ✅ Health & Safety
- **OneDrive**: Always keep Git repos and heavy modules out of synced folders.
- **Verify**: Use `Verify-Profile` and `Verify-Modularity` to ensure system integrity.
