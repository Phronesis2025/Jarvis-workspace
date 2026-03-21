# Phase A: Run collector once (with no-overlap check)
# Usage: .\run_phase_a_collector_once.ps1
# Optional: .\run_phase_a_collector_once.ps1 -QueriesFile "..\examples\phase_a_discovery_queries.json"

param(
    [string]$QueriesFile = ""
)

$ErrorActionPreference = "Stop"
# ops -> research_swarm -> future_modules -> jarvis-workspace
$WorkspaceRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
$ModuleRoot = Join-Path $WorkspaceRoot "future_modules\research_swarm"
$ScriptsDir = Join-Path $ModuleRoot "scripts"
$OutputsDir = Join-Path $ModuleRoot "outputs"
$LockFile = Join-Path $OutputsDir "phase_a_collector.lock"
$UrlsFile = Join-Path $ModuleRoot "docs\Example URLs.txt"
$DefaultQueries = Join-Path $ModuleRoot "examples\phase_a_discovery_queries.json"

# No-overlap: if lock exists and is < 50 min old, skip
if (Test-Path $LockFile) {
    $age = (Get-Date) - (Get-Item $LockFile).LastWriteTime
    if ($age.TotalMinutes -lt 50) {
        Write-Host "Skipping: lock file exists (age $([math]::Round($age.TotalMinutes, 0)) min). Previous run may still be active."
        exit 0
    }
}
# Create lock
New-Item -Path $LockFile -ItemType File -Force | Out-Null
try {
    $pyArgs = @("run_phase_a_collector.py", "--urls-file", $UrlsFile)
    if ($QueriesFile -ne "") {
        $pyArgs += "--queries-file", $QueriesFile
    } elseif (Test-Path $DefaultQueries) {
        $pyArgs += "--queries-file", $DefaultQueries
    }
    Push-Location $ScriptsDir
    & python @pyArgs
    $exitCode = $LASTEXITCODE
} finally {
    Pop-Location
    if (Test-Path $LockFile) { Remove-Item $LockFile -Force }
}
exit $exitCode
