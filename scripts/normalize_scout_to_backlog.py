from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

DEFAULT_RULES_FILENAME = "scout_noise_rules.json"
DEFAULT_RESULTS_FILENAME = "public_scout_results.json"
DEFAULT_REPORT_FILENAME = "scout_normalizer_report.json"

BACKLOG_COLUMNS = [
    ("task_id", "Task ID"),
    ("project", "Project"),
    ("bucket", "Bucket"),
    ("priority", "Priority"),
    ("risk", "Risk"),
    ("status", "Status"),
    ("title", "Title"),
    ("notes", "Notes"),
]

STOPWORDS = {
    "source",
    "label",
    "family",
    "screenshot",
    "typeerror",
    "the",
    "and",
    "for",
    "with",
    "that",
    "this",
    "from",
    "into",
    "page",
    "public",
    "route",
    "scout",
    "detected",
    "request",
    "requests",
    "console",
    "errors",
    "error",
    "failed",
    "failure",
    "initial",
    "load",
    "because",
    "already",
    "exists",
    "issue",
    "issues",
    "localhost",
    "http",
    "https",
    "status",
    "visible",
    "text",
    "empty",
    "body",
    "title",
    "networkidle",
    "timed",
    "out",
    "page",
    "rendered",
    "but",
    "contained",
    "no",
    "summary",
    "all",
    "same",
    "origin",
}


class NormalizerError(Exception):
    pass


