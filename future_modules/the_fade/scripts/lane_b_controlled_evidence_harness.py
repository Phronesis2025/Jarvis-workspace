#!/usr/bin/env python3
"""
Lane B controlled evidence harness (minimal).

Purpose:
- Provide a bounded, lane-B-only local harness so an operator can execute:
  - LANE_B_STALE_UNAVAILABLE_CONTROLLED_REPLAY_V1
  - LANE_B_CONTEXT_DOMINANCE_ADVERSARIAL_CONFLICT_V1

This is NOT the FADE runtime. It is a minimal evidence harness that:
- accepts operator-provided inputs,
- performs basic validation and explicit rule checks,
- emits a single JSON observation to stdout for copy/paste into MVP_LANE_EVIDENCE_LOG.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Optional, Set


LANE_B_ID = "lane_b_official_disclosure"
CONTEXT_ONLY_SOURCE_ALLOWED = "lane_e_research_swarm_context"
PROTOCOL_A_BEHAVIORS_ALLOWED: Set[str] = {"downgrade", "escalate", "omit"}
PROTOCOL_B_PRECEDENCE_ALLOWED: Set[str] = {"lane_b_remained_primary"}


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_json(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Input file not found: {path}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"Invalid JSON in {path}: {e}")


def _require(d: Dict[str, Any], key: str, where: str) -> Any:
    if key not in d:
        raise SystemExit(f"Missing required field `{key}` in {where}")
    return d[key]


def _is_iso8601(s: str) -> bool:
    try:
        datetime.fromisoformat(s.replace("Z", "+00:00"))
        return True
    except Exception:
        return False


@dataclass(frozen=True)
class Observation:
    protocol: str
    observed_at: str
    lane_id: str
    result: Dict[str, Any]
    notes: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "_meta": {
                "title": "lane_b_controlled_evidence_observation",
                "harness": "lane_b_controlled_evidence_harness",
                "protocol": self.protocol,
            },
            "observed_at": self.observed_at,
            "lane_id": self.lane_id,
            "result": self.result,
            "notes": self.notes,
        }


def _reject_unknown_keys(obj: Dict[str, Any], allowed_keys: Set[str], where: str) -> None:
    unknown = set(obj.keys()) - allowed_keys
    if unknown:
        unknown_sorted = ", ".join(sorted(unknown))
        allowed_sorted = ", ".join(sorted(allowed_keys))
        raise SystemExit(f"Unknown field(s) in {where}: {unknown_sorted}. Allowed: {allowed_sorted}")


def _require_str(d: Dict[str, Any], key: str, where: str) -> str:
    v = _require(d, key, where)
    if not isinstance(v, str) or not v.strip():
        raise SystemExit(f"`{key}` must be a non-empty string in {where}")
    return v


def _require_iso8601_str(d: Dict[str, Any], key: str, where: str) -> str:
    v = _require_str(d, key, where)
    if not _is_iso8601(v):
        raise SystemExit(f"`{key}` must be ISO8601 string in {where}")
    return v


def _require_enum(d: Dict[str, Any], key: str, allowed: Set[str], where: str) -> str:
    v = _require_str(d, key, where)
    if v not in allowed:
        raise SystemExit(f"`{key}` must be one of: {', '.join(sorted(allowed))} (in {where})")
    return v


def _bounded_text(s: str, *, where: str, field: str, max_len: int) -> str:
    if "\n" in s or "\r" in s:
        raise SystemExit(f"`{field}` in {where} must be single-line text (no newlines)")
    s2 = s.strip()
    if not s2:
        raise SystemExit(f"`{field}` in {where} must be non-empty text")
    if len(s2) > max_len:
        raise SystemExit(f"`{field}` in {where} is too long (max {max_len} chars)")
    return s2


def _fingerprint(payload: Dict[str, Any]) -> str:
    # Canonicalize to prevent whitespace/ordering smuggling.
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def run_protocol_a(evidence: Dict[str, Any], scenario: Dict[str, Any]) -> Observation:
    """
    Protocol A: controlled stale/unavailable incident replay.

    This harness does NOT fetch any real data. It records outcomes based on operator inputs:
    - evidence item timestamp
    - scenario definitions and explicitly declared observed behavior
    """
    if not isinstance(evidence, dict):
        raise SystemExit("lane_b_evidence must be a JSON object")
    if not isinstance(scenario, dict):
        raise SystemExit("protocol_a_scenario must be a JSON object")

    _reject_unknown_keys(evidence, {"_meta", "lane_id", "evidence_item_timestamp"}, "lane_b_evidence")
    _reject_unknown_keys(
        scenario,
        {"_meta", "stale_window_definition", "unavailable_condition_definition", "observed_behavior"},
        "protocol_a_scenario",
    )

    lane_id = _require_str(evidence, "lane_id", "lane_b_evidence")
    if lane_id != LANE_B_ID:
        raise SystemExit(f"lane_id must be `{LANE_B_ID}` for this harness, got `{lane_id}`")

    evidence_item_timestamp = _require_iso8601_str(evidence, "evidence_item_timestamp", "lane_b_evidence")

    stale_window_definition = _bounded_text(
        _require_str(scenario, "stale_window_definition", "protocol_a_scenario"),
        where="protocol_a_scenario",
        field="stale_window_definition",
        max_len=160,
    )
    unavailable_condition_definition = _bounded_text(
        _require_str(scenario, "unavailable_condition_definition", "protocol_a_scenario"),
        where="protocol_a_scenario",
        field="unavailable_condition_definition",
        max_len=160,
    )
    observed_behavior = _require_enum(
        scenario, "observed_behavior", PROTOCOL_A_BEHAVIORS_ALLOWED, "protocol_a_scenario"
    )

    # Constrained output: only protocol-bounded fields are emitted.
    result = {
        "scenario_name": "LANE_B_STALE_UNAVAILABLE_CONTROLLED_REPLAY_V1",
        "evidence_item_timestamp": evidence_item_timestamp,
        "stale_window_definition": stale_window_definition,
        "unavailable_condition_definition": unavailable_condition_definition,
        "observed_behavior": observed_behavior,
        "input_fingerprint": _fingerprint(
            {
                "lane_id": lane_id,
                "evidence_item_timestamp": evidence_item_timestamp,
                "stale_window_definition": stale_window_definition,
                "unavailable_condition_definition": unavailable_condition_definition,
                "observed_behavior": observed_behavior,
            }
        ),
    }

    return Observation(
        protocol="LANE_B_STALE_UNAVAILABLE_CONTROLLED_REPLAY_V1",
        observed_at=_now_iso(),
        lane_id=LANE_B_ID,
        result=result,
        notes="Harness output is constrained to protocol-bounded fields; no external data was fetched. This is not an approval statement.",
    )


def run_protocol_b(primary: Dict[str, Any], context_only: Dict[str, Any], scenario: Dict[str, Any]) -> Observation:
    """
    Protocol B: context dominance adversarial/conflict-case.

    Operator provides:
    - primary (lane B) asserted truth
    - context-only asserted contradictory truth
    - an explicit precedence_result statement
    Harness validates lane_id and required fields exist and emits observation.
    """
    if not isinstance(primary, dict):
        raise SystemExit("lane_b_primary must be a JSON object")
    if not isinstance(context_only, dict):
        raise SystemExit("context_only must be a JSON object")
    if not isinstance(scenario, dict):
        raise SystemExit("protocol_b_scenario must be a JSON object")

    _reject_unknown_keys(primary, {"_meta", "lane_id", "evidence_item_timestamp"}, "lane_b_primary_truth")
    _reject_unknown_keys(context_only, {"_meta", "source", "evidence_item_timestamp"}, "context_only_signal")
    _reject_unknown_keys(scenario, {"_meta", "conflict_description", "precedence_result"}, "protocol_b_scenario")

    lane_id = _require_str(primary, "lane_id", "lane_b_primary_truth")
    if lane_id != LANE_B_ID:
        raise SystemExit(f"lane_id must be `{LANE_B_ID}` for this harness, got `{lane_id}`")

    primary_ts = _require_iso8601_str(primary, "evidence_item_timestamp", "lane_b_primary_truth")
    context_source = _require_str(context_only, "source", "context_only_signal")
    if context_source != CONTEXT_ONLY_SOURCE_ALLOWED:
        raise SystemExit(
            f"`source` in context_only_signal must be `{CONTEXT_ONLY_SOURCE_ALLOWED}` (context-only), got `{context_source}`"
        )
    context_ts = _require_iso8601_str(context_only, "evidence_item_timestamp", "context_only_signal")

    conflict_description = _bounded_text(
        _require_str(scenario, "conflict_description", "protocol_b_scenario"),
        where="protocol_b_scenario",
        field="conflict_description",
        max_len=200,
    )
    precedence_result = _require_enum(
        scenario, "precedence_result", PROTOCOL_B_PRECEDENCE_ALLOWED, "protocol_b_scenario"
    )

    observed_at = _now_iso()
    result = {
        "scenario_name": "LANE_B_CONTEXT_DOMINANCE_ADVERSARIAL_CONFLICT_V1",
        "primary_truth_source": "lane_b_official_disclosure",
        "context_only_source": context_source,
        "conflict_description": conflict_description,
        "precedence_result": precedence_result,
        "primary_evidence_item_timestamp": primary_ts,
        "context_only_evidence_item_timestamp": context_ts,
        "input_fingerprint": _fingerprint(
            {
                "lane_id": lane_id,
                "primary_evidence_item_timestamp": primary_ts,
                "context_only_source": context_source,
                "context_only_evidence_item_timestamp": context_ts,
                "conflict_description": conflict_description,
                "precedence_result": precedence_result,
            }
        ),
    }

    return Observation(
        protocol="LANE_B_CONTEXT_DOMINANCE_ADVERSARIAL_CONFLICT_V1",
        observed_at=observed_at,
        lane_id=LANE_B_ID,
        result=result,
        notes="Harness output is constrained to protocol-bounded fields; no external data was fetched. This is not an approval statement.",
    )


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Lane B controlled evidence harness (minimal)")
    p.add_argument("--protocol", required=True, choices=["A", "B"], help="Protocol A (stale/unavailable) or B (context dominance)")
    p.add_argument("--lane-b-evidence", type=Path, help="JSON file for lane B evidence item (Protocol A)")
    p.add_argument("--protocol-a-scenario", type=Path, help="JSON scenario file (Protocol A)")
    p.add_argument("--lane-b-primary", type=Path, help="JSON primary truth (lane B) (Protocol B)")
    p.add_argument("--context-only", type=Path, help="JSON context-only truth (Protocol B)")
    p.add_argument("--protocol-b-scenario", type=Path, help="JSON scenario file (Protocol B)")

    args = p.parse_args(argv)

    if args.protocol == "A":
        if not args.lane_b_evidence or not args.protocol_a_scenario:
            raise SystemExit("Protocol A requires --lane-b-evidence and --protocol-a-scenario")
        evidence = _load_json(args.lane_b_evidence)
        scenario = _load_json(args.protocol_a_scenario)
        obs = run_protocol_a(evidence, scenario)
    else:
        if not args.lane_b_primary or not args.context_only or not args.protocol_b_scenario:
            raise SystemExit("Protocol B requires --lane-b-primary, --context-only, and --protocol-b-scenario")
        primary = _load_json(args.lane_b_primary)
        context_only = _load_json(args.context_only)
        scenario = _load_json(args.protocol_b_scenario)
        obs = run_protocol_b(primary, context_only, scenario)

    json.dump(obs.to_dict(), sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

