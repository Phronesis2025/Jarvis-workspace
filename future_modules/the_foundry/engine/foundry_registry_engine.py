import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple


class FoundryEngineError(Exception):
    pass


SOURCE_TYPE_ENUM = {"article_text", "github_repo", "x_post_brief"}
SOURCE_LANE_ENUM = {"article", "github", "x_post"}
REVIEW_STATUS_ENUM = {"pending", "complete", "failed", "escalated"}
EXTRACTION_STATUS_ENUM = {"not_started", "complete", "failed", "escalated"}
IDEA_KIND_ENUM = {
    "pattern",
    "workflow",
    "component",
    "control",
    "architecture",
    "research_method",
    "data_method",
    "tooling",
}
RECOMMENDATION_ENUM = {"discard", "watchlist", "research_next", "implement_soon", "queue_candidate"}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def is_missing_or_vague(value: Any) -> bool:
    if not isinstance(value, str):
        return True
    cleaned = normalize_text(value)
    if len(cleaned) < 20:
        return True
    vague_markers = {"tbd", "todo", "unclear", "unknown", "n/a", "none", "later"}
    return cleaned in vague_markers


def is_integer_score(value: Any) -> bool:
    return isinstance(value, int) and 0 <= value <= 5


def validate_required_fields(record: Dict[str, Any], required_fields: List[str], object_name: str) -> None:
    missing = [field for field in required_fields if field not in record]
    if missing:
        raise FoundryEngineError(f"{object_name} missing required fields: {missing}")


def validate_enum(value: str, allowed: set, field_name: str) -> None:
    if value not in allowed:
        raise FoundryEngineError(f"Invalid enum value for {field_name}: {value!r}")


def validate_score_fields(candidate: Dict[str, Any]) -> None:
    score_fields = [
        "evidence_strength",
        "transferability",
        "expected_upside",
        "risk_reduction_value",
        "implementation_cost",
        "novelty",
        "dependency_burden",
        "confidence",
    ]
    bad_fields = [field for field in score_fields if not is_integer_score(candidate.get(field))]
    if bad_fields:
        raise FoundryEngineError(
            f"Candidate {candidate.get('candidate_id', '<unknown>')} has invalid 0-5 integer scoring fields: {bad_fields}"
        )


@dataclass
class DedupeResult:
    status: str
    reason: str
    registry_match_id: str


def compute_weighted_score(candidate: Dict[str, Any]) -> Tuple[float, Dict[str, float]]:
    weighted_terms = {
        "evidence_strength": candidate["evidence_strength"] * 0.22,
        "transferability": candidate["transferability"] * 0.18,
        "expected_upside": candidate["expected_upside"] * 0.16,
        "risk_reduction_value": candidate["risk_reduction_value"] * 0.14,
        "implementation_cost_inverted": (5 - candidate["implementation_cost"]) * 0.10,
        "novelty": candidate["novelty"] * 0.08,
        "dependency_burden_inverted": (5 - candidate["dependency_burden"]) * 0.07,
        "confidence": candidate["confidence"] * 0.05,
    }
    raw_sum = sum(weighted_terms.values())
    weighted_score = (raw_sum / 5) * 100
    # Fixed precision for deterministic exports.
    weighted_score = round(weighted_score, 4)
    weighted_terms["raw_sum"] = round(raw_sum, 4)
    weighted_terms["weighted_score"] = weighted_score
    return weighted_score, weighted_terms


def dedupe_candidate(candidate: Dict[str, Any], registry_ideas: List[Dict[str, Any]]) -> DedupeResult:
    duplicate_group_key = candidate.get("duplicate_group_key", "")
    if not isinstance(duplicate_group_key, str) or not duplicate_group_key.strip():
        return DedupeResult("needs_review", "duplicate_group_key missing or blank", "")

    title_sig = normalize_text(candidate.get("title", ""))
    category_sig = normalize_text(candidate.get("category", ""))
    problem_sig = normalize_text(candidate.get("problem_solved", ""))
    pattern_sig = normalize_text(candidate.get("proposed_pattern", ""))

    if not title_sig or not category_sig or not problem_sig or not pattern_sig:
        return DedupeResult("needs_review", "signature fields incomplete for deterministic dedupe", "")

    signature = f"{title_sig}|{category_sig}|{problem_sig}|{pattern_sig}"
    group_key = normalize_text(duplicate_group_key)

    for idea in registry_ideas:
        if normalize_text(str(idea.get("dedupe_key", ""))) == group_key:
            return DedupeResult("match", "matched dedupe_key", idea.get("idea_id", ""))

    for idea in registry_ideas:
        idea_signature = (
            f"{normalize_text(str(idea.get('title', '')))}|"
            f"{normalize_text(str(idea.get('category', '')))}|"
            f"{normalize_text(str(idea.get('canonical_problem', '')))}|"
            f"{normalize_text(str(idea.get('canonical_pattern', '')))}"
        )
        if idea_signature == signature:
            return DedupeResult("match", "matched title/category/problem/pattern signature", idea.get("idea_id", ""))

    if len(group_key) < 6:
        return DedupeResult("needs_review", "duplicate_group_key too weak for deterministic confidence", "")
    return DedupeResult("no_match", "no deterministic match found", "")


