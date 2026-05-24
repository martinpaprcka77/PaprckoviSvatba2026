# PAPROS Cross-Agent Workspace Guide

This folder is the coordination layer for any agent working in `C:\DEV\PS7`.
Use it before editing code, moving files, or creating new tools.

## Start Here

1. Read `AGENTS.md` at the workspace root.
2. Read `Docs\KnowledgeBase\AgentMemory.md`.
3. Read `Data\Intelligence\memory.json` for the compact machine-readable state.
4. Read `Docs\Generated\Curation\Inventory.md` for the latest root inventory summary.
5. Use `Docs\Generated\Curation\Inventory.json` when exact file-level details are needed.

## Coordination Rules

- Keep all work rooted in `C:\DEV\PS7`.
- Do not permanently delete files during cleanup; quarantine first.
- Do not place modules or active project state in OneDrive paths.
- Prefer existing scripts, skills, and modules before creating new ones.
- Log automated actions through `Write-Log` when available.
- Treat generated inventories as reference artifacts, not curated source docs.

## Current Canonical Artifacts

- Human navigation: `Docs\index.md`
- Agent memory: `Docs\KnowledgeBase\AgentMemory.md`
- Machine memory: `Data\Intelligence\memory.json`
- Latest inventory summary: `Docs\Generated\Curation\Inventory.md`
- Latest inventory data: `Docs\Generated\Curation\Inventory.json`
- Cleanup manifest: `Archive\Quarantine\YYYYMMDD\manifest.json`
- Known risk list: `Docs\CrossAgent\KnownRisks.md`

## Editing Guidance

- Public PowerShell functions belong in modules under `Modules\`.
- One-off utilities belong in `Scripts\`.
- Curated documentation belongs in `Docs\`.
- Generated reports belong in `Docs\Generated\`.
- Old backups, disabled hooks, root scratch files, and stale generated snapshots belong in `Archive\Quarantine`.
