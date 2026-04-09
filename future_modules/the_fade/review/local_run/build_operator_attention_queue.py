#!/usr/bin/env python3
"""T114 mechanical local operator attention queue from per-run attention signals.

Scans only direct run_* children under outputs/local_happy_path_runs/, reads only
operator_attention_signal.json per folder, writes a single
operator_attention_queue.json. No network, no pipeline invocation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

THE_FADE_ROOT = Path(__file__).resolve().parents[2]
RUNS_ROOT = THE_FADE_ROOT / "outputs" / "local_happy_path_runs"
QUEUE_REL_ROOT = "future_modules/the_fade/outputs/local_happy_path_runs"
QUEUE_FILENAME = "operator_attention_queue.json"

EXPLICIT_NON_SCANNER_STATEMENT = (
    "This queue is a mechanical index of local run folders and existing "
    "operator_attention_signal.json files. It is not a universe scanner execution "
    "result and not a scanner decision artifact."
)
EXPLICIT_NON_TRADING_SIGNAL_STATEMENT = (
    "This queue is not a trading signal, investment recommendation, or "
    "prioritization of markets or instruments."
)

QUEUE_SCHEMA_VERSION = "t114_v1"
_SIGNAL_NAME = "operator_attention_signal.json"

_RUN_TS = re.compile(r"^run_(\d{8}T\d{6}Z)$")


def _read_json_object(path: Path) -> dict[str, Any] | None:
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError, TypeError, UnicodeDecodeError):
        return None
    return data if isinstance(data, dict) else None


def _parse_run_timestamp(folder_name: str) -> str | None:
    m = _RUN_TS.fullmatch(folder_name)
    return m.group(1) if m else None


def _run_folder_paths() -> list[Path]:
    if not RUNS_ROOT.is_dir():
        return []
    out: list[Path] = []
    for p in RUNS_ROOT.iterdir():
        if p.is_dir() and p.name.startswith("run_"):
            out.append(p)
    return out


def _reasons_list(sig: dict[str, Any]) -> list[str]:
    raw = sig.get("operator_attention_reasons")
    if not isinstance(raw, list):
        return []
    out: list[str] = []
    for x in raw:
        if isinstance(x, str):
            out.append(x)
    return out


def _row_from_signal(run_dir: Path, sig: dict[str, Any]) -> dict[str, Any]:
    folder_name = run_dir.name
    signal_rel = f"{QUEUE_REL_ROOT}/{folder_name}/{_SIGNAL_NAME}"
    folder_rel = f"{QUEUE_REL_ROOT}/{folder_name}"

    run_id: str | None = None
    rid = sig.get("run_id")
    if isinstance(rid, str) and rid.strip():
        run_id = rid
    else:
        ts = _parse_run_timestamp(folder_name)
        if ts is not None:
            run_id = ts

    row: dict[str, Any] = {
        "run_id": run_id if run_id is not None else folder_name,
        "operator_attention_status": sig["operator_attention_status"],
        "operator_attention_reasons": _reasons_list(sig),
        "operator_attention_signal_path": signal_rel,
        "run_folder_path": folder_rel,
    }

    st = sig.get("operator_attention_status")
    if isinstance(st, str):
        row["operator_attention_partition"] = st

    for key in (
        "request_id",
        "source_name",
        "review_gate_status",
    ):
        val = sig.get(key)
        if isinstance(val, str):
            row[key] = val

    for key in ("candidate_outputs_count", "deferred_count"):
        val = sig.get(key)
        if isinstance(val, int):
            row[key] = val

    if "results_count" in sig and isinstance(sig["results_count"], int):
        row["results_count"] = sig["results_count"]

    return row


def build_queue_payload() -> dict[str, Any]:
    run_dirs = _run_folder_paths()
    total_run_folders = len(run_dirs)

    skipped = 0
    included: list[tuple[Path, dict[str, Any]]] = []

    for run_dir in run_dirs:
        sig_path = run_dir / _SIGNAL_NAME
        sig = _read_json_object(sig_path) if sig_path.is_file() else None
        if sig is None:
            skipped += 1
            continue
        st = sig.get("operator_attention_status")
        if not isinstance(st, str) or not st.strip():
            skipped += 1
            continue
        included.append((run_dir, sig))

    status_counter: Counter[str] = Counter()
    for _, sig in included:
        s = sig.get("operator_attention_status")
        if isinstance(s, str):
            status_counter[s] += 1

    parseable: list[tuple[str, tuple[Path, dict[str, Any]]]] = []
    unparseable: list[tuple[Path, dict[str, Any]]] = []
    for item in included:
        run_dir, sig = item
        ts = _parse_run_timestamp(run_dir.name)
        if ts is not None:
            parseable.append((ts, item))
        else:
            unparseable.append(item)

    parseable.sort(key=lambda x: x[0], reverse=True)
    unparseable.sort(key=lambda x: x[0].name, reverse=True)
    ordered = [t[1] for t in parseable] + unparseable

    runs = [_row_from_signal(rd, sg) for rd, sg in ordered]

    by_status = {k: status_counter[k] for k in sorted(status_counter.keys())}

    return {
        "generated_at_utc": datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "queue_schema_version": QUEUE_SCHEMA_VERSION,
        "runs_root_relative": QUEUE_REL_ROOT,
        "counts": {
            "total_run_folders": total_run_folders,
            "rows_with_operator_attention_signal": len(included),
            "skipped_missing_or_unparseable_operator_attention_signal": skipped,
            "by_operator_attention_status": by_status,
        },
        "runs": runs,
        "explicit_non_scanner_statement": EXPLICIT_NON_SCANNER_STATEMENT,
        "explicit_non_trading_signal_statement": EXPLICIT_NON_TRADING_SIGNAL_STATEMENT,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write operator_attention_queue.json under local_happy_path_runs."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print JSON to stdout only; do not write the queue file.",
    )
    args = parser.parse_args()

    payload = build_queue_payload()
    text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"

    if args.dry_run:
        sys.stdout.write(text)
        return 0

    out_path = RUNS_ROOT / QUEUE_FILENAME
    try:
        RUNS_ROOT.mkdir(parents=True, exist_ok=True)
        out_path.write_text(text, encoding="utf-8")
    except OSError as e:
        print(f"error: cannot write {out_path}: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
