# PAPROS Agent Memory

This is the readable source of truth for agents working in this workspace.
The machine-readable memory lives at `Data\Intelligence\memory.json`.

## Workspace

- Root: `C:\DEV\PS7`
- Shell: PowerShell 7+
- Primary agent identity: PAPROS
- Current safety posture: local-first, no modules or active projects in OneDrive-synced paths

## Architecture

- `Profiles\Global.Profile.ps1` sets the root, updates `PSModulePath`, loads modules, and starts the session.
- `PAPROS.Core` owns logging, self-healing, session startup, config loading, and dot-source consolidation.
- `PAPROS.Portal` owns interactive menus, prompt switching, help, and developer actions.
- `PAPROS.Core` (via DotSources) owns task skills: planning, initialization, search, backup, deployment, and environment testing.
- `PAPROS.Intelligence` owns durable memory and reasoning helpers.
- `PAPROS.Snapshot` owns snapshot comparison, restore, and dashboard helpers.

## Rules

- Resolve all relative paths inside `C:\DEV\PS7`.
- Use PowerShell 7 syntax and approved Verb-Noun names for public functions.
- Use existing skills and scripts before creating a new tool.
- Put new public module code under `Modules\`, not `DotSources\` or the profile.
- Log automated actions with `Write-Log` when available.
- Check `Test-OneDriveSafety` before writing to user-controlled or module-related paths.
- Prefer quarantine over deletion during cleanup.

## Workflows

- Run `.\Scripts\CheckHealth.ps1` for health checks.
- Use `plan "Task"` before complex tasks.
- Use `init-task "Project Name"` for full project scaffolding.
- Use `watch` to inspect session logs.
- Use `awareness` for agent identity and runtime state.
- Use `self-heal` to repair missing configured directories.

## Known Risks

- The root is not currently a Git repository, so workstation rollback is weaker than the roadmap recommends.
- A OneDrive module path is still present in `PSModulePath` and should be treated as unsafe.
- The host used by Codex can throw `$RawUI.CursorPosition` startup errors.
- Parallel shell sessions can collide while writing `Logs\Session.log`.
- Generated inventories and snapshots are useful references but should live outside curated documentation.

## Cleanup Policy

- First-pass cleanup moves files to `Archive\Quarantine\YYYYMMDD`, never deletes them.
- Every moved file must be recorded in a manifest with original and new paths.
- Live modules, profiles, curated docs, and structured data are keep-first unless explicitly reviewed.
- Huge generated artifacts belong in `Docs\Generated` or quarantine, not in the main docs surface.

## Next Recommendations

- Add root source control after cleanup, with volatile directories ignored.
- Harden `Write-Log` against concurrent writers.
- Guard prompt/host UI code against non-interactive hosts.
- Expand `PAPROS.Intelligence` from key-value memory to structured memory sections.
