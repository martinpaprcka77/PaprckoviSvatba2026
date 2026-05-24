# PAPROS Canonical Rules

This file merges the repeated operating guidance from `AGENTS.md`, `CLAUDE.md`,
`README.md`, `Docs\AI_Instructions.md`, and `Docs\Rules`.

## Environment

- Root is `C:\DEV\PS7`; all relative work should resolve inside this tree.
- PowerShell 7+ is required for normal operation.
- `C:\DEV\PS7\Modules` must be on `PSModulePath`.
- `Profiles\Global.Profile.ps1` is the main startup profile.

## Architecture

- `PAPROS.Core` is the hub for logging, config, self-healing, session startup, and DotSources consolidation.
- `PAPROS.Portal` owns interactive UI and prompt switching.
- `PAPROS.Core` (via DotSources) owns task utilities and automation skills.
- `PAPROS.Intelligence` owns memory and reasoning helpers.
- `PAPROS.Snapshot` owns snapshot, restore, compare, and dashboard helpers.

## Code Rules

- Use PowerShell 7 syntax.
- Use approved Verb-Noun names for public functions.
- Add public module code under `Modules`.
- Keep `Global.Profile.ps1` thin; move logic into modules or scripts.
- Search existing skills and scripts before creating new tools.
- Do not commit placeholder or nonfunctional files.

## Safety Rules

- Never install modules into OneDrive-synced module paths.
- Check `Test-OneDriveSafety` before writing to user-controlled or module-related paths.
- Log automated actions with `Write-Log` when available.
- Quarantine before deletion.
- Destructive operations must require explicit confirmation or a dry-run path.

## Workflow Rules

- Use `.\Scripts\CheckHealth.ps1` for environment checks.
- Use `plan "Task"` for complex work.
- Use `init-task "Name"` for full project setup.
- Use `watch` to monitor logs.
- Use `awareness` to inspect agent identity and runtime context.
- Use generated inventories as references, not as curated source docs.
