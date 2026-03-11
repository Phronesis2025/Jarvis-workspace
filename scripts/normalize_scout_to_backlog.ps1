param(
    [string]$Workspace = "C:\dev\jarvis-workspace",
    [string]$Results = "",
    [switch]$DryRun
)

$ScriptPath = Join-Path $Workspace "scripts\normalize_scout_to_backlog.py"

if (-not (Test-Path $ScriptPath)) {
    Write-Error "Missing script: $ScriptPath"
    exit 1
}

$Args = @($ScriptPath, "--workspace", $Workspace)

if ($Results -ne "") {
    $Args += @("--results", $Results)
}

if ($DryRun) {
    $Args += "--dry-run"
}

python @Args
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}