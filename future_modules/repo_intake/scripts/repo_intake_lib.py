import base64
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


SUPPORTED_PROFILES = {
    "generic_repo_triage",
    "workflow_tooling",
    "prediction_market_execution",
}


@dataclass
class RepoSnapshot:
    owner: str
    repo: str
    repo_url: str
    metadata: Dict[str, Any]
    root_entries: List[Dict[str, Any]]
    readme_text: str
    languages: Dict[str, int]


class RepoIntakeError(Exception):
    pass


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def new_run_id() -> str:
    """UTC run token for audit-safe artifact names and result bodies."""
    return datetime.now(timezone.utc).strftime("run_%Y%m%d_%H%M%SZ")


def _safe_str(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _safe_description(metadata: Dict[str, Any]) -> str:
    return _safe_str(metadata.get("description"))


def _safe_topics_text(topics: Any) -> str:
    if isinstance(topics, list):
        return " ".join(_safe_str(t) for t in topics)
    return _safe_str(topics)


def parse_github_repo(repo_url: str) -> Tuple[str, str]:
    parsed = urlparse(repo_url.strip())
    if parsed.scheme not in {"http", "https"}:
        raise RepoIntakeError("repo_url must be an http/https URL.")
    if parsed.netloc.lower() != "github.com":
        raise RepoIntakeError("repo_url must point to github.com.")
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 2:
        raise RepoIntakeError("repo_url must include owner and repo name.")
    return parts[0], parts[1].replace(".git", "")


def _http_get_json(url: str) -> Dict[str, Any]:
    req = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "repo-intake-local-tool",
        },
    )
    with urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_repo_snapshot(repo_url: str) -> RepoSnapshot:
    owner, repo = parse_github_repo(repo_url)
    base = f"https://api.github.com/repos/{owner}/{repo}"
    metadata = _http_get_json(base)
    root_entries = _http_get_json(f"{base}/contents")
    languages = _http_get_json(f"{base}/languages")
    readme_text = ""
    try:
        readme_obj = _http_get_json(f"{base}/readme")
        if readme_obj.get("encoding") == "base64" and readme_obj.get("content"):
            readme_text = base64.b64decode(readme_obj["content"]).decode(
                "utf-8", errors="ignore"
            )
    except HTTPError:
        readme_text = ""
    return RepoSnapshot(
        owner=owner,
        repo=repo,
        repo_url=repo_url,
        metadata=metadata,
        root_entries=root_entries if isinstance(root_entries, list) else [],
        readme_text=readme_text,
        languages=languages if isinstance(languages, dict) else {},
    )


def validate_input(input_data: Dict[str, Any], schema: Dict[str, Any]) -> None:
    required = schema.get("required", [])
    props = schema.get("properties", {})

    for field in required:
        if field == "profile":
            continue
        if field not in input_data:
            raise RepoIntakeError(f"Missing required input field: {field}")

    unknown = set(input_data.keys()) - set(props.keys())
    if unknown:
        raise RepoIntakeError(f"Unknown input fields: {sorted(unknown)}")

    profile = str(input_data.get("profile", "") or "").strip()
    if profile and profile.lower() != "auto":
        allowed_profiles = set(props["profile"]["enum"])
        if profile not in allowed_profiles or profile not in SUPPORTED_PROFILES:
            raise RepoIntakeError(
                f"Unsupported profile '{profile}'. Supported: {sorted(SUPPORTED_PROFILES)}"
            )

    note = input_data.get("operator_note", "")
    if not isinstance(note, str) or not note.strip():
        raise RepoIntakeError("operator_note must be a non-empty string.")

    repo_url = input_data.get("repo_url", "")
    pattern = props["repo_url"]["pattern"]
    if not re.match(pattern, repo_url):
        raise RepoIntakeError("repo_url must match a GitHub repository URL pattern.")


