import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import sys
from typing import Any, Dict, List

from repo_intake_lib import RepoIntakeError, run_repo_intake


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run bounded repo intake triage for a batch of repositories."
    )
    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument(
        "--input",
        help="Path to batch input JSON with an `items` list.",
    )
    source_group.add_argument(
        "--txt",
        help="Path to .txt file containing one GitHub repo URL per line.",
    )
    parser.add_argument(
        "--workspace-root",
        default=str(Path(__file__).resolve().parents[3]),
        help="Workspace root path. Default resolves from script location.",
    )
    return parser.parse_args()


def _load_batch_input(path: Path) -> List[Dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict) or "items" not in payload:
        raise RepoIntakeError("Batch input must be an object with an `items` field.")
    items = payload["items"]
    if not isinstance(items, list) or not items:
        raise RepoIntakeError("Batch input `items` must be a non-empty array.")
    if not all(isinstance(item, dict) for item in items):
        raise RepoIntakeError("Every batch item must be a JSON object.")
    return items


def _load_txt_batch_input(path: Path) -> List[Dict[str, Any]]:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    items: List[Dict[str, Any]] = []
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        items.append(
            {
                "repo_url": line,
                "profile": "auto",
                "operator_note": "Auto-generated from txt batch input",
                "depth_mode": "triage_only",
            }
        )
    if not items:
        raise RepoIntakeError("TXT batch input has no usable repo URLs.")
    return items


def _row_from_result(
    result: Dict[str, Any], output_json: Path, output_md: Path, workspace_root: Path
) -> Dict[str, Any]:
    def rel(p: Path) -> str:
        try:
            return str(p.relative_to(workspace_root))
        except ValueError:
            return str(p)

    return {
        "repo_name": result["repo_name"],
        "profile_used": result["profile_used"],
        "profile_selected_automatically": result["profile_selected_automatically"],
        "auto_profile_confidence": result["auto_profile_confidence"],
        "auto_profile_reasons": result["auto_profile_reasons"],
        "classification": result["classification"],
        "repo_reality_score": result["repo_reality_score"],
        "our_fit_score": result["our_fit_score"],
        "novelty_flag": result["novelty_flag"],
        "fatal_flags_triggered": result["fatal_flags_triggered"],
        "deeper_review_recommended": result["deeper_review_recommended"],
        "stop_condition": result["stop_condition"],
        "fetch_evaluation_skipped": result.get("fetch_evaluation_skipped", False),
        "run_id": result["run_id"],
        "output_json": rel(output_json),
        "output_md": rel(output_md),
    }


