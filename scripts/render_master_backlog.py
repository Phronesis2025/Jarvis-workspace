from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DEFAULT_COLUMNS = [
    ("task_id", "Task ID"),
    ("project", "Project"),
    ("bucket", "Bucket"),
    ("priority", "Priority"),
    ("risk", "Risk"),
    ("status", "Status"),
    ("title", "Title"),
    ("notes", "Notes"),
]


def escape_md(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    return text.replace("|", "\\|").replace("\n", " ").strip()


def load_backlog(json_path: Path) -> list[dict[str, Any]]:
    if not json_path.exists():
        raise FileNotFoundError(f"Backlog JSON not found: {json_path}")

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Backlog JSON must contain a list of task objects.")

    cleaned: list[dict[str, Any]] = []
    for i, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Task #{i} is not a JSON object.")
        cleaned.append(item)
    return cleaned


def render_markdown(tasks: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    lines.append("# MASTER_BACKLOG")
    lines.append("")
    header = "| " + " | ".join(label for _, label in DEFAULT_COLUMNS) + " |"
    divider = "|" + "|".join(["---"] * len(DEFAULT_COLUMNS)) + "|"
    lines.append(header)
    lines.append(divider)

    for task in tasks:
        row = []
        for key, _label in DEFAULT_COLUMNS:
            row.append(escape_md(task.get(key, "")))
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render MASTER_BACKLOG.md from master_backlog.json"
    )
    parser.add_argument(
        "--json",
        dest="json_path",
        default=None,
        help="Path to master_backlog.json",
    )
    parser.add_argument(
        "--md",
        dest="md_path",
        default=None,
        help="Path to output MASTER_BACKLOG.md",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    state_dir = script_dir.parent / "state"

    json_path = Path(args.json_path).expanduser() if args.json_path else state_dir / "master_backlog.json"
    md_path = Path(args.md_path).expanduser() if args.md_path else state_dir / "MASTER_BACKLOG.md"

    tasks = load_backlog(json_path)
    markdown = render_markdown(tasks)

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(markdown, encoding="utf-8")

    print(f"Rendered {len(tasks)} tasks")
    print(f"JSON source: {json_path}")
    print(f"Markdown output: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
