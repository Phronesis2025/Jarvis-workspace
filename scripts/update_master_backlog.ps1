$Workspace = "C:\dev\jarvis-workspace"
$ScriptPath = Join-Path $Workspace "scripts\render_master_backlog.py"

if (-not (Test-Path $ScriptPath)) {
    Write-Error "Script not found: $ScriptPath"
    exit 1
}

python $ScriptPath