def _count_entries(root_entries: List[Dict[str, Any]]) -> Dict[str, int]:
    counts = {"code": 0, "docs": 0, "config": 0, "tests": 0, "dirs": 0}
    code_ext = {
        ".py",
        ".ts",
        ".tsx",
        ".js",
        ".jsx",
        ".go",
        ".rs",
        ".java",
        ".c",
        ".cpp",
        ".cs",
        ".rb",
    }
    doc_names = {"readme.md", "docs", "architecture.md", "contributing.md", "wiki"}
    config_ext = {".json", ".toml", ".yaml", ".yml", ".ini"}

    for entry in root_entries:
        name = str(entry.get("name", "")).lower()
        entry_type = entry.get("type")
        if entry_type == "dir":
            counts["dirs"] += 1
        if "test" in name:
            counts["tests"] += 1
        if name in doc_names or name.endswith(".md"):
            counts["docs"] += 1
        if any(name.endswith(ext) for ext in code_ext):
            counts["code"] += 1
        if any(name.endswith(ext) for ext in config_ext) or name in {
            "dockerfile",
            "makefile",
            "requirements.txt",
            "package.json",
            "pyproject.toml",
        }:
            counts["config"] += 1
    return counts


def _text_contains_any(text: str, terms: List[str]) -> bool:
    low = text.lower()
    return any(t in low for t in terms)


def _fatal_flags(profile: str, text: str, counts: Dict[str, int]) -> List[str]:
    flags: List[str] = []
    hype_terms = ["guaranteed", "100x", "moonshot", "profit machine", "easy money"]
    risk_terms = ["private key", "seed phrase", "api key", "wallet", "secret"]
    mech_terms = ["architecture", "pipeline", "engine", "flow", "strategy"]

    if profile == "generic_repo_triage":
        if _text_contains_any(text, hype_terms) and counts["code"] == 0:
            flags.append("readme_hype_with_weak_code")
        if _text_contains_any(text, risk_terms):
            flags.append("obvious_secret_sloppiness")
        if "pnl" in text.lower() and "proof" in text.lower():
            flags.append("fake_pnl_as_proof")
        if not _text_contains_any(text, mech_terms):
            flags.append("no_clear_mechanism")
        if counts["docs"] >= 3 and counts["code"] == 0:
            flags.append("docs_bundle_masks_thin_repo")

    if profile == "workflow_tooling":
        if _text_contains_any(text, ["mandatory cloud", "hosted only", "cannot self-host"]):
            flags.append("cloud_lockin_disguised_as_utility")
        if _text_contains_any(text, hype_terms) and counts["code"] == 0:
            flags.append("weak_repo_strong_marketing")
        if _text_contains_any(text, ["all-in-one super app", "everything platform"]):
            flags.append("tool_tries_to_be_entire_stack")
        if not _text_contains_any(text, ["review", "triage", "workflow", "operator", "build"]):
            flags.append("no_clear_operator_pain_solved")

    if profile == "prediction_market_execution":
        if _text_contains_any(text, ["copy trade", "copy-trading"]):
            flags.append("copy_trading_main_value_prop")
        if _text_contains_any(text, ["private key", "seed phrase", "plain text key"]):
            flags.append("direct_secret_or_key_sloppiness")
        if not _text_contains_any(text, ["paper", "sim", "simulation", "sandbox"]):
            flags.append("no_paper_mode")
        if not _text_contains_any(text, ["risk", "limit", "kill switch", "max drawdown"]):
            flags.append("no_risk_controls")
        if _text_contains_any(text, ["pnl flex", "profit screenshot"]):
            flags.append("pnl_flex_as_proof")
        if _text_contains_any(text, ["live trade"]) and not _text_contains_any(
            text, ["kill switch", "circuit breaker"]
        ):
            flags.append("live_execution_without_kill_logic")
        if _text_contains_any(text, ["ai makes money", "guaranteed alpha"]):
            flags.append("magical_ai_makes_money_framing")
        if not _text_contains_any(text, ["data", "auth", "execution", "monitoring"]):
            flags.append("no_clear_separation_between_data_auth_execution_and_monitoring")

    return sorted(set(flags))


