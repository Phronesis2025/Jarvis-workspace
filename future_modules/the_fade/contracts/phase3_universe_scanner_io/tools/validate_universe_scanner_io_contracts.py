#!/usr/bin/env python3
"""Offline validator for Phase 3 universe-scanner I/O contracts.

Scope boundary (T87):
- Reads only schemas/examples and optional fixtures_invalid under this package.
- Emits stdout/stderr and process exit code only.
- Performs no network, scanner, provider, or runtime behavior.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

try:
    from jsonschema import Draft7Validator
except Exception:
    print(
        "ERROR: jsonschema is required for offline validation. "
        "Install locally in your Python environment (no network use by this tool).",
        file=sys.stderr,
    )
    sys.exit(2)


BASE_DIR = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = BASE_DIR / "schemas"
EXAMPLES_DIR = BASE_DIR / "examples"
FIXTURES_INVALID_DIR = BASE_DIR / "fixtures_invalid"

REQUEST_SCHEMA_PATH = SCHEMAS_DIR / "universe_scanner_request.schema.json"
RESULT_SCHEMA_PATH = SCHEMAS_DIR / "universe_scanner_result.schema.json"
REQUEST_EXAMPLE_PATH = EXAMPLES_DIR / "universe_scanner_request.example.json"
RESULT_EXAMPLE_PATH = EXAMPLES_DIR / "universe_scanner_result.example.json"


def _read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _build_validator(schema_path: Path) -> Draft7Validator:
    schema = _read_json(schema_path)
    return Draft7Validator(schema)


def _validate_should_pass(
    validator: Draft7Validator, data_path: Path, label: str
) -> Tuple[bool, str]:
    data = _read_json(data_path)
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    if errors:
        first = errors[0]
        return (
            False,
            f"{label}: FAIL (expected valid) at '{list(first.path)}' -> {first.message}",
        )
    return True, f"{label}: PASS"


def _infer_fixture_target_and_reason(path: Path) -> Tuple[str, str]:
    name = path.stem.lower()
    if "_request_" in name:
        target = "request"
    elif "_result_" in name:
        target = "result"
    else:
        raise ValueError(
            f"{path.name}: invalid fixture name. Must include '_request_' or '_result_'."
        )

    if "_type_" in name:
        reason = "type"
    elif "_required_" in name:
        reason = "required"
    elif "_format_" in name:
        reason = "format"
    elif "_enum_" in name:
        reason = "enum"
    elif "_additionalproperties_" in name or "_additional_props_" in name:
        reason = "additionalProperties"
    elif "_minlength_" in name:
        reason = "minLength"
    elif "_pattern_" in name:
        reason = "pattern"
    elif "_anyof_" in name:
        reason = "anyOf"
    else:
        raise ValueError(
            f"{path.name}: invalid fixture name. Must include one reason token, "
            "e.g. _type_, _required_, _format_, _enum_, _additionalProperties_, "
            "_minLength_, _pattern_, or _anyOf_."
        )
    return target, reason


def _validate_invalid_fixtures(
    request_validator: Draft7Validator, result_validator: Draft7Validator
) -> List[Tuple[bool, str]]:
    if not FIXTURES_INVALID_DIR.exists():
        return [(True, "fixtures_invalid/: not present (skipped)")]

    fixtures = sorted(FIXTURES_INVALID_DIR.glob("*.json"))
    outcomes: List[Tuple[bool, str]] = []

    if len(fixtures) > 5:
        outcomes.append(
            (
                False,
                f"fixtures_invalid/: FAIL expected <= 5 files, found {len(fixtures)}",
            )
        )
        return outcomes

    if not fixtures:
        outcomes.append((True, "fixtures_invalid/: empty (skipped)"))
        return outcomes

    for path in fixtures:
        try:
            target, reason = _infer_fixture_target_and_reason(path)
            data = _read_json(path)
            validator = request_validator if target == "request" else result_validator
            errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
            if not errors:
                outcomes.append((False, f"{path.name}: FAIL expected invalid, got valid"))
                continue
            error_classes = " | ".join(e.validator for e in errors)
            if reason not in {e.validator for e in errors}:
                outcomes.append(
                    (
                        False,
                        f"{path.name}: FAIL expected reason class '{reason}', got '{error_classes}'",
                    )
                )
                continue
            outcomes.append((True, f"{path.name}: PASS (invalid as expected: {reason})"))
        except Exception as exc:
            outcomes.append((False, f"{path.name}: FAIL {exc}"))
    return outcomes


def main() -> int:
    required_paths = [
        REQUEST_SCHEMA_PATH,
        RESULT_SCHEMA_PATH,
        REQUEST_EXAMPLE_PATH,
        RESULT_EXAMPLE_PATH,
    ]
    for path in required_paths:
        if not path.exists():
            print(f"FAIL missing required file: {path}", file=sys.stderr)
            return 1

    request_validator = _build_validator(REQUEST_SCHEMA_PATH)
    result_validator = _build_validator(RESULT_SCHEMA_PATH)

    checks: List[Tuple[bool, str]] = [
        _validate_should_pass(
            request_validator, REQUEST_EXAMPLE_PATH, "request.example vs request.schema"
        ),
        _validate_should_pass(
            result_validator, RESULT_EXAMPLE_PATH, "result.example vs result.schema"
        ),
    ]
    checks.extend(_validate_invalid_fixtures(request_validator, result_validator))

    failed = [msg for ok, msg in checks if not ok]
    for _, msg in checks:
        print(msg)

    if failed:
        print(f"SUMMARY: FAIL ({len(failed)} failure(s))", file=sys.stderr)
        return 1

    print("SUMMARY: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
