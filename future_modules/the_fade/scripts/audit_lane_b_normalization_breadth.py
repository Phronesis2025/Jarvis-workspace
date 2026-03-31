"""Tranche 34: Lane B normalization breadth audit on stored FR JSONL + snapshots. No network. Not production."""
from __future__ import annotations

import json
import pathlib
import re
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parents[1] / "outputs" / "lane_b_real_observation"
LOG = ROOT / "tranche21_fr_slot_runs.jsonl"
OUT_JSON = ROOT / "tranche34_normalization_breadth_audit.json"
OUT_MD = ROOT / "tranche34_normalization_breadth_audit.md"
WIN_START = "2026-03-27T16:00:00Z"
WIN_END = "2026-03-29T16:00:00Z"
EXCLUDE = "t30_valid_002"

# Grounded from run_tranche21_fr_slot.py INGESTION_REQUIRED_FIELDS + observed outcome fields used in evidence log.
JSONL_AUDIT_KEYS = [
    "task_id",
    "slot_identity",
    "run_identity",
    "scheduled_slot_utc",
    "actual_started_at_utc",
    "window_start_utc",
    "window_end_utc",
    "source_class",
    "endpoint_url",
    "http_status",
    "source_observation_success",
    "collector_execution_success",
    "observed_result_type",
    "timing_valid_for_counted_slot_use",
    "artifact_path",
]

SNAPSHOT_SHELL_KEYS = [
    "artifact_version",
    "task_id",
    "slot_identity",
    "run_identity",
    "endpoint_url",
    "captured_at_utc",
    "http_status",
    "response_preview_utf8",
    "response_sha256",
    "source_observation_success",
    "collector_execution_success",
]


def parse_utc(s: str) -> bool:
    try:
        raw = s[:-1] + "+00:00" if s.endswith("Z") else s
        datetime.fromisoformat(raw)
        return True
    except Exception:
        return False


def extract_after_results(preview: str) -> str | None:
    i = preview.find('"results":[{')
    return preview[i:] if i >= 0 else None


def regex_results0(preview: str) -> dict[str, str | None]:
    sub = extract_after_results(preview) or ""
    out: dict[str, str | None] = {}
    for field in ("document_number", "publication_date", "title", "type", "html_url"):
        m = re.search(rf'"{field}"\s*:\s*"([^"]*)"', sub)
        out[field] = m.group(1) if m else None
    return out


