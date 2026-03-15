# Pathfinder

**Status:** recognized, inactive  
**Last updated:** 2026-03-14  
**Location:** `future_modules/pathfinder/`

## Purpose

Pathfinder is the planned Jarvis discovery/research worker.

Its job is to investigate errors, repo context, docs, implementation options, and likely next steps **without editing production code**.

Pathfinder exists to reduce wasted implementation cycles by answering:
- what is actually happening
- what files/docs matter
- what the likely causes/options are
- what the safest next action is

## Current status

Pathfinder is **not active**.

This folder is a dormant contract pack only. It exists so the module can be built faster later without inventing the worker from scratch.

## What is included here

- `PATHFINDER_SPEC.md`
- `PATHFINDER_BOUNDARIES.md`
- `PATHFINDER_ACTIVATION_RULES.md`
- `PATHFINDER_QA_RULES.md`
- `templates/pathfinder_task_packet.template.json`
- `templates/pathfinder_result.template.json`
- `templates/pathfinder_escalation_record.template.json`
- `examples/pathfinder_task_packet.example.json`
- `examples/pathfinder_result.example.json`
- `examples/pathfinder_bad_result.example.json`

## Operating stance

Pathfinder is:
- read-only
- bounded
- evidence-driven
- reviewable
- subordinate to Jarvis

Pathfinder is not:
- a coding worker
- a QA replacement
- a free-roaming autonomous agent
- a justification to expand scope
- a reason to bypass the current WCS/Jarvis proof loop

## Naming conventions

- docs use `PATHFINDER_*.md`
- templates use `pathfinder_*.template.json`
- examples use `pathfinder_*.example.json`

## Future integration note

When Pathfinder is activated later, it should follow the same general contract discipline as the existing Jarvis loop:
- bounded input packet
- structured result JSON
- explicit QA/review path
- explicit escalation path
- no self-certified success
