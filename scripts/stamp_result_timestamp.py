from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


class StampError(Exception):
    pass


def now_local_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise StampError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise StampError(f"Invalid JSON in {path}: {exc}") from exc


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Stamp a result JSON file with the current local ISO timestamp in completed_at."
    )
    parser.add_argument("file", help="Path to the JSON result file to stamp")
    parser.add_argument(
        "--field",
        default="completed_at",
        help="Field name to stamp. Defaults to completed_at.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing non-empty timestamp.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.file).resolve()

    data = read_json(path)
    if not isinstance(data, dict):
        raise StampError(f"Expected a JSON object in {path}, got {type(data).__name__}")

    field_name = args.field
    existing_value = data.get(field_name)

    if existing_value and not args.force:
        print(f"SKIPPED: {path}")
        print(f"Reason: {field_name} already has a value: {existing_value}")
        print("Use --force if you intentionally want to overwrite it.")
        return 0

    stamped_value = now_local_iso()
    data[field_name] = stamped_value
    write_json(path, data)

    print(f"STAMPED: {path}")
    print(f"{field_name}: {stamped_value}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except StampError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)