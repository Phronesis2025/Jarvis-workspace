import argparse
import json
from pathlib import Path
import sys

from repo_intake_lib import RepoIntakeError, run_repo_intake


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run bounded repo intake triage for one GitHub repository."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to intake input JSON (matches repo_intake_input.schema.json).",
    )
    parser.add_argument(
        "--workspace-root",
        default=str(Path(__file__).resolve().parents[3]),
        help="Workspace root path. Default resolves from script location.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).resolve()
    workspace_root = Path(args.workspace_root).resolve()

    if not input_path.exists():
        print(f"ERROR: input file not found: {input_path}")
        return 1

    try:
        input_data = json.loads(input_path.read_text(encoding="utf-8-sig"))
        result, output_json, output_md = run_repo_intake(workspace_root, input_data)
    except (RepoIntakeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    except Exception as exc:
        print(f"ERROR: unexpected failure: {exc}")
        return 1

    print("Repo intake triage complete.")
    print(f"Classification: {result['classification']} (confidence={result['confidence']})")
    print(f"JSON output: {output_json}")
    print(f"Report output: {output_md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
