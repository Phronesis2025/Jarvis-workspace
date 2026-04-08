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
    parser.add_argument(
        "--input",
        required=True,
        help="Path to batch input JSON with an `items` list.",
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


def _build_markdown_report(summary: Dict[str, Any]) -> str:
    lines = [
        f"# Repo Intake Batch Summary: {summary['batch_id']}",
        "",
        f"- Generated At (UTC): {summary['generated_at_utc']}",
        f"- Total Items: {summary['total_items']}",
        f"- Success Count: {summary['success_count']}",
        f"- Failure Count: {summary['failure_count']}",
        "",
        "## Successful Items",
        "",
        "| Repo | Profile | Classification | Repo Reality | Our Fit | Novelty | Fatal Flags | Deeper Review |",
        "|---|---|---|---:|---:|---:|---|---|",
    ]
    for row in summary["successful_items"]:
        fatal = ", ".join(row["fatal_flags_triggered"]) if row["fatal_flags_triggered"] else "none"
        lines.append(
            f"| `{row['repo_name']}` | `{row['profile_used']}` | `{row['classification']}` | "
            f"{row['repo_reality_score']} | {row['our_fit_score']} | {row['novelty_flag']} | "
            f"{fatal} | `{row['deeper_review_recommended']}` |"
        )

    if not summary["successful_items"]:
        lines.append("| none | none | none | 0 | 0 | 0 | none | `False` |")

    lines.extend(
        [
            "",
            "## Failed Items",
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
            "## Grouped by Classification",
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
    input_path = Path(args.input).resolve()
    workspace_root = Path(args.workspace_root).resolve()
    if not input_path.exists():
        print(f"ERROR: input file not found: {input_path}")
        return 1

    try:
        items = _load_batch_input(input_path)
    except (RepoIntakeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1

    outputs_dir = workspace_root / "future_modules" / "repo_intake" / "outputs"
    reports_dir = workspace_root / "future_modules" / "repo_intake" / "reports"
    outputs_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    successful_items: List[Dict[str, Any]] = []
    failed_items: List[Dict[str, Any]] = []
    grouped = {"materially_useful": [], "marginal": [], "too_fuzzy": [], "reject": []}

    for idx, item in enumerate(items, start=1):
        try:
            result, _, _ = run_repo_intake(workspace_root, item)
            successful_items.append(
                {
                    "repo_name": result["repo_name"],
                    "profile_used": result["profile_used"],
                    "classification": result["classification"],
                    "repo_reality_score": result["repo_reality_score"],
                    "our_fit_score": result["our_fit_score"],
                    "novelty_flag": result["novelty_flag"],
                    "fatal_flags_triggered": result["fatal_flags_triggered"],
                    "deeper_review_recommended": result["deeper_review_recommended"],
                }
            )
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

    batch_id = datetime.now(timezone.utc).strftime("repo_intake_batch_%Y%m%d_%H%M%SZ")
    summary = {
        "batch_id": batch_id,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "total_items": len(items),
        "success_count": len(successful_items),
        "failure_count": len(failed_items),
        "successful_items": successful_items,
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
