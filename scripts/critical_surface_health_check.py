"""
Read-only health check for the critical Jarvis hardening surface.
Verifies critical scripts/docs/registry exist, critical helpers compile,
and file_registry_check + naming_drift_check pass on the current workspace.
Does not run the full task loop, mutate state, or auto-fix anything.
"""
from __future__ import annotations

import argparse
import py_compile
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

# Critical scripts (under scripts/)
CRITICAL_SCRIPTS: List[str] = [
    "jarvis.py",
    "prepare_wcs_task_branch.py",
    "worker_change_check.py",
    "commit_gate_check.py",
    "worker_result_validate.py",
    "qa_result_validate.py",
    "qa_failure_triage.py",
    "stamp_guard_check.py",
    "stamp_result_timestamp.py",
    "pre_reconcile_check.py",
    "reconcile_task_outcome.py",
    "post_reconcile_validate.py",
    "file_registry_check.py",
    "naming_drift_check.py",
    "render_file_registry.py",
]

# Critical docs (at workspace root)
CRITICAL_DOCS: List[str] = [
    "JARVIS_SCRIPT_PROCESS_REFERENCE.md",
    "JARVIS_TASK_EXECUTION_CHECKLIST.md",
    "JARVIS_PHASE_CHECKLIST.md",
    "JARVIS_LIVE_HANDOFF_BUNDLE.md",
]

# Critical registry surfaces (under state/)
CRITICAL_REGISTRY: List[str] = [
    "state/file_registry.json",
    "state/FILE_REGISTRY.md",
]

# Scripts to compile-check (newest critical helpers)
COMPILE_SCRIPTS: List[str] = [
    "commit_gate_check.py",
    "qa_failure_triage.py",
    "stamp_guard_check.py",
    "file_registry_check.py",
    "naming_drift_check.py",
    "render_file_registry.py",
]

# Helpers to run (must succeed); each (label, script_basename)
HELPER_RUNS: List[Tuple[str, str]] = [
    ("file_registry_check.py", "file_registry_check.py"),
    ("naming_drift_check.py", "naming_drift_check.py"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Read-only sanity checker for the critical Jarvis hardening surface: "
            "existence of scripts/docs/registry, compile of critical helpers, "
            "and successful run of file_registry_check and naming_drift_check."
        )
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: List[str] = []

    if not workspace.exists():
        print("CRITICAL SURFACE HEALTH CHECK: FAIL")
        print(f"Workspace: {workspace}")
        print("Failures:")
        print("- Workspace path does not exist.")
        return 1

    # A. Existence checks
    for name in CRITICAL_SCRIPTS:
        path = workspace / "scripts" / name
        if not path.is_file():
            failures.append(f"Missing critical script: {path}")

    for name in CRITICAL_DOCS:
        path = workspace / name
        if not path.is_file():
            failures.append(f"Missing critical doc: {path}")

    for rel in CRITICAL_REGISTRY:
        path = workspace / rel
        if not path.is_file():
            failures.append(f"Missing critical registry surface: {path}")

    # B. Compile checks
    for name in COMPILE_SCRIPTS:
        path = workspace / "scripts" / name
        if not path.is_file():
            continue  # already reported in A
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as e:
            failures.append(f"Compile failed for {name}: {e}")

    if failures:
        print("CRITICAL SURFACE HEALTH CHECK: FAIL")
        print(f"Workspace: {workspace}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    # C. Live helper run checks
    for label, script_name in HELPER_RUNS:
        script_path = workspace / "scripts" / script_name
        cmd = [sys.executable, str(script_path), "--workspace", str(workspace)]
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=str(workspace),
                timeout=60,
            )
        except subprocess.TimeoutExpired:
            failures.append(f"Helper {label} timed out.")
            continue
        except Exception as e:
            failures.append(f"Helper {label} failed to run: {e}")
            continue
        if result.returncode != 0:
            failures.append(
                f"Helper {label} returned exit code {result.returncode}."
            )
            if result.stdout:
                failures.append(f"  stdout: {result.stdout.strip()[:500]}")
            if result.stderr:
                failures.append(f"  stderr: {result.stderr.strip()[:500]}")

    if failures:
        print("CRITICAL SURFACE HEALTH CHECK: FAIL")
        print(f"Workspace: {workspace}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    print("CRITICAL SURFACE HEALTH CHECK: PASS")
    print(f"Workspace: {workspace}")
    print("Summary:")
    print("- All critical scripts, docs, and registry surfaces present.")
    print("- All compile-checked helpers compiled successfully.")
    print("- file_registry_check.py and naming_drift_check.py passed on this workspace.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
