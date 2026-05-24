# Microsoft Copilot Context

This file is written for Microsoft Copilot or Copilot-like assistants that need
fast context on the PAPROS workspace.

## Workspace Goal

PAPROS is a PowerShell 7 agentic workstation rooted at `C:\DEV\PS7`.
The current project is a cleanup and knowledge reorganization pass:

- Inventory everything.
- Merge repeated rules and ideas.
- Quarantine junk instead of deleting it.
- Keep live modules stable.
- Build concise agent working memory.
- Preserve latest root inventory artifacts.

## Current Status

- Curation script exists: `Scripts\Invoke-PAPROSCuration.ps1`.
- Latest inventory lives in `Docs\Generated\Curation`.
- Cross-agent status lives in `Docs\CrossAgent\Progress.md`.
- Structured memory lives in `Data\Intelligence\memory.json`.
- Readable memory lives in `Docs\KnowledgeBase\AgentMemory.md`.
- Canonical merged rules live in `Docs\KnowledgeBase\CanonicalRules.md`.

## Safe Editing Rules

- Do not delete files permanently.
- Do not move live module files unless explicitly asked.
- Do not put modules in OneDrive paths.
- Prefer scripts under `Scripts` for one-off maintenance.
- Prefer module code under `Modules` for reusable public behavior.
- Update `Docs\CrossAgent\Progress.md` when making meaningful progress.
- Re-run `Scripts\Invoke-PAPROSCuration.ps1` after file movement so inventory stays current.

## Verification Commands

```powershell
.\Scripts\CheckHealth.ps1
.\Scripts\Verify-Profile.ps1
Import-Module PAPROS.Core -Force
Import-Module PAPROS.Portal -Force
# PAPROS.Agent was removed 2026-05-07 — its functions are now in DotSources, loaded by PAPROS.Core
Import-Module PAPROS.Intelligence -Force
Import-Module PAPROS.Snapshot -Force
Get-Content .\Data\Intelligence\memory.json -Raw | ConvertFrom-Json
```

## Known Hazards

- Root Git is not initialized.
- OneDrive module path warning is still expected.
- This host may show `$RawUI.CursorPosition` errors during startup.
- Parallel sessions can collide on `Logs\Session.log`.