def _score(snapshot: RepoSnapshot, profile: str) -> Tuple[int, int, int, List[str], List[str], List[str]]:
    desc = _safe_description(snapshot.metadata)
    text = (
        snapshot.readme_text
        + "\n"
        + desc
        + "\n"
        + " ".join(_safe_str(e.get("name")) for e in snapshot.root_entries)
    )
    counts = _count_entries(snapshot.root_entries)
    has_readme = bool(snapshot.readme_text.strip())
    language_count = len(snapshot.languages)
    stars = int(snapshot.metadata.get("stargazers_count", 0))
    updated = str(snapshot.metadata.get("updated_at", ""))

    positives: List[str] = []
    negatives: List[str] = []
    dangers: List[str] = []

    if has_readme:
        positives.append("README exists and provides inspectable context.")
    else:
        negatives.append("README missing or unavailable.")
    if counts["code"] > 0:
        positives.append("Top-level code artifacts are present.")
    else:
        negatives.append("Little or no top-level code surface detected.")
    if counts["config"] > 0:
        positives.append("Config/build files suggest implementable structure.")
    if counts["tests"] > 0:
        positives.append("Test-related files/directories appear present.")
    if language_count > 0:
        positives.append(f"Language footprint detected ({language_count} languages).")
    if stars == 0:
        negatives.append("No social proof from stars; requires evidence-based caution.")
    if "T" in updated:
        positives.append("Repository has a recorded update timestamp.")

    fatal_flags = _fatal_flags(profile, text, counts)
    if fatal_flags:
        dangers.extend([f"Fatal flag: {f}" for f in fatal_flags])

    base_reality = min(50, counts["code"] * 5 + counts["docs"] * 3 + counts["config"] * 3)
    if has_readme:
        base_reality = min(50, base_reality + 6)
    if counts["tests"] > 0:
        base_reality = min(50, base_reality + 4)
    if fatal_flags:
        base_reality = max(0, base_reality - min(15, len(fatal_flags) * 3))

    # Narrow refinement: for prediction-market repos, reward static evidence of
    # concrete execution mechanics and slightly discount polished-wrapper surface.
    if profile == "prediction_market_execution":
        low_text = text.lower()
        root_names = " ".join(str(e.get("name", "")).lower() for e in snapshot.root_entries)
        mechanics_terms = [
            "orderbook",
            "websocket",
            "market making",
            "spread",
            "position",
            "inventory",
            "execution",
            "fill",
            "routing",
            "latency",
            "microstructure",
        ]
        mechanics_hits = sum(1 for term in mechanics_terms if term in low_text)

        root_mechanics_terms = [
            "orderbook",
            "market",
            "maker",
            "execution",
            "strategy",
            "position",
            "engine",
        ]
        root_mechanics_hits = sum(1 for term in root_mechanics_terms if term in root_names)

        if mechanics_hits >= 4:
            base_reality = min(50, base_reality + 8)
        elif mechanics_hits >= 2:
            base_reality = min(50, base_reality + 5)
        elif mechanics_hits == 1:
            base_reality = min(50, base_reality + 2)

        if root_mechanics_hits >= 2:
            base_reality = min(50, base_reality + 2)

        shallow_wrapper = (
            counts["code"] == 0
            and counts["docs"] >= 1
            and counts["config"] >= 1
            and mechanics_hits == 0
        )
        official_surface_without_controls = _text_contains_any(
            low_text,
            ["official", "api client", "agent toolkit", "wrapper", "sdk"],
        ) and not _text_contains_any(
            low_text, ["paper", "simulation", "risk", "replay", "kill switch"]
        )

        if shallow_wrapper:
            base_reality = max(0, base_reality - 4)
        if official_surface_without_controls:
            base_reality = max(0, base_reality - 3)

    base_fit = 10
    if profile == "generic_repo_triage":
        if _text_contains_any(text, ["workflow", "review", "triage", "research", "operator"]):
            base_fit += 12
        if counts["code"] > 1:
            base_fit += 8
        if counts["docs"] > 1:
            base_fit += 6
    elif profile == "workflow_tooling":
        if _text_contains_any(text, ["workflow", "review", "pipeline", "operator", "automation"]):
            base_fit += 16
        if _text_contains_any(text, ["local", "self-host", "offline"]):
            base_fit += 8
        if _text_contains_any(text, ["cloud-only", "mandatory cloud"]):
            base_fit -= 5
    elif profile == "prediction_market_execution":
        if _text_contains_any(text, ["prediction", "orderbook", "market making", "execution"]):
            base_fit += 16
        if _text_contains_any(text, ["risk", "paper", "simulation"]):
            base_fit += 8
        if _text_contains_any(text, ["live", "trade", "arb"]):
            base_fit += 4

    if fatal_flags:
        base_fit -= min(12, len(fatal_flags) * 2)

    our_fit = max(0, min(40, base_fit))

    novelty_terms = ["novel", "new approach", "unusual", "experimental", "research"]
    novelty = 2
    if _text_contains_any(text, novelty_terms):
        novelty += 4
    if language_count >= 3:
        novelty += 2
    if profile == "prediction_market_execution" and _text_contains_any(
        text, ["orderbook", "microstructure", "latency"]
    ):
        novelty += 2
    novelty = max(0, min(10, novelty))

    if not positives:
        positives = ["No clear positive signal found in bounded static pass."]
    if not negatives:
        negatives = ["No major negative signal found in bounded static pass."]

    return base_reality, our_fit, novelty, fatal_flags, positives[:5], negatives[:5] + dangers[:3]


