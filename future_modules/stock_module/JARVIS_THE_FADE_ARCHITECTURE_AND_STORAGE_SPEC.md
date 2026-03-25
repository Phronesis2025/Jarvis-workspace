# JARVIS_THE_FADE_ARCHITECTURE_AND_STORAGE_SPEC.md

**Document Type:** Architecture and Storage Specification  
**Status:** Proposed Canonical Spec  
**Version:** 1.0  
**Last Updated:** 2026-03-23  
**Owner:** Jason  
**Project Context:** Jarvis future worker / stock intelligence side quest

---

# 1. Purpose of This Document

This document defines the **system architecture, storage model, file layout, artifact locations, data flow, and state rules** for THE FADE stack.

It exists to answer questions like:
- where do packets live
- where do outputs go
- what files are canonical
- how does the dashboard read the system state
- where do replay artifacts live
- how are failures stored
- what is mutable vs immutable
- what is generated vs source-of-truth

This is not:
- the plain-English overview
- the build checklist
- the signal-engine behavior spec
- the trading/review rules spec
- the dashboard layout spec

This is the **system-structure document**.

---

# 2. Architecture Goals

The architecture must support these properties:

1. **Bounded worker contracts**
2. **Clear file ownership**
3. **Replayable artifacts**
4. **Immutable result packets where possible**
5. **Readable state**
6. **Machine-usable state**
7. **Dashboard visibility**
8. **Escalation traceability**
9. **No hidden mutation**
10. **Separation between canonical docs and generated outputs**

These goals align with Jarvis’s broader preference for packet-driven, auditable workflows with explicit state and readable local truth. 

---

# 3. Architectural Layers

## 3.1 Layer map

```text
Source Adapters / Scanner
        ↓
Scout Engine
        ↓
Signal Packets / Conflict Packets / Failures
        ↓
Operator Review State
        ↓
Research + Risk Gate
        ↓
Paper Trade Engine
        ↓
Portfolio / Daily Summaries
        ↓
Learning / Calibration Reports
        ↓
Dashboard Read Model
````

## 3.2 Storage principle

Every major stage should produce explicit artifacts, not just transient in-memory state.

That means the system should store:

* inputs
* outputs
* state snapshots
* failure records
* daily summaries
* learning reports
* review decisions

If an important stage cannot be reconstructed from artifacts, the architecture is too weak.

---

# 4. Root Folder Structure

Recommended root under the future module area:

```text
future_modules/
  the_fade/
    README.md
    module_spec.md
    docs/
    schemas/
    prompts/
    scripts/
    config/
    examples/
    tasks/
    inputs/
    outputs/
    state/
    logs/
    replay/
    dashboard_contract/
```

If you decide to keep the current stock lane physically under `future_modules/stock_module/`, that is still possible during transition, but the clean target architecture is a dedicated `the_fade/` root.

---

# 5. Canonical Folder Responsibilities

## 5.1 `docs/`

Purpose:

* human-readable documentation
* overview docs
* specs
* checklists
* revision notes

Contains:

* system overview
* build checklist
* signal engine spec
* architecture/storage spec
* trading/review spec
* dashboard spec
* revision/change notes

Rules:

* docs are canonical for design intent
* docs must not be used as runtime state
* generated artifacts do not belong here

---

## 5.2 `schemas/`

Purpose:

* machine-readable contracts

Contains:

* task packet schema
* normalized event schema
* lane scorecard schema
* signal packet schema
* conflict packet schema
* trade candidate schema
* paper trade schema
* daily summary schema
* learning report schema
* portfolio snapshot schema

Rules:

* schemas are canonical for validation
* code and docs must conform to schemas
* schema changes require explicit versioning

---

## 5.3 `prompts/`

Purpose:

* stored prompt templates for worker/scorer/research logic if prompt-based steps are used

Contains:

* signal extraction prompts
* research prompts
* risk gate prompts
* calibration prompts

Rules:

* prompts are implementation assets, not product truth
* prompts must not silently supersede schema or policy rules

---

## 5.4 `scripts/`

Purpose:

* executable entrypoints and helper scripts

Contains examples:

* scanner runner
* source adapter runners
* signal engine runner
* signal packet validator
* research runner
* risk gate runner
* paper trade runner
* daily summary generator
* replay runner

Rules:

* scripts must read/write explicit artifacts
* scripts should not hide core state in memory-only flows
* script output paths must be deterministic

---

## 5.5 `config/`

Purpose:

* runtime-safe configuration and policy files

Contains:

* lane registry
* direction-model registry
* threshold/weight policy
* escalation policy
* scanner policy
* paper-trade simulation policy
* live-readiness policy

Rules:

* these are mutable policy artifacts, but changes must be tracked
* policy changes must never be hidden
* policy files should be versioned or timestamped where appropriate

### Safety Governor Policy

The config layer must include a machine-readable **Safety Governor Policy** file.

Recommended file:
- `config/safety_governor_policy.json`

### Purpose
This file acts as the hard-limit and kill-switch authority for the autonomous or semi-autonomous system.

### It should define limits such as:
- max drawdown
- max daily loss
- max trade frequency
- max exposure per ticker
- max exposure per sector
- max autonomy level allowed
- auto-fallback-to-manual triggers
- engine failover thresholds
- stale-data stop conditions
- route-block conditions

### Hard rule
The Safety Governor Policy must override:
- autonomous routing
- autonomous calibration
- paper-trade continuation
- future live-trade logic

If the Safety Governor is triggered, the system must:
- block or pause autonomous action
- log the event
- surface the event in health state
- optionally route to manual review

---

## 5.6 `examples/`

Purpose:

* example packets and outputs for reference

Contains:

* example task packet
* example normalized event
* example signal packet
* example conflict packet
* example paper trade
* example daily summary
* example learning report

Rules:

* examples are reference only
* examples are not runtime state
* examples must be clearly labeled as examples

---

## 5.7 `tasks/`

Purpose:

* worker job packets and their task-level lifecycle

Recommended subfolders:

```text
tasks/
  queued/
  in_progress/
  done/
  escalated/
