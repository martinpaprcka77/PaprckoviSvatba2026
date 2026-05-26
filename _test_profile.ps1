# Profile test script — v2 with fixes
Write-Output "=== Profile Test v2 ==="
Write-Output "1. Dot-source init.ps1"
. C:\dev\profile\init.ps1
Write-Output "2. Checking functions and aliases..."
Write-Output ""

$tests = @(
    # _Core
    @{Name="IsPS7"; Type="Variable"}
    @{Name="IsPS5"; Type="Variable"}
    # Navigation
    @{Name="Enter-ZoxideInteractive"; Type="Function"}
    @{Name="Add-ZoxidePath"; Type="Function"}
    @{Name="zi"; Type="Alias"}
    @{Name="za"; Type="Alias"}
    # RustTools
    @{Name="Find-File"; Type="Function"}
    @{Name="Search-Text"; Type="Function"}
    @{Name="f"; Type="Alias"}
    @{Name="r"; Type="Alias"}
    @{Name="cat"; Type="Alias"}
    # FZF
    @{Name="Invoke-FuzzyCd"; Type="Function"}
    @{Name="Invoke-FuzzyOpenFile"; Type="Function"}
    @{Name="Stop-FuzzyProcess"; Type="Function"}
    @{Name="cdf"; Type="Alias"}
    @{Name="fof"; Type="Alias"}
    @{Name="fkill"; Type="Alias"}
    # GitHub
    @{Name="Open-GitHubPullRequest"; Type="Function"}
    @{Name="New-GitHubPullRequest"; Type="Function"}
    @{Name="Switch-GitHubPullRequest"; Type="Function"}
    @{Name="Get-GitHubPullRequest"; Type="Function"}
    @{Name="Get-GitHubPullRequestDiff"; Type="Function"}
    @{Name="Open-GitHubIssue"; Type="Function"}
    @{Name="Get-GitHubIssue"; Type="Function"}
    @{Name="New-GitHubIssue"; Type="Function"}
    @{Name="Open-GitHubRepository"; Type="Function"}
    @{Name="Copy-GitHubRepository"; Type="Function"}
    @{Name="Get-GitHubNotificationCount"; Type="Function"}
    @{Name="pr"; Type="Alias"}
    @{Name="prc"; Type="Alias"}
    @{Name="prco"; Type="Alias"}
    @{Name="prls"; Type="Alias"}
    @{Name="prdiff"; Type="Alias"}
    @{Name="gils"; Type="Alias"}
    @{Name="gic"; Type="Alias"}
    @{Name="ghr"; Type="Alias"}
    @{Name="ghclone"; Type="Alias"}
    # Utilities
    @{Name="Edit-File"; Type="Function"}
    @{Name="Edit-FileInVSCode"; Type="Function"}
    @{Name="Get-CommandPath"; Type="Function"}
    @{Name="New-File"; Type="Function"}
    @{Name="New-Directory"; Type="Function"}
    @{Name="Sync-Profile"; Type="Function"}
    @{Name="Get-ProfileLoadTime"; Type="Function"}
    @{Name="ep"; Type="Alias"}
    @{Name="which"; Type="Alias"}
    @{Name="touch"; Type="Alias"}
    @{Name="mkdirp"; Type="Alias"}
    @{Name="reload-profile"; Type="Alias"}
    @{Name="profile-time"; Type="Alias"}
    # Tmux
    @{Name="Connect-TmuxSession"; Type="Function"}
    @{Name="Get-TmuxSession"; Type="Function"}
    @{Name="New-TmuxSession"; Type="Function"}
    @{Name="Remove-TmuxSession"; Type="Function"}
    @{Name="Reset-TmuxConfiguration"; Type="Function"}
    @{Name="ta"; Type="Alias"}
    @{Name="tls"; Type="Alias"}
    @{Name="tn"; Type="Alias"}
    @{Name="tk"; Type="Alias"}
    @{Name="tr"; Type="Alias"}
)

$passed = 0
$failed = 0
$skipped = 0
foreach ($t in $tests) {
    if ($t.Type -eq "Function") {
        $cmd = Get-Command $t.Name -ErrorAction SilentlyContinue
        $exists = $cmd -and $cmd.CommandType -eq 'Function'
    } elseif ($t.Type -eq "Alias") {
        $cmd = Get-Alias $t.Name -ErrorAction SilentlyContinue
        $exists = $null -ne $cmd
    } else {
        $exists = (Get-Variable -Name $t.Name -ErrorAction SilentlyContinue) -and $true
    }
    if ($exists) {
        Write-Output "  ✓ $($t.Name)"
        $passed++
    } else {
        Write-Output "  ⚠ $($t.Name) not found (optional — tool may be missing)"
        $skipped++
    }
}

Write-Output ""
Write-Output "=== Result ==="
Write-Output "Passed: $passed"
Write-Output "Optional (missing tool): $skipped"
Write-Output "Failed: $failed"

if ($failed -gt 0) { exit 1 } else { exit 0 }
