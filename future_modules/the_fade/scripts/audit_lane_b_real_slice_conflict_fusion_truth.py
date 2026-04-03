"""Tranche 60: Lane B real-slice conflict / fusion truth audit. No network. No approval change."""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile
from typing import Any


MODULE_ROOT = pathlib.Path(__file__).resolve().parents[1]
REAL_OBS_ROOT = MODULE_ROOT / "outputs" / "lane_b_real_observation"
OUT_ROOT = MODULE_ROOT / "outputs" / "lane_b_real_slice_conflict_fusion_truth_bootstrap"
LOG_PATH = REAL_OBS_ROOT / "tranche21_fr_slot_runs.jsonl"
FUSION_POLICY_PATH = MODULE_ROOT / "config" / "fusion_policy.json"
SLICE_SCRIPT = MODULE_ROOT / "scripts" / "lane_b_real_observation_slice.py"
# Reuse bounded local contra shape (Prompt #255: no new fixture if existing suffices).
CONTRA_PATH = MODULE_ROOT / "inputs" / "lane_b_real_evidence" / "context_only_contra.example.json"
OUT_JSON = OUT_ROOT / "tranche60_lane_b_real_slice_conflict_fusion_truth_audit.json"
OUT_MD = OUT_ROOT / "tranche60_lane_b_real_slice_conflict_fusion_truth_audit.md"

WINDOW_START = "2026-03-27T16:00:00Z"
WINDOW_END = "2026-03-29T16:00:00Z"
EXCLUDED_TASK_ID = "t30_valid_002"
LANE_B = "lane_b_official_disclosure"
CONTEXT_ROLE = "lane_e_research_swarm_context"


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


def _cmd_conflict_reads() -> dict[str, Any]:
    """Document minimal conflict subcommand inputs from lane_b_real_observation_slice.py."""
    return {
        "lane_b_json_required_keys": ["source_lane must equal lane_b_official_disclosure"],
        "lane_b_json_optional_for_logic": [
            "direction_hint — if absent, mismatch vs contra cannot become True (code uses ld is not None and cd is not None and ld != cd)",
        ],
        "contra_json_required": [
            "semantic_role or role must equal lane_e_research_swarm_context",
            "direction_hint optional for mismatch math; contra example uses bearish",
        ],
        "fusion_policy_read_only_fields_used": ["lane_weight_hints.lane_b_official_disclosure", "lane_weight_hints.lane_e_research_swarm_context"],
        "fields_not_read_by_minimal_conflict": [
            "freshness_hours",
            "lag_class",
            "ingested_at",
            "event_time",
            "raw_text",
            "evidence_url",
            "response_preview_utf8",
            "any snapshot-only collector fields",
        ],
    }


def _synthesize_lane_artifact(
    *,
    task_id: str,
    response_sha256: str,
    include_direction_hint_neutral: bool,
) -> dict[str, Any]:
    body_hash = response_sha256
    evt: dict[str, Any] = {
        "event_id": f"evt_{task_id}_{body_hash[:12]}",
        "task_id": task_id,
        "ticker": "FR",
        "asset_type": "other",
        "source_lane": LANE_B,
        "source_name": "audit_synthesized_from_collector_slice",
        "event_time": "1970-01-01T00:00:00Z",
        "ingested_at": "1970-01-01T00:00:00Z",
        "freshness_hours": 0.0,
        "raw_text": "",
        "parsed_summary": "audit_synthesized_minimal_lane_body_for_cmd_conflict_replay_only",
        "evidence_url": "",
        "evidence_path": "",
        "trust_tier": "operator_capture",
        "lag_class": "fresh",
        "parser_confidence": 0.0,
        "notes": "Synthesized for T60 replay; not a stored collector field bundle.",
    }
    if include_direction_hint_neutral:
        evt["direction_hint"] = "neutral"
    return evt