def gate_failures(candidate: Dict[str, Any], dedupe: DedupeResult) -> List[str]:
    failures: List[str] = []
    if candidate["evidence_strength"] < 2:
        failures.append("evidence_strength_below_2")
    if candidate["transferability"] < 2:
        failures.append("transferability_below_2")
    if is_missing_or_vague(candidate.get("implementation_implication")):
        failures.append("implementation_implication_missing_or_vague")
    if dedupe.status == "needs_review":
        failures.append("dedupe_incomplete")
    return failures


def anti_hype_reasons(candidate: Dict[str, Any], dedupe: DedupeResult) -> List[str]:
    reasons: List[str] = []
    claim = normalize_text(candidate.get("claim", ""))
    summary = normalize_text(candidate.get("summary", ""))
    quality_notes = " ".join(candidate.get("verification_gaps", [])) if isinstance(candidate.get("verification_gaps"), list) else ""
    noise = normalize_text(quality_notes)

    if "hype" in claim or "hype" in summary:
        reasons.append("mostly_hype")
    if candidate.get("idea_kind") == "tooling" and len(normalize_text(candidate.get("proposed_pattern", ""))) < 20:
        reasons.append("bare_tool_mention")
    if is_missing_or_vague(candidate.get("proposed_pattern")):
        reasons.append("unclear_method")
    if dedupe.status == "needs_review":
        reasons.append("unresolved_duplicate")
    weak_noise_markers = {"weak_source", "low_signal", "noisy"}
    if any(marker in noise for marker in weak_noise_markers):
        reasons.append("weak_source_quality_noise")
    return sorted(set(reasons))


def recommendation_from_score(score: float) -> str:
    if score < 35:
        return "discard"
    if score <= 49:
        return "watchlist"
    if score <= 64:
        return "research_next"
    if score <= 79:
        return "implement_soon"
    return "queue_candidate"


def enforce_caps(base_recommendation: str, gate_failures_list: List[str], anti_hype_list: List[str]) -> Tuple[str, List[str]]:
    applied: List[str] = []
    result = base_recommendation

    severe_gate_failure = any(
        failure in gate_failures_list for failure in ["implementation_implication_missing_or_vague", "dedupe_incomplete"]
    )
    if severe_gate_failure:
        result = "discard"
        applied.append("severe_gate_failure_to_discard")
        return result, applied

    if gate_failures_list and result not in {"discard", "watchlist"}:
        result = "watchlist"
        applied.append("hard_gate_cap_watchlist")

    if anti_hype_list and result not in {"discard", "watchlist"}:
        result = "watchlist"
        applied.append("anti_hype_cap_watchlist")

    return result, applied


def map_recommendation_to_registry_status(recommendation: str) -> str:
    return {
        "discard": "rejected",
        "watchlist": "watchlist",
        "research_next": "research_next",
        "implement_soon": "implement_soon",
        "queue_candidate": "queued",
    }[recommendation]


def read_json(path: Path) -> Any:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def load_registry_ideas(state_root: Path) -> List[Dict[str, Any]]:
    registry_dir = state_root / "registry_ideas"
    items: List[Dict[str, Any]] = []
    if not registry_dir.exists():
        return items
    for json_file in sorted(registry_dir.glob("*.json")):
        loaded = read_json(json_file)
        if isinstance(loaded, dict):
            items.append(loaded)
    return items


SOURCE_REQUIRED_FIELDS = [
    "source_id", "source_type", "source_lane", "input_mode", "title", "raw_input_ref", "processed_output_ref",
    "source_url_or_locator", "source_hash", "ingestion_method", "source_timestamp", "created_at", "reviewer_model",
    "review_version", "extraction_version", "review_status", "extraction_status", "review_summary", "key_claims",
    "quality_flags", "processing_notes", "candidate_ids",
]
CANDIDATE_REQUIRED_FIELDS = [
    "candidate_id", "source_id", "source_lane", "title", "summary", "category", "claim", "implementation_implication",
    "problem_solved", "proposed_pattern", "idea_kind", "confidence", "evidence_strength", "transferability",
    "expected_upside", "risk_reduction_value", "implementation_cost", "novelty", "dependency_burden", "needs_validation",
    "verification_gaps", "duplicate_group_key", "dedupe_confidence", "registry_match_id", "recommendation_state",
    "recommendation_reason", "extraction_method", "created_at",
]


