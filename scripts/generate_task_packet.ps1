param(
    [Parameter(Mandatory=$true)]
    [string]$TaskId,
    [switch]$Force,
    [switch]$Dispatch
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path $scriptDir "generate_task_packet.py"

if (-not (Test-Path $pythonScript)) {
    Write-Error "Could not find generate_task_packet.py at $pythonScript"
    exit 1
}

$args = @($pythonScript, "--task", $TaskId)
if ($Force) { $args += "--force" }
if ($Dispatch) { $args += "--dispatch" }

python @args
