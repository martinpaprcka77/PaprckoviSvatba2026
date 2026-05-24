# PAPROS Known Risks

This list is shared context for all agents working in this workspace.

## Active Risks

- `C:\DEV\PS7` is not currently a Git repository. Cleanup and reorg work should preserve restore manifests until source control exists.
- `PSModulePath` still includes a OneDrive module location: `C:\Users\spravce\OneDrive\Dokumenty\PowerShell\Modules`.
- Some shell sessions emit `$RawUI.CursorPosition` errors because the prompt/startup stack assumes an interactive console host.
- Parallel shell sessions can collide on `Logs\Session.log`.
- Large generated inventory and snapshot files can bury curated documentation if they stay in the main docs surface.
- `Data\Intelligence\memory.json` previously contained placeholder test data; agents should treat the structured memory schema as canonical from the 2026-05-06 curation pass onward.

## Safety Defaults

- Quarantine before delete.
- Keep live modules, profiles, curated docs, and memory files unless a human explicitly asks for removal.
- Prefer `-WhatIf` or a manifest-backed move for any broad file operation.
- If a path smells like OneDrive, stop and check `Test-OneDriveSafety`.
