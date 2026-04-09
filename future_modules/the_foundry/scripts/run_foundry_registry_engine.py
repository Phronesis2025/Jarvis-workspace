import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ENGINE_DIR = SCRIPT_DIR.parent / "engine"
if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))

from foundry_registry_engine import FoundryEngineError, run_engine  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Foundry local/core registry engine.")
    parser.add_argument(
        "--input",
        required=True,
        help="Path to input JSON with source_record + candidate_ideas.",
    )
    parser.add_argument(
        "--workspace-root",
        default=str(Path(__file__).resolve().parents[3]),
        help="Workspace root path. Default resolves from script location.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    workspace_root = Path(args.workspace_root).resolve()
    input_path = Path(args.input).resolve()

    if not input_path.exists():
        print(f"ERROR: input file not found: {input_path}")
        return 1

    try:
        payload = json.loads(input_path.read_text(encoding="utf-8-sig"))
        manifest = run_engine(workspace_root, payload)
    except (FoundryEngineError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    except Exception as exc:
        print(f"ERROR: unexpected failure: {exc}")
        return 1

    print("Foundry local/core registry engine run complete.")
    print(f"Run ID: {manifest['run_id']}")
    print(f"Source ID: {manifest['source_id']}")
    print(f"Manifest: future_modules/the_foundry/state/indexes/foundry_registry_manifest.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