```

Contains:

* task packets
* task-level result links
* task-level status metadata

Rules:

* moving a task across these folders should reflect real lifecycle state
* task result packets should not be the only record of task progression

---

## 5.8 `inputs/`

Purpose:

* explicit input artifacts prepared for runtime use

Contains:

* candidate lists
* manually seeded asset lists
* prebuilt signal tasks
* approved handoff packets into research/trading layers

Rules:

* inputs should be stable and replayable
* inputs must not be confused with task status folders
* if generated by a prior stage, provenance should be preserved

### Ghost Lane Registry

The system should maintain a **Ghost Lane Registry** as a control-group mechanism.

Recommended file:
- `inputs/ghost_lane_registry.json`

### Purpose
The Ghost Lane records what the system would have done if it ignored some or all policy/risk restrictions.

This provides a comparison layer to evaluate whether:
- the active rules are too strict
- the active rules are too loose
- the system is overfit
- the policy engine is blocking too much or too little

### Important distinction
Ghost Lane output is observational only.

It must not:
- place trades
- override live policy
- override safety limits
- silently influence active execution

### Recommended fields
- `ghost_decision_id`
- `signal_packet_id`
- `would_route_to`
- `would_trade`
- `would_size`
- `blocked_by_policy_reason`
- `blocked_by_safety_reason`
- `created_at`

### Storage rule
Ghost Lane decisions should be linkable to:
- actual routed decision
- actual trade candidate decision
- final paper-trade result if applicable

This creates a real control group for later calibration analysis.

---

## 5.9 `outputs/`

Purpose:

* immutable or near-immutable result artifacts from system runs

Recommended subfolders:

```text
outputs/
  scanner/
  normalized_events/
  scorecards/
  signal_packets/
  conflict_packets/
  research/
  risk_gate/
  paper_trades/
  daily_summaries/
  learning_reports/
