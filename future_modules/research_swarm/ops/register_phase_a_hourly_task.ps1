# Phase A: Register hourly scheduled task (no-overlap via lock in script)
# Usage: Run as Administrator: .\register_phase_a_hourly_task.ps1

$ErrorActionPreference = "Stop"
$WorkspaceRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
$OpsDir = Join-Path $WorkspaceRoot "future_modules\research_swarm\ops"
$TaskName = "ResearchSwarmPhaseACollector"
$ScriptPath = Join-Path $OpsDir "run_phase_a_collector_once.ps1"

# Unregister if exists (idempotent)
Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue

$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$ScriptPath`""
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Hours 1)
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries

Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings

Write-Host "Registered scheduled task: $TaskName"
Write-Host "  Script: $ScriptPath"
Write-Host "  Interval: hourly"
Write-Host "  No-overlap: lock file in outputs/ (script skips if lock < 50 min old)"
Write-Host ""
Write-Host "To run once now: .\run_phase_a_collector_once.ps1"