def _build_markdown_report(summary: Dict[str, Any]) -> str:
    bid = summary["batch_id"]
    lines = [
        f"# Repo Intake Batch Summary: {bid}",
        "",
        f"- Generated At (UTC): {summary['generated_at_utc']}",
        f"- Batch / Run ID: `{bid}`",
        f"- Total Items: {summary['total_items']}",
        f"- Evaluated (full static pass): {summary['evaluated_count']}",
        f"- Fetch-limited (no GitHub evidence): {summary['fetch_limited_count']}",
        f"- Failed (errors): {summary['failure_count']}",
        "",
        "## Evaluated items (content-scored)",
        "",
        "| Repo | Run ID | Profile | Classification | Reality | Fit | Artifacts |",
        "|---|---|---|---|---:|---:|---|",
    ]
    for row in summary["evaluated_items"]:
        arts = f"`{row['output_json']}` / `{row['output_md']}`"
        lines.append(
            f"| `{row['repo_name']}` | `{row['run_id']}` | `{row['profile_used']}` | "
            f"`{row['classification']}` | {row['repo_reality_score']} | {row['our_fit_score']} | {arts} |"
        )
    if not summary["evaluated_items"]:
        lines.append("| none | — | — | — | — | — | — |")

    lines.extend(
        [
            "",
            "## Fetch-limited items (not content-evaluated)",
            "",
            "These completed without exceptions but GitHub evidence could not be fetched. "
            "They are **not** genuine rejects; classification is `too_fuzzy` due to missing evidence only.",
            "",
            "| Repo | Stop condition | Run ID | Artifacts |",
            "|---|---|---|---|",
        ]
    )
    for row in summary["fetch_limited_items"]:
        sc = row.get("stop_condition") or "unknown"
        arts = f"`{row['output_json']}` / `{row['output_md']}`"
        lines.append(
            f"| `{row['repo_name']}` | `{sc}` | `{row['run_id']}` | {arts} |"
        )
    if not summary["fetch_limited_items"]:
        lines.append("| none | — | — | — |")

    lines.extend(
        [
            "",
            "## Failed Items (processing errors)",
            "",
            "| Repo URL | Profile | Status | Error Message |",
            "|---|---|---|---|",
        ]
    )
    for row in summary["failed_items"]:
        profile = row["profile_used"] if row["profile_used"] else "unknown"
        lines.append(
            f"| `{row['repo_url']}` | `{profile}` | `{row['status']}` | {row['error_message']} |"
        )
    if not summary["failed_items"]:
        lines.append("| none | none | none | none |")

    lines.extend(
        [
            "",
            "## Grouped by Classification (evaluated items only)",
            "",
            f"- `materially_useful`: {len(summary['grouped']['materially_useful'])}",
            f"- `marginal`: {len(summary['grouped']['marginal'])}",
            f"- `too_fuzzy`: {len(summary['grouped']['too_fuzzy'])}",
            f"- `reject`: {len(summary['grouped']['reject'])}",
            "",
        ]
    )

    for bucket in ["materially_useful", "marginal", "too_fuzzy", "reject"]:
        lines.append(f"### {bucket}")
        repos = summary["grouped"][bucket]
        if not repos:
            lines.append("- none")
        else:
            for repo in repos:
                lines.append(f"- `{repo}`")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    input_value = args.input if args.input else args.txt
    input_path = Path(input_value).resolve()
    workspace_root = Path(args.workspace_root).resolve()
    if not input_path.exists():
        print(f"ERROR: input file not found: {input_path}")
        return 1

    try:
        if args.txt:
            items = _load_txt_batch_input(input_path)
        else:
            items = _load_batch_input(input_path)
    except (RepoIntakeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1

    outputs_dir = workspace_root / "future_modules" / "repo_intake" / "outputs"
    reports_dir = workspace_root / "future_modules" / "repo_intake" / "reports"
    outputs_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    batch_id = datetime.now(timezone.utc).strftime("repo_intake_batch_%Y%m%d_%H%M%SZ")

    evaluated_items: List[Dict[str, Any]] = []
    fetch_limited_items: List[Dict[str, Any]] = []
    failed_items: List[Dict[str, Any]] = []
    grouped = {"materially_useful": [], "marginal": [], "too_fuzzy": [], "reject": []}

    for idx, item in enumerate(items, start=1):
        try:
            result, output_json, output_md = run_repo_intake(
                workspace_root, item, run_id=batch_id
            )
            row = _row_from_result(result, output_json, output_md, workspace_root)
            if result.get("stop_condition"):
                fetch_limited_items.append(row)
                print(
                    f"[{idx}/{len(items)}] {result['repo_name']}: FETCH-LIMITED "
                    f"(too_fuzzy, {result['stop_condition']})"
                )
            else:
                evaluated_items.append(row)
                grouped[result["classification"]].append(result["repo_name"])
                print(f"[{idx}/{len(items)}] {result['repo_name']}: {result['classification']}")
        except Exception as exc:
            repo_url = ""
            profile_used = None
            if isinstance(item, dict):
                repo_url = str(item.get("repo_url", ""))
                profile_val = item.get("profile")
                profile_used = str(profile_val) if profile_val is not None else None
            failed_items.append(
                {
                    "repo_url": repo_url,
                    "profile_used": profile_used,
                    "status": "failed",
                    "error_message": str(exc),
                }
            )
            print(f"[{idx}/{len(items)}] FAILED {repo_url or 'unknown_repo'}: {exc}")

    summary = {
        "batch_id": batch_id,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "total_items": len(items),
        "evaluated_count": len(evaluated_items),
        "fetch_limited_count": len(fetch_limited_items),
        "failure_count": len(failed_items),
        "evaluated_items": evaluated_items,
        "fetch_limited_items": fetch_limited_items,
        "failed_items": failed_items,
        "grouped": grouped,
    }

    summary_json_path = outputs_dir / f"{batch_id}_summary.json"
    summary_md_path = reports_dir / f"{batch_id}_summary.md"
    summary_json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    summary_md_path.write_text(_build_markdown_report(summary), encoding="utf-8")

    print("Batch triage complete.")
    print(f"Summary JSON: {summary_json_path}")
    print(f"Summary Report: {summary_md_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
