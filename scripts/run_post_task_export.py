"""
Post-task dashboard export hook for the Jarvis/WCS lane.

Runs automatically after each completed task (reconciled). Uses live export when
env vars are present, otherwise dry-run. Keeps task outcome separate from export
outcome; export failure does not mark the task as failed.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def _env(key: str, alt: str | None = None) -> str:
    v = os.environ.get(key) or (os.environ.get(alt) if alt else None)
    return (v or "").strip()


def run_post_task_export(workspace: Path) -> int:
    """
    Run dashboard export after task completion.
    Uses live export if env vars present, else dry-run.
    Returns exit code (0 = success, 1 = failure). Caller must not fail the task on export failure.
    """
    url = _env("SUPABASE_URL", "NEXT_PUBLIC_SUPABASE_URL")
    key = _env("SUPABASE_SERVICE_KEY", "SUPABASE_SERVICE_ROLE_KEY")
    use_live = bool(url and key)

    scripts_dir = workspace / "scripts"
    export_script = scripts_dir / "export_dashboard_data.py"
    if not export_script.is_file():
        print("POST-TASK EXPORT: SKIP (export script not found)")
        return 1

    cmd = [sys.executable, str(export_script)]
    if not use_live:
        cmd.append("--dry-run")

    proc = subprocess.run(
        cmd,
        cwd=str(workspace),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    out = (proc.stdout or "").strip()
    err = (proc.stderr or "").strip()
    if out:
        print(out)
    if err:
        print(err, file=sys.stderr)

    mode = "live export" if use_live else "dry-run (env missing)"
    if proc.returncode == 0:
        print(f"POST-TASK EXPORT: {mode} - PASS")
    else:
        print(f"POST-TASK EXPORT: {mode} - FAIL (exit {proc.returncode})")
    return proc.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Post-task dashboard export hook")
    parser.add_argument("--workspace", help="Jarvis workspace root")
    args = parser.parse_args()
    workspace = Path(args.workspace).resolve() if args.workspace else Path(__file__).resolve().parent.parent
    return run_post_task_export(workspace)


if __name__ == "__main__":
    sys.exit(main())
