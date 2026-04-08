#!/usr/bin/env python3
"""T100 clean local operator wrapper for the T98 happy-path runner.

Bounded scope:
- Wrap existing T98 runner only (no pipeline logic rewrite).
- Create one per-run folder under outputs/local_happy_path_runs/.
- Copy request/result artifacts for this run and write one concise summary.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


THE_FADE_ROOT = Path(__file__).resolve().parents[2]
REPO_ROOT = THE_FADE_ROOT.parents[1]
T98_RUNNER = THE_FADE_ROOT / "runner" / "local_happy_path" / "run_local_end_to_end_happy_path.py"
RUNS_ROOT = THE_FADE_ROOT / "outputs" / "local_happy_path_runs"
REQUESTS_ROOT = THE_FADE_ROOT / "inputs" / "phase3_universe_scanner_requests"
RESULTS_ROOT = THE_FADE_ROOT / "outputs" / "phase3_universe_scanner_results"
REQUEST_VALIDATOR = (
    THE_FADE_ROOT
    / "contracts"
    / "phase3_universe_scanner_io"
    / "tools"
    / "validate_ingress_request_packets.py"
)
RESULT_VALIDATOR = (
    THE_FADE_ROOT
    / "contracts"
    / "phase3_universe_scanner_io"
    / "tools"
    / "validate_universe_scanner_result_packets.py"
)
MAX_RESULT_ROOT_JSON = 3

REQ_PREFIX = "SUMMARY: request packet path:"
RES_PREFIX = "SUMMARY: result packet path:"


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _utc_stamp(dt: datetime) -> str:
    return dt.strftime("%Y%m%dT%H%M%SZ")


def _utc_iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _extract_path(text: str, prefix: str) -> Path | None:
    for line in text.splitlines():
        if line.startswith(prefix):
            raw = line.split(":", 2)[2].strip()
            if raw:
                return Path(raw)
    return None


def _run_t98() -> tuple[int, str]:
    cmd = [sys.executable, str(T98_RUNNER)]
    completed = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    # Keep operator-facing visibility from the wrapped runner.
    if completed.stdout:
        print(completed.stdout, end="")
    if completed.stderr:
        print(completed.stderr, end="", file=sys.stderr)
    return completed.returncode, f"{completed.stdout}\n{completed.stderr}"


def _run_preflight_validator(script_path: Path, label: str) -> None:
    cmd = [sys.executable, str(script_path)]
    completed = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    if completed.returncode != 0:
        raise RuntimeError(
            f"Preflight failed: {label} reports invalid root-state artifacts. "
            "Run the validator manually for details and clean legacy root artifacts first."
        )


def _preflight_check() -> None:
    if not T98_RUNNER.is_file():
        raise RuntimeError(f"Missing T98 runner: {T98_RUNNER}")
    if not REQUEST_VALIDATOR.is_file() or not RESULT_VALIDATOR.is_file():
        raise RuntimeError("Missing required validator script(s) for preflight checks.")

    root_result_json = sorted(RESULTS_ROOT.glob("*.json")) if RESULTS_ROOT.is_dir() else []
    if len(root_result_json) >= MAX_RESULT_ROOT_JSON:
        names = ", ".join(p.name for p in root_result_json)
        raise RuntimeError(
            "Preflight failed: result root is already at Model B cap "
            f"({len(root_result_json)}/{MAX_RESULT_ROOT_JSON}). "
            f"Manual one-time legacy cleanup required before run. Root files: {names}"
        )

    # Validate current root-state packets before doing any work.
    _run_preflight_validator(REQUEST_VALIDATOR, "request root validation")
    _run_preflight_validator(RESULT_VALIDATOR, "result root validation")


def _assert_transient_request_path(path: Path) -> None:
    resolved = path.resolve()
    base = REQUESTS_ROOT.resolve()
    if resolved.parent != base:
        raise RuntimeError("Request cleanup path is outside governed request root.")
    if not resolved.name.startswith("fr_universe_scanner_request_") or resolved.suffix != ".json":
        raise RuntimeError("Request cleanup path is not a governed transient request artifact.")


def _assert_transient_result_path(path: Path) -> None:
    resolved = path.resolve()
    base = RESULTS_ROOT.resolve()
    if resolved.parent != base:
        raise RuntimeError("Result cleanup path is outside governed result root.")
    if not resolved.name.startswith("bridge_universe_scanner_result_") or resolved.suffix != ".json":
        raise RuntimeError("Result cleanup path is not a governed transient bridge result artifact.")


def main() -> int:
    started = _utc_now()
    run_id = _utc_stamp(started)
    run_dir = RUNS_ROOT / f"run_{run_id}"
    summary_path = run_dir / "run_summary.json"

    try:
        _preflight_check()

        code, combined_output = _run_t98()
        if code != 0:
            raise RuntimeError(f"T98 runner failed with exit code {code}")

        request_path = _extract_path(combined_output, REQ_PREFIX)
        result_path = _extract_path(combined_output, RES_PREFIX)
        if request_path is None or result_path is None:
            raise RuntimeError("Could not identify request/result paths from T98 runner output")
        if not request_path.is_file() or not result_path.is_file():
            raise RuntimeError("Identified request/result paths do not exist on disk")

        run_dir.mkdir(parents=True, exist_ok=False)
        copied_request = run_dir / request_path.name
        copied_result = run_dir / result_path.name
        shutil.copy2(request_path, copied_request)
        shutil.copy2(result_path, copied_result)

        _assert_transient_request_path(request_path)
        _assert_transient_result_path(result_path)
        request_path.unlink()
        result_path.unlink()

        finished = _utc_now()
        summary = {
            "run_id": run_id,
            "started_at_utc": _utc_iso(started),
            "finished_at_utc": _utc_iso(finished),
            "status": "PASS",
            "wrapped_runner_path": str(T98_RUNNER),
            "source_request_path": str(request_path),
            "source_result_path": str(result_path),
            "copied_request_path": str(copied_request),
            "copied_result_path": str(copied_result),
            "cleaned_root_request_path": str(request_path),
            "cleaned_root_result_path": str(result_path),
        }
        summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

        print("SUMMARY: PASS (operator wrapper)")
        print(f"SUMMARY: run folder: {run_dir}")
        print(f"SUMMARY: run summary: {summary_path}")
        print(f"SUMMARY: copied request: {copied_request}")
        print(f"SUMMARY: copied result: {copied_result}")
        return 0
    except Exception as exc:
        print(f"SUMMARY: FAIL (operator wrapper) - {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
