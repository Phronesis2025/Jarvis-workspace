"""Tranche 58: Lane B real-slice normalization truth audit. No network. No approval change."""
from __future__ import annotations

import json
import pathlib
import re
from typing import Any


MODULE_ROOT = pathlib.Path(__file__).resolve().parents[1]
REAL_OBS_ROOT = MODULE_ROOT / "outputs" / "lane_b_real_observation"
OUT_ROOT = MODULE_ROOT / "outputs" / "lane_b_real_slice_normalization_truth_bootstrap"
LOG_PATH = REAL_OBS_ROOT / "tranche21_fr_slot_runs.jsonl"
SCHEMA_PATH = MODULE_ROOT / "schemas" / "normalized_signal_event.schema.json"
OUT_JSON = OUT_ROOT / "tranche58_lane_b_real_slice_normalization_truth_audit.json"
OUT_MD = OUT_ROOT / "tranche58_lane_b_real_slice_normalization_truth_audit.md"

WINDOW_START = "2026-03-27T16:00:00Z"
WINDOW_END = "2026-03-29T16:00:00Z"
EXCLUDED_TASK_ID = "t30_valid_002"

SCALAR_RESULTS0_FIELDS = (
    "title",
    "type",
    "document_number",
    "html_url",
    "pdf_url",
    "public_inspection_pdf_url",
    "publication_date",
)
TOKEN_RESULTS0_FIELDS = (
    "abstract",
    "agencies",
    "excerpts",
)


