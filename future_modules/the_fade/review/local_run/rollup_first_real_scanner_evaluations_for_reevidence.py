#!/usr/bin/env python3
"""T120 re-evidence: read per-run first_real_scanner_rule_evaluation.json files, aggregate.

Optional: subprocess locked T118 script if evaluation missing but snapshot exists.
No network in this file. Does not change rule logic.
"""

from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

THE_FADE_ROOT = Path(__file__).resolve().parents[2]
RUNS_ROOT = THE_FADE_ROOT / "outputs" / "local_happy_path_runs"
SUMMARY_NAME = "first_real_scanner_rule_reevidence_summary.json"
SNAPSHOT_NAME = "source_records_snapshot.json"
EVAL_NAME = "first_real_scanner_rule_evaluation.json"
T118_SCRIPT = Path(__file__).resolve().parent / "build_first_real_scanner_rule_from_run_folder.py"


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        raw = json.load(f)
    if not isinstance(raw, dict):
        raise ValueError(f"Expected object in {path}")
    return raw


def _reason_histogram_from_eval(eval_doc: dict[str, Any]) -> dict[str, int]:
    c: Counter[str] = Counter()
    for key in ("eligible_records", "excluded_records"):
        rows = eval_doc.get(key)
        if not isinstance(rows, list):
            continue
        for row in rows:
            if not isinstance(row, dict):
                continue
            reasons = row.get("scanner_rule_reasons")
            if isinstance(reasons, list):
                for r in reasons:
                    if isinstance(r, str):
                        c[r] += 1
    return dict(sorted(c.items()))


def _ensure_evaluation(run_dir: Path) -> Path | None:
    """Return path to evaluation JSON, generating via subprocess if needed."""
    snap = run_dir / SNAPSHOT_NAME
    ev = run_dir / EVAL_NAME
    if not snap.is_file():
        return None
    if ev.is_file():
        return ev
    repo_root = THE_FADE_ROOT.parent.parent
    r = subprocess.run(
        [sys.executable, str(T118_SCRIPT), str(run_dir.name)],
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        timeout=120,
    )
    if r.returncode != 0:
        raise RuntimeError(f"T118 failed for {run_dir.name}: {r.stderr or r.stdout}")
    if not ev.is_file():
        raise RuntimeError(f"T118 did not write {EVAL_NAME} for {run_dir.name}")
    return ev


def build_summary() -> Path:
    run_dirs = sorted(p for p in RUNS_ROOT.iterdir() if p.is_dir() and p.name.startswith("run_"))

    per_run: list[dict[str, Any]] = []
    global_reasons: Counter[str] = Counter()
    with_snapshot = 0
    with_eval = 0

    for run_dir in run_dirs:
        snap_path = run_dir / SNAPSHOT_NAME
        if not snap_path.is_file():
            continue
        with_snapshot += 1
        snap = _read_json(snap_path)
        fetch_url = snap.get("fetch_url_used")
        fetch_ts = snap.get("fetch_timestamp_utc")
        meta = snap.get("api_response_metadata")
        results_len = None
        if isinstance(meta, dict) and "results_length" in meta:
            results_len = meta.get("results_length")

        ev_path = run_dir / EVAL_NAME
        if not ev_path.is_file():
            ev_path = _ensure_evaluation(run_dir)
        if ev_path is None or not ev_path.is_file():
            per_run.append(
                {
                    "run_folder": run_dir.name,
                    "has_snapshot": True,
                    "has_evaluation": False,
                    "error": "no evaluation and T118 could not run",
                }
            )
            continue

        with_eval += 1
        ev = _read_json(ev_path)
        hist = _reason_histogram_from_eval(ev)
        for k, v in hist.items():
            global_reasons[k] += v

        per_run.append(
            {
                "run_folder": run_dir.name,
                "has_snapshot": True,
                "has_evaluation": True,
                "fetch_url_used": fetch_url,
                "fetch_timestamp_utc": fetch_ts,
                "api_results_length": results_len,
                "source_records_input_count": ev.get("totals", {}).get("source_records_input_count")
                if isinstance(ev.get("totals"), dict)
                else None,
                "eligible_count": ev.get("eligible_count"),
                "excluded_count": ev.get("excluded_count"),
                "scanner_rule_reasons_histogram": hist,
            }
        )

    # Diversity: >=2 runs with evaluation, and not identical fetch_url+timestamp+results_length (simple check)
    eval_runs = [p for p in per_run if p.get("has_evaluation")]
    diversity_met = False
    diversity_note = ""
    if len(eval_runs) >= 2:
        keys = [(r.get("fetch_url_used"), r.get("fetch_timestamp_utc"), r.get("api_results_length")) for r in eval_runs]
        if len(set(keys)) >= 2:
            diversity_met = True
            diversity_note = "At least two runs differ on fetch_url_used, fetch_timestamp_utc, or api_results_length."
        else:
            diversity_note = "Two or more evaluations exist but fetch_url/timestamp/results_length tuple is identical — operator should document deliberate query change or add a differentiated run."
    else:
        diversity_note = f"Only {len(eval_runs)} run(s) with snapshot+evaluation; T120 bar requires >=2 for full diversity gate."

    out_doc: dict[str, Any] = {
        "artifact_kind": "the_fade_t120_first_real_scanner_reevidence_summary_v1",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "runs_root": str(RUNS_ROOT.as_posix()),
        "run_directories_scanned": len(run_dirs),
        "runs_with_source_records_snapshot": with_snapshot,
        "runs_with_first_real_scanner_rule_evaluation": with_eval,
        "t120_diversity_gate_satisfied": diversity_met,
        "t120_diversity_gate_note": diversity_note,
        "aggregate_scanner_rule_reasons_histogram": dict(sorted(global_reasons.items())),
        "per_run": per_run,
        "explicit_non_engine_statement": (
            "This file is a mechanical rollup of existing first_real_scanner_rule_evaluation.json "
            "artifacts for T120 re-evidence. It is not a scanner engine and does not change rule logic."
        ),
    }

    out_path = RUNS_ROOT / SUMMARY_NAME
    out_path.write_text(json.dumps(out_doc, indent=2) + "\n", encoding="utf-8")
    return out_path


def main() -> int:
    try:
        p = build_summary()
        print(f"SUMMARY: PASS - wrote {p}")
        return 0
    except Exception as exc:
        print(f"SUMMARY: FAIL - {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
