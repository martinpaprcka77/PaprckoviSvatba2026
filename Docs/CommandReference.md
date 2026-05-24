# PAPROS Command Reference

This is the quick reference for commands, aliases, and script runners in the
`C:\DEV\PS7` PAPROS workstation.

## Everyday Aliases

| Alias | Runs | Purpose |
|---|---|---|
| `portal` | `Show-Portal` | Open the interactive PAPROS menu. |
| `plan "Task"` | `Start-Plan` | Create a dated plan document in `Docs\Plans`. |
| `init-task "Name"` | `Initialize-Task` | Create a plan, scaffold a project, initialize Git, and open VS Code when available. |
| `status` | `Get-AgentStatus` | Show current agent/environment status. |
| `awareness` | `Get-AgentAwareness` | Show agent identity, context, session, and system awareness. |
| `self-heal` | `Repair-Environment` | Recreate configured missing directories. |
| `test-all` | `Test-Environment` | Run health checks and a performance scan. |
| `watch` | `Watch-Logs` | Tail `Logs\Session.log`. |
| `grep "Query"` | `Search-Code` | Search PowerShell and Markdown files under the root. |
| `gs` | `Get-GitSummary` | Show Git status and recent commits for the current repo. |
| `backup` | `Backup-Environment` | Zip the core environment, excluding projects/modules/git. |
| `deploy .\file.ps1` | `Deploy-Script` | Promote a script into `DotSources` or `Modules`. |
| `optimize .\file.ps1` | `Optimize-Script` | Trim trailing whitespace and add a generated header if missing. |
| `show-skills` | `Get-Skills` | List loaded PAPROS skill functions. |
| `docs` | `Show-Docs` | Open or show documentation entrypoints when available. |
| `papros-inventory` | `New-PAPROSInventory` | Run inventory artifact generation helper from the profile. |

## Core Module Commands

| Command | Module | Purpose |
|---|---|---|
| `Start-Session` | `PAPROS.Core` | Run startup workflow, self-heal, diagnostics, and session readiness checks. |
| `Write-Log` | `PAPROS.Core` | Append structured log messages to `Logs\Session.log`. |
| `Get-SessionContext` | `PAPROS.Core` | Detect interactive/background host context. |
| `Test-OneDriveSafety` | `PAPROS.Core` | Check whether a path is under a OneDrive location. |
| `Repair-Environment` | `PAPROS.Core` | Ensure required directories from config exist. |
| `Get-AgentAwareness` | `PAPROS.Core` | Print identity and runtime awareness. |

## Portal Commands

| Command | Module | Purpose |
|---|---|---|
| `Show-Portal` | `PAPROS.Portal` | Open the main interactive portal. |
| `Show-HelpMenu` | `PAPROS.Portal` | Show help/docs menu. |
| `Show-PromptMenu` | `PAPROS.Portal` | Switch prompt presets. |
| `Show-DevMenu` | `PAPROS.Portal` | Show developer automation menu. |
| `Set-PAPROSPrompt` | `PAPROS.Portal` | Dot-source a prompt preset from `Profiles\Prompts`. |

## Agent Skill Commands

| Command | Module | Purpose |
|---|---|---|
| `Initialize-Task` | `DotSources` | Plan and scaffold a new project. |
| `Search-Code` | `DotSources` | Search project PowerShell/Markdown content. |
| `Search-Skills` | `DotSources` | Find loaded skills by name. |
| `Get-Skills` | `DotSources` | List available skills. |
| `Backup-Environment` | `DotSources` | Create a backup zip of the environment. |
| `Deploy-Script` | `DotSources` | Copy scripts into skill/module locations. |
| `Get-GitSummary` | `DotSources` | Summarize Git status for current directory. |
| `Optimize-Script` | `DotSources` | Apply simple script cleanup. |
| `Test-Environment` | `DotSources` | Run health and performance checks. |
| `Watch-Logs` | `DotSources` | Tail session logs. |

## Intelligence Commands

| Command | Module | Purpose |
|---|---|---|
| `Invoke-PAPROSPersona` | `PAPROS.Intelligence` | Invoke persona-oriented intelligence behavior. |
| `Invoke-PAPROSTask` | `PAPROS.Intelligence` | Invoke task-oriented intelligence behavior. |
| `Get-IntelMemory` | private helper | Load structured memory from `Data\Intelligence\memory.json`. |
| `Save-IntelMemory` | private helper | Save structured memory safely. |
| `Get-IntelKeyValue` | private helper | Read a memory key from the intelligence store. |
| `Save-IntelKeyValue` | private helper | Write a key/value memory entry. |

## Snapshot Commands

| Command | Module | Purpose |
|---|---|---|
| `Compare-PAPROSSnapshot` | `PAPROS.Snapshot` | Compare snapshot data. |
| `Restore-PAPROSSnapshot` | `PAPROS.Snapshot` | Restore from snapshot data. |
| `Show-PAPROSDashboard` | `PAPROS.Snapshot` | Show snapshot/dashboard information. |

## Script Runners

Run these from the root as `.\Scripts\<Name>.ps1`.

| Script | Purpose |
|---|---|
| `Analyze-Project.ps1` | Analyze a project folder: files, line counts, Git info, and dependencies. |
| `AutoBootstrap.ps1` | Bootstrap helper used by disabled hook/bootstrap experiments. |
| `CheckHealth.ps1` | Verify paths, module path, profile loading, and optional modules. |
| `Create-Gist-And-Init.ps1` | Create/initialize gist bootstrap workflow. |
| `Fix-Dependencies.ps1` | Check and resolve missing workstation dependencies. |
| `FixProfile.ps1` | Create/update the current PowerShell profile to load PAPROS. |
| *(removed)* | *(cleanup: these entries were empty stubs)* |
| `Invoke-PAPROSCuration.ps1` | Generate full inventory, quarantine clutter, and update memory. |
| `New-PAPROSSnapshot.ps1` | Create a filesystem/environment snapshot. |
| `Summarize-PAPROSSnapshot.ps1` | Summarize snapshot content. |
| `Verify-Compatibility.ps1` | Check compatibility concerns. |
| `Verify-Modularity.ps1` | Verify module structure/loading expectations. |
| `Verify-Profile.ps1` | Verify profile dot-sources the PAPROS global profile. |

## DeepSeek Commands

| Command | Purpose |
|---------|---------|
| `deepseek "dotaz"` | CLI — jednorázový dotaz, vrátí odpověď a skončí |
| `deepseek run` | CLI — interaktivní chat v terminálu |
| `deepseek-tui` | TUI — plnohodnotné terminálové UI s nástroji |
| `deepseek review` | Code review nad git diffem |
| `deepseek exec` | Neinteraktivní agentní příkaz |
| `deepseek sessions` | Seznam uložených session |
| `deepseek resume` | Obnoví předchozí session |
| `deepseek login` | Uložit API klíč |
| `deepseek config` | Čtení/zápis nastavení |
| `deepseek models` | Seznam live modelů |
| `deepseek doctor` | Diagnostika TUI |
| `deepseek update` | Aktualizace na nejnovější verzi |

Podrobná reference: `Docs\KnowledgeBase\DeepSeek.md`

## Best Starting Points

- Use `portal` when exploring interactively.
- Use `test-all` before larger changes.
- Use `grep "term"` before creating a new helper.
- Use `.\Scripts\Invoke-PAPROSCuration.ps1` after moving or reorganizing files.
- Use `Docs\CrossAgent\Progress.md` to understand current cleanup/reorg state.