def classify_result(
    repo_reality: int,
    our_fit: int,
    fatal_flags_triggered: List[str],
    thresholds: Dict[str, Any],
) -> str:
    materially = thresholds["materially_useful"]
    marginal = thresholds["marginal"]

    if (
        repo_reality >= materially["min_repo_reality_score"]
        and our_fit >= materially["min_our_fit_score"]
        and not fatal_flags_triggered
    ):
        return "materially_useful"
    if repo_reality >= marginal["min_repo_reality_score"] and our_fit >= marginal["min_our_fit_score"]:
        return "marginal"
    if repo_reality < 12 or our_fit < 8:
        return "reject"
    return "too_fuzzy"


def _confidence(repo_reality: int, our_fit: int, fatal_count: int) -> float:
    raw = (repo_reality / 50.0) * 0.55 + (our_fit / 40.0) * 0.45 - (fatal_count * 0.08)
    return round(max(0.05, min(0.98, raw)), 2)


def _top_files(root_entries: List[Dict[str, Any]]) -> List[str]:
    preferred = []
    keys = ("readme", "docs", "src", "package", "pyproject", "requirements", "docker")
    for e in root_entries:
        name = str(e.get("name", ""))
        low = name.lower()
        if any(k in low for k in keys):
            preferred.append(name)
    if not preferred:
        preferred = [str(e.get("name", "")) for e in root_entries[:5]]
    return preferred[:8]


