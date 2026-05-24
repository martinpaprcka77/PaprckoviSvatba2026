# PAPROS 2026 Architecture

This document describes the relationship between the core components of the PAPROS Agentic Workstation.

## 🗺️ System Overview (UML)

```mermaid
graph TD
    subgraph "Core Environment"
        Root["C:\DEV\PS7"]
        Core["PAPROS.Core Module"]
        Portal["PAPROS.Portal Module"]
        Profile["Global.Profile.ps1"]
    end

    subgraph "Automation & Skills"
        DotSources["DotSources (*.ps1)"]
        Skills["Skills.ps1"]
        Scripts["Scripts (*.ps1)"]
    end

    subgraph "Workspaces"
        Projects["C:\DEV\PS7\Projects"]
        Docs["C:\DEV\PS7\Docs"]
    end

    Profile -->|Imports| Core
    Profile -->|Imports| Portal
    Core -->|Consolidates| DotSources
    Core -->|Uses| Scripts
    DotSources -->|Defines| Skills
    Portal -->|Provides UI for| Skills
    Portal -->|Uses| Core
    Skills -->|Manages| Projects
    Skills -->|Documents via| Docs
```

## 🛠️ Components

| Component | Description | Primary File |
| :--- | :--- | :--- |
| **Core** | Heart of the system; handles logging and self-healing consolidation. | `PAPROS.Core.psm1` |
| **Portal** | Interactive UI for the workstation. | `PAPROS.Portal.psm1` |
| **Skills** | Actionable PowerShell functions for tasks/projects. | `DotSources\Skills.ps1` |
| **Scripts** | One-off maintenance and utility tools. | `Scripts\CheckHealth.ps1` |
| **Docs** | Knowledge base and AI instructions. | `Docs\AI_Instructions.md` |

## 🛡️ Safety Protocols
- **OneDrive Isolation**: Core modules and active projects must reside outside of OneDrive-synced paths to prevent latency and sync conflicts.
- **Root Awareness**: All operations are relative to the environment root.
