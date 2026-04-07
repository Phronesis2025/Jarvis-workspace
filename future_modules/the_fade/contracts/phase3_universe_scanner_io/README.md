# Phase 3 universe-scanner I/O — static contract package

**Tranche:** T85 (first implementation slice, static artifacts only)  
**Updated:** 2026-04-08T16:30:00+00:00  

## What this is

A **non-executable** package of **JSON Schemas**, **example JSON files**, and **Python stub types** (`.pyi`) that define a **bounded** request/result shape for a **future** THE FADE universe scanner. It exists so later runtime work has a **narrow, agreed** wire format — **without** implementing scanning, networking, or orchestration.

## What this is not

- **Not** a working scanner, job runner, or CLI.
- **Not** connected to `mvp_lane_approval.json`, lane charters, or `mvp_lane_evidence_registry.json`.
- **Not** production code, provider clients, dashboards, or scheduled tasks.
- **Not** authorization to broaden Phase 3 beyond this slice.

Governance: `THE_FADE_T84_FIRST_IMPLEMENTATION_SLICE_GOVERNANCE.md` and `THE_FADE_T84_FIRST_IMPLEMENTATION_SLICE_ACCEPTANCE_CRITERIA.md`.

## Files

| Path | Role |
|------|------|
| `schemas/universe_scanner_request.schema.json` | Request JSON Schema (draft-07). |
| `schemas/universe_scanner_result.schema.json` | Result JSON Schema (draft-07). |
| `examples/universe_scanner_request.example.json` | Example request (validates against request schema). |
| `examples/universe_scanner_result.example.json` | Example result (validates against result schema). |
| `types/universe_scanner_io_types.pyi` | TypedDict / Literal shapes for type checkers only. |

## Intentionally deferred

- Executable scan loop, HTTP/API calls, persistence, scheduling.
- Mapping universe symbols to MVP lanes or provider adapters.
- Validation tooling wired into CI (schemas can be validated manually or in a future tranche).
- Version negotiation beyond the `contract_version` string field.

## Contract version

This package’s initial **semantic version** is **1.0.0** (`contract_version` in examples and schemas’ `pattern`). Future governance may bump it.