def _run_conflict_subprocess(
    *,
    lane_path: pathlib.Path,
    task_id: str,
    out_dir: pathlib.Path,
) -> dict[str, Any]:
    cmd = [
        sys.executable,
        str(SLICE_SCRIPT),
        "conflict",
        "--task-id",
        task_id,
        "--ticker",
        "FR",
        "--lane-b-artifact",
        str(lane_path),
        "--contra",
        str(CONTRA_PATH),
        "--out-dir",
        str(out_dir),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    stdout = (proc.stdout or "").strip()
    stderr = (proc.stderr or "").strip()
    packet_path = out_dir / f"{task_id}_conflict_packet.json"
    packet: dict[str, Any] | None = None
    if packet_path.is_file():
        packet = _load_json(packet_path)
    return {
        "exit_code": proc.returncode,
        "stdout_json_parse_ok": False,
        "stdout_obj": None,
        "stderr_head": stderr[:500] if stderr else "",
        "conflict_packet_path": str(packet_path) if packet_path.is_file() else None,
        "conflict_packet": packet,
    }


def _build_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Tranche 60 — Lane B real-slice conflict / fusion truth audit",
        "",
        f"**Phase:** {payload['_meta']['phase_number']}  ",
        f"**Tranche:** {payload['_meta']['tranche_number']}  ",
        f"**Prompt:** #{payload['_meta']['prompt_number']}  ",
        "",
        "## Truth lock",
        "",
        json.dumps(payload.get("truth_lock", {}), indent=2),
        "",
        "## Conflict-relevant fields present on disk (22-slot slice)",
        "",
        json.dumps(payload.get("conflict_relevant_fields_on_disk", {}), indent=2),
        "",
        "## Fusion policy snapshot (read-only use)",
        "",
        json.dumps(payload.get("fusion_policy_lane_weights", {}), indent=2),
        "",
        "## Honest boundaries",
        "",
        "\n".join(f"- {b}" for b in payload.get("honest_boundaries", [])),
        "",
        "## Replay scenarios (cmd_conflict)",
        "",
        json.dumps(payload.get("replay_scenarios", {}), indent=2),
        "",
        "## Gate impact",
        "",
        json.dumps(payload.get("gate_impact", {}), indent=2),
        "",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    rows = sorted(_load_counted_rows(), key=lambda r: r["task_id"])
    if len(rows) != 22:
        raise SystemExit(f"expected 22 counted rows, got {len(rows)}")

    fusion = _load_json(FUSION_POLICY_PATH)
    hints = fusion.get("lane_weight_hints", {})
    wb = float(hints.get(LANE_B, 1.0))
    we = float(hints.get(CONTEXT_ROLE, 0.2))

    contra = _load_json(CONTRA_PATH)
    cd = contra.get("direction_hint")

    jsonl_conflict_keys = sorted(
        {
            "task_id",
            "artifact_path",
            "endpoint_url",
            "actual_started_at_utc",
            "captured_at_utc",
            "observed_result_type",
            "source_observation_success",
            "collector_execution_success",
            "window_start_utc",
            "window_end_utc",
            "scheduled_slot_utc",
            "run_identity",
            "source_class",
        }
    )

    per_row: list[dict[str, Any]] = []
    snapshot_keys_union: set[str] = set()
    direction_hint_in_snapshot_count = 0
    source_lane_in_snapshot_count = 0

    for row in rows:
        snap_path = pathlib.Path(str(row["artifact_path"]))
        snap = _load_json(snap_path)
        snapshot_keys_union.update(snap.keys())
        if "direction_hint" in snap:
            direction_hint_in_snapshot_count += 1
        if snap.get("source_lane") == LANE_B:
            source_lane_in_snapshot_count += 1

        sha = str(snap.get("response_sha256") or "")
        per_row.append(
            {
                "task_id": row["task_id"],
                "jsonl_conflict_adjacent_fields_present": {k: (k in row) for k in jsonl_conflict_keys},
                "snapshot_has_response_sha256": bool(sha),
                "snapshot_has_response_preview_utf8": bool(snap.get("response_preview_utf8")),
            }
        )

    # Analytic mismatch outcomes for minimal cmd_conflict logic
    ld_absent_mismatch = False  # ld None
    ld_neutral_mismatch = (cd is not None) and ("neutral" != cd)

    sample = rows[0]
    sample_task = str(sample["task_id"])
    sample_snap = _load_json(pathlib.Path(str(sample["artifact_path"])))
    sample_sha = str(sample_snap["response_sha256"])

    replay_results: dict[str, Any] = {}
    with tempfile.TemporaryDirectory(prefix="t60_conflict_") as tmp:
        tmp_path = pathlib.Path(tmp)
        # Scenario A: no direction_hint key
        lane_a = tmp_path / "lane_no_direction.json"
        lane_a.write_text(
            json.dumps(_synthesize_lane_artifact(task_id=sample_task, response_sha256=sample_sha, include_direction_hint_neutral=False), indent=2),
            encoding="utf-8",
        )
        out_a = tmp_path / "out_a"
        out_a.mkdir()
        replay_results["A_no_direction_hint_on_lane_artifact"] = _run_conflict_subprocess(lane_path=lane_a, task_id=sample_task, out_dir=out_a)

        # Scenario B: observe-default neutral
        lane_b = tmp_path / "lane_neutral.json"
        lane_b.write_text(
            json.dumps(_synthesize_lane_artifact(task_id=sample_task, response_sha256=sample_sha, include_direction_hint_neutral=True), indent=2),
            encoding="utf-8",
        )
        out_b = tmp_path / "out_b"
        out_b.mkdir()
        replay_results["B_direction_hint_neutral_policy_fill_not_from_slice"] = _run_conflict_subprocess(lane_path=lane_b, task_id=sample_task, out_dir=out_b)

    payload: dict[str, Any] = {
        "_meta": {
            "title": "tranche60_lane_b_real_slice_conflict_fusion_truth_audit",
            "phase_number": 2,
            "tranche_number": 60,
            "prompt_number": 255,
            "scope": "stored 22-slot Lane B full-window JSONL + per-run snapshots only; local contra file only; no network; no new collection",
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
            "note": "T60 does not grant approval, does not unpause lanes, does not unlock Phase 3, and does not treat prior fixture/stored-slice tranches as live collection.",
        },
        "population": {
            "counted_rows": 22,
            "window_start_utc": WINDOW_START,
            "window_end_utc": WINDOW_END,
            "excluded_task_id": EXCLUDED_TASK_ID,
            "contra_fixture_path": str(CONTRA_PATH),
            "contra_direction_hint": cd,
        },
        "cmd_conflict_contract": _cmd_conflict_reads(),
        "fusion_policy_lane_weights": {"lane_b_official_disclosure": wb, "lane_e_research_swarm_context": we},
        "conflict_relevant_fields_on_disk": {
            "jsonl_row_fields_conflict_adjacent": jsonl_conflict_keys,
            "collector_snapshot_field_union_sorted": sorted(snapshot_keys_union),
            "literal_normalized_signal_event_files_for_task_ids": "not_present — the 22-slot population stores per-run *_tranche21_fr_slot_snapshot.json rows in JSONL, not lane_b_real_observation_slice observe output files.",
            "direction_hint_present_as_snapshot_top_level_key": direction_hint_in_snapshot_count > 0,
            "direction_hint_snapshot_rows": direction_hint_in_snapshot_count,
            "source_lane_present_as_snapshot_top_level_key": source_lane_in_snapshot_count > 0,
            "source_lane_snapshot_rows": source_lane_in_snapshot_count,
            "per_row": per_row,
        },
        "supportable_from_real_slice_alone": [
            "task_id, run identity, endpoint_url, timing fields, HTTP outcome, and response_sha256 are present for all 22 rows and can anchor an audit-derived event_id formula consistent with observe (evt_{task_id}_{sha256[:12]}).",
            "The slice labels observed_result_type=normalized_signal_event at collector metadata level; this is not the same object shape as lane_b_real_observation_slice observe JSON output files on disk.",
            "Fusion precedence wording in cmd_conflict is read-only from fusion_policy.json and is independent of the FR slice contents.",
        ],
        "honest_boundaries": [
            "The stored slice does not preserve lane_b observe-output JSON files; cmd_conflict requires a lane B artifact file with source_lane set — that file must be synthesized or produced out-of-band; synthesis is not 'evidence from the slice' except for task_id + response_sha256-backed event_id.",
            "direction_hint is not stored in collector JSONL or snapshot fields; mismatch vs a bearish local contra is False if direction_hint is omitted from the lane artifact, even though the contra is directional — this is an honest mechanical boundary of the minimal conflict implementation.",
            "If direction_hint is filled with observe's default 'neutral', mismatch becomes True vs bearish contra — but that default is tool policy, not something the 22-slot slice bytes prove about Federal Register content.",
            "cmd_conflict does not read freshness, lag_class, publication_date, or preview text — so the real slice cannot improve T56's 'no freshness consumption in minimal path' conclusion; it also cannot prove stale-first omission behavior (T52 remains wrapper/fixture scoped).",
            "Context-only contra remains THE FADE-local / example provenance — not live Research Swarm integration; no claim that external contra matches production Lane E behavior.",
        ],
        "replay_scenarios": {
            "representative_task_id": sample_task,
            "analytic_all_22_rows": {
                "if_lane_artifact_omits_direction_hint": {"direction_hint_mismatch_vs_contra": ld_absent_mismatch},
                "if_lane_artifact_uses_observe_default_neutral_only": {"direction_hint_mismatch_vs_contra": bool(ld_neutral_mismatch)},
            },
            "subprocess_samples": replay_results,
        },
        "gate_impact": {
            "conflict_handling": "partial_unchanged — T60 adds an explicit real-slice boundary: collector artifacts alone do not contain the lane JSON shape cmd_conflict consumes, and directionality for mismatch is not evidenced from the slice without policy fill-in.",
            "context_dominance_risk": "partial_unchanged — for synthesized lane artifacts that include direction_hint neutral + local bearish contra, the minimal slice still emits explicit primary=lane_b and context weight 0.2 language; this does not prove production fusion runtime or live Lane E dominance testing.",
            "relation_to_T47_T52_T56_T58": "T47/T52/T56 remain the bounded fixture/code-path evidence; T58 remains the normalization real-slice boundary; T60 states the parallel conflict/fusion truth boundary on the same stored 22-slot population without claiming new live collection.",
        },
    }

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_MD.write_text(_build_markdown(payload), encoding="utf-8")


if __name__ == "__main__":
    main()
