# PAPROS Agent Handoff

Use this when handing work from one agent/session to another.

## Current State

- Workspace root: `C:\DEV\PS7`
- Cleanup strategy: quarantine first
- Memory target: agent working memory first
- Reorg scope: whole workspace, but public module APIs should remain stable unless explicitly reviewed

## What Was Added For Coordination

- `Scripts\Invoke-PAPROSCuration.ps1` generates inventory, quarantine manifest, and curation summaries.
- `Docs\KnowledgeBase\AgentMemory.md` provides readable agent context.
- `Data\Intelligence\memory.json` provides structured machine-readable memory.
- `Docs\CrossAgent\README.md` is the cross-agent start page.
- `Docs\CrossAgent\KnownRisks.md` tracks shared hazards and safety defaults.

## Required Checks After Changes

Run these after cleanup or reorganization:

```powershell
.\Scripts\CheckHealth.ps1
.\Scripts\Verify-Profile.ps1
Import-Module PAPROS.Core -Force
Import-Module PAPROS.Portal -Force
# PAPROS.Agent was removed 2026-05-07 — functions consolidated into DotSources, loaded by PAPROS.Core
Import-Module PAPROS.Intelligence -Force
Import-Module PAPROS.Snapshot -Force
Get-Content .\Data\Intelligence\memory.json -Raw | ConvertFrom-Json
```

## Restore Pattern

If a quarantined file must be restored:

1. Open `Archive\Quarantine\YYYYMMDD\manifest.json`.
2. Find the entry by `originalPath`.
3. Move the file from `quarantinePath` back to `originalPath`.
4. Re-run health and import checks.
