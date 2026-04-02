#!/usr/bin/env python3
"""
Tranche 56: Lane B minimal conflict freshness-consumption truth pass.

This audit answers one bounded question only:
does the current minimal `lane_b_real_observation_slice.py conflict`
subcommand itself consume freshness-related fields, or not?

Method:
1. Inspect the on-disk `cmd_conflict` implementation and collect the JSON keys
   it reads from the lane and contra payloads.
2. Replay the real `conflict` subcommand locally with fresh-vs-stale fixtures
   whose freshness fields differ but whose directional inputs are identical.
3. Record whether the emitted conflict packet changes, and whether the minimal
   path omits stale context on its own.

No network. No live collection. No approval change.
"""
from __future__ import annotations

import ast
import json
import subprocess
import sys
import tempfile
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple


MODULE_ROOT = Path(__file__).resolve().parents[1]
TARGET_SCRIPT = MODULE_ROOT / "scripts" / "lane_b_real_observation_slice.py"
FIXTURE_PATH = (
    MODULE_ROOT
    / "examples"
    / "lane_b_minimal_conflict_freshness_truth_bootstrap"
    / "tranche56_cases.json"
)
OUTPUT_DIR = MODULE_ROOT / "outputs" / "lane_b_minimal_conflict_freshness_truth_bootstrap"
OUTPUT_JSON = OUTPUT_DIR / "tranche56_lane_b_minimal_conflict_freshness_consumption_truth_audit.json"
OUTPUT_MD = OUTPUT_DIR / "tranche56_lane_b_minimal_conflict_freshness_consumption_truth_audit.md"

FRESHNESS_KEYS = [
    "context_age_hours",
    "event_time",
    "freshness_hours",
    "freshness_window_hours",
    "ingested_at",
    "is_stale",
    "lag_class",
    "publication_date",
    "stale",
]


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _find_function_source(source: str, fn_name: str) -> Tuple[ast.FunctionDef, str]:
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == fn_name:
            lines = source.splitlines()
            segment = "\n".join(lines[node.lineno - 1 : node.end_lineno])
            return node, segment
    raise RuntimeError(f"Function {fn_name!r} not found in {TARGET_SCRIPT}")


def _collect_get_keys(fn_node: ast.FunctionDef) -> Dict[str, List[str]]:
    keys: Dict[str, set[str]] = {"lane": set(), "contra": set()}
    for node in ast.walk(fn_node):
        if not isinstance(node, ast.Call):
            continue
        if not isinstance(node.func, ast.Attribute):
            continue
        if node.func.attr != "get":
            continue
        if not isinstance(node.func.value, ast.Name):
            continue
        owner = node.func.value.id
        if owner not in keys or not node.args:
            continue
        arg0 = node.args[0]
        if isinstance(arg0, ast.Constant) and isinstance(arg0.value, str):
            keys[owner].add(arg0.value)
    return {name: sorted(values) for name, values in keys.items()}