def _auto_select_profile(snapshot: RepoSnapshot) -> Tuple[str, float, List[str]]:
    repo_name = snapshot.repo.lower()
    description = _safe_description(snapshot.metadata)
    topics_text = _safe_topics_text(snapshot.metadata.get("topics", []))
    root_names = " ".join(_safe_str(e.get("name")) for e in snapshot.root_entries)
    evidence_text = f"{repo_name}\n{description}\n{topics_text}\n{snapshot.readme_text}\n{root_names}".lower()

    workflow_terms = [
        "workflow",
        "triage",
        "review",
        "automation",
        "developer tool",
        "cli",
        "pack repository",
        "codebase",
    ]
    prediction_terms = [
        "prediction",
        "polymarket",
        "kalshi",
        "orderbook",
        "market making",
        "market-making",
        "execution",
        "arb",
        "arbitrage",
        "trading",
        "trading bot",
        "copy trading",
        "copy-trading",
        "copytrading",
        "position",
        "positions",
        "clob",
        "order",
        "microstructure",
    ]
    strong_prediction_terms = [
        "polymarket",
        "kalshi",
        "arbitrage",
        "copy trading",
        "copy-trading",
        "copytrading",
        "trading bot",
        "orderbook",
        "market making",
        "market-making",
        "position",
        "positions",
        "clob",
        "execution",
    ]
    strong_workflow_terms = [
        "repo analysis",
        "indexing",
        "search",
        "memory",
        "context",
        "mcp",
        "developer tool",
        "workflow",
        "review",
        "triage",
    ]

    workflow_hits = [t for t in workflow_terms if t in evidence_text]
    prediction_hits = [t for t in prediction_terms if t in evidence_text]
    strong_prediction_hits = [t for t in strong_prediction_terms if t in evidence_text]
    strong_workflow_hits = [t for t in strong_workflow_terms if t in evidence_text]

    # Hard precedence rule: strong prediction-market signals win over generic tooling.
    if len(strong_prediction_hits) >= 2:
        confidence = min(0.98, 0.64 + (0.05 * len(strong_prediction_hits)))
        reasons = [
            "Strong prediction-market execution signals take precedence.",
            f"Matched strong terms: {', '.join(strong_prediction_hits[:8])}",
        ]
        return "prediction_market_execution", round(confidence, 2), reasons

    if prediction_hits and len(prediction_hits) >= max(2, len(workflow_hits)):
        confidence = min(0.95, 0.55 + (0.06 * len(prediction_hits)))
        reasons = [
            "Detected prediction-market/mechanics keywords.",
            f"Matched terms: {', '.join(prediction_hits[:6])}",
        ]
        return "prediction_market_execution", round(confidence, 2), reasons

    if workflow_hits and len(workflow_hits) >= 2 and len(strong_prediction_hits) == 0:
        confidence = min(0.9, 0.52 + (0.06 * len(workflow_hits)))
        reasons = [
            "Detected workflow/tooling-oriented keywords.",
            f"Matched terms: {', '.join(workflow_hits[:6])}",
        ]
        return "workflow_tooling", round(confidence, 2), reasons

    if strong_workflow_hits and len(strong_workflow_hits) >= 2 and not prediction_hits:
        confidence = min(0.86, 0.52 + (0.05 * len(strong_workflow_hits)))
        reasons = [
            "Detected repo-analysis/workflow helper signals.",
            f"Matched terms: {', '.join(strong_workflow_hits[:6])}",
        ]
        return "workflow_tooling", round(confidence, 2), reasons

    reasons = [
        "No strong profile-specific signal dominance detected.",
        "Falling back to generic first-pass triage profile.",
    ]
    return "generic_repo_triage", 0.5, reasons