```

Rules:

* outputs should be timestamped or uniquely identified
* outputs should not be silently rewritten in place
* each output type should have a schema-backed structure

---

## 5.10 `state/`

Purpose:

* current machine-readable local state

Contains:

* latest portfolio snapshot
* latest open positions snapshot
* latest signal queue summary
* latest system health summary
* latest lane reliability summary
* latest dashboard-oriented aggregated state

Rules:

* `state/` is mutable
* `outputs/` is historical/artifact-oriented
* `state/` should summarize current truth without destroying historical output traceability

---

## 5.11 `logs/`

Purpose:

* runtime logs and operational traces

Contains:

* execution logs
* adapter logs
* validation logs
* failure traces

Rules:

* logs are not canonical business state
* logs should support debugging, not replace structured outputs

---

## 5.12 `replay/`

Purpose:

* replay cases, test cases, and offline evaluation artifacts

Contains:

* replay input sets
* replay expected outputs
* regression scenarios
* look-ahead-bias-safe evaluation bundles

Rules:

* replay artifacts must be point-in-time safe
* replay data must not leak future data into past simulations

---

## 5.13 `dashboard_contract/`

Purpose:

* explicitly define what the dashboard is allowed to read

Contains:

* dashboard view schemas
* aggregation contracts
* dashboard read-model notes
* route-specific field expectations

Rules:

* dashboard should read structured data, not scrape arbitrary files
* dashboard expectations should be explicit, not implied

---

# 6. Canonical Artifact Types

## 6.1 Task packet

Purpose:

* one unit of scout work

Suggested filename:

* `fade_task_<task_id>.json`

Suggested location:

* `tasks/queued/`
* later moved to `tasks/in_progress/`, `tasks/done/`, or `tasks/escalated/`

---

## 6.2 Normalized event set

Purpose:

* point-in-time normalized event collection for one task/ticker scope

Suggested filename:

* `normalized_events_<task_id>.json`

Suggested location:

* `outputs/normalized_events/`

---

## 6.3 Lane scorecard set

Purpose:

* lane-level scores for one task/ticker scope

Suggested filename:

* `lane_scorecards_<task_id>.json`

Suggested location:

* `outputs/scorecards/`

---

## 6.4 Signal packet

Purpose:

* final scout output for one signal decision

Suggested filename:

* `signal_packet_<task_id>_<ticker>.json`

Suggested location:

* `outputs/signal_packets/`

---

## 6.5 Conflict packet

Purpose:

* explicit conflict-oriented result when fusion cannot cleanly resolve the signal

Suggested filename:

* `conflict_packet_<task_id>_<ticker>.json`

Suggested location:

* `outputs/conflict_packets/`

---

## 6.6 Research brief

Purpose:

* downstream deep-dive artifact for selected signals

Suggested filename:

* `research_brief_<signal_packet_id>.json`

Suggested location:

* `outputs/research/`

---

## 6.7 Risk gate review

Purpose:

* downstream skeptical review for a brief

Suggested filename:

* `risk_gate_review_<signal_packet_id>.json`

Suggested location:

* `outputs/risk_gate/`

---

## 6.8 Trade candidate

Purpose:

* explicit operator-reviewed trade candidate

Suggested filename:

* `trade_candidate_<signal_packet_id>.json`

Suggested location:

* `inputs/` or `outputs/paper_trades/` depending on workflow style

Recommended rule:

* if it is an input to the paper-trade engine, store a source copy in `inputs/`
* if it is a finalized artifact, store a result copy in `outputs/paper_trades/`

---

## 6.9 Paper trade record

Purpose:

* simulated position/trade lifecycle artifact

Suggested filename:

* `paper_trade_<paper_trade_id>.json`

Suggested location:

* `outputs/paper_trades/`

---

## 6.10 Portfolio snapshot

Purpose:

* current paper portfolio/account state

Suggested filename:

* `portfolio_snapshot_latest.json`
* optionally historical snapshots:

  * `portfolio_snapshot_<timestamp>.json`

Suggested location:

* `state/`

Historical copies may also be written to:

* `outputs/paper_trades/`

---

## 6.11 Daily summary

Purpose:

* operator-readable end-of-day summary

Suggested filenames:

* `daily_summary_<date>.json`
* `daily_summary_<date>.md`

Suggested location:

* `outputs/daily_summaries/`

---

## 6.12 Learning report

Purpose:

* calibration recommendations and performance analysis

Suggested filename:

* `learning_report_<period_end>.json`

Suggested location:

* `outputs/learning_reports/`

---

# 7. State vs Output Rules

## 7.1 `outputs/` rule

`outputs/` is for historical result artifacts.

Properties:

* mostly immutable
* timestamped or uniquely identified
* auditable
* replayable

## 7.2 `state/` rule

`state/` is for current mutable truth.

Properties:

* latest snapshot
* dashboard-friendly
* easy to read
* may be replaced by newer snapshots

## 7.3 Critical distinction

If the system only has `state/`, it loses history.
If the system only has `outputs/`, it becomes hard to read “current truth.”

You need both.

---

# 8. File Ownership Rules

## 8.1 Canonical ownership map

| Area                       | Canonical Owner       |
| -------------------------- | --------------------- |
| design intent              | `docs/`               |
| machine contracts          | `schemas/`            |
| runtime policy             | `config/`             |
| executable logic           | `scripts/`            |
| historical results         | `outputs/`            |
| mutable current truth      | `state/`              |
| debug/runtime trace        | `logs/`               |
| replay/testing truth       | `replay/`             |
| dashboard read assumptions | `dashboard_contract/` |

## 8.2 No-crossing rule

No file type should silently act like another.

Examples:

* logs should not act as business state
* docs should not act as runtime storage
* examples should not be mistaken for live outputs
* dashboard should not guess structure by scraping random files

---

# 9. Dashboard Read Model

## 9.1 Principle

The dashboard should read from **structured, stable, explicit data contracts**, not from arbitrary file scraping whenever possible.

## 9.2 Acceptable dashboard sources

The dashboard may read from:

* `state/` aggregated snapshots
* `outputs/` through a defined loader
* `dashboard_contract/` documented view contracts

## 9.3 Discouraged pattern

Do not make the dashboard rely on:

* ad hoc path guessing
* random file discovery without naming rules
* inconsistent packet pairing logic
* uncontrolled latest-by-mtime assumptions unless explicitly defined

## 9.4 Recommended dashboard contract objects

* `signal_review_index`
* `research_review_index`
* `paper_trade_summary`
* `daily_summary_index`
* `system_health_snapshot`

These may live in:

* `state/`
  or
* `dashboard_contract/examples/` for schema reference

---

# 10. Recommended Current-Truth Snapshots

These mutable snapshots should exist in `state/`:

## 10.1 `system_health_snapshot.json`

Fields:

* adapter health
* last successful run times
* stale-source warnings
* schema-validation warnings
* dashboard readiness flags

## 10.2 `signal_queue_snapshot.json`

Fields:

* latest signal packets
* conflict packets
* triage statuses
* unresolved reviews

## 10.3 `portfolio_snapshot_latest.json`

Fields:

* current open positions
* current balance
* realized/unrealized P&L
* exposure

## 10.4 `daily_summary_latest.json`

Fields:

* latest date
* ending balance
* daily P&L
* trades opened/closed
* signal counts
* lane contribution summary

## 10.5 `learning_status_snapshot.json`

Fields:

* most recent learning run
* pending calibration recommendations
* approval status

---

# 11. Suggested Naming Conventions

## 11.1 General rule

Filenames should be:

* deterministic
* grep-friendly
* human-readable
* sortable
* unique enough for replay and audit

## 11.2 Recommended patterns

* `fade_task_<task_id>.json`
* `normalized_events_<task_id>.json`
* `lane_scorecards_<task_id>.json`
* `signal_packet_<task_id>_<ticker>.json`
* `conflict_packet_<task_id>_<ticker>.json`
* `research_brief_<signal_packet_id>.json`
* `risk_gate_review_<signal_packet_id>.json`
* `paper_trade_<paper_trade_id>.json`
* `daily_summary_<yyyy-mm-dd>.json`
* `learning_report_<yyyy-mm-dd>.json`

## 11.3 ID rule

Every key artifact should have a stable ID:

* `task_id`
* `event_id`
* `signal_packet_id`
* `paper_trade_id`
* `learning_report_id`

If an artifact lacks a stable ID, linkage becomes sloppy.

---

# 12. Linkage and Traceability Rules

## 12.1 End-to-end traceability

The system must make it possible to trace:

**scanner candidate → normalized events → lane scorecards → signal packet → research brief → risk gate → trade candidate → paper trade → daily summary → learning report**

## 12.2 Required link fields

At minimum, downstream artifacts should retain:

* source `task_id`
* source `signal_packet_id`
* ticker
* created-at timestamp
* evidence references

## 12.3 Why this matters

Without traceability:

* replay breaks
* daily reporting lies
* learning becomes weak
* operator review becomes guesswork

---

# 13. Policy and Config Storage

## 13.1 Required config files

Recommended files:

* `config/lane_registry.json`
* `config/direction_models.json`
* `config/fusion_policy.json`
* `config/scanner_policy.json`
* `config/escalation_policy.json`
* `config/paper_trade_policy.json`
* `config/live_readiness_policy.json`

## 13.2 Policy file rules

* readable
* version-aware
* explicitly editable
* not silently changed by runtime logic

## 13.3 Change control

Policy changes should produce either:

* a timestamped archive copy
* a change log entry
* or a revision note in canonical docs

---

# 14. Failure Storage Model

## 14.1 Purpose

Failures must be stored in a structured way, not hidden inside logs only.

## 14.2 Recommended failure locations

```text
outputs/
  failures/
    normalization_failures/
    adapter_failures/
    policy_failures/
    packet_validation_failures/