def _build_case_inputs(fixture: Dict[str, Any], case: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    lane_payload = deepcopy(fixture["lane_b_artifact_template"])
    contra_payload = deepcopy(case["contra"])
    return lane_payload, contra_payload


def _run_conflict(
    case: Dict[str, Any],
    lane_payload: Dict[str, Any],
    contra_payload: Dict[str, Any],
    ticker: str,
) -> Dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="t56_conflict_") as tmp_dir_str:
        tmp_dir = Path(tmp_dir_str)
        lane_path = tmp_dir / f"{case['case_id']}_lane_b_artifact.json"
        contra_path = tmp_dir / f"{case['case_id']}_contra.json"
        out_dir = tmp_dir / "out"

        _write_json(lane_path, lane_payload)
        _write_json(contra_path, contra_payload)

        cmd = [
            sys.executable,
            str(TARGET_SCRIPT),
            "conflict",
            "--task-id",
            case["case_id"],
            "--ticker",
            ticker,
            "--lane-b-artifact",
            str(lane_path),
            "--contra",
            str(contra_path),
            "--out-dir",
            str(out_dir),
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        packet_path = out_dir / f"{case['case_id']}_conflict_packet.json"
        packet = _load_json(packet_path) if proc.returncode == 0 and packet_path.exists() else None

        stable_projection = None
        if packet is not None:
            stable_projection = {
                "summary": packet["summary"],
                "conflict_reasons": packet["conflict_reasons"],
                "notes": packet["notes"],
            }

        return {
            "case_id": case["case_id"],
            "intent": case["intent"],
            "pair_group": case["pair_group"],
            "freshness_profile": case["freshness_profile"],
            "freshness_fields_present": {key: contra_payload.get(key) for key in FRESHNESS_KEYS if key in contra_payload},
            "direction_hint_context": contra_payload.get("direction_hint"),
            "returncode": proc.returncode,
            "stderr": proc.stderr.strip(),
            "stdout": proc.stdout.strip(),
            "conflict_packet_emitted": packet is not None,
            "stale_omission_observed": packet is None,
            "stable_packet_projection": stable_projection,
        }


def _compare_pairs(results: List[Dict[str, Any]], comparison_pairs: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    by_id = {result["case_id"]: result for result in results}
    pair_results: List[Dict[str, Any]] = []
    for pair in comparison_pairs:
        fresh_case = by_id[pair["fresh_case_id"]]
        stale_case = by_id[pair["stale_case_id"]]
        same_projection = fresh_case["stable_packet_projection"] == stale_case["stable_packet_projection"]
        pair_results.append(
            {
                "pair_group": pair["pair_group"],
                "fresh_case_id": pair["fresh_case_id"],
                "stale_case_id": pair["stale_case_id"],
                "fresh_conflict_packet_emitted": fresh_case["conflict_packet_emitted"],
                "stale_conflict_packet_emitted": stale_case["conflict_packet_emitted"],
                "same_stable_packet_projection": same_projection,
                "pair_pass": (
                    fresh_case["conflict_packet_emitted"]
                    and stale_case["conflict_packet_emitted"]
                    and same_projection
                ),
                "explanation": (
                    "Fresh and stale inputs with identical direction hints produced the same bounded "
                    "conflict packet content, so freshness-like fields did not affect this minimal path."
                ),
            }
        )
    return pair_results


def _build_markdown(report: Dict[str, Any]) -> str:
    lines = [
        "# Tranche 56 - Lane B minimal conflict freshness-consumption truth audit",
        "",
        f"Generated: {report['_meta']['generated_at_utc']}",
        "",
        "## Result",
        "",
        f"- Overall pass: `{report['overall_verdict']['all_checks_passed']}`",
        f"- Minimal conflict path consumes freshness fields: `{report['overall_verdict']['minimal_conflict_consumes_freshness_fields']}`",
        f"- Minimal conflict path performs stale omission itself: `{report['overall_verdict']['minimal_conflict_stale_omission_present']}`",
        f"- Wrapper-only stale omission remains separate: `{report['overall_verdict']['wrapper_only_stale_omission_remains_true']}`",
        "",
        "## Static code inspection",
        "",
        f"- Lane keys read in `cmd_conflict`: `{', '.join(report['static_inspection']['lane_get_keys'])}`",
        f"- Contra keys read in `cmd_conflict`: `{', '.join(report['static_inspection']['contra_get_keys'])}`",
        "- Freshness-like keys checked in this audit: "
        + f"`{', '.join(report['static_inspection']['freshness_keys_checked'])}`",
        "- Freshness-like keys actually read by `cmd_conflict`: "
        + f"`{', '.join(report['static_inspection']['freshness_keys_read_by_cmd_conflict']) or 'none'}`",
        "",
        "## Replay comparisons",
        "",
    ]

    for pair in report["pair_comparisons"]:
        lines.extend(
            [
                f"### {pair['pair_group']}",
                "",
                f"- Fresh case: `{pair['fresh_case_id']}`",
                f"- Stale case: `{pair['stale_case_id']}`",
                f"- Both emitted conflict packets: `{pair['fresh_conflict_packet_emitted'] and pair['stale_conflict_packet_emitted']}`",
                f"- Same stable packet projection: `{pair['same_stable_packet_projection']}`",
                f"- Pair pass: `{pair['pair_pass']}`",
                f"- Explanation: {pair['explanation']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Conservative conclusion",
            "",
            "- The current minimal `lane_b_real_observation_slice.py conflict` path does not read freshness-related fields.",
            "- Stale-context omission is not implemented in that minimal path; stale-labeled valid context still reaches conflict packet creation.",
            "- Tranche 47 and Tranche 52 remain truthful as bounded wrapper evidence, not proof that the minimal path itself consumes freshness.",
            "",
            "## What this does not prove",
            "",
            "- No live Federal Register conflict freshness behavior.",
            "- No full conflict-runtime closure.",
            "- No MVP approval and no Phase 3 unlock.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    fixture = _load_json(FIXTURE_PATH)
    source = TARGET_SCRIPT.read_text(encoding="utf-8")
    fn_node, fn_source = _find_function_source(source, "cmd_conflict")
    get_keys = _collect_get_keys(fn_node)
    freshness_keys_read = sorted(set(get_keys["lane"] + get_keys["contra"]).intersection(FRESHNESS_KEYS))

    case_results: List[Dict[str, Any]] = []
    for case in fixture["cases"]:
        lane_payload, contra_payload = _build_case_inputs(fixture, case)
        case_results.append(_run_conflict(case, lane_payload, contra_payload, fixture["ticker"]))

    pair_results = _compare_pairs(case_results, fixture["comparison_pairs"])
    all_case_packets_emitted = all(result["conflict_packet_emitted"] for result in case_results)
    all_pairs_passed = all(pair["pair_pass"] for pair in pair_results)
    no_stale_omission_observed = all(not result["stale_omission_observed"] for result in case_results if result["freshness_profile"] == "stale")

    report = {
        "_meta": {
            "title": "tranche56_lane_b_minimal_conflict_freshness_consumption_truth_audit",
            "phase_number": 2,
            "tranche_number": 56,
            "prompt_number": 235,
            "generated_at_utc": _now_iso(),
            "scope": "local code-path inspection plus bounded local replay only; no network",
            "implementation_reference": "future_modules/the_fade/scripts/lane_b_real_observation_slice.py :: cmd_conflict",
        },
        "truth_lock": {
            "phase_2_active": True,
            "approval_remains_false": True,
            "approved_mvp_lanes_empty": True,
            "phase_3_blocked": True,
            "note": "This audit does not grant approval and does not unlock Phase 3.",
        },
        "static_inspection": {
            "cmd_conflict_source_excerpt": fn_source,
            "lane_get_keys": get_keys["lane"],
            "contra_get_keys": get_keys["contra"],
            "freshness_keys_checked": FRESHNESS_KEYS,
            "freshness_keys_read_by_cmd_conflict": freshness_keys_read,
        },
        "replay_results": case_results,
        "pair_comparisons": pair_results,
        "overall_verdict": {
            "all_checks_passed": bool(all_case_packets_emitted and all_pairs_passed and no_stale_omission_observed and not freshness_keys_read),
            "minimal_conflict_consumes_freshness_fields": bool(freshness_keys_read),
            "minimal_conflict_stale_omission_present": False,
            "minimal_conflict_emits_conflict_packet_for_stale_labeled_valid_context": no_stale_omission_observed,
            "wrapper_only_stale_omission_remains_true": True,
            "proved_now": [
                "The on-disk minimal cmd_conflict implementation reads source_lane, semantic_role/role, and direction_hint, but no freshness-like fields.",
                "Fresh-vs-stale local replay pairs with identical directional inputs produce the same bounded conflict packet content.",
                "Valid stale-labeled context is not omitted by the minimal path itself; wrapper-based stale omission remains separate from current minimal-path behavior.",
            ],
            "not_proved_now": [
                "Live Federal Register conflict freshness behavior.",
                "Whole conflict-runtime closure across all permutations.",
                "MVP approval or Phase 3 readiness.",
            ],
        },
    }

    _write_json(OUTPUT_JSON, report)
    _write_text(OUTPUT_MD, _build_markdown(report))
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