def run_repo_intake(
    workspace_root: Path,
    input_data: Dict[str, Any],
    run_id: Optional[str] = None,
) -> Tuple[Dict[str, Any], Path, Path]:
    contracts_dir = workspace_root / "future_modules" / "repo_intake" / "contracts"
    outputs_dir = workspace_root / "future_modules" / "repo_intake" / "outputs"
    reports_dir = workspace_root / "future_modules" / "repo_intake" / "reports"
    outputs_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    effective_run_id = run_id if run_id else new_run_id()

    input_schema = load_json(contracts_dir / "repo_intake_input.schema.json")
    profiles_contract = load_json(contracts_dir / "repo_intake_profiles.json")
    validate_input(input_data, input_schema)

    stop_condition: Optional[str] = None
    try:
        snapshot = fetch_repo_snapshot(input_data["repo_url"])
    except (RepoIntakeError, HTTPError, URLError):
        owner, repo = parse_github_repo(input_data["repo_url"])
        snapshot = RepoSnapshot(
            owner=owner,
            repo=repo,
            repo_url=input_data["repo_url"],
            metadata={},
            root_entries=[],
            readme_text="",
            languages={},
        )
        stop_condition = "repo URL invalid or unreachable"

    requested_profile = str(input_data.get("profile", "") or "").strip()
    auto_requested = (not requested_profile) or requested_profile.lower() == "auto"
    profile_selected_automatically = False
    auto_profile_confidence = 0.0
    auto_profile_reasons: List[str] = []

    if auto_requested:
        profile_selected_automatically = True
        profile, auto_profile_confidence, auto_profile_reasons = _auto_select_profile(snapshot)
    else:
        profile = requested_profile
        auto_profile_confidence = 1.0
        auto_profile_reasons = ["Profile was explicitly provided by operator input."]

    thresholds = profiles_contract["shared_thresholds"]

    if stop_condition:
        repo_reality, our_fit, novelty = 0, 0, 0
        fatal_flags = []
        positives = [
            "Repository URL accepted, but bounded GitHub evidence could not be fetched.",
            "No scoring was performed; this is not a content-based judgment.",
        ]
        negatives = [
            "Triage cannot proceed without reachable metadata/README/root listing from GitHub.",
        ]
        classification = "too_fuzzy"
        confidence = 0.05
    else:
        repo_reality, our_fit, novelty, fatal_flags, positives, negatives = _score(snapshot, profile)
        classification = classify_result(repo_reality, our_fit, fatal_flags, thresholds)
        confidence = _confidence(repo_reality, our_fit, len(fatal_flags))

    escalation_reasons: List[str] = []
    if novelty >= 8 and classification in {"marginal", "too_fuzzy"}:
        escalation_reasons.append("novelty_flag high but fit unclear")
    if classification == "materially_useful" and confidence < 0.55:
        escalation_reasons.append(
            "repo appears materially useful but classification confidence is low"
        )
    if not stop_condition and snapshot.readme_text and len(snapshot.root_entries) == 0:
        escalation_reasons.append("conflicting evidence between README/docs and code")
    if fatal_flags and classification != "reject":
        escalation_reasons.append(
            "fatal flag triggered but repo still appears strategically interesting"
        )

    escalation_triggered = bool(escalation_reasons)
    if stop_condition:
        deeper_review_recommended = False
        escalation_triggered = False
        escalation_reasons = []
    else:
        deeper_review_recommended = classification in {"materially_useful", "marginal"} or escalation_triggered
    status = "triage_complete"
    if not stop_condition and escalation_triggered:
        status = "escalated"
    if not stop_condition and classification == "reject":
        status = "rejected"

    final_disposition = classification
    repo_name = f"{snapshot.owner}/{snapshot.repo}"
    if stop_condition:
        summary_text = (
            "Fetch failed: bounded GitHub evidence could not be retrieved. "
            "This repo was not content-evaluated. Classification is too_fuzzy due to "
            "missing evidence only, not a judgment of repo substance."
        )
    else:
        summary_text = _safe_description(snapshot.metadata) or (
            "Bounded static triage summary only; no runtime execution performed."
        )

    result = {
        "run_id": effective_run_id,
        "repo_url": snapshot.repo_url,
        "repo_name": repo_name,
        "profile_used": profile,
        "profile_selected_automatically": profile_selected_automatically,
        "auto_profile_confidence": auto_profile_confidence,
        "auto_profile_reasons": auto_profile_reasons,
        "summary_of_what_it_is": summary_text,
        "fetch_evaluation_skipped": bool(stop_condition),
        "classification": classification,
        "confidence": confidence,
        "repo_reality_score": repo_reality,
        "our_fit_score": our_fit,
        "novelty_flag": novelty,
        "fatal_flags_triggered": fatal_flags,
        "top_positive_signals": positives,
        "top_negative_signals": negatives,
        "danger_flags": [f"Fatal: {f}" for f in fatal_flags],
        "top_files_to_inspect": _top_files(snapshot.root_entries),
        "best_fit_for_us": (
            "Workflow/operator support"
            if profile in {"generic_repo_triage", "workflow_tooling"}
            else "Pattern extraction for prediction-market execution research"
        ),
        "what_to_steal": [
            "Bounded workflow and scoring patterns",
            "Clear evidence-first repo review mechanics",
        ],
        "what_not_to_steal": [
            "Unbounded autonomous behavior",
            "Any approach requiring direct repo code execution for triage",
        ],
        "deeper_review_recommended": deeper_review_recommended,
        "deeper_review_questions": [
            "What claims require non-execution evidence before deeper review?",
            "Which components are reusable without importing full repo complexity?",
        ],
        "worker_status": status,
        "stop_condition": stop_condition,
        "escalation_triggered": escalation_triggered,
        "escalation_reasons": escalation_reasons,
        "final_disposition": final_disposition,
    }

    slug = f"{snapshot.owner}_{snapshot.repo}_{profile}"
    output_json = outputs_dir / f"{slug}_{effective_run_id}_repo_intake_result.json"
    output_md = reports_dir / f"{slug}_{effective_run_id}_repo_intake_report.md"
    output_json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    output_md.write_text(render_report(result), encoding="utf-8")
    return result, output_json, output_md


