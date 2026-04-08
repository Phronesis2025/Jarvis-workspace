#!/usr/bin/env python3
"""T98 local-only sequential happy-path runner for existing THE FADE tools.

Scope:
- Invoke existing tools only (no reimplementation).
- Order: ingress -> request validator -> bridge -> result validator.
- Console summary only; non-zero exit on any failure.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Iterable, List, Sequence, Set


THE_FADE_ROOT = Path(__file__).resolve().parents[2]
REPO_ROOT = THE_FADE_ROOT.parents[1]

INGRESS = (
    THE_FADE_ROOT
    / "ingress"
    / "federal_register"
    / "build_universe_scanner_request_from_federal_register.py"
)
REQUEST_VALIDATOR = (
    THE_FADE_ROOT
    / "contracts"
    / "phase3_universe_scanner_io"
    / "tools"
    / "validate_ingress_request_packets.py"
)
BRIDGE = (
    THE_FADE_ROOT
    / "bridge"
    / "first_request_to_result"
    / "build_universe_scanner_result_from_single_request.py"
)
RESULT_VALIDATOR = (
    THE_FADE_ROOT
    / "contracts"
    / "phase3_universe_scanner_io"
    / "tools"
    / "validate_universe_scanner_result_packets.py"
)

REQUESTS_DIR = THE_FADE_ROOT / "inputs" / "phase3_universe_scanner_requests"
RESULTS_DIR = THE_FADE_ROOT / "outputs" / "phase3_universe_scanner_results"


def _root_json_names(directory: Path) -> Set[str]:
    if not directory.is_dir():
        return set()
    return {p.name for p in directory.glob("*.json")}


def _new_single_file_name(before: Set[str], after: Set[str], label: str) -> str:
    created = sorted(after - before)
    if len(created) != 1:
        raise RuntimeError(
            f"{label}: expected exactly one new root JSON file, found {len(created)} ({created})"
        )
    return created[0]


def _run_step(label: str, command: Sequence[str]) -> None:
    print(f"STEP: {label}")
    print(f"CMD: {' '.join(command)}")
    completed = subprocess.run(command, cwd=REPO_ROOT)
    if completed.returncode != 0:
        raise RuntimeError(f"{label} failed with exit code {completed.returncode}")


def _python_cmd(script_path: Path, extra_args: Iterable[str] | None = None) -> List[str]:
    args = [sys.executable, str(script_path)]
    if extra_args:
        args.extend(list(extra_args))
    return args


def main() -> int:
    request_path: Path | None = None
    result_path: Path | None = None
    try:
        requests_before = _root_json_names(REQUESTS_DIR)
        _run_step("Ingress (T89)", _python_cmd(INGRESS))

        requests_after = _root_json_names(REQUESTS_DIR)
        request_name = _new_single_file_name(requests_before, requests_after, "Ingress output")
        request_path = REQUESTS_DIR / request_name
        print(f"INFO: request packet path: {request_path}")

        _run_step("Validate ingress request packets (T91)", _python_cmd(REQUEST_VALIDATOR))

        results_before = _root_json_names(RESULTS_DIR)
        _run_step("Bridge request to result (T96)", _python_cmd(BRIDGE, [request_name]))

        results_after = _root_json_names(RESULTS_DIR)
        result_name = _new_single_file_name(results_before, results_after, "Bridge output")
        result_path = RESULTS_DIR / result_name
        print(f"INFO: result packet path: {result_path}")

        _run_step("Validate result packets (T94)", _python_cmd(RESULT_VALIDATOR))
    except Exception as exc:
        print(f"SUMMARY: FAIL - {exc}", file=sys.stderr)
        if request_path is not None:
            print(f"SUMMARY: request packet path: {request_path}")
        if result_path is not None:
            print(f"SUMMARY: result packet path: {result_path}")
        return 1

    print("SUMMARY: PASS")
    print(f"SUMMARY: request packet path: {request_path}")
    print(f"SUMMARY: result packet path: {result_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