def now_local() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise NormalizerError(f"JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise NormalizerError(f"Invalid JSON in {path}: {exc}") from exc


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def escape_md(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def render_master_backlog_md(backlog_items: list[dict[str, Any]]) -> str:
    lines = ["# MASTER_BACKLOG", ""]
    header = "| " + " | ".join(label for _, label in BACKLOG_COLUMNS) + " |"
    divider = "|" + "|".join(["---"] * len(BACKLOG_COLUMNS)) + "|"
    lines.append(header)
    lines.append(divider)
    for item in backlog_items:
        row = [escape_md(item.get(key, "")) for key, _ in BACKLOG_COLUMNS]
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")
    return "\n".join(lines)


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip().lower())


def safe_slug(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", normalize_text(text))
    return slug.strip("-") or "signal"


def latest_scout_results_path(workspace: Path) -> Path:
    scout_root = workspace / "logs" / "wcs_scout"
    if not scout_root.exists():
        raise NormalizerError(f"Scout log directory not found: {scout_root}")

    candidates = sorted(
        [p for p in scout_root.glob("*/public_scout_results.json") if p.is_file()],
        key=lambda p: p.parent.name,
        reverse=True,
    )
    if not candidates:
        raise NormalizerError(f"No {DEFAULT_RESULTS_FILENAME} files found under {scout_root}")
    return candidates[0]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize WCS scout failures into backlog-ready tasks while filtering known noise."
    )
    parser.add_argument("--workspace", help="Workspace root path. Defaults to script grandparent directory.")
    parser.add_argument("--results", help="Path to public_scout_results.json. Defaults to latest scout run in workspace logs.")
    parser.add_argument("--backlog", help="Path to master_backlog.json. Defaults to workspace/state/master_backlog.json")
    parser.add_argument("--md", help="Path to MASTER_BACKLOG.md. Defaults to workspace/state/MASTER_BACKLOG.md")
    parser.add_argument("--rules", help=f"Path to {DEFAULT_RULES_FILENAME}. Defaults to workspace/config/{DEFAULT_RULES_FILENAME}")
    parser.add_argument("--output", help="Path to output normalization report JSON. Defaults next to the scout results file.")
    parser.add_argument("--dry-run", action="store_true", help="Do not modify backlog files. Still writes the normalization report.")
    return parser.parse_args()


def load_rules(path: Path) -> dict[str, Any]:
    data = load_json(path)
    if not isinstance(data, dict):
        raise NormalizerError(f"Rules file must contain a JSON object: {path}")
    data.setdefault("ignore_failed_request_patterns", [])
    data.setdefault("ignore_console_error_patterns", [])
    data.setdefault("ignore_issue_patterns", [])
    return data


def matches_pattern(text: str, pattern: dict[str, Any]) -> bool:
    haystack = normalize_text(text)
    contains_all = pattern.get("contains_all") or []
    contains_any = pattern.get("contains_any") or []
    excludes_any = pattern.get("excludes_any") or []

    if any(normalize_text(token) not in haystack for token in contains_all):
        return False

    if contains_any and not any(normalize_text(token) in haystack for token in contains_any):
        return False

    if any(normalize_text(token) in haystack for token in excludes_any):
        return False

    return True


def filter_signal_list(items: list[str], patterns: list[dict[str, Any]]) -> tuple[list[str], list[dict[str, str]]]:
    kept: list[str] = []
    dropped: list[dict[str, str]] = []
    for item in items:
        matched_reason = None
        for pattern in patterns:
            if matches_pattern(item, pattern):
                matched_reason = str(pattern.get("reason", "matched ignore rule"))
                break
        if matched_reason:
            dropped.append({"value": item, "reason": matched_reason})
        else:
            kept.append(item)
    return kept, dropped


def drop_summary_issue(issue: str, kept_console_errors: list[str], kept_failed_requests: list[str]) -> bool:
    normalized = normalize_text(issue)
    if normalized.startswith("console errors detected:") and not kept_console_errors:
        return True
    if normalized.startswith("failed requests detected:") and not kept_failed_requests:
        return True
    return False


def extract_http_status(issues: list[str]) -> int | None:
    for issue in issues:
        match = re.search(r"HTTP status\s+(\d{3})", issue, flags=re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None


def infer_route_family(route_result: dict[str, Any]) -> str:
    issues = route_result.get("issues", []) or []
    failed_requests = route_result.get("failed_requests", []) or []
    console_errors = route_result.get("console_errors", []) or []
    text = " ".join([*issues, *failed_requests, *console_errors])
    normalized = normalize_text(text)

    if extract_http_status(issues) is not None:
        return "http_status"
    if "navigation/assertion error" in normalized:
        return "navigation"
    if "contained no visible text" in normalized:
        return "blank_body"
    if "page title is empty" in normalized:
        return "empty_title"
    if console_errors and not failed_requests:
        return "console_only"
    if failed_requests and not console_errors:
        return "failed_request_only"
    if console_errors and failed_requests:
        return "mixed_runtime"
    return "generic_failure"


def extract_keywords(route: str, title: str, notes: str) -> set[str]:
    raw = f"{route} {title} {notes}".lower()
    raw = raw.replace("/", " ")
    tokens = re.findall(r"[a-z0-9_]+", raw)
    keywords: set[str] = set()
    for token in tokens:
        if token in STOPWORDS:
            continue
        if token.startswith("wcs-"):
            continue
        if token.isdigit() and len(token) < 3:
            continue
        if len(token) < 4 and token not in {"404", "500", "503", "auth", "api"}:
            continue
        keywords.add(token)
    if route and route != "/":
        keywords.add(route.strip("/").replace("/", "-"))
    return keywords


def find_duplicate(backlog: list[dict[str, Any]], candidate: dict[str, Any]) -> dict[str, Any] | None:
    candidate_title = normalize_text(candidate.get("title", ""))
    candidate_route = str(candidate.get("route", "") or "")
    candidate_keywords = set(candidate.get("keywords", []))

    for item in backlog:
        title = normalize_text(item.get("title", ""))
        notes = normalize_text(item.get("notes", ""))
        combined = f"{title} {notes}"

        if candidate_title and candidate_title == title:
            return item

        route_match = bool(candidate_route and candidate_route in combined)
        if not route_match:
            continue

        existing_keywords = extract_keywords(candidate_route, str(item.get("title", "")), str(item.get("notes", "")))
        overlap = len(candidate_keywords & existing_keywords)
        if overlap >= 2:
            return item
    return None


def classify_candidate(route_result: dict[str, Any], issue_family: str) -> tuple[str, str, str]:
    route = str(route_result.get("route", "") or "")
    home_route = route == "/"
    http_status = extract_http_status(route_result.get("issues", []) or [])

    if issue_family == "empty_title":
        return "ugly", "P3", "low"
    if issue_family == "blank_body":
        return "broken", "P1" if home_route else "P2", "medium"
    if issue_family == "http_status":
        if http_status is not None and http_status >= 500:
            return "broken", "P1" if home_route else "P2", "medium"
        return "investigate", "P2", "low"
    if issue_family == "navigation":
        return "broken", "P1" if home_route else "P2", "medium"
    if issue_family in {"console_only", "failed_request_only", "mixed_runtime", "generic_failure"}:
        return "investigate", "P2" if home_route else "P3", "medium"
    return "investigate", "P3", "medium"


def build_candidate_title(route_result: dict[str, Any], issue_family: str) -> str:
    route = str(route_result.get("route", "") or "")
    if issue_family == "empty_title":
        return f"Set non-empty page title for public {route}"
    if issue_family == "blank_body":
        return f"Investigate blank public {route} render detected by scout"
    if issue_family == "http_status":
        status_code = extract_http_status(route_result.get("issues", []) or [])
        return f"Investigate public {route} scout HTTP {status_code} failure"
    if issue_family == "navigation":
        return f"Investigate public {route} scout navigation failure"
    if issue_family == "console_only":
        return f"Investigate public {route} console errors detected by scout"
    if issue_family == "failed_request_only":
        return f"Investigate public {route} failed requests detected by scout"
    if issue_family == "mixed_runtime":
        return f"Investigate public {route} runtime errors detected by scout"
    return f"Investigate public {route} scout failure"


def build_candidate_keywords(route_result: dict[str, Any], issue_family: str, title: str) -> list[str]:
    route = str(route_result.get("route", "") or "")
    issues = route_result.get("issues", []) or []
    console_errors = route_result.get("console_errors", []) or []
    failed_requests = route_result.get("failed_requests", []) or []
    signal_parts = [route, issue_family, title, *issues, *console_errors, *failed_requests]
    signal_text = " ".join(str(part) for part in signal_parts)
    return sorted(extract_keywords(route, title, signal_text))


def build_candidate_notes(route_result: dict[str, Any], result_source: Path, issue_family: str) -> str:
    route = str(route_result.get("route", "") or "")
    label = str(route_result.get("label", "") or "")
    issues = route_result.get("issues", []) or []
    console_errors = route_result.get("console_errors", []) or []
    failed_requests = route_result.get("failed_requests", []) or []
    screenshot = route_result.get("screenshot") or ""

    evidence_bits = [f"Scout route: {route}"]
    if label:
        evidence_bits.append(f"label: {label}")
    evidence_bits.append(f"family: {issue_family}")
    if issues:
        evidence_bits.append("issues: " + " || ".join(issues[:3]))
    if console_errors:
        evidence_bits.append("console: " + " || ".join(console_errors[:2]))
    if failed_requests:
        evidence_bits.append("failed requests: " + " || ".join(failed_requests[:2]))
    if screenshot:
        evidence_bits.append(f"screenshot: {screenshot}")
    evidence_bits.append(f"source: {result_source}")
    return "; ".join(evidence_bits)


def next_task_id(backlog: list[dict[str, Any]], project: str = "WCS", floor: int = 16) -> str:
    max_id = floor - 1
    pattern = re.compile(rf"^{re.escape(project)}-(\d+)$", re.IGNORECASE)
    for item in backlog:
        match = pattern.match(str(item.get("task_id", "")).strip())
        if match:
            max_id = max(max_id, int(match.group(1)))
    return f"{project}-{max_id + 1:03d}"


def normalize_route_result(route_result: dict[str, Any], rules: dict[str, Any]) -> dict[str, Any]:
    original_issues = [str(x) for x in route_result.get("issues", []) or []]
    original_console = [str(x) for x in route_result.get("console_errors", []) or []]
    original_failed = [str(x) for x in route_result.get("failed_requests", []) or []]

    kept_console, dropped_console = filter_signal_list(
        original_console, rules.get("ignore_console_error_patterns", [])
    )
    kept_failed, dropped_failed = filter_signal_list(
        original_failed, rules.get("ignore_failed_request_patterns", [])
    )

    filtered_issues: list[str] = []
    dropped_issues: list[dict[str, str]] = []
    for issue in original_issues:
        if drop_summary_issue(issue, kept_console, kept_failed):
            dropped_issues.append({"value": issue, "reason": "summary issue collapsed after filtering underlying signals"})
            continue
        matched_reason = None
        for pattern in rules.get("ignore_issue_patterns", []):
            if matches_pattern(issue, pattern):
                matched_reason = str(pattern.get("reason", "matched ignore rule"))
                break
        if matched_reason:
            dropped_issues.append({"value": issue, "reason": matched_reason})
        else:
            filtered_issues.append(issue)

    has_signal = bool(filtered_issues or kept_console or kept_failed)
    normalized = {
        "route": str(route_result.get("route", "") or ""),
        "label": str(route_result.get("label", "") or ""),
        "status": str(route_result.get("status", "") or ""),
        "issues": filtered_issues,
        "console_errors": kept_console,
        "failed_requests": kept_failed,
        "screenshot": route_result.get("screenshot"),
        "dropped_console_errors": dropped_console,
        "dropped_failed_requests": dropped_failed,
        "dropped_issues": dropped_issues,
        "all_signal_removed": not has_signal,
    }
    return normalized


def process_results(
    results: list[dict[str, Any]],
    backlog: list[dict[str, Any]],
    result_source: Path,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    actions: list[dict[str, Any]] = []
    inserted_tasks: list[dict[str, Any]] = []

    for route_result in results:
        route = str(route_result.get("route", "") or "")
        status = normalize_text(route_result.get("status", ""))
        if status == "pass":
            actions.append({
                "route": route,
                "action": "pass",
                "reason": "Scout route passed with no backlog action needed.",
            })
            continue
        if status == "skipped":
            actions.append({
                "route": route,
                "action": "skipped",
                "reason": "Scout route was skipped. No backlog action created.",
            })
            continue

        issue_family = infer_route_family(route_result)
        bucket, priority, risk = classify_candidate(route_result, issue_family)
        title = build_candidate_title(route_result, issue_family)
        notes = build_candidate_notes(route_result, result_source, issue_family)
        keywords = build_candidate_keywords(route_result, issue_family, title)

        candidate = {
            "project": "WCS",
            "bucket": bucket,
            "priority": priority,
            "risk": risk,
            "status": "ready",
            "title": title,
            "notes": notes,
            "route": route,
            "issue_family": issue_family,
            "keywords": keywords,
        }

        duplicate = find_duplicate(backlog, candidate)
        if duplicate:
            actions.append({
                "route": route,
                "action": "duplicate_suppressed",
                "reason": f"Matching backlog item already exists: {duplicate.get('task_id', '')}",
                "candidate": candidate,
                "matched_task": {
                    "task_id": duplicate.get("task_id", ""),
                    "title": duplicate.get("title", ""),
                    "status": duplicate.get("status", ""),
                },
            })
            continue

        task_id = next_task_id(backlog)
        backlog_item = {
            "task_id": task_id,
            "project": candidate["project"],
            "bucket": candidate["bucket"],
            "priority": candidate["priority"],
            "risk": candidate["risk"],
            "status": candidate["status"],
            "title": candidate["title"],
            "notes": candidate["notes"],
        }
        backlog.append(backlog_item)
        inserted_tasks.append(backlog_item)
        actions.append({
            "route": route,
            "action": "inserted",
            "reason": "New backlog task created from scout failure.",
            "candidate": candidate,
            "task": backlog_item,
        })

    return actions, inserted_tasks


def summarize_actions(all_actions: list[dict[str, Any]], inserted: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "routes_total": len(all_actions),
        "routes_failed_or_warn": len([a for a in all_actions if a.get("action") in {"filtered_noise", "duplicate_suppressed", "inserted"}]),
        "routes_fully_filtered": len([a for a in all_actions if a.get("action") == "filtered_noise"]),
        "duplicates_suppressed": len([a for a in all_actions if a.get("action") == "duplicate_suppressed"]),
        "tasks_inserted": len(inserted),
        "inserted_task_ids": [t.get("task_id", "") for t in inserted],
    }


def main() -> int:
    args = parse_args()
    script_path = Path(__file__).resolve()
    workspace = Path(args.workspace).resolve() if args.workspace else script_path.parent.parent

    results_path = Path(args.results).resolve() if args.results else latest_scout_results_path(workspace)
    backlog_path = Path(args.backlog).resolve() if args.backlog else workspace / "state" / "master_backlog.json"
    md_path = Path(args.md).resolve() if args.md else workspace / "state" / "MASTER_BACKLOG.md"
    rules_path = Path(args.rules).resolve() if args.rules else workspace / "config" / DEFAULT_RULES_FILENAME
    output_path = Path(args.output).resolve() if args.output else results_path.parent / DEFAULT_REPORT_FILENAME

    results = load_json(results_path)
    backlog = load_json(backlog_path)
    rules = load_rules(rules_path)

    if not isinstance(results, list):
        raise NormalizerError(f"Scout results must be a JSON array: {results_path}")
    if not isinstance(backlog, list):
        raise NormalizerError(f"Backlog must be a JSON array: {backlog_path}")

    normalized_failures: list[dict[str, Any]] = []
    actionable_results: list[dict[str, Any]] = []
    actions: list[dict[str, Any]] = []

    for raw_route_result in results:
        if not isinstance(raw_route_result, dict):
            raise NormalizerError("Each scout result entry must be a JSON object")

        normalized = normalize_route_result(raw_route_result, rules)
        normalized_failures.append(normalized)
        route = normalized.get("route", "")
        status = normalize_text(normalized.get("status", ""))

        if status == "pass":
            actions.append({
                "route": route,
                "action": "pass",
                "reason": "Scout route passed with no backlog action needed.",
            })
            continue

        if status == "skipped":
            actions.append({
                "route": route,
                "action": "skipped",
                "reason": "Scout route was skipped. No backlog action created.",
            })
            continue

        if normalized["all_signal_removed"]:
            actions.append({
                "route": route,
                "action": "filtered_noise",
                "reason": "All captured scout signals matched ignore rules or collapsed after filtering.",
                "filtered": normalized,
            })
            continue

        actionable_results.append(normalized)

    insertion_actions, inserted_tasks = process_results(actionable_results, backlog, results_path)
    actions.extend(insertion_actions)

    if inserted_tasks and not args.dry_run:
        save_json(backlog_path, backlog)
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(render_master_backlog_md(backlog), encoding="utf-8")

    report = {
        "generated_at": now_local(),
        "dry_run": bool(args.dry_run),
        "results_source": str(results_path),
        "rules_source": str(rules_path),
        "backlog_json": str(backlog_path),
        "backlog_markdown": str(md_path),
        "summary": summarize_actions(actions, inserted_tasks),
        "actions": actions,
    }
    save_json(output_path, report)

    print(f"RESULTS SOURCE: {results_path}")
    print(f"REPORT: {output_path}")
    print(f"TASKS INSERTED: {len(inserted_tasks)}")
    if inserted_tasks and not args.dry_run:
        print(f"UPDATED: {backlog_path}")
        print(f"RENDERED: {md_path}")
    elif inserted_tasks and args.dry_run:
        print("DRY RUN: backlog files were not modified")
    else:
        print("NO NEW TASKS INSERTED")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except NormalizerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)