def render_report(result: Dict[str, Any]) -> str:
    lines = [
        f"# Repo Intake Report: {result['repo_name']}",
        "",
        f"- Run ID: `{result['run_id']}`",
        f"- Fetch evaluation skipped: {result.get('fetch_evaluation_skipped', False)}",
        f"- Repo URL: {result['repo_url']}",
        f"- Profile: {result['profile_used']}",
        f"- Profile Selected Automatically: {result['profile_selected_automatically']}",
        f"- Auto Profile Confidence: {result['auto_profile_confidence']}",
        f"- Classification: **{result['classification']}**",
        f"- Confidence: {result['confidence']}",
        f"- Repo Reality Score: {result['repo_reality_score']}/50",
        f"- Our Fit Score: {result['our_fit_score']}/40",
        f"- Novelty Flag: {result['novelty_flag']}/10",
        "",
        "## Summary",
        result["summary_of_what_it_is"],
        "",
        "## Auto Profile Reasons",
    ]
    lines.extend([f"- {x}" for x in result["auto_profile_reasons"]])
    lines.extend(
        [
            "",
        "## Positive Signals",
        ]
    )
    lines.extend([f"- {x}" for x in result["top_positive_signals"]])
    lines.append("")
    lines.append("## Negative Signals")
    lines.extend([f"- {x}" for x in result["top_negative_signals"]])
    lines.append("")
    lines.append("## Danger Flags")
    danger = result["danger_flags"] or ["- none observed in bounded static pass"]
    if danger and isinstance(danger[0], str) and danger[0].startswith("- "):
        lines.extend(danger)
    else:
        lines.extend([f"- {x}" for x in danger])
    lines.append("")
    lines.append("## Top Files To Inspect")
    lines.extend([f"- {x}" for x in result["top_files_to_inspect"]])
    lines.append("")
    lines.append("## Disposition")
    lines.append(f"- Final Disposition: **{result['final_disposition']}**")
    lines.append(f"- Worker Status: `{result['worker_status']}`")
    lines.append(f"- Deeper Review Recommended: `{result['deeper_review_recommended']}`")
    if result["stop_condition"] is not None:
        lines.append(f"- Stop Condition: `{result['stop_condition']}`")
    if result["escalation_reasons"]:
        lines.append("- Escalation Reasons:")
        lines.extend([f"  - {x}" for x in result["escalation_reasons"]])
    return "\n".join(lines) + "\n"
