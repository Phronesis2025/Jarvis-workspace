from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Render state/FILE_REGISTRY.md from state/file_registry.json "
            "using the current approved registry format."
        )
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def load_registry_json(path: Path) -> List[Dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)
    if not isinstance(data, list):
        raise ValueError("file_registry.json root must be a list of objects.")
    entries: List[Dict[str, Any]] = []
    for idx, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"file_registry.json entry {idx} must be an object.")
        entries.append(item)
    return entries


def escape_cell(value: Any) -> str:
    """Convert a registry value into a single-line markdown-safe cell."""

    if value is None:
        text = ""
    else:
        text = str(value)

    # Replace newlines with spaces to keep each row on a single line.
    text = text.replace("\r\n", " ").replace("\n", " ").replace("\r", " ")
    # Escape pipe characters so they do not split columns.
    text = text.replace("|", r"\|")
    return text


def render_markdown(entries: List[Dict[str, Any]]) -> str:
    header = """# FILE REGISTRY

## Live Doc Status
- Last reviewed: 2026-03-13
- Last updated: 2026-03-13
- Verified against: JARVIS_LIVE_HANDOFF_BUNDLE.md
- Status: aligned to current live hardening state; registry mirrors file_registry.json and is rendered by render_file_registry.py

## Purpose

This file is the human-readable registry of the Jarvis local build system.

It exists to prevent drift between:
- design documents
- live scripts
- state files
- generated task artifacts
- scout outputs
- WCS repo-side test files

JSON is the machine-readable source for later automation.
This markdown file is the human-readable view rendered from file_registry.json.

---

## Conventions

### Source Type
- `source_of_truth` = primary authoritative file
- `generated` = derived from another file
- `template` = reusable starter structure
- `runtime_output` = produced by scripts or test runs

### Categories
- `doc`
- `state`
- `script`
- `config`
- `template`
- `task_packet`
- `worker_result`
- `qa_result`
- `log`
- `repo_test`

### Owners
- `user`
- `jarvis_script`
- `cursor_worker`
- `playwright`
- `scout_runner`

---

## Registry

| File | Path | Category | Source Type | Owner | Purpose | Updated By | Notes |
|---|---|---|---|---|---|---|---|
"""

    lines: List[str] = [header]

    # Preserve JSON order exactly for determinism.
    for entry in entries:
        file_name = escape_cell(entry.get("file", ""))
        path = escape_cell(entry.get("path", ""))
        category = escape_cell(entry.get("category", ""))
        source_type = escape_cell(entry.get("source_type", ""))
        owner = escape_cell(entry.get("owner", ""))
        purpose = escape_cell(entry.get("purpose", ""))
        updated_by = escape_cell(entry.get("updated_by", ""))
        notes = escape_cell(entry.get("notes", ""))

        row = f"| {file_name} | {path} | {category} | {source_type} | {owner} | {purpose} | {updated_by} | {notes} |"
        lines.append(row)

    # Ensure trailing newline at end of file for cleanliness.
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    if not workspace.exists():
        print("RENDER FILE REGISTRY: FAIL")
        print(f"Workspace: {workspace}")
        print("- Workspace path does not exist.")
        return 1

    json_path = workspace / "state" / "file_registry.json"
    md_path = workspace / "state" / "FILE_REGISTRY.md"

    try:
        entries = load_registry_json(json_path)
    except FileNotFoundError:
        print("RENDER FILE REGISTRY: FAIL")
        print(f"Workspace: {workspace}")
        print(f"- Missing file_registry.json at {json_path}")
        return 1
    except Exception as exc:
        print("RENDER FILE REGISTRY: FAIL")
        print(f"Workspace: {workspace}")
        print(f"- Unable to load or parse file_registry.json: {exc}")
        return 1

    markdown = render_markdown(entries)

    try:
        md_path.write_text(markdown, encoding="utf-8", newline="\n")
    except Exception as exc:
        print("RENDER FILE REGISTRY: FAIL")
        print(f"Workspace: {workspace}")
        print(f"- Unable to write FILE_REGISTRY.md: {exc}")
        return 1

    print("RENDER FILE REGISTRY: PASS")
    print(f"Workspace: {workspace}")
    print(f"- Read {len(entries)} entries from {json_path}")
    print(f"- Rendered FILE_REGISTRY.md at {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

