from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple


class RegistryCheckError(Exception):
    pass


CORE_ITEMS: List[Tuple[str, str]] = [
    ("jarvis.py", "C:\\dev\\jarvis-workspace\\scripts\\jarvis.py"),
    ("prepare_wcs_task_branch.py", "C:\\dev\\jarvis-workspace\\scripts\\prepare_wcs_task_branch.py"),
    ("worker_change_check.py", "C:\\dev\\jarvis-workspace\\scripts\\worker_change_check.py"),
    ("commit_gate_check.py", "C:\\dev\\jarvis-workspace\\scripts\\commit_gate_check.py"),
    ("worker_result_validate.py", "C:\\dev\\jarvis-workspace\\scripts\\worker_result_validate.py"),
    ("qa_result_validate.py", "C:\\dev\\jarvis-workspace\\scripts\\qa_result_validate.py"),
    ("qa_failure_triage.py", "C:\\dev\\jarvis-workspace\\scripts\\qa_failure_triage.py"),
    ("stamp_guard_check.py", "C:\\dev\\jarvis-workspace\\scripts\\stamp_guard_check.py"),
    ("stamp_result_timestamp.py", "C:\\dev\\jarvis-workspace\\scripts\\stamp_result_timestamp.py"),
    ("pre_reconcile_check.py", "C:\\dev\\jarvis-workspace\\scripts\\pre_reconcile_check.py"),
    ("reconcile_task_outcome.py", "C:\\dev\\jarvis-workspace\\scripts\\reconcile_task_outcome.py"),
    ("post_reconcile_validate.py", "C:\\dev\\jarvis-workspace\\scripts\\post_reconcile_validate.py"),
    ("JARVIS_SCRIPT_PROCESS_REFERENCE.md", "C:\\dev\\jarvis-workspace\\JARVIS_SCRIPT_PROCESS_REFERENCE.md"),
    ("JARVIS_TASK_EXECUTION_CHECKLIST.md", "C:\\dev\\jarvis-workspace\\JARVIS_TASK_EXECUTION_CHECKLIST.md"),
    ("JARVIS_PHASE_CHECKLIST.md", "C:\\dev\\jarvis-workspace\\JARVIS_PHASE_CHECKLIST.md"),
    ("JARVIS_LIVE_HANDOFF_BUNDLE.md", "C:\\dev\\jarvis-workspace\\JARVIS_LIVE_HANDOFF_BUNDLE.md"),
    ("file_registry.json", "C:\\dev\\jarvis-workspace\\state\\file_registry.json"),
    ("FILE_REGISTRY.md", "C:\\dev\\jarvis-workspace\\state\\FILE_REGISTRY.md"),
]


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise RegistryCheckError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise RegistryCheckError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only file registry drift checker for the Jarvis workspace."
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def load_registry_json(path: Path, failures: List[str]) -> List[Dict[str, Any]]:
    try:
        data = read_json(path)
    except RegistryCheckError as exc:
        failures.append(str(exc))
        return []

    if not isinstance(data, list):
        failures.append(f"file_registry.json root must be a list: {path}")
        return []

    parsed: List[Dict[str, Any]] = []
    for idx, item in enumerate(data):
        if not isinstance(item, dict):
            failures.append(f"file_registry.json entry {idx} must be an object.")
            continue
        parsed.append(item)
    return parsed


def check_required_fields(entries: List[Dict[str, Any]], failures: List[str]) -> None:
    required_fields = ["file", "path", "category", "source_type", "owner", "purpose"]
    for idx, entry in enumerate(entries):
        for field in required_fields:
            if field not in entry:
                failures.append(
                    f"file_registry.json entry {idx} missing required field: {field}."
                )


def detect_duplicates(entries: List[Dict[str, Any]], failures: List[str]) -> None:
    seen_files: Dict[str, int] = {}
    seen_paths: Dict[str, int] = {}

    for idx, entry in enumerate(entries):
        file_name = normalize_text(entry.get("file"))
        path = normalize_text(entry.get("path"))

        if file_name:
            seen_files[file_name] = seen_files.get(file_name, 0) + 1
        if path:
            seen_paths[path] = seen_paths.get(path, 0) + 1

    for file_name, count in seen_files.items():
        if count > 1:
            failures.append(
                f"file_registry.json contains duplicate file entries for {file_name!r} ({count} entries)."
            )
    for path, count in seen_paths.items():
        if count > 1:
            failures.append(
                f"file_registry.json contains duplicate path entries for {path!r} ({count} entries)."
            )


def build_index(entries: List[Dict[str, Any]]) -> Tuple[Set[Tuple[str, str]], Dict[Tuple[str, str], Dict[str, Any]]]:
    index: Set[Tuple[str, str]] = set()
    details: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for entry in entries:
        file_name = normalize_text(entry.get("file"))
        path = normalize_text(entry.get("path"))
        if not file_name or not path:
            continue
        key = (file_name, path)
        index.add(key)
        details[key] = entry
    return index, details


def parse_markdown_registry(path: Path, failures: List[str]) -> Set[Tuple[str, str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        failures.append(f"Missing FILE_REGISTRY markdown file: {path}")
        return set()
    except OSError as exc:
        failures.append(f"Failed to read FILE_REGISTRY markdown file {path}: {exc}")
        return set()

    rows: Set[Tuple[str, str]] = set()
    for line in text.splitlines():
        line = line.strip()
        # Skip header/separator lines
        if not line.startswith("|") or line.startswith("|---"):
            continue
        parts = [col.strip() for col in line.split("|")]
        # Expect at least: "" | File | Path | ...
        if len(parts) < 4:
            continue
        file_name = parts[1]
        path = parts[2]
        if file_name and path and file_name != "File" and path != "Path":
            rows.add((file_name, path))
    return rows


def check_core_coverage(
    json_index: Set[Tuple[str, str]],
    md_index: Set[Tuple[str, str]],
    failures: List[str],
) -> None:
    for file_name, path in CORE_ITEMS:
        key = (file_name, path)
        if key not in json_index:
            failures.append(
                f"Core item missing from file_registry.json: file={file_name!r}, path={path!r}."
            )
        if key not in md_index:
            failures.append(
                f"Core item missing or out of sync in FILE_REGISTRY.md: file={file_name!r}, path={path!r}."
            )


def main() -> int:
    args = parse_args()

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: List[str] = []

    if not workspace.exists():
        print("FILE REGISTRY CHECK: FAIL")
        print(f"Workspace: {workspace}")
        print("Failures:")
        print(f"- Workspace path does not exist.")
        return 1

    json_path = workspace / "state" / "file_registry.json"
    md_path = workspace / "state" / "FILE_REGISTRY.md"

    entries = load_registry_json(json_path, failures)
    check_required_fields(entries, failures)
    detect_duplicates(entries, failures)

    json_index, _ = build_index(entries)
    md_index = parse_markdown_registry(md_path, failures)

    # Core coverage and simple drift detection for hardened-loop items.
    check_core_coverage(json_index, md_index, failures)

    if failures:
        print("FILE REGISTRY CHECK: FAIL")
        print(f"Workspace: {workspace}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    print("FILE REGISTRY CHECK: PASS")
    print(f"Workspace: {workspace}")
    print("Summary:")
    print("- file_registry.json exists, parses, and has required fields for entries.")
    print("- No obvious duplicate file/path entries detected in file_registry.json.")
    print("- FILE_REGISTRY.md exists and contains rows for all core hardened-loop items.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

