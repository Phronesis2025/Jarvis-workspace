param(
    [Parameter(Mandatory = $true)]
    [string]$TaskId,
    [switch]$SkipReview,
    [string]$Workspace = ""
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path $scriptDir "reconcile_task_outcome.py"

$args = @($pythonScript, "--task", $TaskId)
if ($SkipReview) {
    $args += "--skip-review"
}
if ($Workspace -ne "") {
    $args += @("--workspace", $Workspace)
}

python @args