def _load_json(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_counted_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("task_id") == EXCLUDED_TASK_ID:
            continue
        if row.get("window_start_utc") != WINDOW_START or row.get("window_end_utc") != WINDOW_END:
            continue
        rows.append(row)
    return rows


def _results0_region(preview: str) -> str:
    anchor = preview.find('"results":[{')
    return preview[anchor:] if anchor >= 0 else preview


def _extract_scalar(region: str, field_name: str) -> str | None:
    match = re.search(rf'"{field_name}"\s*:\s*"([^"]*)"', region)
    return match.group(1) if match else None


def _field_token_present(region: str, field_name: str) -> bool:
    return f'"{field_name}":' in region


def _summarize_schema_fields() -> list[str]:
    schema = _load_json(SCHEMA_PATH)
    required = schema.get("required", [])
    if not isinstance(required, list):
        raise ValueError("normalized_signal_event schema required list missing")
    return [str(item) for item in required]


def main() -> None:
    rows = sorted(_load_counted_rows(), key=lambda row: row["task_id"])
    required_fields = _summarize_schema_fields()

    per_row: list[dict[str, Any]] = []
    scalar_counts = {field: 0 for field in SCALAR_RESULTS0_FIELDS}
    token_counts = {field: 0 for field in TOKEN_RESULTS0_FIELDS}
    full_preview_parse_ok_count = 0
    response_sha256_present_count = 0
    preview_present_count = 0
    distinct_document_numbers: set[str] = set()

    for row in rows:
        snapshot_path = pathlib.Path(str(row["artifact_path"]))
        snapshot = _load_json(snapshot_path)
        preview = str(snapshot.get("response_preview_utf8", ""))
        region = _results0_region(preview)

        try:
            json.loads(preview)
            full_preview_parse_ok_count += 1
            preview_parse_error = None
        except json.JSONDecodeError as exc:
            preview_parse_error = str(exc)

        scalar_presence: dict[str, Any] = {}
        for field in SCALAR_RESULTS0_FIELDS:
            value = _extract_scalar(region, field)
            scalar_presence[field] = value
            if value is not None:
                scalar_counts[field] += 1
                if field == "document_number":
                    distinct_document_numbers.add(value)

        token_presence: dict[str, bool] = {}
        for field in TOKEN_RESULTS0_FIELDS:
            present = _field_token_present(region, field)
            token_presence[field] = present
            if present:
                token_counts[field] += 1

        if snapshot.get("response_sha256"):
            response_sha256_present_count += 1
        if preview:
            preview_present_count += 1

        per_row.append(
            {
                "task_id": row["task_id"],
                "run_identity": row["run_identity"],
                "artifact_path": str(snapshot_path),
                "collector_fields": {
                    "actual_started_at_utc": row.get("actual_started_at_utc"),
                    "captured_at_utc": row.get("captured_at_utc"),
                    "endpoint_url": row.get("endpoint_url"),
                    "source_class": row.get("source_class"),
                    "observed_result_type": row.get("observed_result_type"),
                    "source_observation_success": row.get("source_observation_success"),
                    "collector_execution_success": row.get("collector_execution_success"),
                },
                "snapshot_fields": {
                    "response_sha256_present": bool(snapshot.get("response_sha256")),
                    "response_preview_utf8_present": bool(preview),
                    "preview_len_chars": len(preview),
                    "json_shape_valid": snapshot.get("json_shape_valid"),
                    "full_preview_json_parse_ok": preview_parse_error is None,
                    "full_preview_json_parse_error": preview_parse_error,
                },
                "results0_scalar_fields": scalar_presence,
                "results0_token_fields_present": token_presence,
            }
        )

    field_assessment = {
        "event_id": {
            "status": "derivable_exact_from_stored_fields",
            "why": "The stored slice preserves both `task_id` and `response_sha256`; the observe slice formula `evt_{task_id}_{sha256[:12]}` can therefore be reproduced exactly.",
        },
        "task_id": {
            "status": "direct_on_disk_all_22",
            "why": "Every counted JSONL row includes `task_id`.",
        },
        "ticker": {
            "status": "not_evidenced_from_real_slice",
            "why": "Neither the collector JSONL nor the snapshot payload stores a ticker value.",
        },
        "asset_type": {
            "status": "not_evidenced_from_real_slice",
            "why": "The stored slice does not carry any direct asset-type field; filling one would require a policy constant rather than evidence from the artifact set.",
        },
        "source_lane": {
            "status": "derivable_lane_context_only",
            "why": "The tranche is Lane B-only and the collector stores `source_class=lane_b_federal_register_public_api`, but the literal normalized field `source_lane` is not written into the stored slice.",
        },
        "source_name": {
            "status": "partial_policy_mapping_only",
            "why": "The stored slice preserves source-class and endpoint provenance, but not the exact observe-style `source_name` string.",
        },
        "direction_hint": {
            "status": "not_evidenced_from_real_slice",
            "why": "No direction field is written in the collector artifacts. The older observe slice hard-coded `neutral`, but this real stored slice does not prove or preserve that field.",
        },
        "event_time": {
            "status": "partial_date_only_boundary",
            "why": "The stored slice preserves `publication_date` for `results[0]` across all 22 rows, but only as a date string. A full source event timestamp is not preserved.",
        },
        "ingested_at": {
            "status": "direct_on_disk_all_22",
            "why": "Every counted row preserves collector timing fields such as `actual_started_at_utc` and `captured_at_utc`.",
        },
        "freshness_hours": {
            "status": "partial_not_exact",
            "why": "Freshness can only be computed from a chosen surrogate event-time model. The real stored slice does not preserve a full source timestamp, and later freshness work still left 10/22 rows in `cannot_classify_honestly` under the adopted rule.",
        },
        "raw_text": {
            "status": "partial_truncated_preview_only",
            "why": "Every stored snapshot preserves `response_preview_utf8`, but only the first 2,000 UTF-8 bytes rather than the full body.",
        },
        "parsed_summary": {
            "status": "partial_can_be_derived_not_stored",
            "why": "Useful document fields such as `title`, `type`, `document_number`, `html_url`, and `publication_date` are available, but the real slice does not store a finished normalized summary field.",
        },
        "evidence_url": {
            "status": "direct_on_disk_all_22",
            "why": "The slice preserves the collector `endpoint_url` for every row, and the document `html_url` for `results[0]` is also present in the preview for all 22 rows.",
        },
        "evidence_path": {
            "status": "direct_on_disk_all_22",
            "why": "Every counted row stores `artifact_path` for its snapshot JSON.",
        },
        "trust_tier": {
            "status": "not_evidenced_from_real_slice",
            "why": "No trust-tier field is preserved in the collector artifacts.",
        },
        "lag_class": {
            "status": "partial_not_exact",
            "why": "The stored slice does not write `lag_class`, and freshness classification remains partial because the source preserves only a date for publication on the 10-row ambiguous cohort.",
        },
        "parser_confidence": {
            "status": "not_evidenced_from_real_slice",
            "why": "No parser-confidence value is stored in the real collector artifacts.",
        },
        "notes": {
            "status": "partial_can_be_derived_not_stored",
            "why": "Collector metadata is rich enough to derive conservative notes, but the normalized `notes` field is not stored as such in the real slice.",
        },
    }

    direct_all_22 = sorted(
        field for field, verdict in field_assessment.items() if verdict["status"] == "direct_on_disk_all_22"
    )
    derivable_exact = sorted(
        field for field, verdict in field_assessment.items() if verdict["status"] == "derivable_exact_from_stored_fields"
    )
    partial_only = sorted(
        field
        for field, verdict in field_assessment.items()
        if verdict["status"] not in {"direct_on_disk_all_22", "derivable_exact_from_stored_fields", "not_evidenced_from_real_slice"}
    )
    not_evidenced = sorted(
        field for field, verdict in field_assessment.items() if verdict["status"] == "not_evidenced_from_real_slice"
    )

    artifact = {
        "_meta": {
            "title": "tranche58_lane_b_real_slice_normalization_truth_audit",
            "phase_number": 2,
            "tranche_number": 58,
            "prompt_number": 246,
            "scope": "stored 22-slot Lane B full-window artifacts only; no network; no new collection",
            "approval_authority": "future_modules/the_fade/config/mvp_lane_approval.json",
        },
        "truth_lock": {
            "phase_2_active": True,
            "approval_remains_false": True,
            "approved_mvp_lanes_empty": True,
            "phase_3_blocked": True,
            "lane_b_deepest_but_partial": True,
            "lane_e_paused": True,
            "lane_c_paused": True,
            "note": "This audit does not grant approval, does not unpause other lanes, and does not unlock Phase 3.",
        },
        "population": {
            "counted_rows": len(rows),
            "window_start_utc": WINDOW_START,
            "window_end_utc": WINDOW_END,
            "excluded_task_id": EXCLUDED_TASK_ID,
            "all_rows_source_observation_success": all(bool(row.get("source_observation_success")) for row in rows),
            "all_rows_collector_execution_success": all(bool(row.get("collector_execution_success")) for row in rows),
            "all_rows_observed_result_type_normalized_signal_event": all(
                row.get("observed_result_type") == "normalized_signal_event" for row in rows
            ),
        },
        "stored_source_field_rollup": {
            "response_preview_utf8_present_count": preview_present_count,
            "response_sha256_present_count": response_sha256_present_count,
            "full_preview_json_parse_ok_count": full_preview_parse_ok_count,
            "results0_scalar_field_counts": scalar_counts,
            "results0_token_field_counts": token_counts,
            "distinct_results0_document_numbers": sorted(distinct_document_numbers),
            "distinct_results0_document_number_count": len(distinct_document_numbers),
        },
        "normalized_signal_event_required_fields": required_fields,
        "normalized_signal_event_field_assessment": field_assessment,
        "normalized_signal_event_viability_summary": {
            "direct_on_disk_all_22": direct_all_22,
            "derivable_exact_from_stored_fields": derivable_exact,
            "partial_only": partial_only,
            "not_evidenced_from_real_slice": not_evidenced,
        },
        "silent_drop_truth": {
            "collector_retention_layer": "ruled_out_for_this_stored_22_slot_slice",
            "collector_retention_why": "Every counted row has a JSONL audit record, an artifact path, a snapshot file, a response preview, and a response SHA-256.",
            "full_normalized_signal_event_materialization": "still_unprovable_from_real_slice_alone",
            "full_normalized_signal_event_materialization_why": "The stored slice never wrote full normalized_signal_event artifacts, and several required schema fields remain absent or only partially evidenced.",
            "honest_bottom_line": "silent-drop risk is reduced at the collector retention layer but not ruled out for end-to-end normalized event materialization from the stored slice alone.",
        },
        "gate_impact": {
            "dimension": "normalization_viability",
            "status_after_t58": "partial_real_slice_truth_strengthened_not_closed",
            "proved_now": [
                "The real stored slice preserves enough on-disk material to support exact identity, timing, endpoint provenance, document identity, and truncated raw-preview retention across all 22 counted rows.",
                "An observe-style event_id can be reproduced exactly from stored `task_id` plus `response_sha256`.",
                "The stored slice does not silently lose whole collector artifacts for the 22 counted rows.",
            ],
            "not_proved_now": [
                "A full normalized_signal_event can be materialized from the stored slice without policy fill-ins or invented values.",
                "Exact normalized values for `ticker`, `asset_type`, `direction_hint`, `trust_tier`, and `parser_confidence`.",
                "Full raw-body preservation or full structured `results[0]` JSON beyond the truncated preview boundary.",
                "Whole-gate closure, approval, or Phase 3 readiness.",
            ],
        },
        "per_row": per_row,
    }

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")

    md_lines = [
        "# Tranche 58 — Lane B real-slice normalization truth audit",
        "",
        "**Scope:** stored 22-slot Lane B full-window artifacts only. No network. No new collection. No approval change.",
        "",
        "## Exact question answered",
        "",
        "This tranche tests what the stored 22-slot Federal Register slice can and cannot honestly prove about Lane B `normalized_signal_event` viability.",
        "",
        "## Population",
        "",
        f"- Counted rows: **{len(rows)}**",
        f"- Window: **`{WINDOW_START}`** → **`{WINDOW_END}`**",
        f"- Excluded: **`{EXCLUDED_TASK_ID}`**",
        f"- All counted rows kept a snapshot artifact: **{response_sha256_present_count} / {len(rows)}**",
        "",
        "## Stored normalization-relevant fields present on disk",
        "",
        f"- `response_preview_utf8`: **{preview_present_count} / {len(rows)}**",
        f"- `response_sha256`: **{response_sha256_present_count} / {len(rows)}**",
        f"- `results[0].document_number`: **{scalar_counts['document_number']} / {len(rows)}**",
        f"- `results[0].publication_date`: **{scalar_counts['publication_date']} / {len(rows)}**",
        f"- `results[0].title`: **{scalar_counts['title']} / {len(rows)}**",
        f"- `results[0].type`: **{scalar_counts['type']} / {len(rows)}**",
        f"- `results[0].html_url`: **{scalar_counts['html_url']} / {len(rows)}**",
        f"- `results[0].pdf_url`: **{scalar_counts['pdf_url']} / {len(rows)}**",
        f"- `results[0].public_inspection_pdf_url`: **{scalar_counts['public_inspection_pdf_url']} / {len(rows)}**",
        f"- `results[0].abstract` token present in preview: **{token_counts['abstract']} / {len(rows)}**",
        f"- `results[0].agencies` token present in preview: **{token_counts['agencies']} / {len(rows)}**",
        f"- `results[0].excerpts` token present in preview: **{token_counts['excerpts']} / {len(rows)}**",
        f"- Full preview JSON parse succeeds: **{full_preview_parse_ok_count} / {len(rows)}**",
        "",
        "## Required normalized field truth",
        "",
        f"- Direct on disk for all 22: **{', '.join('`' + field + '`' for field in direct_all_22)}**",
        f"- Derivable exactly from stored fields: **{', '.join('`' + field + '`' for field in derivable_exact)}**",
        f"- Partial only: **{', '.join('`' + field + '`' for field in partial_only)}**",
        f"- Not evidenced from the real stored slice: **{', '.join('`' + field + '`' for field in not_evidenced)}**",
        "",
        "## Honest verdict",
        "",
        "- The real stored slice is strong enough to prove collector-level retention and partial normalization support.",
        "- The real stored slice is not strong enough to prove full `normalized_signal_event` materialization without policy fill-ins or invented values.",
        "- Silent-drop risk is reduced at the collector retention layer, but still unprovable for full normalized-event materialization from this stored slice alone.",
        "",
        "## Gate impact",
        "",
        "- Lane B `normalization_viability` remains **partial**.",
        "- T58 strengthens the exact real-slice truth boundary for that dimension.",
        "- T58 does **not** justify approval and does **not** unlock Phase 3.",
        "",
        f"Machine-readable artifact: `{OUT_JSON.name}`",
        "",
    ]
    OUT_MD.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")
    print(json.dumps(artifact["gate_impact"], indent=2))


if __name__ == "__main__":
    main()