```

## 14.3 Failure artifact structure

Suggested fields:

* `failure_id`
* `stage`
* `task_id`
* `ticker`
* `error_type`
* `error_summary`
* `raw_context_path`
* `created_at`
* `escalation_required`
* `resolved`

## 14.4 Rule

If a failure matters to operator review or downstream correctness, it needs a structured failure artifact, not just a console trace.

---

# 15. Replay and Testing Storage

## 15.1 Purpose

The replay area supports:

* regression
* point-in-time safety
* historical evaluation
* look-ahead bias prevention
* stable proof packs

## 15.2 Recommended structure

```text
replay/
  cases/
  expected_outputs/
  point_in_time_inputs/
  evaluation_reports/
```

## 15.3 Replay rules

* replay inputs must be point-in-time safe
* future data must not leak into historical evaluations
* replay expected outputs should be stored explicitly
* replay must be reproducible

---

# 16. Dashboard Data Flow

## 16.1 Recommended model

The dashboard should not directly depend on every raw artifact type.

Instead:

```text
Raw Outputs → State Snapshots / Review Indexes → Dashboard Views
```

## 16.2 Recommended review indexes

Suggested files in `state/` or `dashboard_contract/`:

* `signal_review_index.json`
* `research_review_index.json`
* `paper_trade_index.json`
* `daily_summary_index.json`

These are aggregated views optimized for dashboard reads.

## 16.3 Why this matters

Without review indexes:

* every dashboard page becomes custom file-parsing logic
* pairing rules get duplicated
* visibility drifts from real state
* operator trust declines

---

# 17. Mutable vs Immutable Artifact Table

| Artifact Type      | Mutable?                                | Recommended Location         |
| ------------------ | --------------------------------------- | ---------------------------- |
| task packet        | mostly no after queue                   | `tasks/`                     |
| normalized events  | no                                      | `outputs/normalized_events/` |
| lane scorecards    | no                                      | `outputs/scorecards/`        |
| signal packet      | no                                      | `outputs/signal_packets/`    |
| conflict packet    | no                                      | `outputs/conflict_packets/`  |
| research brief     | no                                      | `outputs/research/`          |
| risk gate review   | no                                      | `outputs/risk_gate/`         |
| paper trade record | append/update until closed, then freeze | `outputs/paper_trades/`      |
| portfolio snapshot | yes                                     | `state/`                     |
| daily summary      | no after close of day                   | `outputs/daily_summaries/`   |
| learning report    | no                                      | `outputs/learning_reports/`  |
| config policy      | yes with controlled changes             | `config/`                    |
| docs               | yes with explicit revision              | `docs/`                      |

---

# 18. Recommended MVP Architecture Subset

For the first real proof slice, only these are required:

## Required

* `schemas/` for scout artifacts
* `scripts/` for scanner + signal-engine flow
* `config/` for lane/direction/fusion policy
* `outputs/normalized_events/`
* `outputs/scorecards/`
* `outputs/signal_packets/`
* `outputs/conflict_packets/`
* `state/signal_queue_snapshot.json`
* basic dashboard contract definition for signal review

## Not yet required

* research outputs
* risk gate outputs
* paper trade outputs
* daily summaries
* learning reports
* live-readiness policy

This keeps the architecture bounded.

---

# 19. Migration Notes from Current Stock Module

## 19.1 Current reality

The existing stock side-quest already has:

* brief outputs
* risk gate outputs
* review dashboard surfaces
* a pipeline wrapper

## 19.2 Architecture implication

Those artifacts should not be thrown away.

They should be repositioned as downstream outputs under the new architecture.

## 19.3 Clean migration target

Old stock work becomes:

* `outputs/research/`
* `outputs/risk_gate/`
* downstream review pages

THE FADE scout becomes the new front-end producer of signal packets.

---

# 20. Hard Architecture Rules

The following must remain true:

* no business-critical stage is memory-only
* no important result exists only in logs
* no dashboard view depends on undocumented file guessing
* no packet type lacks a schema
* no mutable current snapshot replaces historical outputs
* no hidden runtime mutation rewrites policy files silently
* no “latest by mtime” shortcut should become the only long-term pairing rule unless explicitly documented and justified

---

# 21. Final Summary

This architecture and storage spec defines how THE FADE system should be physically organized.

The key design choices are:

* keep docs, schemas, scripts, state, and outputs separated
* store historical outputs and mutable current state separately
* make dashboard reads explicit through review indexes and contracts
* keep all key stages traceable and replayable
* store failures structurally, not just in logs
* constrain the MVP architecture to the scout layer first
* reposition existing stock-module research/risk artifacts as downstream layers, not the primary worker

If this architecture is followed, the system stays:

* auditable
* bounded
* understandable
* replayable
* dashboard-friendly
* aligned with Jarvis worker discipline

---

