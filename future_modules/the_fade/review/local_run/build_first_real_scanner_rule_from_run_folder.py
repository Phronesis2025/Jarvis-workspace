#!/usr/bin/env python3
"""T118: one mechanical first-real-scanner-rule evaluation per run folder.

Reads only source_records_snapshot.json (T116 output). No network. Writes
first_real_scanner_rule_evaluation.json per THE_FADE_T117_* governance.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

THE_FADE_ROOT = Path(__file__).resolve().parents[2]
RUNS_ROOT = THE_FADE_ROOT / "outputs" / "local_happy_path_runs"
SNAPSHOT_NAME = "source_records_snapshot.json"
OUTPUT_NAME = "first_real_scanner_rule_evaluation.json"

ARTIFACT_KIND_REQUIRED = "the_fade_t115_source_records_snapshot_v1"
RULE_SCHEMA_VERSION = "t117_v1"
RULE_ID = "first_real_scanner_rule_t117_v1"

TYPE_ALLOWLIST = frozenset({"Rule", "Proposed Rule", "Notice"})

_EXPLICIT_NON_ENGINE = (
    "This artifact is one bounded mechanical scanner-rule evaluation for a single local run folder. "
    "It is not a full scanner engine, not ranking or scoring, not selection, and not a recommendation."
)

_RULE_DESCRIPTION = (
    "Eligible only if document_number and title are non-empty strings, publication_date parses as a date, "
    "document_type or type is exactly Rule|Proposed Rule|Notice, and publication UTC date is in the inclusive "
    "three-day window ending on fetch_timestamp_utc UTC date."
)

# Deterministic order for exclusion reasons when multiple apply
_REASON_ORDER = (
    "missing_document_number",
    "missing_title",
    "missing_publication_date",
    "invalid_publication_date",
    "document_type_not_allowed",
    "publication_date_out_of_window",
)


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        raw = json.load(f)
    if not isinstance(raw, dict):
        raise ValueError(f"Expected JSON object in {path}")
    return raw


def _resolve_run_dir(run_arg: str) -> Path:
    candidate = Path(run_arg)
    if candidate.is_absolute():
        run_dir = candidate
    else:
        run_dir = RUNS_ROOT / run_arg
    run_dir = run_dir.resolve()
    runs_root_resolved = RUNS_ROOT.resolve()
    if run_dir.parent != runs_root_resolved:
        raise ValueError("Run folder must be one direct child under outputs/local_happy_path_runs/")
    if not run_dir.name.startswith("run_"):
        raise ValueError("Run folder name must start with run_")
    if not run_dir.is_dir():
        raise ValueError(f"Run folder not found: {run_dir}")
    return run_dir


def _parse_d_fetch(fetch_timestamp_utc: Any) -> date:
    if not isinstance(fetch_timestamp_utc, str) or not fetch_timestamp_utc.strip():
        raise ValueError("fetch_timestamp_utc must be a non-empty string")
    s = fetch_timestamp_utc.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(s)
    except ValueError as e:
        raise ValueError(f"Unparseable fetch_timestamp_utc: {fetch_timestamp_utc!r}") from e
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    else:
        dt = dt.astimezone(timezone.utc)
    return dt.date()


def _parse_publication_date(pub: Any) -> tuple[date | None, str]:
    """Return (date, status) where status is 'ok', 'missing', or 'invalid'."""
    if pub is None:
        return None, "missing"
    if not isinstance(pub, str):
        return None, "invalid"
    s = pub.strip()
    if not s:
        return None, "missing"
    if len(s) >= 10 and s[4] == "-" and s[7] == "-":
        prefix = s[:10]
        if re.match(r"^\d{4}-\d{2}-\d{2}$", prefix):
            try:
                y, m, d = int(prefix[0:4]), int(prefix[5:7]), int(prefix[8:10])
                return date(y, m, d), "ok"
            except ValueError:
                pass
    try:
        part = s[:10] if len(s) >= 10 else s
        return date.fromisoformat(part), "ok"
    except ValueError:
        return None, "invalid"


def _type_label(rec: dict[str, Any]) -> str | None:
    for key in ("document_type", "type"):
        v = rec.get(key)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None


def _bounded_row_copy(rec: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key in ("document_number", "publication_date", "title", "document_type", "type", "html_url", "pdf_url"):
        if key in rec:
            out[key] = rec[key]
    return out


def _evaluate_record(
    rec: dict[str, Any],
    d_fetch: date,
    allowed_dates: frozenset[date],
) -> tuple[str, list[str]]:
    """Return (status, reasons)."""
    reasons: list[str] = []

    # document_number
    dn = rec.get("document_number")
    if not isinstance(dn, str) or not dn.strip():
        reasons.append("missing_document_number")

    # title
    title = rec.get("title")
    if not isinstance(title, str) or not title.strip():
        reasons.append("missing_title")

    # publication_date
    d_pub, pub_status = _parse_publication_date(rec.get("publication_date"))
    if pub_status == "missing":
        reasons.append("missing_publication_date")
    elif pub_status == "invalid":
        reasons.append("invalid_publication_date")

    # document type
    label = _type_label(rec)
    if label is None or label not in TYPE_ALLOWLIST:
        reasons.append("document_type_not_allowed")

    # recency (only if we have a valid D_pub)
    if d_pub is not None and pub_status == "ok":
        if d_pub not in allowed_dates:
            reasons.append("publication_date_out_of_window")

    if reasons:
        # deterministic order, dedupe
        ordered = [r for r in _REASON_ORDER if r in reasons]
        return "excluded_by_rule", ordered
    return "eligible_by_rule", ["meets_first_real_scanner_rule"]


def build_evaluation(run_dir: Path) -> Path:
    snap_path = run_dir / SNAPSHOT_NAME
    if not snap_path.is_file():
        raise ValueError(f"Missing {SNAPSHOT_NAME} in {run_dir}")

    snap = _read_json(snap_path)
    if snap.get("artifact_kind") != ARTIFACT_KIND_REQUIRED:
        raise ValueError(
            f"artifact_kind must be {ARTIFACT_KIND_REQUIRED!r}, got {snap.get('artifact_kind')!r}"
        )
    records = snap.get("source_records")
    if not isinstance(records, list):
        raise ValueError("source_records must be a JSON array")

    fetch_ts = snap.get("fetch_timestamp_utc")
    d_fetch = _parse_d_fetch(fetch_ts)
    allowed_dates = frozenset(
        {
            d_fetch,
            d_fetch - timedelta(days=1),
            d_fetch - timedelta(days=2),
        }
    )

    run_folder_name = run_dir.name
    rid = snap.get("run_id")
    if rid is not None:
        run_id = rid if isinstance(rid, str) else str(rid)
    else:
        run_id = run_folder_name

    source_name = snap.get("source_name")
    if not isinstance(source_name, str) or not source_name.strip():
        source_name = "Federal Register"

    eligible: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []

    for rec in records:
        if not isinstance(rec, dict):
            rec = {}

        status, reasons = _evaluate_record(rec, d_fetch, allowed_dates)
        row = _bounded_row_copy(rec)
        row["scanner_rule_status"] = status
        row["scanner_rule_reasons"] = reasons

        if status == "eligible_by_rule":
            eligible.append(row)
        else:
            excluded.append(row)

    generated = datetime.now(timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")

    out_doc: dict[str, Any] = {
        "rule_id": RULE_ID,
        "generated_at_utc": generated,
        "rule_schema_version": RULE_SCHEMA_VERSION,
        "run_folder": run_folder_name,
        "run_folder_name": run_folder_name,
        "run_id": run_id,
        "input_snapshot_path": str(snap_path.as_posix()),
        "source_name": source_name,
        "fetch_timestamp_utc": fetch_ts,
        "rule_metadata": {
            "rule_id": RULE_ID,
            "description": _RULE_DESCRIPTION,
        },
        "eligible_count": len(eligible),
        "excluded_count": len(excluded),
        "eligible_records": eligible,
        "excluded_records": excluded,
        "totals": {
            "source_records_input_count": len(records),
            "eligible_count": len(eligible),
            "excluded_count": len(excluded),
        },
        "explicit_non_engine_statement": _EXPLICIT_NON_ENGINE,
    }

    if len(eligible) + len(excluded) != len(records):
        raise RuntimeError("internal: eligible + excluded != input count")

    out_path = run_dir / OUTPUT_NAME
    out_path.write_text(json.dumps(out_doc, indent=2) + "\n", encoding="utf-8")
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Evaluate T117 first real scanner rule from source_records_snapshot.json; "
            "writes first_real_scanner_rule_evaluation.json (no network)."
        )
    )
    parser.add_argument(
        "run_folder",
        help="Run folder under outputs/local_happy_path_runs/ or absolute path (e.g. run_20260408T125708Z)",
    )
    args = parser.parse_args()

    try:
        run_dir = _resolve_run_dir(args.run_folder)
        out = build_evaluation(run_dir)
        print(f"SUMMARY: PASS - wrote {out}")
        return 0
    except Exception as exc:
        print(f"SUMMARY: FAIL - {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