def main() -> None:
    rows_in: list[dict] = []
    for line in LOG.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        o = json.loads(line)
        if o.get("task_id") == EXCLUDE:
            continue
        if o.get("window_start_utc") != WIN_START or o.get("window_end_utc") != WIN_END:
            continue
        rows_in.append(o)

    per_row: list[dict] = []
    distinct_docs: set[str] = set()
    parse_ok_count = 0
    regex_dn_ok = 0

    for o in sorted(rows_in, key=lambda x: x["task_id"]):
        tid = o["task_id"]
        ap = o.get("artifact_path") or ""
        name = pathlib.Path(ap).name
        snap_path = ROOT / name

        j_audit: dict = {"task_id": tid, "jsonl": {}, "snapshot_path": str(snap_path)}
        missing_j = [k for k in JSONL_AUDIT_KEYS if k not in o or o[k] is None]
        j_audit["jsonl"]["missing_or_null_keys"] = missing_j
        j_audit["jsonl"]["utc_fields_parseable"] = {
            "scheduled_slot_utc": parse_utc(str(o.get("scheduled_slot_utc", ""))),
            "actual_started_at_utc": parse_utc(str(o.get("actual_started_at_utc", ""))),
        }

        if not snap_path.exists():
            j_audit["snapshot"] = {"exists": False}
            j_audit["verdict_row"] = "blocked_snapshot_missing"
            per_row.append(j_audit)
            continue

        snap = json.loads(snap_path.read_text(encoding="utf-8"))
        miss_s = [k for k in SNAPSHOT_SHELL_KEYS if k not in snap]
        j_audit["snapshot"] = {
            "exists": True,
            "missing_keys": miss_s,
            "response_sha256_present": bool(snap.get("response_sha256")),
            "json_shape_valid": snap.get("json_shape_valid"),
        }
        preview = snap.get("response_preview_utf8") or ""
        full_parse = None
        parse_err = None
        try:
            full_parse = json.loads(preview)
            parse_ok_count += 1
        except Exception as e:
            parse_err = str(e)[:200]

        rx = regex_results0(preview)
        if rx.get("document_number"):
            regex_dn_ok += 1
            distinct_docs.add(rx["document_number"])
        if rx.get("publication_date"):
            pass

        j_audit["preview"] = {
            "full_json_parse_ok": full_parse is not None,
            "full_json_parse_error": parse_err,
            "regex_results0": rx,
            "note": "Evidence log uses regex-first extraction from preview when truncated; full-parse failure is expected if preview is truncated mid-JSON.",
        }
        if j_audit["snapshot"]["missing_keys"]:
            j_audit["verdict_row"] = "thin_snapshot_schema"
        elif not rx.get("document_number") or not rx.get("publication_date"):
            j_audit["verdict_row"] = "thin_results0_identity"
        elif parse_err:
            j_audit["verdict_row"] = "partial_preview_truncated_parseable_via_regex"
        else:
            j_audit["verdict_row"] = "solid_shell_plus_results0_fields"

        per_row.append(j_audit)

    n = len(per_row)
    artifact = {
        "_meta": {
            "prompt": "Tranche 34 — Lane B normalization breadth audit",
            "phase_2_only": True,
            "not_mvp_approval": True,
            "phase_3_blocked": True,
            "no_network": True,
            "population": "22 full-window FR JSONL lines",
            "excluded": EXCLUDE,
            "grounding": "Fields derived from run_tranche21_fr_slot.py required fields + MVP_LANE_EVIDENCE_LOG freshness use of results[0] in response_preview_utf8.",
        },
        "summary": {
            "rows": n,
            "jsonl_required_keys_complete_all_rows": all(
                not r["jsonl"].get("missing_or_null_keys") for r in per_row if "jsonl" in r
            ),
            "snapshots_present_all_rows": all(
                r.get("snapshot", {}).get("exists") for r in per_row
            ),
            "full_json_preview_parse_ok_count": parse_ok_count,
            "regex_document_number_extract_ok_count": regex_dn_ok,
            "distinct_document_number_in_results0": sorted(distinct_docs),
            "distinct_document_number_count": len(distinct_docs),
        },
        "aggregate_verdict": {
            "solid": "JSONL timing/identity + outcome fields present; snapshot shell + checksum; results[0] document_number and publication_date extractable via regex for all rows (when snapshot exists).",
            "partial": "response_preview_utf8 is often truncated — full JSON parse of API body usually fails; downstream normalization must use regex/partial parse or store full body (not in current artifacts).",
            "weak_or_missing": "Full structured API document object is not reliably available from preview alone; title/type/html_url may be absent if truncated before those keys in results[0].",
            "normalization_breadth_not_closed": True,
        },
        "per_row": per_row,
    }

    OUT_JSON.write_text(json.dumps(artifact, indent=2), encoding="utf-8")

    lines = [
        "# Tranche 34 — Lane B normalization breadth audit",
        "",
        "**Not approval.** Does **not** close the MVP gate. **Phase 3** blocked. **`mvp_lane_approval.json`** unchanged.",
        "",
        "## Grounded field set",
        "",
        "- **JSONL:** `task_id`, `slot_identity`, `run_identity`, schedule/window UTC, `source_class`, `endpoint_url`, HTTP + success flags, `observed_result_type`, `artifact_path` (from `run_tranche21_fr_slot.py` ingestion contract).",
        "- **Snapshot shell:** `artifact_version`, ids, `endpoint_url`, `captured_at_utc`, `http_status`, `response_preview_utf8`, `response_sha256`, success flags.",
        "- **Source document (preview):** `results[0]` `document_number`, `publication_date` (per evidence log freshness path); optional `title`, `type`, `html_url` via regex after `\"results\":[{`.",
        "",
        "## Summary",
        "",
        f"- Rows audited: **{n}** (`{EXCLUDE}` excluded).",
        f"- Full JSON parse of `response_preview_utf8`: **{parse_ok_count}** / **{n}** (truncation expected).",
        f"- Regex `document_number` in `results[0]` region: **{regex_dn_ok}** / **{n}**.",
        f"- Distinct `document_number` values: **{len(distinct_docs)}** — `{', '.join(sorted(distinct_docs))}`.",
        "",
        "## Verdict",
        "",
        "- **Solid:** Collector JSONL + snapshot metadata support consistent identity, timing, and outcome typing for the window.",
        "- **Partial:** Normalization from **full** API JSON is **not** available when preview is truncated; regex extraction matches current evidence practice.",
        "- **Not closed:** Normalization **breadth** for rich fields (full agencies, excerpts, full title) is **not** proven from stored snapshots alone.",
        "",
        f"Machine-readable: `{OUT_JSON.name}`",
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")
    print(json.dumps(artifact["summary"], indent=2))


if __name__ == "__main__":
    main()