def pick_fields(record: Dict[str, Any], allowed_fields: List[str]) -> Dict[str, Any]:
    return {field: record[field] for field in allowed_fields}


def validate_source_record(source: Dict[str, Any]) -> None:
    validate_required_fields(source, SOURCE_REQUIRED_FIELDS, "Source Record")
    validate_enum(source["source_type"], SOURCE_TYPE_ENUM, "source_type")
    validate_enum(source["source_lane"], SOURCE_LANE_ENUM, "source_lane")
    validate_enum(source["review_status"], REVIEW_STATUS_ENUM, "review_status")
    validate_enum(source["extraction_status"], EXTRACTION_STATUS_ENUM, "extraction_status")


def validate_candidate_idea(candidate: Dict[str, Any]) -> None:
    validate_required_fields(candidate, CANDIDATE_REQUIRED_FIELDS, "Candidate Idea")
    validate_enum(candidate["source_lane"], SOURCE_LANE_ENUM, "source_lane")
    validate_enum(candidate["idea_kind"], IDEA_KIND_ENUM, "idea_kind")
    validate_enum(candidate["recommendation_state"], RECOMMENDATION_ENUM, "recommendation_state")
    validate_score_fields(candidate)
    if not isinstance(candidate.get("dedupe_confidence"), (int, float)) or not (0 <= float(candidate["dedupe_confidence"]) <= 1):
        raise FoundryEngineError(
            f"Candidate {candidate.get('candidate_id', '<unknown>')} has invalid dedupe_confidence (expected 0..1 number)."
        )


def build_registry_idea(candidate: Dict[str, Any], weighted_score: float, breakdown: Dict[str, float], recommendation: str) -> Dict[str, Any]:
    now = utc_now()
    return {
        "idea_id": f"idea_{candidate['candidate_id']}",
        "title": candidate["title"],
        "summary": candidate["summary"],
        "category": candidate["category"],
        "canonical_problem": candidate["problem_solved"],
        "canonical_pattern": candidate["proposed_pattern"],
        "dedupe_key": candidate["duplicate_group_key"],
        "source_refs": [candidate["source_id"]],
        "supporting_source_count": 1,
        "contradicting_source_count": 0,
        "confidence": candidate["confidence"],
        "evidence_strength": candidate["evidence_strength"],
        "transferability": candidate["transferability"],
        "expected_upside": candidate["expected_upside"],
        "risk_reduction_value": candidate["risk_reduction_value"],
        "implementation_cost": candidate["implementation_cost"],
        "novelty": candidate["novelty"],
        "dependency_burden": candidate["dependency_burden"],
        "score_breakdown": breakdown,
        "weighted_score": weighted_score,
        "status": map_recommendation_to_registry_status(recommendation),
        "review_state": "pending_review",
        "promotion_reason": candidate["recommendation_reason"],
        "review_notes": "",
        "implementation_notes": "",
        "dependencies": [],
        "related_ideas": [],
        "queue_eligibility": recommendation == "queue_candidate",
        "queue_reason": "eligible_by_score_and_gates" if recommendation == "queue_candidate" else "not_queue_candidate",
        "first_seen_at": candidate["created_at"],
        "created_at": now,
        "last_updated": now,
    }


def build_queue_item(registry_idea: Dict[str, Any], queue_rank: int) -> Dict[str, Any]:
    now = utc_now()
    return {
        "queue_id": f"queue_{registry_idea['idea_id']}",
        "idea_id": registry_idea["idea_id"],
        "queue_rank": queue_rank,
        "priority_band": "high" if registry_idea["weighted_score"] >= 90 else "medium",
        "why_now": "Scored 80+ with all hard gates passed.",
        "required_resources": [],
        "expected_build_output": "Design/build plan for approved registry idea",
        "owner": "unassigned",
        "operator_approval_state": "pending",
        "approval_notes": "",
        "target_module": "stock_module",
        "effort_estimate": "tbd",
        "dependency_status": "unknown",
        "source_confidence_snapshot": float(registry_idea["confidence"]),
        "success_criteria": ["Operator confirms design intent and acceptance criteria."],
        "next_action": "Operator review",
        "status": "proposed",
        "blockers": [],
        "created_at": now,
        "last_updated": now,
    }


def run_engine(workspace_root: Path, payload: Dict[str, Any]) -> Dict[str, Any]:
    state_root = workspace_root / "future_modules" / "the_foundry" / "state"
    for folder in ["source_records", "candidate_ideas", "registry_ideas", "queue_recommendations", "indexes"]:
        (state_root / folder).mkdir(parents=True, exist_ok=True)

    source_record = payload.get("source_record")
    candidate_ideas = payload.get("candidate_ideas")
    if not isinstance(source_record, dict):
        raise FoundryEngineError("Input must include object field `source_record`.")
    if not isinstance(candidate_ideas, list) or not all(isinstance(item, dict) for item in candidate_ideas):
        raise FoundryEngineError("Input must include array field `candidate_ideas` of objects.")

    validate_source_record(source_record)
    if source_record.get("candidate_ids") != [candidate.get("candidate_id") for candidate in candidate_ideas]:
        raise FoundryEngineError("source_record.candidate_ids must exactly match candidate_ideas[].candidate_id order.")

    existing_registry = load_registry_ideas(state_root)
    processed_candidates: List[Dict[str, Any]] = []
    generated_registry: List[Dict[str, Any]] = []
    generated_queue: List[Dict[str, Any]] = []
    candidate_assessments: List[Dict[str, Any]] = []

    for candidate in candidate_ideas:
        validate_candidate_idea(candidate)
        if candidate["source_id"] != source_record["source_id"]:
            raise FoundryEngineError(f"Candidate {candidate['candidate_id']} source_id mismatch vs source_record.source_id.")
        weighted_score, breakdown = compute_weighted_score(candidate)
        dedupe = dedupe_candidate(candidate, existing_registry + generated_registry)
        failures = gate_failures(candidate, dedupe)
        hype = anti_hype_reasons(candidate, dedupe)

        base = recommendation_from_score(weighted_score)
        recommendation, caps = enforce_caps(base, failures, hype)
        reason_parts = [f"base={base}", f"score={weighted_score}", f"dedupe={dedupe.status}"]
        if failures:
            reason_parts.append("gate_failures=" + ",".join(failures))
        if hype:
            reason_parts.append("anti_hype=" + ",".join(hype))
        if caps:
            reason_parts.append("caps=" + ",".join(caps))

        candidate_clean = pick_fields(candidate, CANDIDATE_REQUIRED_FIELDS)
        candidate_clean["recommendation_state"] = recommendation
        candidate_clean["recommendation_reason"] = " | ".join(reason_parts)
        candidate_clean["registry_match_id"] = dedupe.registry_match_id
        processed_candidates.append(candidate_clean)

        candidate_assessments.append({
            "candidate_id": candidate["candidate_id"],
            "weighted_score": weighted_score,
            "score_breakdown": breakdown,
            "dedupe_result": {
            "status": dedupe.status,
            "reason": dedupe.reason,
            "registry_match_id": dedupe.registry_match_id,
            },
            "gate_failures": failures,
            "anti_hype_reasons": hype,
            "base_recommendation": base,
            "final_recommendation": recommendation,
            "caps_applied": caps,
        })

        registry_idea = build_registry_idea(candidate_clean, weighted_score, breakdown, recommendation)
        generated_registry.append(registry_idea)
        if recommendation == "queue_candidate" and not failures and not hype:
            generated_queue.append(build_queue_item(registry_idea, len(generated_queue) + 1))

    source_path = state_root / "source_records" / f"{source_record['source_id']}.json"
    write_json(source_path, source_record)

    for candidate in processed_candidates:
        write_json(state_root / "candidate_ideas" / f"{candidate['candidate_id']}.json", candidate)

    for registry in generated_registry:
        write_json(state_root / "registry_ideas" / f"{registry['idea_id']}.json", registry)

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    queue_path = state_root / "queue_recommendations" / f"queue_recommendations_{run_id}.json"
    write_json(queue_path, {"run_id": run_id, "items": generated_queue})
    assessment_path = state_root / "indexes" / f"candidate_assessments_{run_id}.json"
    write_json(assessment_path, {"run_id": run_id, "items": candidate_assessments})

    manifest = {
        "run_id": run_id,
        "source_id": source_record["source_id"],
        "counts": {
            "candidate_ideas": len(processed_candidates),
            "registry_ideas_generated": len(generated_registry),
            "queue_recommendations_generated": len(generated_queue),
        },
        "output_paths": {
            "source_record": str(source_path.relative_to(workspace_root)).replace("\\", "/"),
            "candidate_ideas_dir": str((state_root / "candidate_ideas").relative_to(workspace_root)).replace("\\", "/"),
            "registry_ideas_dir": str((state_root / "registry_ideas").relative_to(workspace_root)).replace("\\", "/"),
            "queue_recommendation_file": str(queue_path.relative_to(workspace_root)).replace("\\", "/"),
            "candidate_assessment_file": str(assessment_path.relative_to(workspace_root)).replace("\\", "/"),
        },
    }
    write_json(state_root / "indexes" / "foundry_registry_manifest.json", manifest)
    return manifest
