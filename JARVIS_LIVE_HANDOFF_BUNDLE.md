# JARVIS_LIVE_HANDOFF_BUNDLE.md

## Live Doc Status
- Last reviewed: 2026-03-13
- Last updated: 2026-03-13
- Status: active live handoff bundle for current Jarvis hardening state

## FILE: JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3
````md
# JARVIS Multi-Agent Development System
## System Source of Truth

**Version:** v3.0  
**Date:** March 9, 2026  
**Status:** Current authoritative decisions  
**Use:** Final reference for architecture, constraints, and phase-1 rules

---

## 1. Purpose of This Document

This file records the hard decisions that govern the Jarvis rebuild.

It exists so the project does not drift every time a new idea sounds exciting.

If another note, prompt, or conversation conflicts with this file, this file wins until it is intentionally revised.

---

## 2. Core Identity

Jarvis is a **local-first development foreman** for one operator.

Jarvis is not the main builder.
Jarvis is the coordinator that turns project state into bounded work.

The system is meant to help move real projects forward through:

- planning
- packet generation
- worker routing
- verification
- logging
- escalation

The system succeeds by creating **trustworthy progress**, not by sounding autonomous.

---

## 3. Governing Rule

> **Small verified progress beats large speculative progress.**

Everything below follows from that rule.

---

## 4. Architecture Verdict

### 4.1 Phase-1 runtime
**Chosen:** simple Python orchestration script

### 4.2 Phase-1 state model
**Chosen:** markdown + JSON sidecars

### 4.3 Phase-1 coding execution truth
**Chosen:** semi-manual Cursor worker for WCS

### 4.4 Phase-1 verification truth
**Chosen:** Playwright for WCS

### 4.5 Phase-1 activation scope
**Chosen:** WCS planning and proof loop first

### 4.6 Deferred elements
- LangGraph
- project leads
- fully automated coding worker
- n8n autonomous worker
- voice interface
- machine maintenance worker
- dashboard-first work

---

## 5. Phase-1 Mission

The mission of phase 1 is **not** to build the full Jarvis dream.

The mission is to prove one boring loop:

1. state exists
2. Jarvis reads it
3. Jarvis chooses one bounded WCS task
4. Jarvis writes a valid packet
5. task is executed in Cursor
6. result is recorded
7. Playwright QA runs
8. task becomes done or escalated
9. status and logs update correctly

If that loop is not trustworthy, nothing else should be added.

---

## 6. Current Project Priority

### Priority 1
**WCS stabilization and cleanup**

Reason:
- visible value
- bounded UI issues
- clear acceptance criteria
- Playwright is a strong QA path

### Priority 2
**n8n quality improvement design**

Reason:
- important project
- current workflow exists
- quality criteria still too subjective for real automation

### Priority 3
**Future workers**

Only after phase-1 loop stability.

---

## 7. WCS Truth

### 7.1 WCS is the first active build domain
This is the first project where the system must prove it can generate and move real tasks.

### 7.2 WCS task sourcing
Initial WCS backlog categories:

1. Broken
2. Ugly
3. Incomplete
4. Optimization

### 7.3 WCS phase-1 pull rule
Jarvis only pulls from:

- Broken
- Ugly

### 7.4 WCS task size rule
No phase-1 WCS task should require:

- broad redesign
- multi-route change
- database migration
- dependency upgrade
- auth flow rewrite

If it does, the task is too big or wrongly framed.

---

## 8. n8n Truth

### 8.1 n8n is real but deferred
The n8n project matters, but it is not phase-1 execution priority.

### 8.2 Why it is deferred
The system does not yet have a machine-checkable rubric for “better output.”

### 8.3 Activation requirement
Before n8n becomes an active worker path, the build must define:

- output schema
- scoreable quality rubric
- required blocks
- regression tests
- fail conditions

Until then, n8n planning can exist, but n8n automation cannot be trusted.

---

## 9. Worker Truth

### 9.1 Worker rule
Every worker must have:

- purpose
- scope
- input packet
- output contract
- QA path
- escalation rules

### 9.2 No undefined workers
If a worker cannot state those five things clearly, it is not a worker yet. It is just an idea.

### 9.3 No self-grading
No worker may certify final success for its own work.

---

## 10. WCS Worker Truth

### 10.1 Current reality
The WCS worker is **semi-manual**.

### 10.2 What that means
- Jarvis writes the packet
- the operator executes the packet in Cursor
- the result is captured back into the system
- QA verifies independently

### 10.3 Why this is correct
It matches current habits, current tooling, and current reliability.

Pretending phase 1 is fully autonomous coding would be fake autonomy.

---

## 11. State Truth

### 11.1 Markdown remains mandatory
The operator must be able to inspect and edit state directly.

### 11.2 JSON remains mandatory
Scripts must not depend on scraping prose only.

### 11.3 No premature database
SQLite is not phase-1 state.

If markdown + JSON sidecars become genuinely painful in real use, database adoption can be reconsidered later.

### 11.4 Source-of-truth stance
In phase 1, markdown and JSON sidecars are the official state pair.

---

## 12. File Truth

### Mandatory markdown files

- `MASTER_BACKLOG.md`
- `DAILY_PLAN.md`
- `RUN_LOG.md`
- `PROJECT_STATUS_WCS.md`
- `PROJECT_STATUS_N8N.md`
- `ESCALATIONS.md`
- `AGENT_REGISTRY.md`
- `OPERATING_RULES.md`

### Mandatory JSON files

- `master_backlog.json`
- `daily_plan.json`
- `run_log.json`
- `project_status_wcs.json`
- `project_status_n8n.json`
- `escalations.json`

### Mandatory template files

- `task_packet.template.json`
- `worker_result.template.json`
- `qa_result.template.json`
- `escalation_record.template.json`

---

## 13. Script Truth

### Scripts that must exist in phase 1

1. `jarvis.py`
2. `truth_map_wcs.py`
3. `seed_backlog_wcs.py`
4. `record_worker_result.py`
5. `run_wcs_qa.py`
6. `escalate_task.py`

### What does not need to exist yet

- LangGraph graph definitions
- lead-manager scripts
- voice loop scripts
- machine cleanup scripts
- scheduler-first infrastructure
- dashboard-first infrastructure

---

## 14. Task Packet Truth

Every executable task packet must include:

- task ID
- project
- worker
- title
- problem
- goal
- scope
- suspected files
- acceptance criteria
- QA method
- risk level
- system impact
- stop conditions
- status
- created timestamp

### Why “system impact” is mandatory
A task must declare whether it is expected to touch:

- UI only
- workflow only
- auth
- data
- payment
- deployment
- shared infra

This is a hard risk-control field, not optional flavor text.

---

## 15. Truth Mapping Truth

Truth mapping is mandatory before broad automation.

### Minimum WCS truth mapping outputs

- repo structure summary
- framework indicators
- scripts and entry points
- route map overview
- component map overview
- obvious fragile areas
- recent known blockers if any

Truth mapping records facts.
It does not generate completion claims.

---

## 16. Failure Policy Truth

### Hard numbers for phase 1

- max planned tasks per cycle: **1**
- max WCS tasks per day: **1**
- planning timeout: **90 sec**
- QA timeout: **300 sec**
- parse retry: **1**
- QA auto-retry: **0**
- consecutive escalations before pause: **2**

### Immediate escalation conditions

- malformed JSON
- missing required packet fields
- target files missing
- task exceeds scope
- unexpected high-risk impact
- QA hard fail
- operator clarification required

### Pause rule
After 2 consecutive active task escalations/failures, pause further execution until review.

---

## 17. Scheduling Truth

Scheduling is **not** phase-1 proof.

The system must first prove:

- planning loop works
- packet contract works
- WCS worker result capture works
- WCS QA works
- escalation handling works

Only after that may scheduling be enabled.

Initial scheduling rule:
- one run
- one task
- no overlap

---

## 18. Voice Truth

Voice is explicitly later-phase work.

The voice layer does not solve the hard problem.
The hard problem is trustworthy orchestration and verification.

Only when the boring loop works should voice be added.

---

## 19. Future Worker Truth

Allowed future workers include:

- error/issues research scout
- content/topic research scout
- n8n workflow/content improver
- local machine maintenance worker
- voice interface worker

Each future worker must satisfy the standard worker rule before activation.

No new worker may be added just to hide a broken core loop.

---

## 20. Build Order Truth

### Week 1 order

#### Days 1–2
- create workspace structure
- create markdown files
- create JSON sidecars
- implement `jarvis.py` planning loop
- implement WCS truth mapping

#### Day 3
- define task packet, worker result, QA result, escalation record templates
- run a mock worker test

#### Days 4–5
- execute one semi-manual WCS task through Cursor
- record worker result

#### Days 6–7
- run Playwright QA
- prove done/fail/escalate transitions
- update run log and project status correctly

### Explicitly rejected for week 1

- building the full agent fleet
- building voice interaction
- building full LangGraph orchestration
- building a dashboard before the loop works
- adding project leads
- pretending n8n quality automation is solved

---

## 21. Expansion Trigger

The system is ready for phase-2 discussion only when:

- 5 or more WCS tasks have completed or escalated through the full loop
- state files remain understandable
- task packets stay stable
- QA catches real issues
- pause/escalation behavior works
- operator trust is increasing, not decreasing

Until then, phase 1 stays phase 1.

---

## 22. Final Statement

Jarvis is not being rebuilt to look intelligent.

Jarvis is being rebuilt to make **controlled, auditable, low-drama progress** on real projects.

That means the phase-1 system must stay small, honest, and verifiable.
```

## FILE: JARVIS_MULTI_AGENT_SYSTEM_PRD_v3
````md
# Jarvis Multi-Agent Development System
## Product Requirements Document (PRD)

**Version:** 3.0  
**Date:** March 9, 2026  
**Status:** Current rebuild baseline  
**Type:** Product definition and implementation direction

---

## 1. Product Overview

The **Jarvis Multi-Agent Development System** is a **local-first development operations system** for one operator running multiple real projects from one workstation.

Jarvis is **not** the main coder.  
Jarvis is the **foreman**.

Jarvis exists to:

- read durable project state
- select the next bounded task
- generate a strict task packet
- route work to the correct worker
- require independent verification
- record outcomes and next actions
- keep progress moving with minimal babysitting

The system is designed around one governing principle:

> **Small verified progress beats large speculative progress.**

### Initial project domains

1. **WCS website**
   - mostly built
   - needs stabilization, cleanup, and completion work
   - current code editing tool is Cursor

2. **n8n voice/content system**
   - working but uneven
   - needs quality improvements for X.com content generation
   - needs a tighter quality rubric before real automation

### Phase-1 architectural truth

Phase 1 is **not** a flashy autonomous multi-agent empire.

Phase 1 is:

- one simple Python orchestration loop
- markdown files for human-readable state
- JSON sidecars for machine-readable state
- one semi-manual WCS worker flow through Cursor
- one independent QA flow through Playwright
- one repeatable proof loop

---

## 2. Product Problem

The user already has tools and projects, but they are fragmented:

- planning is scattered
- priorities drift
- small fixes accumulate
- verification is inconsistent
- project memory is mostly informal
- current AI tooling either over-promises or requires babysitting

Typical AI-agent setups fail because they:

- blur planning, execution, and QA
- hide state inside chats
- lack durable task contracts
- make autonomous claims without evidence
- burn time and money on orchestration theater

Jarvis solves that by creating:

- visible system state
- bounded tasks
- narrow workers
- hard verification gates
- a repeatable daily operating loop

---

## 3. Product Goals

### Primary goals

1. Turn project chaos into a prioritized bounded backlog.
2. Keep durable project state across days and sessions.
3. Generate clear task packets instead of vague missions.
4. Move work through planning → execution → verification → logging.
5. Reduce manual coordination overhead.
6. Keep runtime and API costs controlled.
7. Support future modular workers without redesigning the core.

### Secondary goals

- enable later voice interaction
- support scheduled daily cycles
- preserve local-first control
- keep tooling replaceable
- avoid dependency on one fragile runtime shell

### Non-goals for Phase 1

- full autonomy across multiple repos
- automatic voice conversation
- automatic cleanup of the whole machine
- multi-lead hierarchy
- LangGraph-first orchestration
- a giant all-in-one agent framework

---

## 4. Product Principles

### 4.1 Jarvis is a coordinator, not a worker
Jarvis selects, routes, and records.
Jarvis does not pretend to be the builder, the researcher, and the QA lead at once.

### 4.2 Every task must be bounded
No worker receives a vague instruction like “improve the site.”
Every task packet must define scope, acceptance criteria, and exit conditions.

### 4.3 No worker self-certifies success
Independent verification is mandatory for anything that counts as completed work.

### 4.4 Human-readable state is required
State must remain visible and editable by the operator.

### 4.5 Machine-readable state is also required
Automation must not depend on parsing loose prose only.

### 4.6 Start with the simplest durable runtime
A boring script that survives real use is better than a “smart” framework that collapses under debugging.

---

## 5. Current Architecture Decision

### Phase-1 runtime decision
**Chosen:** simple Python orchestration script

### Phase-1 state decision
**Chosen:** markdown + JSON sidecars

### Phase-1 WCS worker truth
**Chosen:** semi-manual Cursor worker with Jarvis-generated task packets

### First proof-of-work sequence
1. planning loop
2. mock worker loop
3. semi-manual WCS packet through Cursor
4. Playwright QA verification
5. logging and escalation handling

### Deferred items
- LangGraph
- project leads
- fully automated coding worker
- fully autonomous research loops
- voice layer
- machine maintenance worker

---

## 6. Phase-1 Architecture

```text
User
  ↓
Jarvis (python foreman)
  ↓
State files (.md + .json)
  ↓
Task packet
  ↓
Semi-manual WCS worker (Cursor)
  ↓
QA worker (Playwright)
  ↓
Run log / project status / escalation record
```

### Initial active components

- **Jarvis planner/orchestrator**
- **WCS task packet flow**
- **WCS semi-manual Cursor worker**
- **WCS QA worker**
- **truth-mapping scripts**
- **logging + escalation flow**

### Workers deferred but recognized

- **Research Scout**
- **n8n content worker**
- **n8n QA worker**
- **machine maintenance worker**
- **topic research worker**

---

## 7. Worker Model

Each worker must have:

- a defined purpose
- a defined input packet
- an approved scope
- a known output contract
- a verification path
- escalation rules

Every worker contract must answer:

1. What can it touch?
2. What tasks can it accept?
3. What file or process starts it?
4. What output JSON does it return?
5. What does success look like?
6. What causes immediate escalation?

---

## 8. Initial Worker Definitions

### 8.1 WCS Semi-Manual Cursor Worker

**Purpose:** Implement bounded WCS code changes.

**Reality in Phase 1:** Jarvis prepares the packet. A human opens Cursor and executes the task using the packet.

**Why this is correct now:** It is honest, cheap, and buildable this week. Fully automated coding can come later if the packet interface proves stable.

**Allowed tasks:**
- broken UI fixes
- small styling cleanup
- small completion tasks
- minor refactors
- small wiring repairs

**Not allowed:**
- broad redesigns
- multi-page rewrites
- database migrations without explicit approval
- large dependency changes
- repo-wide refactors

**Required outputs:**
- worker result JSON
- changed files list
- short implementation summary
- blocker notes if applicable

---

### 8.2 WCS QA Worker

**Purpose:** Verify that WCS changes actually work.

**Execution path:** Playwright

**Checks may include:**
- route loads
- target elements exist
- target interaction works
- screenshot or layout check where needed
- regression notes

**Required outputs:**
- QA result JSON
- pass/fail status
- evidence location
- issue notes
- retest recommendation

---

### 8.3 n8n Content Worker (recognized, not phase-1 active)

**Purpose:** Improve the n8n content-generation system.

**Current status:** Deferred until the quality rubric is machine-checkable.

**Reason for deferral:** “Better content” is too subjective unless reduced to a measurable rubric.

**Activation requirement:**
- clear output schema
- measurable scoring rubric
- known regression checks
- sample test set

---

### 8.4 Research Scout (recognized, not phase-1 active)

**Purpose:** Investigate errors, docs, and implementation options without editing production code.

**Current status:** Deferred until the planning loop and WCS loop are proven.

---

## 9. Task Packet Requirements

Every task packet must include:

- task ID
- project
- worker type
- title
- problem statement
- desired outcome
- suspected files or scope
- acceptance criteria
- QA method
- risk level
- system impact
- stop conditions
- status
- created timestamp

### Example WCS task shape

- **Task ID:** WCS-021
- **Project:** WCS
- **Worker:** wcs-cursor-worker
- **Title:** Fix mobile navbar overlap on home page
- **Problem:** menu overlays hero text at small widths
- **Goal:** navbar collapses without blocking hero
- **Scope:** navbar component and related styles only
- **Acceptance Criteria:** no overlap at mobile width; menu opens and closes correctly
- **QA Method:** Playwright locator + screenshot check
- **Risk:** Low
- **System Impact:** UI only; no auth, DB, or payment impact
- **Stop Conditions:** if fix requires route redesign or large layout rewrite

---

## 10. State Model

### Human-readable state
Markdown files remain the operator-facing source of truth.

### Machine-readable sidecars
JSON sidecars make planning, routing, logging, and QA reliable.

### Phase-1 rule
No critical automation decision may depend only on free-form markdown prose.

---

## 11. Core Files

### Required markdown files

- `MASTER_BACKLOG.md`
- `DAILY_PLAN.md`
- `RUN_LOG.md`
- `PROJECT_STATUS_WCS.md`
- `PROJECT_STATUS_N8N.md`
- `ESCALATIONS.md`
- `OPERATING_RULES.md`
- `AGENT_REGISTRY.md`

### Required JSON files

- `master_backlog.json`
- `daily_plan.json`
- `run_log.json`
- `project_status_wcs.json`
- `project_status_n8n.json`
- `escalations.json`

### Required task folders

- `tasks/open/`
- `tasks/in_progress/`
- `tasks/done/`
- `tasks/failed/`
- `tasks/escalated/`

### Required template folders

- `templates/task_packets/`
- `templates/results/`
- `templates/qa/`

---

## 12. Minimal Phase-1 Scripts

### Must exist in phase 1

1. `jarvis.py`
   - loads backlog and project status
   - chooses next task
   - writes task packet
   - writes daily plan entry
   - appends run log entry

2. `truth_map_wcs.py`
   - scans WCS repo
   - records structure and obvious status signals
   - updates project status files

3. `seed_backlog_wcs.py`
   - creates initial bounded WCS backlog items

4. `record_worker_result.py`
   - ingests worker result JSON
   - updates task state

5. `run_wcs_qa.py`
   - triggers Playwright verification
   - writes QA result JSON

6. `escalate_task.py`
   - records failure or human-intervention need

### Nice to have later

- `truth_map_n8n.py`
- `daily_summary.py`
- `cost_report.py`
- `health_check.py`

---

## 13. Failure and Escalation Policy

### Phase-1 limits

- **Max planned tasks per cycle:** 1
- **Max WCS tasks per day:** 1 initially
- **Planning timeout:** 90 seconds
- **QA timeout:** 300 seconds
- **Automatic retries for transient parsing issues:** 1
- **Automatic retries for failed QA:** 0
- **Consecutive escalations before pausing the system:** 2

### Immediate escalation conditions

- malformed worker result JSON
- missing required task fields
- required target files not found
- QA hard fail
- task exceeds allowed scope
- task affects unexpected high-risk areas
- operator clarification required

### Phase-1 pause rule

If 2 consecutive active tasks escalate or fail verification, the system pauses new execution and writes a pause note to `ESCALATIONS.md` and `escalations.json`.

---

## 14. Verification Model

### Verification rule
Anything recorded as complete must have evidence.

### WCS evidence examples
- Playwright pass/fail
- screenshot file path
- route check result
- relevant notes

### n8n rule for later activation
n8n work cannot be promoted to “completed” until the rubric is machine-checkable.

---

## 15. Scheduling Strategy

Scheduling is **not** the first proof.

Phase 1 proves the loop manually.

Scheduling becomes active only after:

- planning loop is stable
- task packet contract is stable
- WCS QA flow is stable
- escalation logic is stable

When scheduling is introduced, it should start with:

- 1 daytime cycle
- 1 task max
- no overlapping runs

---

## 16. Voice Strategy

Voice is explicitly deferred.

### Why
Voice is a UX layer, not the core operating problem.

### Later design
- speech-to-text in
- Jarvis reads logs and status
- Jarvis responds in text
- text-to-speech reads summary aloud

This is phase-later work only.

---

## 17. Success Criteria

Phase 1 is successful when the following loop works cleanly:

1. backlog item exists
2. Jarvis selects it
3. Jarvis writes a valid task packet
4. human executes the packet in Cursor
5. worker result is recorded
6. Playwright QA runs
7. task is marked done or escalated
8. project status and run log update correctly

If this loop does not work, the system is not ready for more workers.

---

## 18. Future Expansion

Future workers can be added if they provide:

- a bounded purpose
- a strict input packet
- a strict output contract
- a known QA path
- escalation rules
- low-risk activation plan

Likely future workers:

- research scout for debugging
- research scout for content/topic gathering
- n8n workflow/content improver
- local machine maintenance worker
- voice interaction layer

Expansion happens only after the phase-1 loop is stable.

---

## 19. Final Product Position

This system is not an AI toy.

It is a **development operations layer** that coordinates work across real projects with visible state, bounded tasks, and independent verification.

The product does not win by sounding intelligent.

It wins by making boring, trustworthy progress.
```

## FILE: JARVIS_SYSTEM_DOCUMENTATION_v3
````md
# JARVIS Multi-Agent Development System
## Master Documentation

**Version:** v3.0  
**Date:** March 9, 2026  
**Status:** Current operating documentation for the rebuild  
**Audience:** Operator / developer / future maintainer

---

## Table of Contents

1. Purpose
2. What Jarvis Is
3. What Jarvis Is Not
4. Current Build Decision
5. Operating Philosophy
6. Phase-1 Architecture
7. Workspace Layout
8. Core Files
9. JSON Sidecars
10. Task Packet Standard
11. Truth Mapping
12. WCS Operating Flow
13. QA Operating Flow
14. n8n Status
15. Failure Handling
16. Cost Controls
17. Scheduling Rules
18. Future Modules
19. Build Order
20. Glossary

---

## 1. Purpose

This document explains how the rebuilt Jarvis system is supposed to work **right now**, not as a fantasy future version.

It exists to answer:

- what the system is
- how phase 1 really works
- what files matter
- what the first proof loop is
- what is intentionally deferred
- how to add future workers without wrecking the core

---

## 2. What Jarvis Is

Jarvis is a **small local orchestration layer**.

In phase 1, Jarvis is a **Python foreman script** that reads file-based state, chooses the next bounded task, writes a task packet, records progress, and enforces escalation rules.

Jarvis owns:

- planning
- task selection
- task packet generation
- logging
- state updates
- escalation decisions

Jarvis does **not** own:

- making big code changes itself
- verifying its own work
- broad repo roaming
- unsupervised multi-task execution
- fake “autonomous company” behavior

---

## 3. What Jarvis Is Not

Jarvis is not:

- a full coding agent in phase 1
- a LangGraph deployment in phase 1
- a voice assistant in phase 1
- a general machine-admin bot in phase 1
- a replacement for your judgment
- an excuse to skip verification

If the system cannot perform one boring loop reliably, it is not ready for any glamorous features.

---

## 4. Current Build Decision

### Hard choices already made

| Area | Current decision |
|---|---|
| Runtime | Simple Python script |
| State model | Markdown + JSON sidecars |
| WCS builder | Semi-manual Cursor workflow |
| WCS QA | Playwright |
| n8n worker | Deferred until rubric is machine-checkable |
| LangGraph | Deferred |
| Voice | Deferred |
| Scheduling | Deferred until manual loop is stable |
| Project leads | Deferred |

### Why this is correct

Because it is buildable, debuggable, cheap, and honest.

Anything more ambitious at this stage is ceremony.

---

## 5. Operating Philosophy

### The five rules

1. **One task at a time**
2. **No vague missions**
3. **No self-certified success**
4. **Visible state beats hidden context**
5. **Cheap boring progress beats expensive agent theater**

### Translation into practice

That means:

- one active task packet per cycle
- clear acceptance criteria
- JSON outputs where machines need certainty
- markdown where humans need readability
- no launching new workers just because it sounds cool

---

## 6. Phase-1 Architecture

```text
workspace-jarvis/
  ├─ brain/
  │   ├─ markdown state
  │   └─ json sidecars
  ├─ tasks/
  │   ├─ open
  │   ├─ in_progress
  │   ├─ done
  │   ├─ failed
  │   └─ escalated
  ├─ scripts/
  │   ├─ jarvis.py
  │   ├─ truth_map_wcs.py
  │   ├─ seed_backlog_wcs.py
  │   ├─ record_worker_result.py
  │   ├─ run_wcs_qa.py
  │   └─ escalate_task.py
  ├─ templates/
  ├─ reports/
  └─ qa/
```

### Runtime picture

```text
backlog + status files
        ↓
      jarvis.py
        ↓
   task packet written
        ↓
 human executes in Cursor
        ↓
 worker result captured
        ↓
 Playwright QA runs
        ↓
 done / failed / escalated
        ↓
 logs + status updated
```

This is the first real operating loop.

---

## 7. Workspace Layout

Recommended top-level layout:

```text
workspace-jarvis/
  brain/
    MASTER_BACKLOG.md
    DAILY_PLAN.md
    RUN_LOG.md
    PROJECT_STATUS_WCS.md
    PROJECT_STATUS_N8N.md
    ESCALATIONS.md
    AGENT_REGISTRY.md
    OPERATING_RULES.md
    master_backlog.json
    daily_plan.json
    run_log.json
    project_status_wcs.json
    project_status_n8n.json
    escalations.json

  tasks/
    open/
    in_progress/
    done/
    failed/
    escalated/

  templates/
    task_packet.template.json
    worker_result.template.json
    qa_result.template.json
    escalation_record.template.json

  scripts/
    jarvis.py
    truth_map_wcs.py
    seed_backlog_wcs.py
    record_worker_result.py
    run_wcs_qa.py
    escalate_task.py

  qa/
    playwright/
      tests/
      screenshots/
      reports/

  reports/
    daily/
    qa/
    truth_maps/
```

---

## 8. Core Files

### Markdown state files

#### `MASTER_BACKLOG.md`
Human-readable backlog view.
Should group WCS backlog by:

- Broken
- Ugly
- Incomplete
- Optimization

Phase 1 should only pull from:

- Broken
- Ugly

#### `DAILY_PLAN.md`
Shows the current selected task and why it was chosen.

#### `RUN_LOG.md`
Append-only human-readable log of runs, task selection, outcomes, and escalation notes.

#### `PROJECT_STATUS_WCS.md`
Repo truth snapshot, major areas, known risks, recent changes, and current confidence.

#### `PROJECT_STATUS_N8N.md`
Current known facts only. This project remains partially deferred until its quality rubric is formalized.

#### `ESCALATIONS.md`
Human-readable record of failures, pauses, operator intervention needs, and unresolved blockers.

### JSON sidecars

The JSON files mirror the operational parts of the markdown files and should be treated as the machine-facing contract.

---

## 9. JSON Sidecars

### Why sidecars exist

Markdown is good for people.  
JSON is good for scripts.

Using both avoids two bad outcomes:

- unreadable state hidden in a database too early
- brittle automation trying to scrape loose prose only

### Required sidecars

- `master_backlog.json`
- `daily_plan.json`
- `run_log.json`
- `project_status_wcs.json`
- `project_status_n8n.json`
- `escalations.json`

### Rule

Any field that affects routing, verification, escalation, or status transitions must exist in JSON.

---

## 10. Task Packet Standard

### Minimum packet fields

Every task packet must contain:

- `task_id`
- `project`
- `worker`
- `title`
- `problem`
- `goal`
- `scope`
- `suspected_files`
- `acceptance_criteria`
- `qa_method`
- `risk_level`
- `system_impact`
- `stop_conditions`
- `status`
- `created_at`

### Example packet shape

```json
{
  "task_id": "WCS-021",
  "project": "WCS",
  "worker": "wcs-cursor-worker",
  "title": "Fix mobile navbar overlap on home page",
  "problem": "Menu overlaps hero copy at small widths",
  "goal": "Navbar collapses cleanly without blocking hero content",
  "scope": "Navbar component and related mobile styles only",
  "suspected_files": [
    "components/navbar.tsx",
    "app/page.tsx",
    "app/globals.css"
  ],
  "acceptance_criteria": [
    "No overlap at mobile width",
    "Menu opens and closes correctly",
    "Hero content remains visible"
  ],
  "qa_method": "Playwright locator + screenshot",
  "risk_level": "low",
  "system_impact": "UI only; no auth, payment, or database changes expected",
  "stop_conditions": [
    "Requires route redesign",
    "Touches unrelated pages",
    "Needs new dependency"
  ],
  "status": "ready",
  "created_at": "2026-03-09T00:00:00"
}
```

---

## 11. Truth Mapping

### What truth mapping is

Truth mapping is the first discipline step before broad automation.

It means:

- scan the repo
- record structure
- identify likely app entry points
- capture scripts/configs
- note obvious risk areas
- update project status files with facts, not guesses

### WCS truth mapping should capture

- top-level folders
- framework indicators
- package scripts
- routing structure
- component structure
- key config files
- current test status if known
- likely fragile areas
- excluded areas if any

### Truth mapping outputs

- markdown summary in `PROJECT_STATUS_WCS.md`
- JSON summary in `project_status_wcs.json`
- optional report under `reports/truth_maps/`

### What truth mapping should not do

- invent architecture
- rewrite code
- mark tasks done
- make quality claims without evidence

---

## 12. WCS Operating Flow

### Phase-1 real flow

1. backlog is seeded
2. truth mapping is performed
3. `jarvis.py` selects the top bounded WCS task
4. Jarvis writes:
   - `DAILY_PLAN.md`
   - `daily_plan.json`
   - task packet file
5. operator opens Cursor and executes the packet
6. worker result is recorded
7. Playwright QA runs
8. task becomes:
   - done
   - failed
   - escalated
9. logs and project status update

### Why semi-manual is correct

Because you already use Cursor, already pay for it, and can get real value without pretending the interface is mature enough for unattended coding.

This is honest progress, not fake autonomy.

---

## 13. QA Operating Flow

### QA inputs

- task packet
- changed files summary
- acceptance criteria
- target route or test target

### QA outputs

- `qa_result.json`
- pass/fail
- evidence path
- issue notes
- retest recommendation

### QA rules

- builder confidence does not matter if QA fails
- failed QA does not auto-retry the code change in phase 1
- QA hard fail triggers escalation
- evidence must be written before a task can be marked complete

### WCS QA examples

- page loads
- button exists
- modal opens
- navigation works
- screenshot looks acceptable
- no overlap / visibility regression

---

## 14. n8n Status

The n8n project is important but under-defined for automation.

### Current decision

n8n remains **recognized but deferred** until the quality rubric is machine-checkable.

### Why

Because “better content” is not enough.  
The system needs measurable checks such as:

- required blocks present
- schema valid
- output length within bounds
- score against a known rubric
- banned failures absent

### Until then

n8n can still exist in the backlog and status files, but it should not be treated as a phase-1 autonomous worker path.

---

## 15. Failure Handling

### Failure types

- malformed JSON output
- missing required packet fields
- missing target files
- QA hard fail
- task exceeds scope
- unclear system impact
- operator input required

### Phase-1 numeric policy

| Policy item | Value |
|---|---|
| Planned tasks per cycle | 1 |
| WCS tasks per day | 1 |
| Planning timeout | 90 sec |
| QA timeout | 300 sec |
| Parse retry | 1 |
| QA auto-retry | 0 |
| Consecutive escalations before pause | 2 |

### Pause rule

Two consecutive escalated or failed active tasks pause further execution until reviewed.

### Escalation record should include

- task ID
- time
- reason
- evidence
- recommended next action
- pause flag

---

## 16. Cost Controls

Cost discipline must be operational, not rhetorical.

### Phase-1 cost rules

- use one LLM decision call per planning cycle where possible
- do not run multiple workers per cycle
- avoid premium model usage for low-value file shuffling
- log model usage if available
- keep phase 1 manual enough to avoid runaway tool churn

### Why this matters

If a project cannot stay understandable and cheap at low scale, it has no business pretending it will scale.

---

## 17. Scheduling Rules

Scheduling is deferred until the manual loop feels trustworthy.

### Scheduling activation requirements

- valid task packets produced consistently
- worker result flow stable
- WCS QA stable
- escalation handling proven
- no silent state corruption

### First scheduled configuration

- one cycle at a fixed time
- one task max
- no overlapping runs
- pause honored automatically

---

## 18. Future Modules

Future workers are allowed, but only if each new worker defines:

- purpose
- scope
- input packet
- output JSON
- QA path
- escalation rules
- activation conditions

### Likely future modules

- error/issues research scout
- X.com content topic researcher
- n8n content improver
- local machine maintenance worker
- voice interface layer

### Expansion rule

Do not add a new worker to compensate for a broken core.

Fix the core first.

---

## 19. Build Order

### The realistic sequence

#### Days 1–2
- create workspace structure
- create markdown files
- create JSON sidecars
- build `jarvis.py` planning loop
- build WCS truth mapping

#### Day 3
- create task packet templates
- create worker result template
- create QA result template
- test mock worker loop

#### Days 4–5
- run one semi-manual WCS task through Cursor
- capture result
- record changed files and notes

#### Days 6–7
- run Playwright QA
- test done/fail/escalate transitions
- update logs and status correctly

### Anything beyond this in week 1 is greed

No voice.  
No LangGraph.  
No extra workers.  
No scheduling hype.

---

## 20. Glossary

### Jarvis
The orchestrator / foreman script.

### Task packet
The bounded machine-readable work order.

### Truth mapping
The fact-gathering repo scan that grounds project state.

### Worker
A narrow executor with known scope and outputs.

### QA worker
The verification layer that checks work independently.

### Sidecar
A JSON file paired with a markdown file for machine-readable state.

### Escalation
A recorded failure, blocker, or operator-intervention event.

### System impact
A statement about what areas a task could affect and why that matters.
```

## FILE: JARVIS_SCRIPT_PROCESS_REFERENCE.md
````md
# JARVIS_SCRIPT_PROCESS_REFERENCE_v2.md

## Purpose

This document defines the **current live Jarvis WCS task execution process** and the **intended future process** the system is being hardened toward.

It is a working reference for:

- how the process works now
- what each script currently does
- what is still manual or semi-manual
- what contracts must be satisfied
- what parts are intended to be automated later
- what guardrails already exist
- what guardrails are still being built

This document is meant to orient a new chat or operator to the **real operating process**, not an idealized version.

---

# System Intent

Jarvis is a **local-first Python foreman/orchestrator**.

Jarvis is **not** the primary coding agent.

The active project is the **WCS website**.

The current Phase 1 architecture is intentionally simple:

- local Python scripts
- JSON as source-of-truth
- Markdown as rendered human-readable view
- Cursor as the current semi-manual worker
- Playwright as the QA layer
- one bounded task at a time
- Git branch correctness enforced as part of task completion

The intended long-term direction is a more automated local-first multi-agent system, but without weakening auditability, branch correctness, or source-of-truth discipline.

---

# Current Operating Truth

## Current WCS loop

The current **proven live WCS task loop** is:

1. Run `jarvis.py` (or `jarvis.py --force` when an intentional fresh selection is required).
2. Jarvis validates selected task execution eligibility from JSON state.
3. Jarvis validates packet/result placeholder contracts and shapes.
4. Jarvis writes/updates daily plan and run-log state.
5. Jarvis generates or reuses task packet artifacts.
6. Jarvis prepares the correct WCS task branch.
7. Jarvis verifies final branch state after prep and reports it.
8. Worker performs a bounded implementation in the WCS repo.
9. Operator verifies the diff and confirms scope is correct.
10. `worker_change_check.py` is run as a read-only worker-boundary validator before commit/finalization.
11. A commit is created on the correct task branch with a clean worktree afterward.
12. The worker result JSON is finalized truthfully (placeholders replaced with factual data).
13. QA is run in the WCS repo using:
    - `npm run build`
    - `npm run test:e2e:smoke`
14. The QA result JSON is finalized truthfully (placeholders replaced with factual data).
15. `stamp_result_timestamp.py` is run once for the worker result file and once for the QA result file.
16. `pre_reconcile_check.py` is run as a read-only readiness gate.
17. `reconcile_task_outcome.py --task WCS-XXX` is run.
18. Reconcile verifies:
    - valid worker result
    - valid QA result
    - expected branch == current branch
    - task branch has committed work and is ahead of `main`
    - repo/task evidence is sufficient
19. Backlog JSON and rendered Markdown are updated from reconcile output.
20. `post_reconcile_validate.py` is run as a read-only validator of final state surfaces.

## Current process reality

### Automated now
- task selection
- daily plan updates
- run log updates
- task packet generation
- WCS branch preparation
- master backlog rendering
- scout normalization into backlog
- timestamp stamping
- reconcile state updates
- branch verification during reconcile

### Semi-manual now
- worker implementation in Cursor or by operator
- worker result JSON content fill-in
- QA command execution
- QA result JSON content fill-in
- Git commit creation in the WCS repo
- terminal output review and go/no-go decisioning

### Not yet fully automated
- direct Python QA entrypoint in the live workspace
- automatic worker result generation from actual implementation activity
- automatic QA result generation from actual test output
- full pre-reconcile readiness checking before script execution
- richer operator-safety prompts and recovery guidance
- unattended end-to-end execution

---

# Governing Rules

## Completion rule

A task must **not** be marked done unless all of the following are true:

1. a worker result file exists
2. the worker result file is truthful and final
3. the worker result status is valid
4. a QA result file exists
5. the QA result file is truthful and final
6. the QA result status is valid and passing
7. the repo changes are committed
8. the repo is on the correct task branch
9. reconcile branch verification passes
10. reconcile completes successfully

## Source-of-truth rule

Where JSON exists, JSON is authoritative for machine decisions.

Markdown is the paired human-readable rendered view.

Logs are evidence and history. Logs are **not** source-of-truth.

## Result timestamp rule

Worker and QA result files should keep `completed_at` blank until their content is final.

The local timestamp helper stamps the real local timestamp afterward.

## Process documentation rule

Whenever a new process change, guardrail, contract, or script behavior is **locked in and live**, the corresponding working process and hardening documentation files in this workspace **must be updated immediately** to match the new reality.

## One-task rule

Phase 1 remains a one-task-at-a-time loop.

The system does not widen scope merely because the repo is already open.

## Contract rule

Result files must use the actual system contracts, not invented statuses.

Placeholder files are not proof of execution.

---

# Core Process Scripts

## 1. `scripts/jarvis.py`

### Role
Phase-1 foreman / orchestrator.

### Current behavior
The current hardened `jarvis.py` foreman loop:

- reads `state/master_backlog.json`
- reads `state/project_status_wcs.json`
- checks whether a task is already selected for the current day
- reuses the selected task unless a forced reselection is requested
- deterministically selects one valid WCS task when selection is needed
- validates that the selected task is currently eligible for execution based on backlog and project status
- validates that task packet/result placeholders exist and are in the expected contract shape (not treated as evidence)
- records durable escalation state when hard failures occur in state loading, selection, packet validation, or branch preparation/verification
- writes/updates:
  - `state/daily_plan.json`
  - `state/DAILY_PLAN.md`
  - `state/run_log.json`
  - `state/RUN_LOG.md`
- triggers task packet generation (or reuse) for the selected task
- triggers task branch preparation for the WCS repo
- verifies final branch state after prep (expected branch, current branch, cleanliness) and records the result
- skips packet regeneration if the artifacts already exist unless force behavior is used

### Current operator-facing output

The current operator-safe output from `jarvis.py` is intended to:

- clearly state whether it reused an existing task or selected a new one (and when `--force` was respected)
- print the selected task id and title
- summarize which plan/log files were updated
- state whether task packet artifacts were generated or reused
- show branch-prep mode, target task branch, and repo path
- show the final branch verification result after prep (expected branch, current branch, dirty/clean)
- warn that generated worker/QA result files are placeholders and **not** proof of execution
- remind the operator of the worker/QA result contracts and allowed statuses
- print an explicit **“TASK IS NOT COMPLETE YET”** handoff block
- print next-step commands for worker implementation, QA, stamping, and reconcile
- remind that process/docs must be updated whenever a new hardening rule or behavior is locked in
- mention when an escalation record was written on hard failure, including paths to `state/escalations.json` and `state/ESCALATIONS.md`

### Escalation state surfaces

`jarvis.py` now maintains durable escalation state:

- `state/escalations.json` — authoritative machine-readable escalation list
- `state/ESCALATIONS.md` — rendered human-readable escalation view

Whenever a hard failure occurs during `jarvis.py` execution (for example invalid JSON state, invalid selected task, partial packet artifacts, packet/placeholder contract mismatch, branch preparation failure, or post-branch-prep branch verification failure), Jarvis appends a new escalation record with:

- timestamp
- task id (when known)
- project
- phase (e.g. `jarvis_state_load`, `jarvis_selection`, `jarvis_packet_validation`, `jarvis_branch_preparation`, `jarvis_branch_verification`)
- severity (`error`)
- status (`open`)
- human_action_required (`true`)
- reason_code (e.g. `invalid_json_state`, `invalid_selected_task`, `partial_packet_artifacts`, `packet_contract_mismatch`, `branch_prepare_failed`, `branch_verification_failed`, `repo_inspection_failed`)
- summary
- details
- recommended next action

`ESCALATIONS.md` is always rendered from `escalations.json`; JSON remains source-of-truth.

### What Jarvis does not currently do
- it does not perform the code change
- it does not run Cursor
- it does not run QA commands
- it does not finalize worker result content
- it does not finalize QA result content
- it does not create Git commits
- it does not stamp timestamps
- it does not reconcile completion by itself

### Current operator reality
If a task was already selected for the day, `jarvis.py` will usually reuse it.

If a fresh selection is intentionally needed, `jarvis.py --force` is required.

### Intended future build direction
Future work for `jarvis.py` is focused on:
- even stronger preflight validation before selection and branch prep
- richer escalation and human-action-required recording into durable state surfaces
- optional automatic generation of worker and QA handoff prompts
- clearer pause/stop behavior when guardrails fail instead of relying on operator memory

---

## 2. `scripts/generate_task_packet.py`

### Role
Task packet generator.

### Current behavior
For a task like `WCS-016`, it generates:
- `tasks/WCS-016_task.json`
- `tasks/WCS-016_task.md`

It also generates placeholder files:
- `results/WCS-016_worker_result.json`
- `qa/WCS-016_qa_result.json`
- `logs/WCS-016_escalation.json`

### Important current truth
The worker and QA result files generated here are placeholders.

Their existence does **not** mean:
- work has been implemented
- QA has been performed
- a task is reconcile-ready

### What this script does not currently do
- it does not fill factual worker result content
- it does not fill factual QA result content
- it does not stamp timestamps
- it does not validate Git state
- it does not prove completion

### Intended future build direction
- stronger packet schema validation
- stronger warnings that placeholder files are not execution proof
- packet generation checks for obvious task/repo baseline mismatch

---

## 3. `scripts/prepare_wcs_task_branch.py`

### Role
Pre-execution Git branch safety step for the WCS repo.

### Current behavior
- reads the configured WCS repo path
- checks current repo branch
- checks dirty state
- refuses unsafe switching when the repo is dirty on the wrong branch
- switches to the correct task branch if it exists
- creates the correct task branch from `main` when needed
- reports:
  - mode
  - current branch
  - target branch
  - dirty state
  - repo path

### Why it exists
This reduces the risk of doing the right task on the wrong branch.

### What this script does not currently prove
- that a commit later exists
- that the worker result is valid
- that reconcile should succeed
- that the repo stayed correct after subsequent operator actions

### Current operator reality
The operator still manually verifies:
- `git branch --show-current`
- `git status`

before implementation begins.

### Intended future build direction
- stronger explicit failure reasons
- optional post-switch verification summary
- better operator messaging when switching away from a previous task branch

---

## 4. `scripts/reconcile_task_outcome.py`

### Role
Final evidence validator and backlog reconciler.

### Current behavior
- requires an explicit task id via `--task WCS-XXX`
- reads the task packet
- reads worker result JSON
- reads QA result JSON
- validates result contracts
- verifies final reconcile conditions
- verifies repo branch state
- verifies task branch commit state
- updates backlog/state if all conditions pass
- re-renders the backlog markdown view
- updates review output where applicable

### Current required worker result statuses
Allowed worker statuses are:
- `worker_complete`
- `blocked`
- `escalated`

Any other worker status is invalid.

### Current required QA result statuses
Allowed QA statuses are:
- `qa_pass`
- `qa_fail`
- `escalated`

Any other QA status is invalid or non-final.

### Current done-path hardening behavior
For a done-path reconcile, the script verifies:
- expected branch matches current branch
- repo path is valid
- branch verification passes
- the task branch has committed work
- the task branch is ahead of `main`
- the worker and QA files satisfy the expected contracts

### Current write behavior
Typically updates:
- `state/master_backlog.json`
- `state/MASTER_BACKLOG.md`
- `state/DAILY_REVIEW.md`

### What this script does not currently do
- it does not guess the task if `--task` is omitted
- it does not create commits
- it does not finalize placeholder result files for the operator
- it does not excuse contract violations
- it does not replace operator review of terminal output

### Current operator reality
Reconcile is only run after:
- work is implemented
- work is committed
- worker result is truthful and final
- QA result is truthful and final
- both results are stamped
- the repo is still on the correct task branch

### Intended future build direction
- pre-reconcile readiness checks before full reconcile (now partially satisfied by `scripts/pre_reconcile_check.py`)
- clearer contract error output
- explicit placeholder-shape rejection earlier in the flow
- optional dry-run / explain mode
- stronger operator-safety guidance before state mutation

---

## 5. `scripts/pre_reconcile_check.py`

### Role

Read-only pre-reconcile readiness gate for a single WCS task.

### Current behavior

For a task id like `WCS-016`, it:

- requires `--task WCS-XXX`
- optionally accepts `--workspace` (defaults from script location)
- verifies that `tasks/WCS-XXX_task.json` exists
- verifies that `results/WCS-XXX_worker_result.json` exists
- verifies that `qa/WCS-XXX_qa_result.json` exists
- validates worker result JSON:
  - parses successfully
  - has matching `task_id`
  - uses an allowed status: `worker_complete | blocked | escalated`
  - status is not `draft`
  - `completed_at` is present and non-blank
- validates QA result JSON:
  - parses successfully
  - has matching `task_id`
  - uses an allowed status: `qa_pass | qa_fail | escalated`
  - status is not `draft`
  - `completed_at` is present and non-blank
- reads `state/project_status_wcs.json` for the WCS repo path
- verifies:
  - repo path exists
  - `git branch --show-current` works
  - expected branch is `jarvis-task-wcs-XXX`
  - current branch matches the expected branch
  - `git status --porcelain` is clean
  - the task branch is ahead of `main` (or `master` when `main` is missing) by at least one commit

### Output and behavior

- prints `PRE-RECONCILE CHECK: PASS` or `PRE-RECONCILE CHECK: FAIL`
- prints the task id
- on PASS, prints:
  - repo path
  - expected branch
  - current branch
  - commits ahead of main/master
  - a concise list of passed checks
- on FAIL, prints a `Failures:` section listing all failed prerequisites
- exits with:
  - code `0` on PASS
  - code `1` on FAIL or malformed input/state
- remains strictly read-only:
  - does not mutate backlog
  - does not stamp results
  - does not write escalations
  - does not call reconcile

### Why it exists

This script provides a blunt, local-first, read-only gate that can be run before `reconcile_task_outcome.py` to confirm that artifacts and repo state appear ready, without mutating any state.

---

## 6. `scripts/post_reconcile_validate.py`

### Role

Read-only post-reconcile validation for a single WCS task.

### Current behavior

For a task id like `WCS-016`, it:

- requires `--task WCS-XXX`
- optionally accepts `--workspace` (defaults from script location)
- verifies state files exist:
  - `state/master_backlog.json`
  - `state/MASTER_BACKLOG.md`
  - `state/DAILY_REVIEW.md`
- validates backlog JSON:
  - parses successfully
  - root is a list
  - exactly one backlog record exists for the task id
  - that record has `project == "WCS"` and `status == "done"`
- validates rendered backlog markdown:
  - file exists and is readable
  - contains the task id
  - contains the task title (if present in backlog JSON)
  - contains a simple, visible “done” indicator on a line that also contains the task id
- validates `DAILY_REVIEW.md`:
  - file exists and is readable
  - contains the task id
- validates worker result and QA result files:
  - `results/WCS-XXX_worker_result.json` exists and parses
  - `qa/WCS-XXX_qa_result.json` exists and parses
  - both `task_id` fields match the requested task id
  - worker status is one of: `worker_complete | blocked | escalated`
  - QA status is one of: `qa_pass | qa_fail | escalated`
  - both `completed_at` fields are present and non-blank

### Output and behavior

- prints `POST-RECONCILE VALIDATION: PASS` or `POST-RECONCILE VALIDATION: FAIL`
- prints `Task: WCS-XXX`
- on PASS, prints:
  - task title (when available)
  - backlog status
  - a concise list of passed checks
- on FAIL, prints:
  - a `Failures:` section
  - every failed prerequisite on its own line
- exits with:
  - code `0` on PASS
  - code `1` on FAIL or malformed input/state
- remains strictly read-only:
  - does not mutate backlog
  - does not rewrite markdown
  - does not stamp results
  - does not write escalations
  - does not call reconcile

### Why it exists

This script provides a blunt, local-first, read-only validator that can be run after `reconcile_task_outcome.py` to confirm that the intended task is actually marked done and visible in the expected state surfaces.

---

## 7. `scripts/stamp_result_timestamp.py`

---

## 8. `scripts/worker_change_check.py`

### Role

Read-only worker change boundary validator for a single WCS task before commit/finalization.

### Current behavior

For a task id like `WCS-016`, it:

- requires `--task WCS-XXX`
- optionally accepts `--workspace` (defaults from script location)
- reads `tasks/WCS-XXX_task.json` to determine expected file scope using a simple Phase 1 rule:
  - prefers an explicit `target_files` list when present
  - otherwise uses a single `target_file` / `file_path` / `file` field when present
  - as a last resort, uses a `notes` field that looks like a single path
- fails bluntly when it cannot determine expected file scope from the task packet
- reads `state/project_status_wcs.json` to resolve the WCS repo path
- verifies the repo path exists
- verifies:
  - `git status --short` works
  - `git diff --name-only` works
  - `git branch --show-current` works
  - expected branch is `jarvis-task-wcs-XXX`
  - current branch matches the expected branch
- gathers changed files from `git status` and `git diff`
- validates changed files:
  - at least one changed file exists
  - every changed file is within the expected file scope derived from the task packet
- validates diff sanity:
  - runs `git diff --unified=0` for each changed file
  - counts simple changed lines per file
  - fails if more than 3 files are changed
  - fails if any single file has more than 40 changed lines (adds+deletes)

### Output and behavior

- prints `WORKER CHANGE CHECK: PASS` or `WORKER CHANGE CHECK: FAIL`
- prints `Task: WCS-XXX`
- on PASS, prints:
  - repo path
  - expected branch
  - current branch
  - expected file scope
  - actual changed files
  - a concise list of passed checks
- on FAIL, prints:
  - a `Failures:` section
  - every failed prerequisite on its own line
- exits with:
  - code `0` on PASS
  - code `1` on FAIL or malformed input/state
- remains strictly read-only:
  - does not mutate backlog
  - does not rewrite markdown
  - does not stamp results
  - does not write escalations
  - does not create commits
  - does not call reconcile

### Why it exists

This script provides a blunt, local-first, read-only worker-boundary validator that can be run before commit/finalization to catch obvious scope drift and suspiciously large diffs for a bounded WCS task.

---

## 9. `scripts/worker_result_validate.py`

### Role

Read-only worker-result schema validator for a single WCS task.

### Current behavior

For a task id like `WCS-016`, it:

- requires `--task WCS-XXX`
- optionally accepts `--workspace` (defaults from script location)
- supports `--mode pre-stamp` (default) and `--mode post-stamp`
- reads `results/WCS-XXX_worker_result.json` and validates:
  - file exists
  - JSON parses and root is an object
  - `task_id` matches the requested task id
  - `status` is one of: `worker_complete | blocked | escalated`
  - `status` is not `draft`
- requires the following fields to exist:
  - `task_id`
  - `status`
  - `executor`
  - `summary`
  - `files_changed`
  - `commands_run`
  - `issues_encountered`
  - `notes`
  - `completed_at`
- validates field content:
  - `executor` is non-blank
  - `summary` is non-blank
  - `files_changed` is a list
  - `commands_run` is a list
  - `issues_encountered` is a list
  - `notes` field exists (content may be blank or non-blank)
  - `files_changed` contains at least one entry when `status == worker_complete`
  - every `files_changed` entry is a non-blank string
- optionally reads `tasks/WCS-XXX_task.json` and derives expected file scope using the same simple Phase 1 rule as `worker_change_check.py`:
  - `target_files` list when present
  - otherwise a single `target_file` / `file_path` / `file`
  - otherwise a `notes` field that clearly looks like a single repo-relative path
- when expected file scope is available, requires every `files_changed` entry to be within that scope; if expected scope cannot be determined, it skips this consistency check instead of failing
- validates `completed_at` based on mode:
  - in `pre-stamp` mode, `completed_at` must be blank
  - in `post-stamp` mode, `completed_at` must be non-blank

### Output and behavior

- prints `WORKER RESULT VALIDATION: PASS` or `WORKER RESULT VALIDATION: FAIL`
- prints `Task: WCS-XXX`
- prints `Mode: pre-stamp` or `Mode: post-stamp`
- on PASS, prints:
  - executor
  - status
  - files_changed
  - a concise list of passed checks
- on FAIL, prints:
  - a `Failures:` section
  - every failed prerequisite on its own line
- exits with:
  - code `0` on PASS
  - code `1` on FAIL or malformed input/state
- remains strictly read-only:
  - does not mutate backlog
  - does not rewrite markdown
  - does not stamp results
  - does not write escalations
  - does not call reconcile

### Why it exists

This script provides a blunt, local-first, read-only worker-result schema validator that can be run before and after timestamp stamping to catch missing or malformed worker-result fields and simple task-scope inconsistencies.

---

## 10. `scripts/qa_result_validate.py`

### Role

Read-only QA-result schema validator for a single WCS task.

### Current behavior

For a task id like `WCS-016`, it:

- requires `--task WCS-XXX`
- optionally accepts `--workspace` (defaults from script location)
- supports `--mode pre-stamp` (default) and `--mode post-stamp`
- reads `qa/WCS-XXX_qa_result.json` and validates:
  - file exists
  - JSON parses and root is an object
  - `task_id` matches the requested task id
  - `status` is one of: `qa_pass | qa_fail | escalated`
  - `status` is not `draft`
- requires the following fields to exist:
  - `task_id`
  - `status`
  - `qa_tool`
  - `summary`
  - `checks_run`
  - `checks_passed`
  - `checks_failed`
  - `artifacts`
  - `notes`
  - `completed_at`
- validates field content:
  - `qa_tool` is non-blank
  - `summary` is non-blank
  - `checks_run` is a list
  - `checks_passed` is a list
  - `checks_failed` is a list
  - `artifacts` is a list
  - `notes` field exists (content may be blank or non-blank)
  - `checks_run` contains at least one entry when `status` is `qa_pass` or `qa_fail`
  - every entry in `checks_run`, `checks_passed`, `checks_failed`, and `artifacts` is a non-blank string
- validates simple internal consistency:
  - when `status == qa_pass`:
    - `checks_failed` is empty
    - `checks_passed` contains at least one entry
  - when `status == qa_fail`:
    - `checks_failed` contains at least one entry
  - when `status == escalated`:
    - does not require non-empty `checks_passed` or `checks_failed` beyond type/shape checks
- validates `completed_at` based on mode:
  - in `pre-stamp` mode, `completed_at` must be blank
  - in `post-stamp` mode, `completed_at` must be non-blank

### Output and behavior

- prints `QA RESULT VALIDATION: PASS` or `QA RESULT VALIDATION: FAIL`
- prints `Task: WCS-XXX`
- prints `Mode: pre-stamp` or `Mode: post-stamp`
- on PASS, prints:
  - `qa_tool`
  - status
  - checks_run
  - a concise list of passed checks
- on FAIL, prints:
  - a `Failures:` section
  - every failed prerequisite on its own line
- exits with:
  - code `0` on PASS
  - code `1` on FAIL or malformed input/state
- remains strictly read-only:
  - does not mutate backlog
  - does not rewrite markdown
  - does not stamp results
  - does not write escalations
  - does not call reconcile

### Why it exists

This script provides a blunt, local-first, read-only QA-result schema validator that can be run before and after timestamp stamping to catch missing or malformed QA-result fields and simple internal inconsistencies.

### Role
Local result finalization helper.

### Current behavior
- accepts a file path argument
- stamps a timestamp into a result JSON field
- defaults to `completed_at` unless another field is specified

### Actual current usage pattern
```powershell
python .\stamp_result_timestamp.py ..\results\WCS-016_worker_result.json
python .\stamp_result_timestamp.py ..\qa\WCS-016_qa_result.json
````

### Important current truth

This script does **not** take `--task-id`.

It stamps one file at a time.

### What this script does not currently do

* it does not validate task semantics
* it does not validate allowed statuses
* it does not reconcile
* it does not repair bad result content

### Current operator reality

This helper is used only after the result file is already finalized and truthful.

### Intended future build direction

* wrapper that stamps worker and QA files together by task id
* optional validation that the file is no longer in draft/template shape before stamping

---

## 6. `scripts/render_master_backlog.py`

### Role

Backlog renderer.

### Current behavior

* reads `state/master_backlog.json`
* renders `state/MASTER_BACKLOG.md`

### Why it exists

This enforces the rule that JSON is authoritative and Markdown follows.

### What this script does not currently do

* it does not select tasks
* it does not reconcile completion
* it does not independently change backlog truth

### Current operator reality

The normal path is:

1. update `master_backlog.json`
2. run the renderer
3. let `MASTER_BACKLOG.md` update from JSON

### Intended future build direction

* automatic render on approved backlog edits
* schema validation before render
* clearer drift detection when rendered markdown is stale

---

## 7. `scripts/run_wcs_scout.py`

### Role

Public-route WCS scout runner.

### Current behavior

* runs the public scout loop
* writes timestamped scout outputs
* feeds scout findings into normalization

### Typical outputs

Under timestamped scout folders:

* public results JSON
* public summary text
* Playwright stdout
* Playwright stderr
* normalization reports

### Why it exists

This turns public-route failures into discoverable backlog work.

### What this script does not currently do

* it does not fix code
* it does not close tasks
* it does not verify worker task completion

### Intended future build direction

* better route-specific grouping
* stronger duplicate suppression
* better scheduled/scored reporting

---

## 8. `scripts/normalize_scout_to_backlog.py`

### Role

Scout defect normalizer.

### Current behavior

* reads scout outputs
* applies noise filtering
* suppresses duplicates already represented in backlog
* inserts new findings into `state/master_backlog.json`
* re-renders `state/MASTER_BACKLOG.md`
* writes normalization output

### Why it exists

It converts scout findings into bounded backlog tasks.

### What this script does not currently do

* it does not implement fixes
* it does not commit repo changes
* it does not mark tasks done

### Intended future build direction

* stronger deduplication
* more robust issue bucketing
* confidence scoring for scout-generated tasks

---

## 9. `scripts/overnight_health_check.py`

### Role

Read-only workspace/repo health check.

### Current behavior

Checks:

* workspace path
* repo path
* dirty repo state
* key tool availability
* basic health conditions

### Why it exists

It provides a low-risk sanity check of the environment.

### What this script does not currently do

* it does not repair failures
* it does not select tasks
* it does not reconcile tasks

### Intended future build direction

* richer guardrail reporting
* escalation/pause integration
* scheduled health polling once the manual loop is more stable
- automatically update the working process/documentation files whenever a new process change, guardrail, contract, or script behavior is locked in
---

# Current QA Reality

## Live workspace truth

The broader source-of-truth documents may still reference a phase-1 Python QA script like `run_wcs_qa.py`, but in the current live workspace the QA path is still effectively operator-driven.

What is actually present and used is:

* saved QA command references
* WCS repo build command
* WCS repo Playwright smoke command
* manual interpretation of test results
* manual update of the QA result JSON

## Current QA flow

The live QA flow is:

1. run:

   * `npm run build`
2. run:

   * `npm run test:e2e:smoke`
3. inspect terminal output
4. update `qa/WCS-XXX_qa_result.json`
5. stamp `completed_at`

## Current QA truth

QA is currently **semi-manual evidence capture**, not a fully automated Python QA runner.

---

# Main WCS Task Loop

## Current proven loop

### Step 1 — Decide task reuse vs fresh selection

* run `jarvis.py`
* or run `jarvis.py --force` if intentional fresh reselection is required

### Step 2 — Generate packet artifacts

Usually triggered by `jarvis.py`

Artifacts include:

* task JSON
* task markdown
* placeholder worker result JSON
* placeholder QA result JSON
* placeholder escalation JSON

### Step 3 — Prepare the task branch

Usually triggered by `jarvis.py`

The goal is to place the WCS repo on:

* `jarvis-task-wcs-XXX`

### Step 4 — Manually verify Git state

In the WCS repo:

* `git branch --show-current`
* `git status`

The repo should be:

* on the correct task branch
* clean before work begins

### Step 5 — Perform worker implementation

The worker implementation currently happens in Cursor or by direct operator action.

The code change must stay bounded to the task scope.

### Step 6 — Verify the diff

The operator inspects the diff to confirm:

* the change is small and in-scope
* unrelated logic was not removed
* the task intent matches the actual file change

### Step 7 — Commit gate

In the WCS repo:

* stage the intended file changes
* commit on the correct task branch
* verify the worktree is clean after commit

### Step 8 — Finalize worker result

The worker result JSON is filled truthfully.

It must include:

* correct task id
* valid worker status
* factual summary
* actual file changes
* actual issues encountered
* `completed_at` still blank until stamping

### Step 9 — Run QA

The operator currently runs:

* `npm run build`
* `npm run test:e2e:smoke`

### Step 10 — Finalize QA result

The QA result JSON is filled truthfully.

It must include:

* correct task id
* valid QA status
* checks actually run
* actual passed/failed items
* notes tied to actual evidence
* `completed_at` still blank until stamping

### Step 11 — Stamp result timestamps

The timestamp helper is run once for the worker result file and once for the QA result file.

### Step 12 — Reconcile the task

The operator runs:

* `reconcile_task_outcome.py --task WCS-XXX`

Reconcile is responsible for final state transition only if all contract and branch checks pass.

### Step 13 — Verify final state

The operator verifies:

* the correct task changed state
* `state/master_backlog.json` is correct
* `state/MASTER_BACKLOG.md` was rendered correctly
* review output was updated as expected

---

# Files Commonly Touched in the Process

## State files

* `state/master_backlog.json`
* `state/MASTER_BACKLOG.md`
* `state/daily_plan.json`
* `state/DAILY_PLAN.md`
* `state/run_log.json`
* `state/RUN_LOG.md`
* `state/DAILY_REVIEW.md`
* `state/project_status_wcs.json`

## Packet and result files

* `tasks/WCS-XXX_task.json`
* `tasks/WCS-XXX_task.md`
* `results/WCS-XXX_worker_result.json`
* `qa/WCS-XXX_qa_result.json`
* `logs/WCS-XXX_escalation.json`

## WCS repo files

* bounded source files under `C:\dev\wcsv2.0-new`
* repo tests and test artifacts where applicable

---

# Result File Contracts

## Worker result JSON

### Allowed statuses

* `worker_complete`
* `blocked`
* `escalated`

### Current truth requirement

A valid worker result must be factual and should include:

* correct task id
* actual execution summary
* real changed file list
* real commands run if tracked
* real issues encountered
* empty `completed_at` until stamped

### Current invalid examples

* `status: "completed"`
* blank placeholder values treated as final
* fake Cursor attribution when the operator actually did the work

---

## QA result JSON

### Allowed statuses

* `qa_pass`
* `qa_fail`
* `escalated`

### Current truth requirement

A valid QA result must be factual and should include:

* correct task id
* actual checks run
* actual pass/fail outcome
* actual notes
* empty `completed_at` until stamped

### Current invalid examples

* default placeholder JSON treated as evidence
* claimed pass with no build/test evidence
* invented artifacts

---

# Current Guardrails

## Already in place

* one-task-per-cycle process
* JSON source-of-truth discipline
* rendered markdown views
* branch-prep before worker execution
* operator verification of branch and clean repo state
* timestamp stamping kept local
* reconcile status contract enforcement
* reconcile branch verification
* reconcile commit-ahead-of-main verification

## Still weak or still manual

* worker-result truthfulness depends on operator discipline
* QA-result truthfulness depends on operator discipline
* current QA execution is not wrapped by a dedicated Python entrypoint
* some docs still describe planned artifacts more than live ones
* task text may drift from actual repo baseline if backlog maintenance is sloppy

---

# Intended Final Automation Map

## Processes intended to be automated later

### Selection and routing

* task eligibility validation
* safer reuse vs force decisioning
* clearer next-step instructions after selection
* stronger backlog/packet contract checks

### Worker handoff

* structured worker prompt generation
* changed-file sanity checks
* allowed-scope enforcement
* worker result schema validation before stamping

### QA handoff

* direct QA command orchestration
* automatic QA result generation from actual build/test outputs
* artifact linking from test outputs
* explicit fail/escalate routing

### Completion controls

* task-level dual-file timestamp stamping
* pre-reconcile readiness validation
* reconcile dry-run or explain mode
* clearer state transition enforcement
* stronger rejection of draft/template evidence

### Safety and reporting

* stronger operator-facing summaries
* pause-after-failure behavior
* daily review improvements
* more robust backlog/render drift checks

## Processes not intended to be fully automated until later

* broad autonomous coding
* vague multi-task execution
* voice-first execution flow
* unattended expansion into other worker domains
* any automation that weakens auditability, source-of-truth discipline, or branch correctness

---

# Process Direction

## What the system is now

The current system is:

* local-first
* partly automated
* partly operator-driven
* auditable
* contract-based
* getting safer through hardening

## What the system is being built toward

The intended final system is:

* more automated
* still local-first
* still auditable
* still branch-safe
* still source-of-truth driven
* more explicit about prerequisites
* less dependent on operator memory
* more resistant to false completion

---

# Bottom Line

The process only counts as progress when it produces **truthful evidence**.

That means:

* the right task was selected
* the right branch was used
* the bounded code change was committed
* the worker result is factual
* the QA result is factual
* timestamps were applied after finalization
* reconcile verified branch and commit state
* backlog truth changed only after all of that passed

Anything weaker than that is not completion. It is noise.

```
```


## FILE: JARVIS_TASK_EXECUTION_CHECKLIST.md
````md
# JARVIS_TASK_EXECUTION_CHECKLIST_v2.md

## Purpose

This checklist defines the **current live execution steps** for a bounded Jarvis WCS task and the **future direction** the process is being hardened toward.

It is intended to be used during task execution.

It is not the architecture reference.  
It is the **operator checklist** for running the loop correctly.

---

# Core Rule

A task is **not complete** unless all of the following are true:

1. Jarvis selected or reused the correct task intentionally
2. The WCS repo is on the correct task branch
3. The code change was made in bounded scope
4. The code change was committed on the correct branch
5. The worker result JSON is truthful and final
6. The QA result JSON is truthful and final
7. Both result files were timestamp-stamped after finalization
8. Reconcile passed
9. Backlog state reflects the correct completed task

---

# Current Live Execution Checklist

## Phase 0 — Decide whether to reuse or force a new task

### Current action
Decide whether today’s already-selected task should be reused or whether a fresh task selection is intentionally needed.

### Current commands
Normal reuse path:
```powershell
python .\jarvis.py
````

Forced reselection path:

```powershell
python .\jarvis.py --force
```

### Current success condition

* Jarvis either intentionally reuses the current day’s task
* or intentionally selects a new one

### Current failure condition

* operator assumes a fresh selection occurred when Jarvis actually reused the existing task
* operator starts work on the wrong task because `--force` was not used when needed

### Current verification

Read the terminal output carefully and confirm:

* whether Jarvis reused or newly selected
* the exact task id
* the exact task title

### Intended future automation

* explicit reuse-vs-force warning output
* stronger pre-selection operator guidance
* safer fresh-selection confirmation path

---

## Phase 1 — Run Jarvis and inspect its output

### Current action

Run Jarvis and confirm it completed the foreman portion of the loop.

### Current success condition

Jarvis should:

* identify the active task
* update daily plan and run log state
* generate or reuse task packet artifacts
* prepare the correct WCS task branch

### Current failure condition

Stop if:

* the wrong task is selected
* packet generation errors occur
* branch-prep errors occur (and escalations are recorded)
* output is ambiguous about what task is active

### Current verification

The terminal output should clearly identify:

* task id
* task title
* packet generation status
* branch-prep result
* target task branch
* whether an escalation record was written and where to find `state/escalations.json` and `state/ESCALATIONS.md`

### Intended future automation

* stronger summary output
* explicit next-step guidance after task selection
* automatic handoff package generation for worker and QA

---

## Phase 2 — Verify branch and repo cleanliness before touching code

### Current action

Go to the WCS repo and verify the repo is on the correct task branch and clean before implementation begins.

### Current commands

```powershell
git branch --show-current
git status
```

### Current success condition

* current branch matches the selected task branch
* working tree is clean

### Current failure condition

Stop if:

* branch is not the expected task branch
* repo is dirty before the task starts
* unrelated changes are present
* repo is in merge/rebase/conflict state

### Current verification

The repo should show:

* the correct `jarvis-task-wcs-XXX` branch
* nothing to commit
* working tree clean

### Intended future automation

* post-branch-prep automatic verification
* stronger script-side warnings for dirty state
* clearer recovery instructions when branch state is unsafe

---

## Phase 3 — Review the task packet before implementation

### Current action

Read the task packet so the implementation stays bounded.

### Current files to review

* `tasks/WCS-XXX_task.json`
* `tasks/WCS-XXX_task.md`

### Current success condition

The packet clearly defines:

* task id
* task title
* intended scope
* target file(s) or area(s)

### Current failure condition

Stop if:

* task scope is unclear
* task title does not match the actual repo baseline
* packet appears stale or misleading
* the requested change is broader than intended

### Current verification

Confirm:

* the implementation target is understood
* the desired change matches the actual current repo state
* the task is still bounded and safe

### Intended future automation

* packet/repo mismatch detection
* packet validation before worker handoff
* explicit allowed-scope enforcement

---

## Phase 4 — Perform the worker implementation

### Current action

Perform the bounded code change in Cursor or by direct operator edit.

### Current success condition

* only the intended file(s) are changed
* the change stays within task scope
* no unrelated cleanup or refactor work is introduced
* the implementation actually matches the task intent

### Current failure condition

Stop if:

* unrelated logic is removed
* multiple unrelated files change
* the task drifts into broader work
* the implementation direction no longer matches the task definition

### Current operator reality

The worker implementation is currently semi-manual.

Cursor may help perform the change, but the operator still validates the result.

### Intended future automation

* structured worker prompts generated from the task packet
* scope-limited changed-file validation
* automated detection of suspiciously broad diffs
* contract-safe worker result generation

---

## Phase 5 — Verify the diff before commit

### Current action

Inspect the diff before staging or committing.

### Current commands

Examples:

```powershell
git status --short
git diff -- path\to\target_file
git diff --unified=5 -- path\to\target_file
```

### Current success condition

* diff is bounded
* only expected file(s) changed
* no unrelated behavior was removed
* the task intent matches the actual code change

### Current failure condition

Stop if:

* diff is much larger than expected
* unrelated code was changed
* the file was partially broken by tool output
* the implementation does not match the selected task

### Current verification

Confirm:

* file count is correct
* changed lines are correct
* no hidden accidental refactor slipped in

### Intended future automation

* automated diff sanity checks (now partially available via `worker_change_check.py`)
* stronger changed-file allowlist validation
* suspicious-diff warning output

---

## Phase 6 — Run worker change boundary check (read-only)

### Current action

Run the read-only worker change boundary validator before committing, to confirm the changed files and diff size stay within the intended task scope.

### Current command

```powershell
python .\worker_change_check.py --task WCS-XXX
```

### Current success condition

* the script exits with code `0`
* output shows `WORKER CHANGE CHECK: PASS`
* current branch matches the expected task branch
* expected file scope matches the task packet
* the actual changed files are within the expected file scope
* the number of changed files is small and each diff is within the allowed size limit

### Current failure condition

Stop and investigate if:

* the script exits with code `1`
* it cannot determine expected file scope from the task packet
* any changed file is outside the expected task scope
* too many files are changed
* any single file has too many changed lines
* the current branch does not match the expected task branch

### Current verification

Confirm:

* the printed task id matches the intended task
* repo path and branch are correct
* expected file scope matches the task’s true intent
* actual changed files list matches what you meant to touch

### Intended future automation

* tighter integration with the commit gate
* clearer reporting when scope drift is detected

---

## Phase 7 — Commit gate

### Current action

Stage and commit the bounded change on the correct task branch.

### Current commands

Examples:

```powershell
git add .\path\to\changed_file
git commit -m "WCS-XXX concise factual message"
git status
```

### Current success condition

* the commit is created on the correct task branch
* the commit message references the task id
* the worktree is clean after commit

### Current failure condition

Stop if:

* nothing is committed
* the commit occurs on the wrong branch
* unrelated files are included
* the worktree remains dirty afterward

### Current verification

Confirm:

* commit succeeded
* current branch is still correct
* `git status` shows a clean worktree after commit

### Intended future automation

* commit-state verification before worker result finalization
* stronger branch/commit summaries
* commit gate helper that refuses unsafe repo state

---

## Phase 7 — Finalize the worker result JSON truthfully

### Current action

Replace the placeholder worker result with factual execution data.

### Current file

* `results/WCS-XXX_worker_result.json`

### Current required worker statuses

Allowed values:

* `worker_complete`
* `blocked`
* `escalated`

### Current success condition

The worker result is truthful and includes:

* correct task id
* valid worker status
* honest executor identity
* factual summary
* actual files changed
* real commands run if tracked
* real issues encountered
* `completed_at` left blank for now (pre-stamp)

### Current failure condition

Stop if:

* status is invalid such as `completed`
* the file is still a blank placeholder
* changed files are missing or false
* executor attribution is false
* `completed_at` is stamped too early

### Current verification

Read the JSON and confirm:

* it matches what actually happened
* it uses a valid worker status
* it still has `completed_at: ""`

### Intended future automation

* direct generation of worker results from validated activity
* automatic rejection of placeholder-shaped worker results

---

## Phase 8 — Validate worker result schema (read-only)

### Current action

Run the read-only worker-result schema validator to confirm the worker result JSON has the required fields and shape.

### Current commands

Pre-stamp mode (before timestamps are applied):

```powershell
python .\worker_result_validate.py --task WCS-XXX --mode pre-stamp
```

Post-stamp mode (after timestamps are applied):

```powershell
python .\worker_result_validate.py --task WCS-XXX --mode post-stamp
```

### Current success condition

* the script exits with code `0`
* output shows `WORKER RESULT VALIDATION: PASS`
* executor and summary are non-blank
* files_changed, commands_run, and issues_encountered are lists
* files_changed is non-empty when status is `worker_complete`
* completed_at matches the expected mode (blank in pre-stamp, non-blank in post-stamp)

### Current failure condition

Stop and investigate if:

* the script exits with code `1`
* any required worker-result fields are missing
* executor or summary are blank
* list fields have the wrong type
* completed_at does not match the expected mode

### Current verification

Confirm:

* the printed task id matches the intended task
* the printed executor and status match what actually happened
* the printed files_changed list matches the real changed files

### Intended future automation

* tighter integration with the worker completion path
* clearer reporting when schema violations are detected

---

## Phase 9 — Run QA

### Current action

Run the live QA commands for the WCS repo.

### Current live QA commands

```powershell
npm run build
npm run test:e2e:smoke
```

### Current success condition

* build passes
* smoke QA passes
* the terminal output clearly supports a pass decision

### Current failure condition

Stop if:

* build fails
* smoke tests fail
* no tests are found unexpectedly
* browsers/dependencies are missing
* output is ambiguous or broken

### Current operator reality

QA is currently semi-manual.

The operator runs the commands and interprets the terminal results.

### Intended future automation

* dedicated Python QA entrypoint
* direct capture of build/test results into QA artifacts
* automatic pass/fail/escalate routing

---

## Phase 9 — Finalize the QA result JSON truthfully

### Current action

Replace the placeholder QA result with factual QA evidence.

### Current file

* `qa/WCS-XXX_qa_result.json`

### Current required QA statuses

Allowed values:

* `qa_pass`
* `qa_fail`
* `escalated`

### Current success condition

The QA result is truthful and includes:

* correct task id
* valid QA status
* actual checks run
* actual checks passed
* actual checks failed
* factual notes
* `completed_at` left blank for now (pre-stamp)

### Current failure condition

Stop if:

* the QA result is still a placeholder
* QA status is invalid
* the claimed checks do not match what was run
* pass/fail reporting is invented
* `completed_at` is stamped too early

### Current verification

Read the JSON and confirm:

* it matches actual QA activity
* it uses a valid QA status
* it still has `completed_at: ""`

### Intended future automation

* direct generation of QA result content from actual command output
* stronger evidence linking from test runs

---

## Phase 10 — Validate QA result schema (read-only)

### Current action

Run the read-only QA-result schema validator to confirm the QA result JSON has the required fields and shape.

### Current commands

Pre-stamp mode (before timestamps are applied):

```powershell
python .\qa_result_validate.py --task WCS-XXX --mode pre-stamp
```

Post-stamp mode (after timestamps are applied):

```powershell
python .\qa_result_validate.py --task WCS-XXX --mode post-stamp
```

### Current success condition

* the script exits with code `0`
* output shows `QA RESULT VALIDATION: PASS`
* qa_tool and summary are non-blank
* checks_run, checks_passed, checks_failed, and artifacts are lists
* checks_run is non-empty when status is `qa_pass` or `qa_fail`
* internal consistency between status, checks_passed, and checks_failed is satisfied
* completed_at matches the expected mode (blank in pre-stamp, non-blank in post-stamp)

### Current failure condition

Stop and investigate if:

* the script exits with code `1`
* any required QA-result fields are missing
* qa_tool or summary are blank
* list fields have the wrong type
* checks_run is empty for `qa_pass` or `qa_fail`
* status-specific checks for checks_passed/checks_failed fail
* completed_at does not match the expected mode

### Current verification

Confirm:

* the printed task id matches the intended task
* the printed qa_tool and status match what actually happened
* the printed checks_run list matches the real checks that were run

### Intended future automation

* tighter integration with the QA execution path
* clearer reporting when schema violations are detected

---

## Phase 11 — Stamp finalized result timestamps

### Current action

Stamp the finalized worker result and QA result files with real local timestamps.

### Current commands

```powershell
python .\stamp_result_timestamp.py ..\results\WCS-XXX_worker_result.json
python .\stamp_result_timestamp.py ..\qa\WCS-XXX_qa_result.json
```

### Current success condition

* both files are stamped successfully
* both files now contain real `completed_at` values

### Current failure condition

Stop if:

* file path is wrong
* JSON is malformed
* stamping is attempted before the file is final
* only one file is stamped and the other is forgotten

### Current verification

Read both files and confirm:

* timestamps are present
* all other fields remain intact
* stamped content is still truthful

### Intended future automation

* task-level dual stamping helper
* refusal to stamp draft/template-shaped files
* stronger output when stamping succeeds or should be blocked

---

## Process documentation rule

Whenever a new process change, guardrail, contract, or script behavior is **locked in and live**, the corresponding working process and checklist documentation in this workspace **must be updated immediately** so execution checklists stay aligned with the real loop.

## Phase 11 — Run pre-reconcile readiness check (read-only)

### Current action

Run the read-only pre-reconcile gate for the selected task to confirm artifacts and repo state look ready before reconcile.

### Current command

```powershell
python .\pre_reconcile_check.py --task WCS-XXX
```

### Current success condition

* the script exits with code `0`
* output shows `PRE-RECONCILE CHECK: PASS`
* repo path, expected branch, current branch, and commits ahead of main/master are printed
* all listed readiness checks are reported as passed

### Current failure condition

Stop and investigate if:

* the script exits with code `1`
* any failures are listed for artifacts, worker result, QA result, or repo/branch state

### Current verification

Confirm:

* the printed task id matches the intended task
* repo path and branch match what you expect
* commits-ahead count is at least 1

### Intended future automation

* tighter integration with reconcile
* optional enforcement that reconcile may only run after a passing pre-reconcile check

---

## Phase 12 — Reconcile the task

### Current action

Run reconcile explicitly for the task.

### Current command

```powershell
python .\reconcile_task_outcome.py --task WCS-XXX
```

### Current success condition

Reconcile should:

* accept the worker result contract
* accept the QA result contract
* verify the repo path
* verify the expected branch
* verify the current branch
* verify committed work exists
* verify the task branch is ahead of `main`
* update backlog state
* render backlog markdown
* update review output where applicable

### Current failure condition

Stop if:

* task id is missing
* worker status is invalid
* QA status is invalid
* result files are missing or malformed
* branch verification fails
* commit verification fails
* reconcile reports an error

### Current verification

Read the terminal output and confirm:

* the correct task was reconciled
* branch verification passed
* commit-ahead-of-main check passed
* state files were updated

### Intended future automation

* dry-run / explain mode
* richer contract error messages
* stronger rejection of placeholder evidence before deep reconcile

---

## Phase 13 — Verify final backlog and rendered state

### Current action

Inspect the resulting state files after reconcile.

### Current files to inspect

* `state/master_backlog.json`
* `state/MASTER_BACKLOG.md`
* `state/DAILY_REVIEW.md`

### Current success condition

* the correct task changed state
* the task is marked appropriately
* no wrong task was mutated
* backlog markdown reflects the JSON truth
* review output is updated as expected

### Current failure condition

Stop if:

* the wrong task changed state
* the task remained in the wrong status after reported success
* backlog JSON and Markdown drift
* state files appear malformed

### Current verification

Confirm:

* selected task id matches the updated done task
* neighboring tasks remain unchanged unless intentionally affected
* rendered markdown matches the JSON update

### Intended future automation

* JSON/Markdown drift detection
* stronger review summary generation

---

## Phase 14 — Run post-reconcile validation (read-only)

### Current action

Run the read-only post-reconcile validator for the reconciled task to confirm that backlog, rendered markdown, review output, and result files all reflect the intended done state.

### Current command

```powershell
python .\post_reconcile_validate.py --task WCS-XXX
```

### Current success condition

* the script exits with code `0`
* output shows `POST-RECONCILE VALIDATION: PASS`
* the printed task title and backlog status match expectations
* the passed-checks list indicates backlog JSON, rendered markdown, review, worker result, and QA result are all consistent

### Current failure condition

Stop and investigate if:

* the script exits with code `1`
* any failures are listed for backlog JSON, MASTER_BACKLOG.md, DAILY_REVIEW.md, worker result, or QA result

### Current verification

Confirm:

* the printed task id matches the reconciled task
* backlog JSON shows the task as done for project WCS
* MASTER_BACKLOG.md and DAILY_REVIEW.md both include the task
* worker and QA results are present, have allowed statuses, and non-blank completed_at

### Intended future automation

* tighter integration with reconcile outcome reporting
* automatic drift detection when backlog JSON and rendered markdown disagree

---

# Current Result Contracts

## Worker result contract

### Allowed worker statuses

* `worker_complete`
* `blocked`
* `escalated`

### Minimum truth requirements

* correct `task_id`
* truthful `status`
* truthful `executor`
* factual `summary`
* real `files_changed`
* actual `commands_run` if tracked
* real `issues_encountered`
* truthful `notes`
* blank `completed_at` until stamping

### Invalid examples

* `status: "completed"`
* blank placeholder treated as final
* fake executor attribution
* fake changed-file reporting

---

## QA result contract

### Allowed QA statuses

* `qa_pass`
* `qa_fail`
* `escalated`

### Minimum truth requirements

* correct `task_id`
* truthful `status`
* truthful `qa_tool`
* factual `summary`
* actual `checks_run`
* actual `checks_passed`
* actual `checks_failed`
* truthful `notes`
* blank `completed_at` until stamping

### Invalid examples

* placeholder JSON treated as final evidence
* pass claim without actual build/test support
* invented artifacts or notes

---

# Current Manual or Semi-Manual Areas

The current process still relies on operator discipline in these areas:

* deciding when to use `--force`
* confirming the selected task is the intended one
* verifying branch and repo cleanliness after branch prep
* validating the actual code diff
* creating the correct Git commit
* filling worker result JSON truthfully
* running build and smoke QA manually
* filling QA result JSON truthfully
* confirming reconcile terminal output is actually correct
* validating final backlog state
* reviewing new entries in `state/ESCALATIONS.json` / `state/ESCALATIONS.md` when Jarvis reports a hard failure

---

# Processes Being Built Toward

## Worker-side improvements

* structured worker handoff prompt generation
* bounded-scope validation before implementation
* automated changed-file sanity checking
* direct worker-result generation from validated execution activity

## QA-side improvements

* dedicated Python QA runner
* automated build/test orchestration
* direct QA-result generation from actual command output
* stronger fail/escalate routing

## Safety improvements

* reuse-vs-force guardrails
* stronger preflight repo checks
* stronger rejection of placeholder result files
* clearer branch/commit status summaries
* pre-reconcile readiness validation

## State and reporting improvements

* more explicit terminal guidance after each stage
* better daily review reporting
* stronger JSON/Markdown drift detection
* clearer operator-facing failure messages
* less dependence on operator memory

---

# Processes Not Intended to Be Fully Automated Yet

These are not current Phase-1 goals:

* broad autonomous coding
* vague multi-task execution
* unattended scope expansion
* voice-first execution flow
* any automation that weakens auditability
* any automation that weakens branch correctness
* any automation that weakens JSON source-of-truth discipline

---

# Current Execution Mindset

The process is considered correct only when:

* the right task is active
* the right branch is active
* the code change is bounded
* the code change is committed
* the worker result is factual
* the QA result is factual
* timestamps are applied after finalization
* reconcile verifies branch and commit state
* backlog truth changes only after all of that passes

Anything less is not completion.

```
```


## FILE: JARVIS_PHASE_CHECKLIST.md
# JARVIS_REBUILD_PHASE_CHECKLIST.md

## Purpose

This checklist summarizes the Jarvis rebuild from the beginning through roughly Phase 3–4, using the project decisions we already locked:

- local-first
- Jarvis as foreman/orchestrator, not main coder
- JSON as machine truth
- Markdown as rendered human view
- WCS as the first active project
- Cursor as the current coding worker
- Playwright as the QA layer
- parent login deferred
- voice deferred
- n8n worker deferred until later

---

# Current broad position

**Current reality:**  
We are **past the reset/foundation stage** and **well into the WCS proof-loop stage**.

### Rough progress by phase
- **Phase 0 — reset / architecture lock:** mostly complete
- **Phase 1 — file/state/script foundation:** mostly complete
- **Phase 2 — WCS semi-manual proof loop:** strong progress, mostly working
- **Phase 3 — true Jarvis foreman loop:** foreman built; daily plan/run log active; live cycles and optional state (escalations, etc.) still in progress
- **Phase 4 — controlled autonomy / more workers:** future

### Short version
We have built a lot of the rails.  
The central Jarvis foreman (`jarvis.py`) is **built and in use**; remaining Phase 3 work is state completeness and proving live Jarvis-controlled cycles.

---

# Phase 0 — Reset and architecture lock

## Goal
Stop chasing fake autonomy and lock the real project shape.

## Checklist
- [x] Decide Jarvis is a **foreman/orchestrator**, not the main coding worker
- [x] Decide the system is **local-first**
- [x] Decide WCS is the **first active proof domain**
- [x] Decide Cursor remains the current semi-manual coding worker
- [x] Decide Playwright is the QA truth for WCS
- [x] Decide phase 1 uses **Python scripts**, not heavy orchestration frameworks
- [x] Decide state uses **JSON as source of truth** and **Markdown as human view**
- [x] Defer parent login area for now
- [x] Defer voice for later phases
- [x] Defer n8n worker until WCS foundation is stronger
- [x] Lock “one bounded task at a time” as the phase-1 operating rule

## Deliverable outcome
- Project direction stopped being vague
- Scope was reduced to something boring and buildable
- The rebuild stopped pretending to be fully autonomous on day one

---

# Phase 1 — Core file/state foundation

## Goal
Create the minimum durable system structure so the project can operate on visible state instead of chat memory.

## Checklist
- [x] Create core source-of-truth docs
- [x] Create machine-readable backlog state
- [x] Create human-readable backlog render
- [x] Establish file registry concept
- [x] Establish project status concept
- [x] Establish logs folder structure
- [x] Establish scripts/config/state folder pattern
- [x] Define WCS backlog categories
- [x] Define “do not mark done without evidence” rule
- [x] Define escalation/pause philosophy
- [x] Initialize local Git repo for `C:\dev\jarvis-workspace`

## Expected files / concepts in this phase
- `master_backlog.json`
- `MASTER_BACKLOG.md`
- `file_registry.json`
- `FILE_REGISTRY.md`
- `project_status_wcs.json`
- `PROJECT_STATUS_WCS.md`
- workspace logs structure
- source-of-truth docs

## Deliverable outcome
- The system has visible state
- The project can now operate from files instead of vague discussion
- The workspace now has basic version history via Git

---

# Phase 2 — WCS semi-manual proof loop

## Goal
Prove one boring loop works cleanly before building more agents.

## Core loop to prove
1. backlog item exists
2. task packet is generated
3. Cursor executes the work
4. result is recorded/reconciled
5. QA runs
6. task becomes done or escalated
7. state updates correctly

---

## Phase 2A — Backlog and packet mechanics

### Checklist
- [x] Build `render_master_backlog.py`
- [x] Confirm `MASTER_BACKLOG.md` renders from `master_backlog.json`
- [x] Build `generate_task_packet.py`
- [x] Build `reconcile_task_outcome.py`
- [x] Confirm task packet generation works
- [x] Confirm reconcile flow works
- [x] Confirm multiple WCS tasks have already moved through the loop successfully

### Deliverable outcome
- The backlog-to-packet-to-reconcile loop is real
- WCS tasks are not just conceptual; they are moving

---

## Phase 2B — QA and scout layer

### Checklist
- [x] Stabilize Playwright home smoke path
- [x] Confirm `WCS-011` QA plumbing is in main
- [x] Build public scout route config
- [x] Build `public_scout.spec.ts`
- [x] Build `run_wcs_scout.py`
- [x] Run public scout successfully
- [x] Filter false positives so Public Scout v1 returns PASS correctly

### Deliverable outcome
- WCS now has a repeatable route-checking and defect-detection layer
- QA/intake is stronger than before
- Public Scout v1 is working

---

## Phase 2C — Defect-to-backlog normalization

### Checklist
- [x] Design defect normalizer in same style as current system
- [x] Build `normalize_scout_to_backlog.py`
- [x] Build `normalize_scout_to_backlog.ps1`
- [x] Build `scout_noise_rules.json`
- [x] Prove clean-run no-op behavior
- [x] Prove synthetic failure insertion behavior
- [x] Prove duplicate suppression behavior
- [x] Integrate normalizer into `run_wcs_scout.py`
- [x] Confirm integrated scout -> normalizer run works cleanly
- [x] Log normalizer output into same timestamped scout log folder

### Deliverable outcome
- Real scout failures can now become backlog-ready tasks
- Known noise can be filtered
- Duplicate tasks can be suppressed
- Defect intake is now partially automated

---

## Phase 2D — Health and operational guardrails

### Checklist
- [x] Build `overnight_health_check.py`
- [x] Run overnight health check successfully
- [x] Confirm overnight health check reports PASS/WARN honestly
- [x] Confirm warning handling is visible and useful
- [x] Keep health check read-only instead of pretending it “fixes” things

### Deliverable outcome
- The system has a basic operational self-check
- Shutdown/startup confidence is better
- Guardrails are present

---

## Phase 2 overall status
### Status: **Mostly complete / strongly working**

### What is proven
- Backlog rendering works
- Task packet generation works
- Reconcile works
- Public scout works
- Overnight health check works
- Defect normalization works
- Several WCS tasks have already been completed successfully

### What is still missing in Phase 2
- More live WCS tasks should continue moving through the loop
- State files still need continued cleanup and consistency work
- Some original planned phase-1 scripts were replaced by practical equivalents and may still need naming cleanup

---

# Phase 3 — Build the true Jarvis foreman

## Goal
Stop relying on manual glue between scripts and create the actual Jarvis planning/orchestration script.

## Status: foreman built and in use

### Checklist
- [x] Build `jarvis.py`
- [x] Have `jarvis.py` load backlog + WCS project status
- [x] Have `jarvis.py` choose exactly **one valid bounded WCS task**
- [x] Enforce pull rules for allowed WCS task categories
- [x] Write a valid task packet automatically
- [x] Write/update `DAILY_PLAN.md`
- [x] Write/update `daily_plan.json`
- [x] Append to `RUN_LOG.md`
- [x] Append to `run_log.json`
- [x] Record the selected task, reason, and timestamp
- [x] Prevent selecting blocked, done, or invalid tasks
- [x] Prevent selecting more than one task per cycle
- [x] Respect initial “max 1 WCS task per day” rule
- [ ] Record when human/operator action is required
- [x] Make Jarvis operate from files/state instead of chat memory

## Optional companion cleanup in Phase 3
- [ ] Decide whether current working scripts keep their present names
- [ ] Or wrap/re-map them to the original planned script naming model
- [ ] Clean drift between “working system” and “planned system” terminology

## Deliverable outcome
- Jarvis becomes a real foreman script
- The system no longer depends on manual operator stitching between every step
- The architecture finally matches the core promise of the project

---

# Phase 3B — Complete the missing state model

## Goal
Finish the state surfaces the docs originally assumed would exist.

### Checklist
- [x] Make `daily_plan.json` real and active
- [x] Make `RUN_LOG.md` real and active
- [x] Make `run_log.json` real and active
- [ ] Make `escalations.json` real and active
- [ ] Make `ESCALATIONS.md` real and active
- [x] Make `project_status_n8n.json` real even if deferred
- [ ] Make `AGENT_REGISTRY.md` real if still part of the intended system
- [ ] Make `OPERATING_RULES.md` real if still part of the intended system
- [ ] Ensure all state files have a clear source-of-truth relationship
- [ ] Ensure no state file is lying or stale

## Deliverable outcome
- The file-based operating model becomes complete
- The system becomes more self-explanatory and durable

---

# Phase 3C — Live Jarvis-controlled WCS cycles

## Goal
Run real WCS work through Jarvis control, not just supporting scripts.

### Checklist
- [x] Jarvis selects a real WCS task
- [x] Jarvis writes a valid packet
- [x] Human executes task in Cursor
- [x] Worker result is captured cleanly
- [x] QA runs against the changed work
- [x] Task becomes done or escalated based on evidence
- [x] Run log updates correctly
- [ ] Project status updates correctly
- [x] Repeat successfully across multiple real tasks (currently proven for WCS-016, WCS-017, WCS-018, and WCS-019 as full completed/reconciled loops)
- [ ] Prove longer-run consecutive-task stability beyond the current four-task proof

## Deliverable outcome
- The boring core loop is now proven for multiple real WCS tasks under Jarvis control (currently WCS-016, WCS-017, WCS-018, WCS-019)

---

# Phase 4 — Controlled autonomy and expansion

## Goal
Only after Phase 3 is stable, turn on more automation carefully.

## Phase 4A — Scheduling / timed runs

### Checklist
- [ ] Enable very limited scheduled cycles
- [ ] Start with one run at a time
- [ ] Prevent overlapping cycles
- [ ] Respect pause/escalation conditions
- [ ] Confirm scheduling does not create duplicate or conflicting work
- [ ] Confirm scheduled runs preserve logs and state correctly

## Deliverable outcome
- Jarvis starts acting on a clock, not just manual launch
- Still boring, controlled, and auditable

---

## Phase 4B — Additional worker types

### Checklist
- [ ] Add research scout for debugging support
- [ ] Add research scout for topic/content gathering if still valuable
- [ ] Revisit n8n improvement worker once rubric is machine-checkable
- [ ] Add truth-mapping helpers for other projects if needed
- [ ] Add additional bounded workers only when packet + output + QA path are clear
- [ ] Refuse to add “cool” workers that do not have a strict contract

## Deliverable outcome
- Jarvis grows from one proof loop into a true multi-worker system
- Expansion happens from stable contracts, not hype

---

## Phase 4C — System hardening and renderer cleanup

### Checklist
- [ ] Build `render_file_registry.py`
- [ ] Stop hand-maintaining `FILE_REGISTRY.md`
- [ ] Add health checks for new critical scripts/configs
- [ ] Harden all script wrappers
- [ ] Standardize output log locations
- [ ] Reduce naming drift across docs/state/scripts
- [ ] Improve evidence reporting and human review surfaces

## Deliverable outcome
- The system becomes easier to maintain and trust over time

---

# Later phases — not now

## These are explicitly later, not current focus
- [ ] voice interface
- [ ] parent login / private family workflows in WCS
- [ ] autonomous n8n worker path
- [ ] broader multi-project scheduling
- [ ] larger agent fleet
- [ ] advanced mission-control dashboards
- [ ] robot/device coordination layers

---

# Practical current checkpoint

## Completed successfully
- [x] Core architecture decisions locked
- [x] WCS chosen as phase-1 proof domain
- [x] Backlog state exists in JSON + Markdown
- [x] Task packet generation works
- [x] Reconcile works
- [x] Playwright QA layer is active
- [x] Public Scout v1 works
- [x] Defect normalizer works
- [x] Overnight health check works
- [x] Local Git repo created for `jarvis-workspace`
- [x] Build `jarvis.py` (foreman selects task, writes daily plan and run log, generates packet, prepares branch)
- [x] Daily plan and run log state files real and active

## Next real priorities
- [ ] Complete escalation state files (`escalations.json` / `ESCALATIONS.md`) and any remaining state surfaces
- [ ] Run real Jarvis-controlled WCS cycles and prove consecutive-task stability
- [ ] Only then consider scheduling
- [ ] Only after that consider more workers

---

# Bottom line

We are **not** at the beginning anymore.

We are also **not** at “Jarvis complete.”

We are roughly here:

- **Foundation:** mostly done
- **WCS support loop:** working
- **QA and defect intake:** strong
- **True Jarvis foreman/orchestrator:** built and in use (`jarvis.py` selects task, writes plan/run log, packet, branch)
- **Scheduling and additional workers:** future

That means the next serious step is not more idea generation.

It is:

## **Run real Jarvis-controlled WCS cycles and complete remaining state (escalations, etc.).**

## FILE: JARVIS HARDENING CONTEXT ANCHOR — CURRENT PRIORITIES_3-12-26.txt
# JARVIS HARDENING CONTEXT ANCHOR — CURRENT PRIORITIES

We are **not** designing Jarvis from scratch.
We are **not** prioritizing sexy features, dashboards, more agents, or broad expansion right now.

We are in the middle of **hardening `jarvis.py`** so the system can move toward **little to zero human interaction** without turning into uncontrolled garbage.

## Current truth

The project already has meaningful working pieces:
- backlog rendering
- task packet generation
- reconcile flow
- public scout / defect normalization
- overnight health check
- real WCS tasks already completed through the system
- `jarvis.py` exists and is active

So the problem is **not** “invent more architecture.”
The problem is:

> the live loop still depends too much on operator discipline.

That means the next work is to convert fragile human checks into enforced system guardrails.

---

# What we are optimizing for

Primary goal:
- **low-human-interaction autonomy**

That means Jarvis must be able to:
1. choose work safely
2. detect when work is not safe to proceed
3. validate artifacts truthfully
4. detect bad repo/task state
5. pause and escalate cleanly
6. reconcile state without corruption

We are aiming for:
- **human exception handling**
- **not human babysitting**

---

# What "hardening jarvis.py" means right now

## Top priority items

### 1. Escalation state completion
Jarvis must formally track:
- blockers
- repeated failures
- pause conditions
- human intervention required
- escalation notes

This should use real state surfaces such as:
- `ESCALATIONS.md`
- `escalations.json`

This is a high priority because autonomy is fake if failures only live in the operator’s head.

---

### 2. Human-action-required recording
`jarvis.py` should explicitly record when it cannot safely proceed and why.

Examples:
- task packet missing
- wrong branch
- repo dirty
- repeated QA failure
- malformed worker result
- malformed QA result
- reconcile not safe
- circuit-breaker condition hit

This should be machine-visible state, not informal terminal commentary.

---

### 3. State-surface completion
Finish and harden the state files and their relationships.

Examples:
- `AGENT_REGISTRY.md`
- `OPERATING_RULES.md`
- `ESCALATIONS.md`
- `escalations.json`

Goal:
- every state surface should have a clear purpose
- no stale fake placeholders
- no ambiguity about which file is authoritative for what

---

### 4. Prove repeated live WCS cycles
We need repeated real-world proof of the boring loop:

1. Jarvis selects task
2. Jarvis writes packet
3. correct task branch is prepared
4. worker executes
5. worker result is captured
6. QA runs
7. QA result is captured
8. reconcile updates state
9. task ends as done / failed / escalated
10. loop repeats across multiple tasks

The goal is not one lucky run.
The goal is repeatable reliability.

---

### 5. Reuse vs `--force` guardrail
Jarvis currently risks confusion around reusing today’s selected task versus forcing a fresh selection.

Need:
- explicit logic
- explicit messaging
- explicit guardrails so the wrong task does not get worked accidentally

---

### 6. Branch and repo cleanliness verification
Before execution, Jarvis should verify:
- correct task branch
- repo clean before work starts
- no unresolved merge/rebase/conflict state
- branch matches packet task
- expected repo path is correct

This should be enforced, not assumed.

---

### 7. Packet/repo mismatch detection
Jarvis should detect when:
- packet context does not match repo state
- scope drift has occurred
- actual changed files do not fit the intended task

This helps stop work before it becomes unrelated repo thrashing.

---

### 8. Diff sanity / changed-file allowlist validation
Jarvis should detect:
- suspiciously broad diffs
- unrelated changed files
- accidental refactors
- edits outside expected scope

This is a major anti-stupidity safeguard.

---

### 9. Worker-result schema validation
Jarvis should reject worker result artifacts that are:
- missing required fields
- invalid status
- fake or placeholder-shaped
- incorrectly stamped
- claiming files that do not match reality
- missing executor identity or evidence

No reconcile should happen from trash artifacts.

---

### 10. QA-result schema validation
Jarvis should reject QA artifacts that are:
- placeholder-shaped
- missing checks
- fake pass/fail output
- invalid status
- not tied to actual build/test evidence

---

### 11. Pre-reconcile readiness check
Before reconcile, Jarvis should confirm:
- worker result exists
- QA result exists
- both are valid
- statuses are allowed
- evidence is real
- task is actually ready for reconcile

No more blind reconcile.

---

### 12. Post-reconcile state validation
After reconcile, Jarvis should verify:
- correct task changed
- adjacent tasks did not accidentally change
- JSON state is correct
- rendered Markdown matches JSON
- no drift or corruption was introduced

This is critical because the system uses JSON as state and Markdown as rendered human view.

---

### 13. Dedicated Python QA runner
QA should move away from semi-manual interpretation and toward a controlled entrypoint that:
- runs build/test commands
- captures stdout/stderr
- writes real QA artifacts
- returns structured pass/fail/escalate status

This should be pulled earlier if possible because it reduces operator dependency.

---

### 14. Commit gate helper
Before finalizing task work, Jarvis should verify:
- correct branch
- no unrelated file changes
- valid commit exists
- worktree state is acceptable
- no post-commit repo mess remains

---

# Implementation priority order

## Build now (current high-priority hardening focus)
1. commit gate helper
2. dual-stamp / no-draft-stamping guardrails
3. file registry automation
4. naming drift cleanup

## Build later
18. limited scheduling
19. Research Scout worker
20. n8n improver worker
21. additional workers / productization

---

# What we are NOT prioritizing right now

Do **not** derail into:
- dashboards
- sexy UI
- more agents
- worker marketplaces
- voice features
- office copilots
- sandboxes everywhere
- generalized platform expansion
- productization before the loop is trustworthy

Those may matter later.
They are not the blocker now.

---

# CURRENT STATUS VS NEXT

## What is already proven
- reconcile branch verification is live
- reconcile verifies that the task branch is ahead of `main` for done-path completion
- `jarvis.py` exists and has materially improved operator-safety output
- task-state execution eligibility validation exists in `jarvis.py`
- packet/result placeholder contract validation exists in `jarvis.py`
- repeated live WCS cycles have been proven for `WCS-016`, `WCS-017`, `WCS-018`, and `WCS-019`
- fake tasks must be baseline-relative when new task branches are created from `main`
- `jarvis.py` now records durable escalation state on hard failures into `state/escalations.json` and renders `state/ESCALATIONS.md` as the human view
- `pre_reconcile_check.py` exists and is proven as a read-only readiness gate that validates task/result/repo prerequisites before running reconcile
- `post_reconcile_validate.py` exists and is proven as a read-only post-reconcile validator that confirms the intended task is done and visible in backlog JSON, rendered backlog markdown, review output, and result files
- `worker_change_check.py` exists and is proven as a read-only worker-boundary validator that checks changed-file scope and simple diff sanity before commit/finalization (including a successful PASS path on `WCS-019`)
- `commit_gate_check.py` exists and is proven as a read-only commit-state gate for a WCS task branch and HEAD, with a real PASS path inside a completed/reconciled loop (currently including `WCS-019`)

## What remains the next priority
- Dual-stamp / no-draft-stamping core guardrails are now live via `stamp_guard_check.py` as a read-only pre-stamp helper that runs before `stamp_result_timestamp.py`.
- File-registry drift/coverage checking is now live via `file_registry_check.py` (read-only helper; part of hardening surfaces, not the core task execution loop).
- Naming-drift detection across core hardening surfaces is now live via `naming_drift_check.py` as a read-only helper that reports obvious inconsistencies between core scripts/docs and the file registry without auto-fixing names.
- Registry rendering is now live via `render_file_registry.py` as a helper that renders `state/FILE_REGISTRY.md` from `state/file_registry.json` in the approved registry format.
- Critical-surface health checking is now live via `critical_surface_health_check.py` as a read-only sanity checker (existence of critical scripts/docs/registry, compile of critical helpers, and file_registry_check + naming_drift_check pass).
- Cursor handoff building is now live via `build_cursor_handoff.py` as a workflow helper that writes bounded, copy/paste-ready handoff files from task packets (does not execute tasks or mutate state). It fails with exit code 1 and does not write a handoff file when bounded file scope cannot be derived from the task packet.
- Task-cycle summary building is now live via `build_task_cycle_summary.py` as a workflow helper that reads current task packet, worker result, and QA result (when present) and writes a human-readable markdown summary under `scratch/task_cycle_summaries/` for a single WCS task cycle; it does not execute tasks, change task state, or mutate backlog/results.
- Next hardening focus areas:
  - manual naming drift cleanup guided by `naming_drift_check.py`
  - optional: further registry automation or script wrappers

## What is explicitly not being prioritized yet
- dashboards and “sexy” UI
- additional workers or marketplaces
- voice features
- broad multi-project scheduling
- generalized productization before the current loop is trustworthy

---

# Process documentation rule

Whenever a new process change, guardrail, contract, or script behavior is **locked in and live**, the working process and hardening documentation files in this workspace **must be updated immediately** so they stay aligned with the actual system.

---

# Simple framing for the next assistant

If you are helping on this project, assume this rule:

> The next best work is anything that converts operator discipline into system-enforced guardrails inside or immediately around `jarvis.py`.

Do not propose broad redesign unless it directly helps the above hardening goals.

Do not treat the project as greenfield.

Do not push scheduling or more workers before the current loop is trustworthy.

---

# Immediate coding focus

We are currently hardening `jarvis.py`.

The assistant should help identify and implement:
- escalation recording
- human-action-required state
- branch/repo/packet guardrails
- artifact schema validation
- reconcile readiness checks
- post-reconcile validation

These are the current priorities.

## FILE: JARVIS_CODEBASE_STRUCTURE.md
# Jarvis Workspace — Codebase Structure

## Purpose

This document describes the layout and conventions of the Jarvis workspace so you can find things quickly and understand how folders and files relate. For a full list of registered files and their roles, see `state\FILE_REGISTRY.md` and `state\file_registry.json`.

**Conventions (locked):**

- **JSON** = machine-readable source of truth where it exists.
- **Markdown** = human-readable view (often rendered from JSON or written by scripts).
- **scripts** = Python (and some PowerShell wrappers) that operate on **state** and **config**.
- **One bounded WCS task at a time**; task artifacts live under `tasks\`, `results\`, `qa\`, and sometimes `logs\`.

---

## Top-Level Layout

```
jarvis-workspace/
├── config/           # Configuration (scout routes, noise rules)
├── logs/             # All runtime logs (scout, health check, escalation)
├── qa/               # QA result JSONs per task (e.g. WCS-010_qa_result.json)
├── results/          # Worker result JSONs per task (e.g. WCS-010_worker_result.json)
├── scripts/          # Python foreman and support scripts (+ PS1 wrappers, docs)
├── state/            # Source-of-truth state (backlog, plan, run log, project status, registry)
├── tasks/            # Task packets (JSON + Markdown) per WCS task
├── scratch/          # Ad-hoc working copies and rescue files (not part of official loop)
│
├── README_START_HERE.md
├── JARVIS_PHASE_CHECKLIST.md
├── JARVIS_AGENT_IDEA_BACKLOG.md
├── CODEBASE_STRUCTURE.md   # this file
└── (handoff/other root docs as needed)
```

---

## Folder Roles

### `config/`

- **Purpose:** Configuration consumed by scripts; not state.
- **Key files:**
  - `scout_noise_rules.json` — Rules for filtering known scout noise in defect normalization.
  - `wcs_scout_routes.json` — Routes and options for the WCS public scout run.

### `logs/`

- **Purpose:** Runtime output only; append-only or timestamped. Do not treat as source of truth.
- **Contents:**
  - `wcs_scout/<timestamp>/` — Per-run scout output (Playwright results, normalizer report, summaries).
  - `overnight_health_*.json` / `overnight_health_*.txt` — Overnight health check results.
  - `WCS-<id>_escalation.json` — Escalation records for a task (when used).

### `qa/`

- **Purpose:** One QA result file per task, e.g. `WCS-010_qa_result.json`. Evidence for done/fail/escalate.
- **Owner:** Playwright (or manual) run; reconciled by `reconcile_task_outcome.py`.

### `results/`

- **Purpose:** One worker result file per task, e.g. `WCS-010_worker_result.json`. What the worker (e.g. Cursor) did.
- **Owner:** Operator / Cursor worker; timestamps can be set via `stamp_result_timestamp.py`.

### `scripts/`

- **Purpose:** All automation and runbooks. Python is canonical; `.ps1` files are wrappers or convenience.
- **Key scripts:**
  - **Foreman:** `jarvis.py` — Selects one WCS task, writes `daily_plan.json` / `DAILY_PLAN.md`, appends to run log, generates task packet, prepares branch.
  - **Backlog / packet:** `render_master_backlog.py`, `generate_task_packet.py`, `reconcile_task_outcome.py`.
  - **Scout / intake:** `run_wcs_scout.py`, `normalize_scout_to_backlog.py` (plus `.ps1` wrappers where present).
  - **Operations:** `overnight_health_check.py`, `prepare_wcs_task_branch.py`, `stamp_result_timestamp.py`.
- **Also:** `manual_loop_checklist.md`, `cursor_completion_contract.txt`, and other runbook/spec snippets.

### `state/`

- **Purpose:** Durable, source-of-truth state that drives the system. JSON is primary; Markdown is human view.
- **Key files:**
  - **Backlog:** `master_backlog.json`, `MASTER_BACKLOG.md`.
  - **Plan / run log:** `daily_plan.json`, `DAILY_PLAN.md`, `run_log.json`, `RUN_LOG.md`.
  - **Project status:** `project_status_wcs.json`, `PROJECT_STATUS_WCS.md`, `project_status_n8n.json`, `PROJECT_STATUS_N8N.md`.
  - **Registry:** `file_registry.json`, `FILE_REGISTRY.md`.
  - **Other:** `DAILY_REVIEW.md`; test/backlog variants (e.g. `master_backlog_test.json`) as needed.

### `tasks/`

- **Purpose:** One task packet per WCS task. Generated by `generate_task_packet.py` (or by Jarvis); consumed by the worker.
- **Pattern:** `WCS-<id>_task.json`, `WCS-<id>_task.md`.

### `scratch/`

- **Purpose:** Ad-hoc or rescue work (e.g. copied components, one-off specs). Not part of the official task/result/QA loop. Can be ignored for “where does the system live?” questions.

---

## Data Flow (Simplified)

1. **Backlog** (`state\master_backlog.json`) + **project status** (`state\project_status_wcs.json`) → **Jarvis** (`scripts\jarvis.py`) selects one task.
2. **Jarvis** writes **daily plan** and **run log** (`state\daily_plan.json`, `state\run_log.json`, plus `.md`), then generates **task packet** (`tasks\WCS-<id>_task.*`) and prepares branch (WCS repo).
3. **Worker** (e.g. Cursor) does the work; fills **worker result** (`results\WCS-<id>_worker_result.json`).
4. **QA** (semi-manual, via Playwright) runs:
   - `npm run build`
   - `npm run test:e2e:smoke`
   and produces **QA result** (`qa\WCS-<id>_qa_result.json`).
5. **Pre-reconcile check** (`pre_reconcile_check.py`) runs as a read-only gate to confirm task/result/repo readiness.
6. **Reconcile** (`reconcile_task_outcome.py`) updates backlog and status from worker + QA evidence, verifying branch state and commits ahead of main; escalation artifacts may go to `logs\` or state.
7. **Post-reconcile validation** (`post_reconcile_validate.py`) runs as a read-only validator to confirm the task is marked done and visible in backlog JSON, rendered backlog markdown, review surfaces, and result files.
8. **Escalation state surfaces** (`state\escalations.json`, `state\ESCALATIONS.md`) reflect durable Jarvis hard failures when they occur.
9. **Worker-boundary and result-schema helpers**:
   - `worker_change_check.py` — read-only validator for changed-file scope and simple diff sanity before commit.
   - `worker_result_validate.py` — read-only schema validator for worker result JSON in pre-stamp and post-stamp modes.
   - `qa_result_validate.py` — read-only schema validator for QA result JSON in pre-stamp and post-stamp modes.

Scout path: **Scout run** → `logs\wcs_scout\<timestamp>\` → **normalizer** (`normalize_scout_to_backlog.py`) → backlog updates (and optional `MASTER_BACKLOG.md` re-render).

---

## Where to Look Next

- **First-time setup and one manual loop:** `README_START_HERE.md`
- **Phase status and what’s done next:** `JARVIS_PHASE_CHECKLIST.md`
- **Every registered file and its role:** `state\FILE_REGISTRY.md` (and `state\file_registry.json` for tooling)
- **WCS repo path and local URL:** `README_START_HERE.md` (e.g. `C:\dev\wcsv2.0-new`, `http://localhost:3000`)


## FILE: state/file_registry.json
[
  {
    "file": "JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md",
    "path": "C:\\dev\\jarvis-workspace\\docs\\JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "High-level product requirements for Jarvis rebuild",
    "updated_by": "user",
    "notes": "Core planning doc"
  },
  {
    "file": "JARVIS_SYSTEM_DOCUMENTATION_v3.md",
    "path": "C:\\dev\\jarvis-workspace\\docs\\JARVIS_SYSTEM_DOCUMENTATION_v3.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Detailed architecture and operating documentation",
    "updated_by": "user",
    "notes": "Core planning doc"
  },
  {
    "file": "JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md",
    "path": "C:\\dev\\jarvis-workspace\\docs\\JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Current authoritative decisions and system rules",
    "updated_by": "user",
    "notes": "Most important design reference"
  },
  {
    "file": "master_backlog.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\master_backlog.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Machine-readable task backlog",
    "updated_by": "user / jarvis_script",
    "notes": "Primary backlog source"
  },
  {
    "file": "MASTER_BACKLOG.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\MASTER_BACKLOG.md",
    "category": "state",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable backlog table",
    "updated_by": "render_master_backlog.py",
    "notes": "Rendered from master_backlog.json"
  },
  {
    "file": "DAILY_REVIEW.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\DAILY_REVIEW.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Daily execution log and summary",
    "updated_by": "user / jarvis_script",
    "notes": "Reconcile appends entries"
  },
  {
    "file": "DAILY_PLAN.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\DAILY_PLAN.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Current planned work for the day",
    "updated_by": "user",
    "notes": "Lightly used so far"
  },
  {
    "file": "PROJECT_STATUS_WCS.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\PROJECT_STATUS_WCS.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Human-readable WCS project status",
    "updated_by": "user / jarvis_script",
    "notes": "May later be rendered"
  },
  {
    "file": "PROJECT_STATUS_N8N.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\PROJECT_STATUS_N8N.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Human-readable n8n project status",
    "updated_by": "user",
    "notes": "n8n worker deferred"
  },
  {
    "file": "file_registry.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\file_registry.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Machine-readable file registry",
    "updated_by": "user / jarvis_script",
    "notes": "Source for FILE_REGISTRY.md"
  },
  {
    "file": "FILE_REGISTRY.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\FILE_REGISTRY.md",
    "category": "state",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable file registry",
    "updated_by": "user / future renderer",
    "notes": "Registry view"
  },
  {
    "file": "render_master_backlog.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\render_master_backlog.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Renders MASTER_BACKLOG.md from backlog JSON",
    "updated_by": "user",
    "notes": "Working"
  },
  {
    "file": "update_master_backlog.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\update_master_backlog.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "PowerShell wrapper for backlog renderer",
    "updated_by": "user",
    "notes": "Convenience wrapper"
  },
  {
    "file": "generate_task_packet.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\generate_task_packet.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Creates task packet files and blank result files",
    "updated_by": "user",
    "notes": "Working"
  },
  {
    "file": "generate_task_packet.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\generate_task_packet.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "PowerShell wrapper for task generator",
    "updated_by": "user",
    "notes": "Convenience wrapper"
  },
  {
    "file": "reconcile_task_outcome.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\reconcile_task_outcome.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Reconciles worker and QA results into backlog state",
    "updated_by": "user",
    "notes": "Working"
  },
  {
    "file": "reconcile_task_outcome.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\reconcile_task_outcome.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "PowerShell wrapper for reconciler",
    "updated_by": "user",
    "notes": "Convenience wrapper"
  },
  {
    "file": "cursor_completion_contract.txt",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\cursor_completion_contract.txt",
    "category": "template",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Forces structured Cursor completion summaries",
    "updated_by": "user",
    "notes": "Used in worker prompts"
  },
  {
    "file": "overnight_health_check.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\overnight_health_check.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only overnight system health watcher",
    "updated_by": "user",
    "notes": "Working"
  },
  {
    "file": "run_overnight_health_check.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\run_overnight_health_check.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Wrapper for overnight health watcher",
    "updated_by": "user",
    "notes": "Used for manual or scheduled runs"
  },
  {
    "file": "register_overnight_health_task.txt",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\register_overnight_health_task.txt",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Task Scheduler command notes",
    "updated_by": "user",
    "notes": "Scheduling helper"
  },
  {
    "file": "run_wcs_scout.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\run_wcs_scout.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Runs public WCS scout and stores results",
    "updated_by": "user",
    "notes": "Working"
  },
  {
    "file": "wcs_scout_routes.json",
    "path": "C:\\dev\\jarvis-workspace\\config\\wcs_scout_routes.json",
    "category": "config",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Public routes list for WCS scout",
    "updated_by": "user",
    "notes": "/shop and /news removed for now"
  },
  {
    "file": "WCS-001_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-001_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-001_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-001_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-002_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-002_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-002_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-002_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-003_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-003_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-003_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-003_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Example completed task"
  },
  {
    "file": "WCS-004_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-004_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Completed after branch cleanup"
  },
  {
    "file": "WCS-004_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-004_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "Completed after branch cleanup"
  },
  {
    "file": "WCS-011_task.md",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-011_task.md",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "QA infrastructure task"
  },
  {
    "file": "WCS-011_task.json",
    "path": "C:\\dev\\jarvis-workspace\\tasks\\WCS-011_task.json",
    "category": "task_packet",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Machine-readable task packet",
    "updated_by": "generate_task_packet.py",
    "notes": "QA infrastructure task"
  },
  {
    "file": "*_worker_result.json",
    "path": "C:\\dev\\jarvis-workspace\\results\\*_worker_result.json",
    "category": "worker_result",
    "source_type": "runtime_output",
    "owner": "cursor_worker",
    "purpose": "Worker completion record per task",
    "updated_by": "user / cursor_worker",
    "notes": "Reconciler input"
  },
  {
    "file": "*_qa_result.json",
    "path": "C:\\dev\\jarvis-workspace\\qa\\*_qa_result.json",
    "category": "qa_result",
    "source_type": "runtime_output",
    "owner": "playwright",
    "purpose": "QA completion record per task",
    "updated_by": "user / playwright",
    "notes": "Reconciler input"
  },
  {
    "file": "*_escalation.json",
    "path": "C:\\dev\\jarvis-workspace\\logs\\*_escalation.json",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "jarvis_script",
    "purpose": "Escalation record for blocked or escalated tasks",
    "updated_by": "user / jarvis_script",
    "notes": "May be blank for many tasks"
  },
  {
    "file": "overnight_health_*.json",
    "path": "C:\\dev\\jarvis-workspace\\logs\\overnight_health_*.json",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "jarvis_script",
    "purpose": "Machine-readable overnight health output",
    "updated_by": "overnight_health_check.py",
    "notes": "Working"
  },
  {
    "file": "overnight_health_*.txt",
    "path": "C:\\dev\\jarvis-workspace\\logs\\overnight_health_*.txt",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "jarvis_script",
    "purpose": "Human-readable overnight health summary",
    "updated_by": "overnight_health_check.py",
    "notes": "Working"
  },
  {
    "file": "public_scout_results.json",
    "path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\public_scout_results.json",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "scout_runner",
    "purpose": "Structured route scout results",
    "updated_by": "run_wcs_scout.py / public_scout.spec.ts",
    "notes": "Latest run currently PASS"
  },
  {
    "file": "public_scout_summary.txt",
    "path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\public_scout_summary.txt",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "scout_runner",
    "purpose": "Human-readable scout summary",
    "updated_by": "run_wcs_scout.py",
    "notes": "Latest run currently PASS"
  },
  {
    "file": "playwright_stdout.txt",
    "path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\playwright_stdout.txt",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "scout_runner",
    "purpose": "Raw Playwright stdout from scout run",
    "updated_by": "run_wcs_scout.py",
    "notes": "Debug support"
  },
  {
    "file": "playwright_stderr.txt",
    "path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\playwright_stderr.txt",
    "category": "log",
    "source_type": "runtime_output",
    "owner": "scout_runner",
    "purpose": "Raw Playwright stderr from scout run",
    "updated_by": "run_wcs_scout.py",
    "notes": "Debug support"
  },
  {
    "file": "public_scout.spec.ts",
    "path": "C:\\dev\\wcsv2.0-new\\tests\\e2e\\public_scout.spec.ts",
    "category": "repo_test",
    "source_type": "source_of_truth",
    "owner": "playwright",
    "purpose": "Public route scout spec for WCS",
    "updated_by": "user",
    "notes": "External WCS repo Playwright spec at C:\\dev\\wcsv2.0-new\\tests\\e2e"
  },
  {
    "file": "home.spec.ts",
    "path": "C:\\dev\\wcsv2.0-new\\tests\\e2e\\home.spec.ts",
    "category": "repo_test",
    "source_type": "source_of_truth",
    "owner": "playwright",
    "purpose": "Smoke QA spec for home page",
    "updated_by": "user",
    "notes": "External WCS repo Playwright spec at C:\\dev\\wcsv2.0-new\\tests\\e2e"
  },
  {
    "file": "global-setup.ts",
    "path": "C:\\dev\\wcsv2.0-new\\tests\\e2e\\helpers\\global-setup.ts",
    "category": "repo_test",
    "source_type": "source_of_truth",
    "owner": "playwright",
    "purpose": "Shared Playwright startup and readiness logic",
    "updated_by": "user",
    "notes": "External WCS repo Playwright helper at C:\\dev\\wcsv2.0-new\\tests\\e2e\\helpers"
  },
  {
    "file": "package.json",
    "path": "C:\\dev\\wcsv2.0-new\\package.json",
    "category": "repo_test",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Repo scripts including test:e2e:smoke",
    "updated_by": "user",
    "notes": "WCS repo-side dependency in external WCS repo at C:\\dev\\wcsv2.0-new"
  },
  {
    "file": "normalize_scout_to_backlog.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\normalize_scout_to_backlog.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Normalizes scout defects into backlog-ready tasks and updates backlog state",
    "updated_by": "user",
    "notes": "Filters known scout noise, inserts valid tasks, and re-renders MASTER_BACKLOG.md"
  },
  {
    "file": "normalize_scout_to_backlog.ps1",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\normalize_scout_to_backlog.ps1",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "PowerShell wrapper for scout defect normalizer",
    "updated_by": "user",
    "notes": "Convenience wrapper"
  },
  {
    "file": "scout_noise_rules.json",
    "path": "C:\\dev\\jarvis-workspace\\config\\scout_noise_rules.json",
    "category": "config",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Known scout noise filtering rules for backlog normalization",
    "updated_by": "user",
    "notes": "Used by normalize_scout_to_backlog.py"
  },
  {
    "file": "JARVIS_PHASE_CHECKLIST.md",
    "path": "C:\\dev\\jarvis-workspace\\JARVIS_PHASE_CHECKLIST.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Phase-by-phase rebuild checklist and status for Jarvis workspace",
    "updated_by": "user",
    "notes": "Current canonical overview of phases, missing state surfaces, and next priorities"
  },
  {
    "file": "JARVIS_AGENT_IDEA_BACKLOG.md",
    "path": "C:\\dev\\jarvis-workspace\\JARVIS_AGENT_IDEA_BACKLOG.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Idea backlog for short-term modules and longer-term agent business concepts",
    "updated_by": "user",
    "notes": "Reusable idea backlog aligned with current Jarvis architecture"
  },
  {
    "file": "manual_loop_checklist.md",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\manual_loop_checklist.md",
    "category": "doc",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Manual proof-loop checklist for running a WCS task through backlog, worker, QA, and reconcile",
    "updated_by": "user",
    "notes": "Operator runbook; should be aligned with actual script and state behavior to avoid drift"
  },
  {
    "file": "jarvis.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\jarvis.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Phase 3 foreman; reads backlog and project status, selects one WCS task, writes daily_plan and run_log",
    "updated_by": "user",
    "notes": "Does not modify backlog or run workers; selection and plan/run-log recording only"
  },
  {
    "file": "prepare_wcs_task_branch.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\prepare_wcs_task_branch.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Prepares WCS task branch for bounded task work",
    "updated_by": "user",
    "notes": "Used in task workflow to create or switch to task branch in WCS repo"
  },
  {
    "file": "stamp_result_timestamp.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\stamp_result_timestamp.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Stamps completed_at (or similar) on worker and QA result JSON files",
    "updated_by": "user",
    "notes": "Helper to keep result timestamps consistent"
  },
  {
    "file": "daily_plan.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\daily_plan.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Current selected task and plan metadata; machine-readable",
    "updated_by": "jarvis.py",
    "notes": "Written by jarvis.py; pairs with DAILY_PLAN.md"
  },
  {
    "file": "run_log.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\run_log.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Append-only machine-readable run history",
    "updated_by": "jarvis.py",
    "notes": "Written by jarvis.py when a task is selected"
  },
  {
    "file": "RUN_LOG.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\RUN_LOG.md",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Append-only human-readable run log",
    "updated_by": "jarvis.py",
    "notes": "Written by jarvis.py when a task is selected"
  },
  {
    "file": "project_status_wcs.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\project_status_wcs.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Machine-readable WCS project status",
    "updated_by": "user",
    "notes": "Mirror of PROJECT_STATUS_WCS.md; consumed by jarvis.py and scripts"
  },
  {
    "file": "project_status_n8n.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\project_status_n8n.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "user",
    "purpose": "Machine-readable n8n project status",
    "updated_by": "user",
    "notes": "Mirror of PROJECT_STATUS_N8N.md; n8n worker deferred"
  },
  {
    "file": "escalations.json",
    "path": "C:\\dev\\jarvis-workspace\\state\\escalations.json",
    "category": "state",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Machine-readable escalation records for Jarvis hard failures",
    "updated_by": "jarvis.py",
    "notes": "Authoritative escalation state; rendered to ESCALATIONS.md"
  },
  {
    "file": "ESCALATIONS.md",
    "path": "C:\\dev\\jarvis-workspace\\state\\ESCALATIONS.md",
    "category": "state",
    "source_type": "generated",
    "owner": "jarvis_script",
    "purpose": "Human-readable escalation log",
    "updated_by": "jarvis.py",
    "notes": "Rendered from escalations.json whenever Jarvis records an escalation"
  },
  {
    "file": "pre_reconcile_check.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\pre_reconcile_check.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only pre-reconcile readiness gate for a WCS task",
    "updated_by": "user",
    "notes": "Validates task/result/repo prerequisites before running reconcile"
  },
  {
    "file": "post_reconcile_validate.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\post_reconcile_validate.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only post-reconcile validator for a WCS task",
    "updated_by": "user",
    "notes": "Confirms the intended task is done and visible in backlog JSON, rendered backlog markdown, DAILY_REVIEW.md, and result files"
  },
  {
    "file": "worker_change_check.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\worker_change_check.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only worker-boundary validator for changed-file scope and simple diff sanity",
    "updated_by": "user",
    "notes": "Validates that changed files stay within task scope and diffs are small before commit/finalization"
  },
  {
    "file": "worker_result_validate.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\worker_result_validate.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only worker-result schema validator for a WCS task",
    "updated_by": "user",
    "notes": "Validates worker result fields and simple task-scope consistency in pre-stamp and post-stamp modes"
  },
  {
    "file": "qa_result_validate.py",
    "path": "C:\\dev\\jarvis-workspace\\scripts\\qa_result_validate.py",
    "category": "script",
    "source_type": "source_of_truth",
    "owner": "jarvis_script",
    "purpose": "Read-only QA-result schema validator for a WCS task",
    "updated_by": "user",
    "notes": "Validates QA result fields, list shapes, and simple internal consistency in pre-stamp and post-stamp modes"
  }
]

## FILE: state/FILE_REGISTRY.md
# FILE REGISTRY

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
This markdown file is the human-readable view.

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
| JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md | C:\dev\jarvis-workspace\docs\JARVIS_MULTI_AGENT_SYSTEM_PRD_v3.md | doc | source_of_truth | user | High-level product requirements for Jarvis rebuild | user | Core planning doc |
| JARVIS_SYSTEM_DOCUMENTATION_v3.md | C:\dev\jarvis-workspace\docs\JARVIS_SYSTEM_DOCUMENTATION_v3.md | doc | source_of_truth | user | Detailed architecture and operating documentation | user | Core planning doc |
| JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md | C:\dev\jarvis-workspace\docs\JARVIS_SYSTEM_SOURCE_OF_TRUTH_v3.md | doc | source_of_truth | user | Current authoritative decisions and system rules | user | Most important design reference |
| JARVIS_PHASE_CHECKLIST.md | C:\dev\jarvis-workspace\JARVIS_PHASE_CHECKLIST.md | doc | source_of_truth | user | Phase-by-phase rebuild checklist and status for Jarvis workspace | user | Current canonical overview of phases, missing state surfaces, and next priorities |
| JARVIS_AGENT_IDEA_BACKLOG.md | C:\dev\jarvis-workspace\JARVIS_AGENT_IDEA_BACKLOG.md | doc | source_of_truth | user | Idea backlog for short-term modules and longer-term agent business concepts | user | Reusable idea backlog aligned with current Jarvis architecture |
| master_backlog.json | C:\dev\jarvis-workspace\state\master_backlog.json | state | source_of_truth | user | Machine-readable task backlog | user / jarvis_script | Primary backlog source |
| MASTER_BACKLOG.md | C:\dev\jarvis-workspace\state\MASTER_BACKLOG.md | state | generated | jarvis_script | Human-readable backlog table | render_master_backlog.py | Rendered from master_backlog.json |
| DAILY_REVIEW.md | C:\dev\jarvis-workspace\state\DAILY_REVIEW.md | state | source_of_truth | user | Daily execution log and summary | user / jarvis_script | Reconcile appends entries |
| DAILY_PLAN.md | C:\dev\jarvis-workspace\state\DAILY_PLAN.md | state | source_of_truth | user | Current planned work for the day | user | Lightly used so far |
| PROJECT_STATUS_WCS.md | C:\dev\jarvis-workspace\state\PROJECT_STATUS_WCS.md | state | source_of_truth | user | Human-readable WCS project status | user / jarvis_script | May later be rendered |
| PROJECT_STATUS_N8N.md | C:\dev\jarvis-workspace\state\PROJECT_STATUS_N8N.md | state | source_of_truth | user | Human-readable n8n project status | user | n8n worker deferred |
| escalations.json | C:\dev\jarvis-workspace\state\escalations.json | state | source_of_truth | jarvis_script | Machine-readable escalation records for Jarvis hard failures | jarvis.py | Authoritative escalation state; rendered to ESCALATIONS.md |
| ESCALATIONS.md | C:\dev\jarvis-workspace\state\ESCALATIONS.md | state | generated | jarvis_script | Human-readable escalation log | jarvis.py | Rendered from escalations.json whenever Jarvis records an escalation |
| file_registry.json | C:\dev\jarvis-workspace\state\file_registry.json | state | source_of_truth | user | Machine-readable file registry | user / jarvis_script | Source for this markdown file |
| FILE_REGISTRY.md | C:\dev\jarvis-workspace\state\FILE_REGISTRY.md | state | generated | jarvis_script | Human-readable file registry | user / future renderer | Human-readable registry view; currently hand-maintained and intended to be rendered from file_registry.json later |
| render_master_backlog.py | C:\dev\jarvis-workspace\scripts\render_master_backlog.py | script | source_of_truth | jarvis_script | Renders MASTER_BACKLOG.md from backlog JSON | user | Working |
| update_master_backlog.ps1 | C:\dev\jarvis-workspace\scripts\update_master_backlog.ps1 | script | source_of_truth | user | PowerShell wrapper for backlog renderer | user | Convenience wrapper |
| generate_task_packet.py | C:\dev\jarvis-workspace\scripts\generate_task_packet.py | script | source_of_truth | jarvis_script | Creates task packet files and blank result files | user | Working |
| generate_task_packet.ps1 | C:\dev\jarvis-workspace\scripts\generate_task_packet.ps1 | script | source_of_truth | user | PowerShell wrapper for task generator | user | Convenience wrapper |
| reconcile_task_outcome.py | C:\dev\jarvis-workspace\scripts\reconcile_task_outcome.py | script | source_of_truth | jarvis_script | Reconciles worker + QA results into backlog state | user | Working |
| reconcile_task_outcome.ps1 | C:\dev\jarvis-workspace\scripts\reconcile_task_outcome.ps1 | script | source_of_truth | user | PowerShell wrapper for reconciler | user | Convenience wrapper |
| cursor_completion_contract.txt | C:\dev\jarvis-workspace\scripts\cursor_completion_contract.txt | template | source_of_truth | user | Forces structured Cursor completion summaries | user | Used in worker prompts |
| overnight_health_check.py | C:\dev\jarvis-workspace\scripts\overnight_health_check.py | script | source_of_truth | jarvis_script | Read-only overnight system health watcher | user | Working |
| run_overnight_health_check.ps1 | C:\dev\jarvis-workspace\scripts\run_overnight_health_check.ps1 | script | source_of_truth | user | Wrapper for overnight health watcher | user | Used for manual or scheduled runs |
| register_overnight_health_task.txt | C:\dev\jarvis-workspace\scripts\register_overnight_health_task.txt | doc | source_of_truth | user | Task Scheduler command notes | user | Scheduling helper |
| manual_loop_checklist.md | C:\dev\jarvis-workspace\scripts\manual_loop_checklist.md | doc | source_of_truth | user | Manual proof-loop checklist for running a WCS task through backlog, worker, QA, and reconcile | user | Operator runbook; should be aligned with actual script and state behavior to avoid drift |
| run_wcs_scout.py | C:\dev\jarvis-workspace\scripts\run_wcs_scout.py | script | source_of_truth | jarvis_script | Runs public WCS scout and stores results | user | Working after env-var fixes |
| wcs_scout_routes.json | C:\dev\jarvis-workspace\config\wcs_scout_routes.json | config | source_of_truth | user | Public routes list for WCS scout | user | /shop and /news removed for now |
| WCS-001_task.md | C:\dev\jarvis-workspace\tasks\WCS-001_task.md | task_packet | generated | jarvis_script | Human-readable task packet | generate_task_packet.py | Example completed task |
| WCS-001_task.json | C:\dev\jarvis-workspace\tasks\WCS-001_task.json | task_packet | generated | jarvis_script | Machine-readable task packet | generate_task_packet.py | Example completed task |
| WCS-002_task.md | C:\dev\jarvis-workspace\tasks\WCS-002_task.md | task_packet | generated | jarvis_script | Human-readable task packet | generate_task_packet.py | Example completed task |
| WCS-002_task.json | C:\dev\jarvis-workspace\tasks\WCS-002_task.json | task_packet | generated | jarvis_script | Machine-readable task packet | generate_task_packet.py | Example completed task |
| WCS-003_task.md | C:\dev\jarvis-workspace\tasks\WCS-003_task.md | task_packet | generated | jarvis_script | Human-readable task packet | generate_task_packet.py | Example completed task |
| WCS-003_task.json | C:\dev\jarvis-workspace\tasks\WCS-003_task.json | task_packet | generated | jarvis_script | Machine-readable task packet | generate_task_packet.py | Example completed task |
| WCS-004_task.md | C:\dev\jarvis-workspace\tasks\WCS-004_task.md | task_packet | generated | jarvis_script | Human-readable task packet | generate_task_packet.py | Completed after branch cleanup |
| WCS-004_task.json | C:\dev\jarvis-workspace\tasks\WCS-004_task.json | task_packet | generated | jarvis_script | Machine-readable task packet | generate_task_packet.py | Completed after branch cleanup |
| WCS-011_task.md | C:\dev\jarvis-workspace\tasks\WCS-011_task.md | task_packet | generated | jarvis_script | Human-readable task packet | generate_task_packet.py | QA infrastructure task |
| WCS-011_task.json | C:\dev\jarvis-workspace\tasks\WCS-011_task.json | task_packet | generated | jarvis_script | Machine-readable task packet | generate_task_packet.py | QA infrastructure task |
| *_worker_result.json | C:\dev\jarvis-workspace\results\*_worker_result.json | worker_result | runtime_output | cursor_worker | Worker completion record per task | user / cursor_worker | Reconciler input |
| *_qa_result.json | C:\dev\jarvis-workspace\qa\*_qa_result.json | qa_result | runtime_output | playwright | QA completion record per task | user / playwright | Reconciler input |
| *_escalation.json | C:\dev\jarvis-workspace\logs\*_escalation.json | log | runtime_output | jarvis_script | Escalation record for blocked/escalated tasks | user / jarvis_script | May be blank for many tasks |
| overnight_health_*.json | C:\dev\jarvis-workspace\logs\overnight_health_*.json | log | runtime_output | jarvis_script | Machine-readable overnight health output | overnight_health_check.py | Working |
| overnight_health_*.txt | C:\dev\jarvis-workspace\logs\overnight_health_*.txt | log | runtime_output | jarvis_script | Human-readable overnight health summary | overnight_health_check.py | Working |
| public_scout_results.json | C:\dev\jarvis-workspace\logs\wcs_scout\<timestamp>\public_scout_results.json | log | runtime_output | scout_runner | Structured route scout results | run_wcs_scout.py / public_scout.spec.ts | Latest run currently PASS |
| public_scout_summary.txt | C:\dev\jarvis-workspace\logs\wcs_scout\<timestamp>\public_scout_summary.txt | log | runtime_output | scout_runner | Human-readable scout summary | run_wcs_scout.py | Latest run currently PASS |
| playwright_stdout.txt | C:\dev\jarvis-workspace\logs\wcs_scout\<timestamp>\playwright_stdout.txt | log | runtime_output | scout_runner | Raw Playwright stdout from scout run | run_wcs_scout.py | Debug support |
| playwright_stderr.txt | C:\dev\jarvis-workspace\logs\wcs_scout\<timestamp>\playwright_stderr.txt | log | runtime_output | scout_runner | Raw Playwright stderr from scout run | run_wcs_scout.py | Debug support |
| public_scout.spec.ts | C:\dev\wcsv2.0-new\tests\e2e\public_scout.spec.ts | repo_test | source_of_truth | playwright | Public route scout spec for WCS | user | External WCS repo Playwright spec at C:\dev\wcsv2.0-new\tests\e2e |
| home.spec.ts | C:\dev\wcsv2.0-new\tests\e2e\home.spec.ts | repo_test | source_of_truth | playwright | Smoke QA spec for home page | user | External WCS repo Playwright spec at C:\dev\wcsv2.0-new\tests\e2e |
| global-setup.ts | C:\dev\wcsv2.0-new\tests\e2e\helpers\global-setup.ts | repo_test | source_of_truth | playwright | Shared Playwright startup and readiness logic | user | External WCS repo Playwright helper at C:\dev\wcsv2.0-new\tests\e2e\helpers |
| package.json | C:\dev\wcsv2.0-new\package.json | repo_test | source_of_truth | user | Repo scripts including test:e2e:smoke | user | WCS repo-side dependency in external WCS repo at C:\dev\wcsv2.0-new |
| normalize_scout_to_backlog.py | C:\dev\jarvis-workspace\scripts\normalize_scout_to_backlog.py | script | source_of_truth | jarvis_script | Normalizes scout defects into backlog-ready tasks and updates backlog state | user | Filters known scout noise, inserts valid tasks, and re-renders MASTER_BACKLOG.md |
| normalize_scout_to_backlog.ps1 | C:\dev\jarvis-workspace\scripts\normalize_scout_to_backlog.ps1 | script | source_of_truth | user | PowerShell wrapper for scout defect normalizer | user | Convenience wrapper |
| scout_noise_rules.json | C:\dev\jarvis-workspace\config\scout_noise_rules.json | config | source_of_truth | user | Known scout noise filtering rules for backlog normalization | user | Used by normalize_scout_to_backlog.py |
| jarvis.py | C:\dev\jarvis-workspace\scripts\jarvis.py | script | source_of_truth | jarvis_script | Phase 3 foreman; reads backlog and project status, selects one WCS task, writes daily_plan and run_log | user | Does not modify backlog or run workers; selection and plan/run-log recording only |
| prepare_wcs_task_branch.py | C:\dev\jarvis-workspace\scripts\prepare_wcs_task_branch.py | script | source_of_truth | user | Prepares WCS task branch for bounded task work | user | Used in task workflow to create or switch to task branch in WCS repo |
| stamp_result_timestamp.py | C:\dev\jarvis-workspace\scripts\stamp_result_timestamp.py | script | source_of_truth | user | Stamps completed_at (or similar) on worker and QA result JSON files | user | Helper to keep result timestamps consistent |
| daily_plan.json | C:\dev\jarvis-workspace\state\daily_plan.json | state | source_of_truth | jarvis_script | Current selected task and plan metadata; machine-readable | jarvis.py | Written by jarvis.py; pairs with DAILY_PLAN.md |
| run_log.json | C:\dev\jarvis-workspace\state\run_log.json | state | source_of_truth | jarvis_script | Append-only machine-readable run history | jarvis.py | Written by jarvis.py when a task is selected |
| RUN_LOG.md | C:\dev\jarvis-workspace\state\RUN_LOG.md | state | source_of_truth | jarvis_script | Append-only human-readable run log | jarvis.py | Written by jarvis.py when a task is selected |
| project_status_wcs.json | C:\dev\jarvis-workspace\state\project_status_wcs.json | state | source_of_truth | user | Machine-readable WCS project status | user | Mirror of PROJECT_STATUS_WCS.md; consumed by jarvis.py and scripts |
| project_status_n8n.json | C:\dev\jarvis-workspace\state\project_status_n8n.json | state | source_of_truth | user | Machine-readable n8n project status | user | Mirror of PROJECT_STATUS_N8N.md; n8n worker deferred |
| pre_reconcile_check.py | C:\dev\jarvis-workspace\scripts\pre_reconcile_check.py | script | source_of_truth | jarvis_script | Read-only pre-reconcile readiness gate for a WCS task | user | Validates task/result/repo prerequisites before running reconcile |
| post_reconcile_validate.py | C:\dev\jarvis-workspace\scripts\post_reconcile_validate.py | script | source_of_truth | jarvis_script | Read-only post-reconcile validator for a WCS task | user | Confirms the intended task is done and visible in backlog JSON, rendered backlog markdown, DAILY_REVIEW.md, and result files |
| worker_change_check.py | C:\dev\jarvis-workspace\scripts\worker_change_check.py | script | source_of_truth | jarvis_script | Read-only worker-boundary validator for changed-file scope and simple diff sanity | user | Validates that changed files stay within task scope and diffs are small before commit/finalization |
| worker_result_validate.py | C:\dev\jarvis-workspace\scripts\worker_result_validate.py | script | source_of_truth | jarvis_script | Read-only worker-result schema validator for a WCS task | user | Validates worker result fields and simple task-scope consistency in pre-stamp and post-stamp modes |
| qa_result_validate.py | C:\dev\jarvis-workspace\scripts\qa_result_validate.py | script | source_of_truth | jarvis_script | Read-only QA-result schema validator for a WCS task | user | Validates QA result fields, list shapes, and simple internal consistency in pre-stamp and post-stamp modes |

## FILE: state/project_status_wcs.json
{
  "project": "WCS",
  "repo_path": "C:\\dev\\wcsv2.0-new",
  "install_command": "npm install",
  "dev_command": "npm run dev",
  "build_command": "npm run build",
  "local_url": "http://localhost:3000",
  "deploy_target": "Vercel via GitHub push",
  "priority_routes": [
    "/",
    "/about",
    "/teams"
  ],
  "checks_needed": [
    "python_version",
    "node_version",
    "playwright_installed",
    "testids_present"
  ],
  "scout_defect_intake": {
    "enabled": true,
    "runner": "run_wcs_scout.py",
    "normalizer": "normalize_scout_to_backlog.py",
    "noise_rules": "scout_noise_rules.json",
    "results_path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\public_scout_results.json",
    "report_path": "C:\\dev\\jarvis-workspace\\logs\\wcs_scout\\<timestamp>\\scout_normalizer_report.json",
    "backlog_target": "C:\\dev\\jarvis-workspace\\state\\master_backlog.json",
    "backlog_markdown": "C:\\dev\\jarvis-workspace\\state\\MASTER_BACKLOG.md"
  },
  "validation_completed": [
    "public_scout_clean_noop_path",
    "public_scout_synthetic_failure_insertion",
    "public_scout_duplicate_suppression",
    "integrated_scout_to_normalizer_run"
  ]
}

## FILE: state/master_backlog.json
[
  {
    "task_id": "WCS-001",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P2",
    "risk": "low",
    "status": "done",
    "title": "Fix testimonial typo in PlayerTestimonials quote",
    "notes": "src/components/PlayerTestimonials.tsx"
  },
  {
    "task_id": "WCS-002",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P1",
    "risk": "medium",
    "status": "done",
    "title": "Fix stats section showing 0 for all metrics",
    "notes": "src/components/StatsSection.tsx"
  },
  {
    "task_id": "WCS-003",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P1",
    "risk": "medium",
    "status": "done",
    "title": "Add timeout/fallback handling for long loading states",
    "notes": "TodaysEvents.tsx, LogoMarquee.tsx"
  },
  {
    "task_id": "WCS-004",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P2",
    "risk": "low",
    "status": "done",
    "title": "Improve empty Around the WCS state",
    "notes": "src/components/TeamUpdates.tsx"
  },
  {
    "task_id": "WCS-005",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P1",
    "risk": "medium",
    "status": "done",
    "title": "Make footer email signup form functional",
    "notes": "src/components/Footer.tsx"
  },
  {
    "task_id": "WCS-006",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Fix hero headline accessibility spacing/aria label",
    "notes": "src/components/Hero.tsx"
  },
  {
    "task_id": "WCS-007",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Hide test site banner in production",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  {
    "task_id": "WCS-008",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P3",
    "risk": "low",
    "status": "ready",
    "title": "Clarify navbar Coaches link label for logged-out users",
    "notes": "src/components/Navbar.tsx"
  },
  {
    "task_id": "WCS-009",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "medium",
    "status": "done",
    "title": "Improve LogoMarquee response.ok handling and fallback",
    "notes": "src/components/LogoMarquee.tsx"
  },
  {
    "task_id": "WCS-010",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "medium",
    "status": "done",
    "title": "Show fallback message instead of hiding TodaysEvents on error",
    "notes": "src/components/TodaysEvents.tsx"
  },
  {
    "task_id": "WCS-011",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P1",
    "risk": "low",
    "status": "done",
    "title": "Stabilize local Playwright smoke QA for home page",
    "notes": "tests/e2e, playwright config, global setup for http://localhost:3000"
  },
  {
    "task_id": "WCS-013",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "low",
    "status": "ready",
    "title": "Hide links to unfinished /shop page",
    "notes": "Public navigation or CTA paths should not expose /shop until the page is built out"
  },
  {
    "task_id": "WCS-014",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "low",
    "status": "ready",
    "title": "Hide links to unfinished /news page",
    "notes": "Public links should not expose /news until the page is built out"
  },
  {
    "task_id": "WCS-015",
    "project": "WCS",
    "bucket": "broken",
    "priority": "P2",
    "risk": "medium",
    "status": "ready",
    "title": "Investigate /schedules Supabase realtime auth console error",
    "notes": "Scout detected websocket auth failure on public /schedules page: Supabase realtime connection attempted without valid credentials"
  },
  {
    "task_id": "WCS-016",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "done",
    "title": "Flip TestSiteBanner background from black to white",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  {
    "task_id": "WCS-017",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "done",
    "title": "Flip TestSiteBanner background from white back to black",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  {
    "task_id": "WCS-018",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "done",
    "title": "Flip TestSiteBanner text color from white to black",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  {
    "task_id": "WCS-019",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "ready",
    "title": "Flip TestSiteBanner text color from black back to white",
    "notes": "src/components/TestSiteBanner.tsx"
  }
]


## FILE: state/MASTER_BACKLOG.md
# MASTER_BACKLOG

| Task ID | Project | Bucket | Priority | Risk | Status | Title | Notes |
|---|---|---|---|---|---|---|---|
| WCS-001 | WCS | ugly | P2 | low | done | Fix testimonial typo in PlayerTestimonials quote | src/components/PlayerTestimonials.tsx |
| WCS-002 | WCS | broken | P1 | medium | done | Fix stats section showing 0 for all metrics | src/components/StatsSection.tsx |
| WCS-003 | WCS | broken | P1 | medium | done | Add timeout/fallback handling for long loading states | TodaysEvents.tsx, LogoMarquee.tsx |
| WCS-004 | WCS | ugly | P2 | low | done | Improve empty Around the WCS state | src/components/TeamUpdates.tsx |
| WCS-005 | WCS | broken | P1 | medium | ready | Make footer email signup form functional | src/components/Footer.tsx |
| WCS-006 | WCS | ugly | P3 | low | ready | Fix hero headline accessibility spacing/aria label | src/components/Hero.tsx |
| WCS-007 | WCS | ugly | P3 | low | ready | Hide test site banner in production | src/components/TestSiteBanner.tsx |
| WCS-008 | WCS | ugly | P3 | low | ready | Clarify navbar Coaches link label for logged-out users | src/components/Navbar.tsx |
| WCS-009 | WCS | broken | P2 | medium | ready | Improve LogoMarquee response.ok handling and fallback | src/components/LogoMarquee.tsx |
| WCS-010 | WCS | broken | P2 | medium | done | Show fallback message instead of hiding TodaysEvents on error | src/components/TodaysEvents.tsx |
| WCS-011 | WCS | broken | P1 | low | done | Stabilize local Playwright smoke QA for home page | tests/e2e, playwright config, global setup for http://localhost:3000 |
| WCS-013 | WCS | broken | P2 | low | ready | Hide links to unfinished /shop page | Public navigation or CTA paths should not expose /shop until the page is built out |
| WCS-014 | WCS | broken | P2 | low | ready | Hide links to unfinished /news page | Public links should not expose /news until the page is built out |
| WCS-015 | WCS | broken | P2 | medium | ready | Investigate /schedules Supabase realtime auth console error | Scout detected websocket auth failure on public /schedules page: Supabase realtime connection attempted without valid credentials |
| WCS-016 | WCS | broken | P2 | medium | ready | Investigate public /teams scout HTTP 500 failure | Scout route: /teams; label: Teams; family: http_status; issues: HTTP status 500 on initial load. \|\| Console errors detected: 1; console: TypeError: Cannot read properties of undefined (reading ''map''); screenshot: C:\dev\jarvis-workspace\logs\wcs_scout\synthetic\public-teams.png; source: C:\dev\jarvis-workspace\logs\wcs_scout\synthetic_scout_fail.json |


## FILE: state/daily_plan.json
{
  "generated_at": "2026-03-12T15:04:13-05:00",
  "selected_task": {
    "task_id": "WCS-019",
    "project": "WCS",
    "bucket": "ugly",
    "priority": "P1",
    "risk": "low",
    "status": "ready",
    "title": "Flip TestSiteBanner text color from black back to white",
    "notes": "src/components/TestSiteBanner.tsx"
  },
  "selection_reason": {
    "rule": "priority_risk_task_id",
    "details": "Selected highest-priority eligible ready WCS task using deterministic ordering (priority, then risk, then numeric task id)."
  }
}


## FILE: state/DAILY_PLAN.md
# DAILY PLAN

**Generated at:** 2026-03-12T15:04:13-05:00

## Selected Task

- **Task ID:** WCS-019
- **Project:** WCS
- **Bucket:** ugly
- **Priority:** P1
- **Risk:** low
- **Status:** ready
- **Title:** Flip TestSiteBanner text color from black back to white
- **Notes:** src/components/TestSiteBanner.tsx

## Selection Reason

- **Rule:** priority_risk_task_id
- **Details:** Selected highest-priority eligible ready WCS task using deterministic ordering (priority, then risk, then numeric task id).


## FILE: state/run_log.json
[
  {
    "timestamp": "2026-03-11T12:19:02-05:00",
    "event": "task_selected",
    "task_id": "WCS-005",
    "project": "WCS",
    "title": "Make footer email signup form functional",
    "summary": "Jarvis selected task for current daily plan."
  },
  {
    "timestamp": "2026-03-11T13:46:40-05:00",
    "event": "task_selected",
    "task_id": "WCS-009",
    "project": "WCS",
    "title": "Improve LogoMarquee response.ok handling and fallback",
    "summary": "Jarvis selected task for current daily plan."
  },
  {
    "timestamp": "2026-03-11T13:46:40-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-009",
    "project": "WCS",
    "title": "Improve LogoMarquee response.ok handling and fallback",
    "summary": "Jarvis generated task packet and placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-009_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-009_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-009_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-009_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-009_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-11T14:49:02-05:00",
    "event": "task_selected",
    "task_id": "WCS-010",
    "project": "WCS",
    "title": "Show fallback message instead of hiding TodaysEvents on error",
    "summary": "Jarvis selected task for current daily plan."
  },
  {
    "timestamp": "2026-03-11T14:49:02-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-010",
    "project": "WCS",
    "title": "Show fallback message instead of hiding TodaysEvents on error",
    "summary": "Jarvis generated task packet and placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-010_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-010_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-010_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-010_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-010_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-11T14:49:02-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-010",
    "project": "WCS",
    "title": "Show fallback message instead of hiding TodaysEvents on error",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-010",
    "artifacts": [
      "jarvis-task-wcs-010"
    ]
  },
  {
    "timestamp": "2026-03-11T21:24:48-05:00",
    "event": "task_selected",
    "task_id": "WCS-016",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from black to white",
    "summary": "Jarvis selected task for current daily plan."
  },
  {
    "timestamp": "2026-03-11T21:24:48-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-016",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from black to white",
    "summary": "Jarvis generated task packet and placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-016_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-016_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-016_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-016_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-016_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-11T21:24:49-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-016",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from black to white",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-016",
    "artifacts": [
      "jarvis-task-wcs-016"
    ]
  },
  {
    "timestamp": "2026-03-12T10:37:44-05:00",
    "event": "task_selected",
    "task_id": "WCS-017",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from white back to black",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T10:37:44-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-017",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from white back to black",
    "summary": "Jarvis generated task packet and placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-017_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-017_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-017_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-017_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-017_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-12T10:37:45-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-017",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from white back to black",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-017",
    "artifacts": [
      "jarvis-task-wcs-017",
      "C:\\dev\\wcsv2.0-new"
    ]
  },
  {
    "timestamp": "2026-03-12T11:16:29-05:00",
    "event": "task_selected",
    "task_id": "WCS-017",
    "project": "WCS",
    "title": "Flip TestSiteBanner background from white back to black",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T12:28:50-05:00",
    "event": "task_selected",
    "task_id": "WCS-018",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from white to black",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T12:28:50-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-018",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from white to black",
    "summary": "Jarvis generated task packet and contract-valid placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-018_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-018_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-018_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-018_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-018_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-12T12:28:51-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-018",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from white to black",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-018",
    "artifacts": [
      "jarvis-task-wcs-018",
      "C:\\dev\\wcsv2.0-new"
    ]
  },
  {
    "timestamp": "2026-03-12T13:04:45-05:00",
    "event": "task_selected",
    "task_id": "WCS-018",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from white to black",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T14:57:08-05:00",
    "event": "task_selected",
    "task_id": "WCS-019",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from black back to white",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T14:57:08-05:00",
    "event": "task_packet_generated",
    "task_id": "WCS-019",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from black back to white",
    "summary": "Jarvis generated task packet and contract-valid placeholder execution artifacts.",
    "artifacts": [
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-019_task.json",
      "C:\\dev\\jarvis-workspace\\tasks\\WCS-019_task.md",
      "C:\\dev\\jarvis-workspace\\results\\WCS-019_worker_result.json",
      "C:\\dev\\jarvis-workspace\\qa\\WCS-019_qa_result.json",
      "C:\\dev\\jarvis-workspace\\logs\\WCS-019_escalation.json"
    ]
  },
  {
    "timestamp": "2026-03-12T15:04:13-05:00",
    "event": "task_selected",
    "task_id": "WCS-019",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from black back to white",
    "summary": "Jarvis selected task for current daily plan.",
    "artifacts": []
  },
  {
    "timestamp": "2026-03-12T15:04:14-05:00",
    "event": "task_branch_prepared",
    "task_id": "WCS-019",
    "project": "WCS",
    "title": "Flip TestSiteBanner text color from black back to white",
    "summary": "Jarvis prepared repo branch for task execution: jarvis-task-wcs-019",
    "artifacts": [
      "jarvis-task-wcs-019",
      "C:\\dev\\wcsv2.0-new"
    ]
  }
]


## FILE: state/RUN_LOG.md
# RUN LOG

## 2026-03-11T12:19:02-05:00 — task_selected

- **Task ID:** WCS-005
- **Project:** WCS
- **Title:** Make footer email signup form functional
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-11T13:46:40-05:00 — task_selected

- **Task ID:** WCS-009
- **Project:** WCS
- **Title:** Improve LogoMarquee response.ok handling and fallback
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-11T13:46:40-05:00 — task_packet_generated

- **Task ID:** WCS-009
- **Project:** WCS
- **Title:** Improve LogoMarquee response.ok handling and fallback
- **Summary:** Jarvis generated task packet and placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-009_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-009_task.md
  - C:\dev\jarvis-workspace\results\WCS-009_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-009_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-009_escalation.json

## 2026-03-11T14:49:02-05:00 — task_selected

- **Task ID:** WCS-010
- **Project:** WCS
- **Title:** Show fallback message instead of hiding TodaysEvents on error
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-11T14:49:02-05:00 — task_packet_generated

- **Task ID:** WCS-010
- **Project:** WCS
- **Title:** Show fallback message instead of hiding TodaysEvents on error
- **Summary:** Jarvis generated task packet and placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-010_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-010_task.md
  - C:\dev\jarvis-workspace\results\WCS-010_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-010_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-010_escalation.json

## 2026-03-11T14:49:02-05:00 — task_branch_prepared

- **Task ID:** WCS-010
- **Project:** WCS
- **Title:** Show fallback message instead of hiding TodaysEvents on error
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-010
- **Artifacts:**
  - jarvis-task-wcs-010

## 2026-03-11T21:24:48-05:00 — task_selected

- **Task ID:** WCS-016
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from black to white
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-11T21:24:48-05:00 — task_packet_generated

- **Task ID:** WCS-016
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from black to white
- **Summary:** Jarvis generated task packet and placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-016_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-016_task.md
  - C:\dev\jarvis-workspace\results\WCS-016_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-016_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-016_escalation.json

## 2026-03-11T21:24:49-05:00 — task_branch_prepared

- **Task ID:** WCS-016
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from black to white
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-016
- **Artifacts:**
  - jarvis-task-wcs-016

## 2026-03-12T10:37:44-05:00 — task_selected

- **Task ID:** WCS-017
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from white back to black
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T10:37:44-05:00 — task_packet_generated

- **Task ID:** WCS-017
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from white back to black
- **Summary:** Jarvis generated task packet and placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-017_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-017_task.md
  - C:\dev\jarvis-workspace\results\WCS-017_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-017_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-017_escalation.json

## 2026-03-12T10:37:45-05:00 — task_branch_prepared

- **Task ID:** WCS-017
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from white back to black
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-017
- **Artifacts:**
  - jarvis-task-wcs-017
  - C:\dev\wcsv2.0-new

## 2026-03-12T11:16:29-05:00 — task_selected

- **Task ID:** WCS-017
- **Project:** WCS
- **Title:** Flip TestSiteBanner background from white back to black
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T12:28:50-05:00 — task_selected

- **Task ID:** WCS-018
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from white to black
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T12:28:50-05:00 — task_packet_generated

- **Task ID:** WCS-018
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from white to black
- **Summary:** Jarvis generated task packet and contract-valid placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-018_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-018_task.md
  - C:\dev\jarvis-workspace\results\WCS-018_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-018_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-018_escalation.json

## 2026-03-12T12:28:51-05:00 — task_branch_prepared

- **Task ID:** WCS-018
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from white to black
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-018
- **Artifacts:**
  - jarvis-task-wcs-018
  - C:\dev\wcsv2.0-new

## 2026-03-12T13:04:45-05:00 — task_selected

- **Task ID:** WCS-018
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from white to black
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T14:57:08-05:00 — task_selected

- **Task ID:** WCS-019
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from black back to white
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T14:57:08-05:00 — task_packet_generated

- **Task ID:** WCS-019
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from black back to white
- **Summary:** Jarvis generated task packet and contract-valid placeholder execution artifacts.
- **Artifacts:**
  - C:\dev\jarvis-workspace\tasks\WCS-019_task.json
  - C:\dev\jarvis-workspace\tasks\WCS-019_task.md
  - C:\dev\jarvis-workspace\results\WCS-019_worker_result.json
  - C:\dev\jarvis-workspace\qa\WCS-019_qa_result.json
  - C:\dev\jarvis-workspace\logs\WCS-019_escalation.json

## 2026-03-12T15:04:13-05:00 — task_selected

- **Task ID:** WCS-019
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from black back to white
- **Summary:** Jarvis selected task for current daily plan.

## 2026-03-12T15:04:14-05:00 — task_branch_prepared

- **Task ID:** WCS-019
- **Project:** WCS
- **Title:** Flip TestSiteBanner text color from black back to white
- **Summary:** Jarvis prepared repo branch for task execution: jarvis-task-wcs-019
- **Artifacts:**
  - jarvis-task-wcs-019
  - C:\dev\wcsv2.0-new


## FILE: state/DAILY_REVIEW.md
# DAILY\_REVIEW

Date: 2026-03-09

## Summary

* WCS-001 completed.
* \- Updated Michael J. testimonial text in src/components/PlayerTestimonials.tsx
* \- npm run build passed
* \- Manual browser QA passed on localhost:3000
* \- Existing Playwright suite timed out during global setup and needs stabilization as a separate task
* WCS-011 completed.
* \- Stabilized Playwright global setup by waiting for local server readiness before browser navigation
* \- Added a dedicated home page smoke test
* \- Added a test:e2e:smoke script to package.json
* \- Playwright smoke QA passed locally with 1 passing test

## Wins

* Workspace initialized.

## Failures / blockers

* &nbsp;

## Next step

* Next step
* Execute WCS-002: fix stats section showing 0 for all metrics, and verify with build + smoke QA.

### WCS-002 — done
- Title: Fix stats section showing 0 for all metrics
- Worker: Added a 400ms fallback in StatsSection StatCard so the count-up animation always starts, preventing the metrics from staying at 0.
- QA: QA passed. Build completed successfully, Playwright home-page smoke test passed, and manual browser verification confirmed the stats animate from 0 to their target values instead of remaining stuck at 0.
- Files changed: src/components/StatsSection.tsx
- Commands run: cd c:\dev\wcsv2.0-new; npm run build, cd c:\dev\wcsv2.0-new; npm run test:e2e:smoke
- Reconciled at: 2026-03-09T18:46:09-05:00

### WCS-003 — done
- Title: Add timeout/fallback handling for long loading states
- Worker: Added AbortController-based timeout handling to TodaysEvents and LogoMarquee so long-running fetches fail instead of hanging indefinitely, allowing the existing error and fallback behavior to run.
- QA: QA passed. Build completed successfully, Playwright home-page smoke test passed, and manual browser verification confirmed long-loading requests no longer hang indefinitely. TodaysEvents exits loading state correctly and LogoMarquee uses fallback behavior on timeout/error.
- Files changed: src/components/TodaysEvents.tsx, src/components/LogoMarquee.tsx
- Commands run: cd c:\dev\wcsv2.0-new; npm run build, cd c:\dev\wcsv2.0-new; npm run test:e2e:smoke
- Reconciled at: 2026-03-09T19:16:49-05:00

### WCS-011 — done
- Title: Stabilize local Playwright smoke QA for home page
- Worker: Stabilized Playwright smoke QA by updating global setup to poll for server readiness for up to 90 seconds before verifying page load, adding a dedicated home page smoke test, and adding a test:e2e:smoke script.
- QA: QA passed. Build completed successfully, Playwright global setup successfully waited for the local server, and the dedicated home page smoke test passed.
- Files changed: tests/e2e/helpers/global-setup.ts, tests/e2e/home.spec.ts, package.json
- Commands run: cd c:\dev\wcsv2.0-new; npm run build, cd c:\dev\wcsv2.0-new; npm run test:e2e:smoke
- Reconciled at: 2026-03-09T20:22:30-05:00

### WCS-004 — done
- Title: Improve empty Around the WCS state
- Worker: Improved the empty 'Around the WCS' state in TeamUpdates by replacing the generic message with friendlier copy and increasing padding so the card looks intentional instead of broken.
- QA: Partial QA only. Build passed, but automated smoke QA was unavailable in this branch and manual browser verification did not reproduce the empty-state condition for 'Around the WCS', so the acceptance criteria could not be confirmed.
- Files changed: src/components/TeamUpdates.tsx
- Commands run: cd c:\dev\wcsv2.0-new; npm run build, cd c:\dev\wcsv2.0-new; npx playwright test tests/e2e/home.spec.ts
- Reconciled at: 2026-03-09T20:35:32-05:00

### WCS-005 — done
- Title: Make footer email signup form functional
- Worker: Wired the footer email signup form to open a prefilled mailto to info@wcsbasketball.com using the entered address, and ensured the app still builds and the home smoke Playwright test passes.
- QA: Verified that the footer email signup form now opens a prefilled mailto to info@wcsbasketball.com using the entered address, and that build and home smoke QA still pass.
- Files changed: src/components/Footer.tsx
- Commands run: npm run build, npm run test:e2e:smoke
- Reconciled at: 2026-03-11T13:35:42-05:00

### WCS-009 — done
- Title: Improve LogoMarquee response.ok handling and fallback
- Worker: Improved LogoMarquee API error handling by logging non-OK responses from the /api/teams endpoint while preserving the existing fallback behavior.
- QA: Confirmed that LogoMarquee now logs a devError when /api/teams returns a non-OK response while preserving the existing success path and fallback behavior, and that build and home smoke QA still pass.
- Files changed: src/components/LogoMarquee.tsx
- Commands run: npm run build, npm run test:e2e:smoke
- Reconciled at: 2026-03-11T14:19:09-05:00

### WCS-010 — done
- Title: Show fallback message instead of hiding TodaysEvents on error
- Worker: Updated TodaysEvents to show a clear fallback message when an error occurs instead of rendering nothing, while keeping the normal loading and no-events behaviors unchanged.
- QA: Verified that TodaysEvents now shows a visible fallback message when an error occurs instead of disappearing, while the normal loading and no-events behaviors remain unchanged and existing build and smoke QA still pass.
- Files changed: src/components/TodaysEvents.tsx
- Commands run: npm run build, npm run test:e2e:smoke
- Reconciled at: 2026-03-11T15:09:54-05:00

### WCS-016 — done
- Title: Flip TestSiteBanner background from black to white
- Worker: Updated src/components/TestSiteBanner.tsx to change the banner background from amber to white for the bounded WCS-016 fake hardening task.
- QA: Build passed and Playwright home smoke QA passed after updating TestSiteBanner background to white on the WCS-016 task branch.
- Files changed: src/components/TestSiteBanner.tsx
- Commands run: git branch --show-current, git status, git add .\src\components\TestSiteBanner.tsx, git commit -m "WCS-016 fake hardening test: flip TestSiteBanner background to white"
- Repo path: C:\dev\wcsv2.0-new
- Verified branch: jarvis-task-wcs-016
- Commits ahead of main: 1
- HEAD commit: 190060c
- Branch verified at: 2026-03-12T08:11:07-05:00
- Reconciled at: 2026-03-12T08:11:07-05:00

### WCS-017 — done
- Title: Flip TestSiteBanner background from white back to black
- Worker: Updated src/components/TestSiteBanner.tsx to change the banner background from amber to black for the bounded WCS-017 fake hardening task.
- QA: Build passed and Playwright home smoke QA passed after updating TestSiteBanner background to black on the WCS-017 task branch.
- Files changed: src/components/TestSiteBanner.tsx
- Commands run: git branch --show-current, git status, git add .\src\components\TestSiteBanner.tsx, git commit -m "WCS-017 fake hardening test: flip TestSiteBanner background to black"
- Repo path: C:\dev\wcsv2.0-new
- Verified branch: jarvis-task-wcs-017
- Commits ahead of main: 1
- HEAD commit: 197dce7
- Branch verified at: 2026-03-12T11:54:49-05:00
- Reconciled at: 2026-03-12T11:54:49-05:00

### WCS-018 — done
- Title: Flip TestSiteBanner text color from white to black
- Worker: Updated src/components/TestSiteBanner.tsx to change the banner text color to black for the bounded WCS-018 fake hardening task.
- QA: Build passed and Playwright home smoke QA passed after updating TestSiteBanner text color to black on the WCS-018 task branch.
- Files changed: src/components/TestSiteBanner.tsx
- Commands run: git branch --show-current, git status, git add .\src\components\TestSiteBanner.tsx, git commit -m "WCS-018 fake hardening test: flip TestSiteBanner text color to black"
- Repo path: C:\dev\wcsv2.0-new
- Verified branch: jarvis-task-wcs-018
- Commits ahead of main: 1
- HEAD commit: cd40f04
- Branch verified at: 2026-03-12T14:21:14-05:00
- Reconciled at: 2026-03-12T14:21:14-05:00


## FILE: state/escalations.json
[
  {
    "timestamp": "2026-03-12T13:04:45-05:00",
    "task_id": "WCS-018",
    "project": "WCS",
    "phase": "jarvis_packet_validation",
    "severity": "error",
    "status": "open",
    "human_action_required": true,
    "reason_code": "packet_contract_mismatch",
    "summary": "Jarvis detected invalid or mismatched packet/result placeholder contracts.",
    "details": [
      "C:\\dev\\jarvis-workspace\\results\\WCS-018_worker_result.json: expected placeholder status 'draft' before execution. Found: worker_complete"
    ],
    "recommended_next_action": "Inspect the generated packet and result placeholder files, correct the contract shape, then rerun jarvis.py (optionally with --force-packet)."
  },
  {
    "timestamp": "2026-03-12T14:57:08-05:00",
    "task_id": "WCS-019",
    "project": "WCS",
    "phase": "jarvis_branch_preparation",
    "severity": "error",
    "status": "open",
    "human_action_required": true,
    "reason_code": "branch_prepare_failed",
    "summary": "Jarvis branch preparer reported a non-zero exit code.",
    "details": [
      "Return code: 1",
      "STDERR: ERROR: Refusing to switch branches because the WCS repo has uncommitted changes on the wrong branch.\nCurrent branch: jarvis-task-wcs-018\nTarget branch: jarvis-task-wcs-019\nDirty files:\n M src/components/TestSiteBanner.tsx"
    ],
    "recommended_next_action": "Inspect prepare_wcs_task_branch.py output and the WCS repo state, fix issues, then rerun jarvis.py."
  }
]


## FILE: state/ESCALATIONS.md
# ESCALATIONS

## 2026-03-12T13:04:45-05:00 - packet_contract_mismatch

- **Task ID:** WCS-018
- **Project:** WCS
- **Phase:** jarvis_packet_validation
- **Severity:** error
- **Status:** open
- **Human action required:** yes
- **Summary:** Jarvis detected invalid or mismatched packet/result placeholder contracts.

- **Details:**
  - C:\dev\jarvis-workspace\results\WCS-018_worker_result.json: expected placeholder status 'draft' before execution. Found: worker_complete

- **Recommended next action:** Inspect the generated packet and result placeholder files, correct the contract shape, then rerun jarvis.py (optionally with --force-packet).

## 2026-03-12T14:57:08-05:00 - branch_prepare_failed

- **Task ID:** WCS-019
- **Project:** WCS
- **Phase:** jarvis_branch_preparation
- **Severity:** error
- **Status:** open
- **Human action required:** yes
- **Summary:** Jarvis branch preparer reported a non-zero exit code.

- **Details:**
  - Return code: 1
  - STDERR: ERROR: Refusing to switch branches because the WCS repo has uncommitted changes on the wrong branch.
Current branch: jarvis-task-wcs-018
Target branch: jarvis-task-wcs-019
Dirty files:
 M src/components/TestSiteBanner.tsx

- **Recommended next action:** Inspect prepare_wcs_task_branch.py output and the WCS repo state, fix issues, then rerun jarvis.py.


## FILE: scripts/jarvis.py
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


class JarvisError(Exception):
    pass


PRIORITY_ORDER = {"P1": 1, "P2": 2, "P3": 3, "P4": 4}
RISK_ORDER = {"low": 1, "medium": 2, "high": 3}
ELIGIBLE_BUCKETS = {"broken", "ugly"}
ALLOWED_PROJECT = "WCS"
REQUIRED_TASK_FIELDS = {"task_id", "project", "bucket", "priority", "risk", "status", "title"}
PLACEHOLDER_STATUS = "draft"


ESCALATIONS_JSON_NAME = "escalations.json"
ESCALATIONS_MD_NAME = "ESCALATIONS.md"


def now_local_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def today_local_date() -> str:
    return datetime.now().astimezone().date().isoformat()


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def read_json(path: Path, expected_type: type | None = None) -> Any:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise JarvisError(f"Required JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise JarvisError(f"Invalid JSON in {path}: {exc}") from exc

    if expected_type is not None and not isinstance(data, expected_type):
        raise JarvisError(
            f"Expected {expected_type.__name__} in {path}, got {type(data).__name__}"
        )
    return data


def read_optional_json(path: Path, default: Any, expected_type: type | None = None) -> Any:
    if not path.exists():
        return default
    return read_json(path, expected_type=expected_type)


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_escalations(escalations_path: Path) -> list[dict[str, Any]]:
    """Load existing escalations, initializing an empty list if the file does not exist."""
    if not escalations_path.exists():
        return []
    data = read_json(escalations_path, expected_type=list)
    # Defensive: ensure list of dict-like items
    cleaned: list[dict[str, Any]] = []
    for item in data:
        if isinstance(item, dict):
            cleaned.append(item)
    return cleaned


def render_escalations_md(records: list[dict[str, Any]]) -> str:
    lines = ["# ESCALATIONS", ""]
    if not records:
        lines.append("_No escalations recorded._")
        return "\n".join(lines)

    for record in records:
        timestamp = normalize_text(record.get("timestamp"))
        reason_code = normalize_text(record.get("reason_code"))
        human_action_required = "yes" if bool(record.get("human_action_required")) else "no"

        lines.extend(
            [
                f"## {timestamp} - {reason_code}",
                "",
                f"- **Task ID:** {normalize_text(record.get('task_id'))}",
                f"- **Project:** {normalize_text(record.get('project'))}",
                f"- **Phase:** {normalize_text(record.get('phase'))}",
                f"- **Severity:** {normalize_text(record.get('severity'))}",
                f"- **Status:** {normalize_text(record.get('status'))}",
                f"- **Human action required:** {human_action_required}",
                f"- **Summary:** {normalize_text(record.get('summary'))}",
                "",
                "- **Details:**",
            ]
        )

        details = record.get("details")
        if isinstance(details, list) and details:
            for detail in details:
                lines.append(f"  - {normalize_text(detail)}")
        else:
            lines.append("  - (none)")

        lines.extend(
            [
                "",
                f"- **Recommended next action:** {normalize_text(record.get('recommended_next_action'))}",
                "",
            ]
        )

    return "\n".join(lines).rstrip()


def append_escalation(
    *,
    state_dir: Path,
    task_id: str,
    phase: str,
    reason_code: str,
    summary: str,
    details: list[str],
    recommended_next_action: str,
) -> None:
    """Append a durable escalation record and render the markdown view."""
    escalations_path = state_dir / ESCALATIONS_JSON_NAME
    escalations_md_path = state_dir / ESCALATIONS_MD_NAME

    records = load_escalations(escalations_path)

    record = {
        "timestamp": now_local_iso(),
        "task_id": normalize_text(task_id).upper(),
        "project": ALLOWED_PROJECT,
        "phase": phase,
        "severity": "error",
        "status": "open",
        "human_action_required": True,
        "reason_code": reason_code,
        "summary": summary,
        "details": details,
        "recommended_next_action": recommended_next_action,
    }
    records.append(record)
    write_json(escalations_path, records)
    write_text(escalations_md_path, render_escalations_md(records))

    print("")
    print("JARVIS: escalation recorded")
    print(f"- JSON: {escalations_path}")
    print(f"- Markdown: {escalations_md_path}")


def parse_task_number(task_id: str) -> int:
    task_id = normalize_text(task_id).upper()
    if not task_id.startswith("WCS-"):
        raise JarvisError(f"Expected task id like WCS-016. Got: {task_id}")
    number_part = task_id.split("-", 1)[1]
    if not number_part.isdigit():
        raise JarvisError(f"Expected numeric WCS task id suffix. Got: {task_id}")
    return int(number_part)


def task_branch_name(task_id: str) -> str:
    return f"jarvis-task-{normalize_text(task_id).lower()}"


def priority_rank(task: dict[str, Any]) -> int:
    return PRIORITY_ORDER.get(normalize_text(task.get("priority")).upper(), 999)


def risk_rank(task: dict[str, Any]) -> int:
    return RISK_ORDER.get(normalize_text(task.get("risk")).lower(), 999)


def validate_task_shape(task: dict[str, Any], *, context: str) -> None:
    missing = [field for field in sorted(REQUIRED_TASK_FIELDS) if not normalize_text(task.get(field))]
    if missing:
        raise JarvisError(f"{context}: task is missing required fields: {', '.join(missing)}")

    task_id = normalize_text(task.get("task_id")).upper()
    parse_task_number(task_id)

    project = normalize_text(task.get("project")).upper()
    if project != ALLOWED_PROJECT:
        raise JarvisError(f"{context}: task project must be {ALLOWED_PROJECT}. Found: {project}")

    bucket = normalize_text(task.get("bucket")).lower()
    if bucket not in ELIGIBLE_BUCKETS:
        raise JarvisError(
            f"{context}: task bucket must be one of {sorted(ELIGIBLE_BUCKETS)}. Found: {bucket}"
        )

    status = normalize_text(task.get("status")).lower()
    if status != "ready":
        raise JarvisError(f"{context}: task status must be ready for execution. Found: {status}")

    priority = normalize_text(task.get("priority")).upper()
    if priority not in PRIORITY_ORDER:
        raise JarvisError(f"{context}: invalid priority: {priority}")

    risk = normalize_text(task.get("risk")).lower()
    if risk not in RISK_ORDER:
        raise JarvisError(f"{context}: invalid risk: {risk}")


def validate_backlog_task_uniqueness(backlog: list[dict[str, Any]], task_id: str) -> None:
    normalized = normalize_text(task_id).upper()
    matches = [
        task for task in backlog
        if isinstance(task, dict) and normalize_text(task.get("task_id")).upper() == normalized
    ]
    if len(matches) != 1:
        raise JarvisError(
            f"Backlog must contain exactly one entry for {normalized}. Found: {len(matches)}"
        )


def is_ready_wcs_task(task: dict[str, Any]) -> bool:
    if normalize_text(task.get("project")).upper() != ALLOWED_PROJECT:
        return False
    if normalize_text(task.get("status")).lower() != "ready":
        return False
    if normalize_text(task.get("bucket")).lower() not in ELIGIBLE_BUCKETS:
        return False
    task_id = normalize_text(task.get("task_id")).upper()
    return task_id.startswith("WCS-")


def select_task(backlog: list[dict[str, Any]]) -> dict[str, Any]:
    eligible = [task for task in backlog if isinstance(task, dict) and is_ready_wcs_task(task)]
    if not eligible:
        raise JarvisError("No eligible ready WCS task found in master_backlog.json.")

    try:
        eligible.sort(
            key=lambda task: (
                priority_rank(task),
                risk_rank(task),
                parse_task_number(normalize_text(task.get("task_id"))),
            )
        )
    except JarvisError:
        raise
    except Exception as exc:
        raise JarvisError(f"Failed to sort eligible tasks: {exc}") from exc

    return eligible[0]


def get_backlog_task_by_id(backlog: list[dict[str, Any]], task_id: str) -> dict[str, Any] | None:
    normalized = normalize_text(task_id).upper()
    for task in backlog:
        if not isinstance(task, dict):
            continue
        if normalize_text(task.get("task_id")).upper() == normalized:
            return task
    return None


def task_selected_today(
    daily_plan: dict[str, Any],
    run_log: list[dict[str, Any]],
    current_date: str,
) -> dict[str, Any] | None:
    selected_task = daily_plan.get("selected_task")
    generated_at = normalize_text(daily_plan.get("generated_at"))

    if isinstance(selected_task, dict) and generated_at.startswith(current_date):
        return selected_task

    for entry in reversed(run_log):
        if not isinstance(entry, dict):
            continue
        if normalize_text(entry.get("event")) != "task_selected":
            continue
        timestamp = normalize_text(entry.get("timestamp"))
        if not timestamp.startswith(current_date):
            continue
        task_id = normalize_text(entry.get("task_id"))
        if task_id:
            return {"task_id": task_id}
    return None


def build_daily_plan(selected_task: dict[str, Any], timestamp: str) -> dict[str, Any]:
    return {
        "generated_at": timestamp,
        "selected_task": selected_task,
        "selection_reason": {
            "rule": "priority_risk_task_id",
            "details": (
                "Selected highest-priority eligible ready WCS task using deterministic "
                "ordering (priority, then risk, then numeric task id)."
            ),
        },
    }


def render_daily_plan_md(plan: dict[str, Any]) -> str:
    selected_task = plan.get("selected_task", {})
    selection_reason = plan.get("selection_reason", {})
    lines = [
        "# DAILY PLAN",
        "",
        f"**Generated at:** {normalize_text(plan.get('generated_at'))}",
        "",
        "## Selected Task",
        "",
        f"- **Task ID:** {normalize_text(selected_task.get('task_id'))}",
        f"- **Project:** {normalize_text(selected_task.get('project'))}",
        f"- **Bucket:** {normalize_text(selected_task.get('bucket'))}",
        f"- **Priority:** {normalize_text(selected_task.get('priority'))}",
        f"- **Risk:** {normalize_text(selected_task.get('risk'))}",
        f"- **Status:** {normalize_text(selected_task.get('status'))}",
        f"- **Title:** {normalize_text(selected_task.get('title'))}",
        f"- **Notes:** {normalize_text(selected_task.get('notes'))}",
        "",
        "## Selection Reason",
        "",
        f"- **Rule:** {normalize_text(selection_reason.get('rule'))}",
        f"- **Details:** {normalize_text(selection_reason.get('details'))}",
    ]
    return "\n".join(lines)


def render_run_log_md(run_log: list[dict[str, Any]]) -> str:
    lines = ["# RUN LOG", ""]
    if not run_log:
        lines.append("_No run log entries yet._")
        return "\n".join(lines)

    for entry in run_log:
        lines.extend(
            [
                f"## {normalize_text(entry.get('timestamp'))} — {normalize_text(entry.get('event'))}",
                "",
                f"- **Task ID:** {normalize_text(entry.get('task_id'))}",
                f"- **Project:** {normalize_text(entry.get('project'))}",
                f"- **Title:** {normalize_text(entry.get('title'))}",
                f"- **Summary:** {normalize_text(entry.get('summary'))}",
            ]
        )
        artifacts = entry.get("artifacts")
        if isinstance(artifacts, list) and artifacts:
            lines.append("- **Artifacts:**")
            for artifact in artifacts:
                lines.append(f"  - {normalize_text(artifact)}")
        lines.append("")
    return "\n".join(lines).rstrip()


def build_run_log_entry(
    *,
    event: str,
    selected_task: dict[str, Any],
    timestamp: str,
    summary: str,
    artifacts: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "timestamp": timestamp,
        "event": event,
        "task_id": normalize_text(selected_task.get("task_id")).upper(),
        "project": normalize_text(selected_task.get("project")).upper(),
        "title": normalize_text(selected_task.get("title")),
        "summary": summary,
        "artifacts": artifacts or [],
    }


def append_run_log_entry(
    run_log_json_path: Path,
    run_log_md_path: Path,
    run_log: list[dict[str, Any]],
    entry: dict[str, Any],
) -> None:
    run_log.append(entry)
    write_json(run_log_json_path, run_log)
    write_text(run_log_md_path, render_run_log_md(run_log))


def task_artifact_paths(workspace: Path, task_id: str) -> dict[str, Path]:
    normalized_task_id = normalize_text(task_id).upper()
    return {
        "task_json": workspace / "tasks" / f"{normalized_task_id}_task.json",
        "task_md": workspace / "tasks" / f"{normalized_task_id}_task.md",
        "worker_result": workspace / "results" / f"{normalized_task_id}_worker_result.json",
        "qa_result": workspace / "qa" / f"{normalized_task_id}_qa_result.json",
        "escalation": workspace / "logs" / f"{normalized_task_id}_escalation.json",
    }


def analyze_artifacts(artifact_map: dict[str, Path]) -> tuple[list[Path], list[Path]]:
    existing = []
    missing = []
    for path in artifact_map.values():
        if path.exists():
            existing.append(path)
        else:
            missing.append(path)
    return existing, missing


def run_packet_generator(workspace: Path, task_id: str, *, force_packet: bool) -> tuple[int, str, str]:
    helper_path = workspace / "scripts" / "generate_task_packet.py"
    if not helper_path.exists():
        raise JarvisError(f"Packet generator not found: {helper_path}")

    cmd = [
        sys.executable,
        str(helper_path),
        "--workspace",
        str(workspace),
        "--task",
        normalize_text(task_id).upper(),
    ]
    if force_packet:
        cmd.append("--force")

    result = subprocess.run(
        cmd,
        cwd=workspace,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )
    return result.returncode, result.stdout, result.stderr


def run_branch_preparer(workspace: Path, task_id: str) -> tuple[int, str, str]:
    helper_path = workspace / "scripts" / "prepare_wcs_task_branch.py"
    if not helper_path.exists():
        raise JarvisError(f"Branch preparer not found: {helper_path}")

    cmd = [
        sys.executable,
        str(helper_path),
        "--workspace",
        str(workspace),
        "--task",
        normalize_text(task_id).upper(),
    ]

    result = subprocess.run(
        cmd,
        cwd=workspace,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )
    return result.returncode, result.stdout, result.stderr


def parse_branch_prep_output(stdout: str) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for line in stdout.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        parsed[key.strip().upper()] = value.strip()
    return parsed


def run_git(repo_path: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def verify_repo_branch_state(repo_path: Path) -> dict[str, str]:
    current_branch_result = run_git(repo_path, ["branch", "--show-current"])
    if current_branch_result.returncode != 0:
        raise JarvisError(
            current_branch_result.stderr.strip() or f"Failed to inspect repo branch at {repo_path}"
        )

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        raise JarvisError(
            status_result.stderr.strip() or f"Failed to inspect repo status at {repo_path}"
        )

    current_branch = current_branch_result.stdout.strip()
    dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
    return {
        "current_branch": current_branch,
        "dirty": "true" if dirty_lines else "false",
        "dirty_count": str(len(dirty_lines)),
    }


def validate_task_json_contract(path: Path, expected_task: dict[str, Any]) -> None:
    data = read_json(path, expected_type=dict)
    expected_id = normalize_text(expected_task.get("task_id")).upper()

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != expected_id:
        raise JarvisError(f"{path}: task_id mismatch. Expected {expected_id}, found {actual_id}")

    required = ["task_id", "title"]
    missing = [field for field in required if not normalize_text(data.get(field))]
    if missing:
        raise JarvisError(f"{path}: missing required task packet fields: {', '.join(missing)}")


def validate_result_placeholder_contract(path: Path, expected_task_id: str, kind: str) -> None:
    data = read_json(path, expected_type=dict)
    actual_id = normalize_text(data.get("task_id")).upper()
    expected_id = normalize_text(expected_task_id).upper()

    if actual_id != expected_id:
        raise JarvisError(f"{path}: {kind} task_id mismatch. Expected {expected_id}, found {actual_id}")

    status = normalize_text(data.get("status")).lower()
    if status != PLACEHOLDER_STATUS:
        raise JarvisError(
            f"{path}: expected placeholder status '{PLACEHOLDER_STATUS}' before execution. Found: {status}"
        )

    completed_at = data.get("completed_at")
    if normalize_text(completed_at):
        raise JarvisError(f"{path}: placeholder completed_at must be blank before execution")

    if kind == "worker_result":
        for field in ["executor", "summary", "notes"]:
            if field not in data:
                raise JarvisError(f"{path}: missing worker placeholder field: {field}")
        for list_field in ["files_changed", "commands_run", "issues_encountered"]:
            value = data.get(list_field)
            if not isinstance(value, list):
                raise JarvisError(f"{path}: worker placeholder field must be a list: {list_field}")

    if kind == "qa_result":
        for field in ["qa_tool", "summary", "notes"]:
            if field not in data:
                raise JarvisError(f"{path}: missing QA placeholder field: {field}")
        for list_field in ["checks_run", "checks_passed", "checks_failed", "artifacts"]:
            value = data.get(list_field)
            if not isinstance(value, list):
                raise JarvisError(f"{path}: QA placeholder field must be a list: {list_field}")


def validate_existing_artifacts(
    artifact_map: dict[str, Path],
    selected_task: dict[str, Any],
) -> None:
    task_id = normalize_text(selected_task.get("task_id")).upper()

    if not artifact_map["task_md"].exists():
        raise JarvisError(f"Existing packet set is invalid: missing markdown packet: {artifact_map['task_md']}")
    if not artifact_map["escalation"].exists():
        raise JarvisError(
            f"Existing packet set is invalid: missing escalation file: {artifact_map['escalation']}"
        )

    validate_task_json_contract(artifact_map["task_json"], selected_task)
    validate_result_placeholder_contract(artifact_map["worker_result"], task_id, "worker_result")
    validate_result_placeholder_contract(artifact_map["qa_result"], task_id, "qa_result")


def validate_generated_placeholders(
    artifact_map: dict[str, Path],
    selected_task: dict[str, Any],
) -> None:
    for path in artifact_map.values():
        if not path.exists():
            raise JarvisError(f"Expected generated artifact not found after packet generation: {path}")

    validate_existing_artifacts(artifact_map, selected_task)


def print_mode_banner(mode: str) -> None:
    print("=" * 72)
    print(f"JARVIS MODE: {mode}")
    print("=" * 72)


def print_packet_placeholder_warning(task_id: str, artifact_map: dict[str, Path], skipped_existing: bool) -> None:
    print("")
    print("JARVIS: artifact safety warning")
    print(
        "These task packet result files are placeholders until the worker result and QA result are filled truthfully."
    )
    print("They are NOT execution proof and do NOT mean the task is reconcile-ready.")
    print(f"- Worker placeholder: {artifact_map['worker_result']}")
    print(f"- QA placeholder:     {artifact_map['qa_result']}")
    print(f"- Escalation file:   {artifact_map['escalation']}")
    if skipped_existing:
        print("")
        print("JARVIS: packet generation was skipped because all artifacts already exist.")
        print("That does NOT mean the task is complete.")
        print("Existing packet/result artifacts were contract-validated before continuing.")
        print("Inspect existing worker/QA result contents before relying on them.")


def print_result_contracts() -> None:
    print("")
    print("JARVIS: result contracts")
    print("- Worker result status must be one of: worker_complete | blocked | escalated")
    print("- QA result status must be one of: qa_pass | qa_fail | escalated")
    print("- Keep completed_at blank in worker/QA result files until stamp_result_timestamp.py runs")


def print_contract_validation_summary(
    selected_task: dict[str, Any],
    packet_validated: bool,
    task_validated: bool,
) -> None:
    print("")
    print("JARVIS: contract validation")
    print(f"- Selected task execution-eligible: {'yes' if task_validated else 'no'}")
    print(f"- Packet/result placeholder contract valid: {'yes' if packet_validated else 'no'}")
    print(f"- Selected task: {normalize_text(selected_task.get('task_id')).upper()}")


def print_next_steps(
    selected_task: dict[str, Any],
    workspace: Path,
    repo_path: Path,
    artifact_map: dict[str, Path],
    branch_name: str,
) -> None:
    task_id = normalize_text(selected_task.get("task_id")).upper()
    print("")
    print("JARVIS: foreman phase complete")
    print("TASK IS NOT COMPLETE YET")
    print("Do NOT run reconcile until code is committed, worker result is final, QA result is final, and both are stamped.")
    print("")
    print("Next steps:")
    print(f"1. Open repo: {repo_path}")
    print("2. Verify git state:")
    print("   - git branch --show-current")
    print("   - git status")
    print(f"3. Confirm branch is: {branch_name}")
    print("4. Review task packet:")
    print(f"   - {artifact_map['task_json']}")
    print(f"   - {artifact_map['task_md']}")
    print("5. Perform the bounded implementation only")
    print("6. Inspect the diff before commit")
    print(f"   - git diff -- {normalize_text(selected_task.get('notes')) or '<target_file>'}")
    print("7. Commit on the correct task branch")
    print(f"8. Finalize worker result JSON: {artifact_map['worker_result']}")
    print("9. Run QA (current live path):")
    print("   - npm run build")
    print("   - npm run test:e2e:smoke")
    print(f"10. Finalize QA result JSON: {artifact_map['qa_result']}")
    print("11. Stamp timestamps:")
    print(f"   - python .\\stamp_result_timestamp.py ..\\results\\{task_id}_worker_result.json")
    print(f"   - python .\\stamp_result_timestamp.py ..\\qa\\{task_id}_qa_result.json")
    print("12. Reconcile only when ready:")
    print(f"   - python .\\reconcile_task_outcome.py --task {task_id}")
    print("")
    print("Working process/documentation files should be updated whenever a new process rule or hardening change is locked in.")
    print(f"Workspace: {workspace}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Jarvis foreman v6: select or reuse one WCS task, validate task/artifact contracts, generate packet artifacts, prepare the correct repo branch, and print operator-safe handoff guidance."
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow a new selection even if a WCS task was already selected today.",
    )
    parser.add_argument(
        "--force-packet",
        action="store_true",
        help="Force overwrite of existing task packet/result/qa/escalation files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    script_path = Path(__file__).resolve()
    workspace = script_path.parent.parent
    state_dir = workspace / "state"

    backlog_path = state_dir / "master_backlog.json"
    project_status_path = state_dir / "project_status_wcs.json"
    daily_plan_json_path = state_dir / "daily_plan.json"
    daily_plan_md_path = state_dir / "DAILY_PLAN.md"
    run_log_json_path = state_dir / "run_log.json"
    run_log_md_path = state_dir / "RUN_LOG.md"

    try:
        backlog = read_json(backlog_path, expected_type=list)
        project_status_wcs = read_json(project_status_path, expected_type=dict)
        daily_plan = read_optional_json(daily_plan_json_path, default={}, expected_type=dict)
        run_log = read_optional_json(run_log_json_path, default=[], expected_type=list)
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id="",
            phase="jarvis_state_load",
            reason_code="invalid_json_state",
            summary="Jarvis failed to load required JSON state during startup.",
            details=[str(exc)],
            recommended_next_action="Inspect the referenced JSON file, repair or restore it, then rerun jarvis.py.",
        )
        print("JARVIS: hard failure while loading required JSON state.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    current_date = today_local_date()
    current_timestamp = now_local_iso()

    used_existing_selection = False
    mode_banner = "NEW_SELECTION_NO_EXISTING_TODAY_TASK"

    try:
        if not args.force:
            existing_today = task_selected_today(daily_plan, run_log, current_date)
            if existing_today:
                existing_task_id = normalize_text(existing_today.get("task_id"))
                backlog_match = get_backlog_task_by_id(backlog, existing_task_id)
                if not backlog_match:
                    raise JarvisError(
                        f"Daily plan references task {existing_task_id}, but that task was not found in master_backlog.json."
                    )
                selected_task = backlog_match
                used_existing_selection = True
                mode_banner = "REUSING_ALREADY_SELECTED_TASK"
            else:
                selected_task = select_task(backlog)
        else:
            selected_task = select_task(backlog)
            mode_banner = "FORCED_FRESH_SELECTION"

        task_id = normalize_text(selected_task.get("task_id")).upper()
        validate_backlog_task_uniqueness(backlog, task_id)
        validate_task_shape(selected_task, context=f"Selected task {task_id}")
        task_validated = True
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id=locals().get("task_id", ""),
            phase="jarvis_selection",
            reason_code="invalid_selected_task",
            summary="Jarvis failed to select a valid execution-eligible WCS task.",
            details=[str(exc)],
            recommended_next_action="Inspect the backlog entry and project status for this task, correct invalid fields or duplicates, then rerun jarvis.py.",
        )
        print("JARVIS: task selection/validation failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    if not used_existing_selection:
        plan = build_daily_plan(selected_task, current_timestamp)
        selection_entry = build_run_log_entry(
            event="task_selected",
            selected_task=selected_task,
            timestamp=current_timestamp,
            summary="Jarvis selected task for current daily plan.",
        )

        write_json(daily_plan_json_path, plan)
        write_text(daily_plan_md_path, render_daily_plan_md(plan))
        append_run_log_entry(run_log_json_path, run_log_md_path, run_log, selection_entry)
    else:
        plan = daily_plan

    artifact_map = task_artifact_paths(workspace, task_id)
    existing_artifacts, missing_artifacts = analyze_artifacts(artifact_map)

    packet_generated = False
    packet_skipped_existing = False
    packet_contract_validated = False

    if existing_artifacts and missing_artifacts and not args.force_packet:
        message = (
            "Partial packet artifact state detected. Some packet files already exist, but not all of them. "
            "Inspect the task artifacts and rerun with --force-packet only if overwrite is intentional.\n"
            + "\n".join(f"- existing: {path}" for path in existing_artifacts)
            + "\n"
            + "\n".join(f"- missing: {path}" for path in missing_artifacts)
        )
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_packet_validation",
            reason_code="partial_packet_artifacts",
            summary="Jarvis detected partial packet artifact state for the selected task.",
            details=[message],
            recommended_next_action="Inspect existing/missing packet artifacts, decide whether to clean up or rerun with --force-packet, then rerun jarvis.py.",
        )
        print("JARVIS: partial packet artifact state detected.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    try:
        if existing_artifacts and not missing_artifacts and not args.force_packet:
            validate_existing_artifacts(artifact_map, selected_task)
            packet_contract_validated = True
            packet_skipped_existing = True
        else:
            returncode, packet_stdout, packet_stderr = run_packet_generator(
                workspace,
                task_id,
                force_packet=args.force_packet,
            )

            if returncode != 0:
                append_escalation(
                    state_dir=state_dir,
                    task_id=task_id,
                    phase="jarvis_packet_validation",
                    reason_code="packet_contract_mismatch",
                    summary="Jarvis packet generator reported a non-zero exit code.",
                    details=[
                        f"Return code: {returncode}",
                        f"STDERR: {packet_stderr.strip() or '(no stderr output)'}",
                    ],
                    recommended_next_action="Inspect generate_task_packet.py output, fix the underlying issue, then rerun jarvis.py (optionally with --force-packet).",
                )
                print("JARVIS: packet generation failed.", file=sys.stderr)
                print("An escalation record was written for operator follow-up.", file=sys.stderr)
                raise SystemExit(returncode)

            validate_generated_placeholders(artifact_map, selected_task)
            packet_contract_validated = True
            packet_generated = True
            packet_event = build_run_log_entry(
                event="task_packet_generated",
                selected_task=selected_task,
                timestamp=now_local_iso(),
                summary="Jarvis generated task packet and contract-valid placeholder execution artifacts.",
                artifacts=[str(path) for path in artifact_map.values()],
            )
            append_run_log_entry(run_log_json_path, run_log_md_path, run_log, packet_event)
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_packet_validation",
            reason_code="packet_contract_mismatch",
            summary="Jarvis detected invalid or mismatched packet/result placeholder contracts.",
            details=[str(exc)],
            recommended_next_action="Inspect the generated packet and result placeholder files, correct the contract shape, then rerun jarvis.py (optionally with --force-packet).",
        )
        print("JARVIS: packet/result placeholder contract validation failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    branch_returncode, branch_stdout, branch_stderr = run_branch_preparer(workspace, task_id)

    if branch_returncode != 0:
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_branch_preparation",
            reason_code="branch_prepare_failed",
            summary="Jarvis branch preparer reported a non-zero exit code.",
            details=[
                f"Return code: {branch_returncode}",
                f"STDERR: {branch_stderr.strip() or '(no stderr output)'}",
            ],
            recommended_next_action="Inspect prepare_wcs_task_branch.py output and the WCS repo state, fix issues, then rerun jarvis.py.",
        )
        print("JARVIS: branch preparation failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(branch_returncode)

    branch_info = parse_branch_prep_output(branch_stdout)
    target_branch = branch_info.get("TARGET_BRANCH", task_branch_name(task_id))
    repo_path = Path(
        branch_info.get("REPO_PATH") or normalize_text(project_status_wcs.get("repo_path"))
    ).resolve()

    try:
        verified_repo_state = verify_repo_branch_state(repo_path)
    except JarvisError as exc:
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_branch_verification",
            reason_code="repo_inspection_failed",
            summary="Jarvis failed to inspect the WCS repo branch/status after preparation.",
            details=[str(exc)],
            recommended_next_action="Inspect the WCS repo manually (branch and status), resolve issues, then rerun jarvis.py.",
        )
        print("JARVIS: repo branch/status inspection failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    branch_mode = branch_info.get("MODE", "")
    if branch_mode in {"switched_to_existing_target", "created_new_target_from_main"}:
        branch_event = build_run_log_entry(
            event="task_branch_prepared",
            selected_task=selected_task,
            timestamp=now_local_iso(),
            summary=f"Jarvis prepared repo branch for task execution: {target_branch}",
            artifacts=[target_branch, str(repo_path)],
        )
        append_run_log_entry(run_log_json_path, run_log_md_path, run_log, branch_event)

    print_mode_banner(mode_banner)

    if used_existing_selection:
        print("JARVIS: using existing task selected today")
    else:
        print("JARVIS: task selected")
        print(f"Workspace: {workspace}")
        print(f"Priority: {normalize_text(selected_task.get('priority'))}")
        print(f"Risk: {normalize_text(selected_task.get('risk'))}")
        print(f"Bucket: {normalize_text(selected_task.get('bucket'))}")
        print(f"daily_plan.json: {daily_plan_json_path}")
        print(f"DAILY_PLAN.md: {daily_plan_md_path}")
        print(f"run_log.json: {run_log_json_path}")
        print(f"RUN_LOG.md: {run_log_md_path}")

    print(f"Task ID: {task_id}")
    print(f"Title: {normalize_text(selected_task.get('title'))}")

    print("")
    if packet_skipped_existing:
        print("JARVIS: packet generation skipped")
        print("Reason: all packet artifacts already exist for this task. Use --force-packet to overwrite.")
        for path in artifact_map.values():
            print(f"- {path}")
    elif packet_generated:
        print("JARVIS: packet generation complete")
        for path in artifact_map.values():
            print(f"WROTE: {path}")
        print("")
        print("Task packet generation complete.")
        print(f"Task packet markdown: {artifact_map['task_md']}")
        print(f"Task packet JSON:     {artifact_map['task_json']}")

    print("")
    print("JARVIS: branch preparation result")
    for line in branch_stdout.strip().splitlines():
        print(line)

    print("")
    print("JARVIS: final branch verification")
    print(f"VERIFIED_REPO_PATH: {repo_path}")
    print(f"VERIFIED_CURRENT_BRANCH: {verified_repo_state['current_branch']}")
    print(f"VERIFIED_EXPECTED_BRANCH: {target_branch}")
    print(f"VERIFIED_DIRTY: {verified_repo_state['dirty']}")
    print(f"VERIFIED_DIRTY_COUNT: {verified_repo_state['dirty_count']}")

    if verified_repo_state["current_branch"] != target_branch:
        details = [
            "Post-branch-prep verification failed. Repo is not on the expected task branch.",
            f"Expected: {target_branch}",
            f"Actual:   {verified_repo_state['current_branch']}",
        ]
        append_escalation(
            state_dir=state_dir,
            task_id=task_id,
            phase="jarvis_branch_verification",
            reason_code="branch_verification_failed",
            summary="Jarvis detected a branch mismatch after branch preparation.",
            details=details,
            recommended_next_action="Switch the WCS repo to the expected task branch or repair the branch state, then rerun jarvis.py.",
        )
        print("JARVIS: post-branch-prep branch verification failed.", file=sys.stderr)
        print("An escalation record was written for operator follow-up.", file=sys.stderr)
        raise SystemExit(1)

    print_contract_validation_summary(selected_task, packet_contract_validated, task_validated)
    print_packet_placeholder_warning(task_id, artifact_map, packet_skipped_existing)
    print_result_contracts()
    print_next_steps(selected_task, workspace, repo_path, artifact_map, target_branch)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except JarvisError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        # Record a generic escalation when a JarvisError bubbles out that was not already
        # handled by a more specific escalation path.
        script_path = Path(__file__).resolve()
        state_dir = script_path.parent.parent / "state"
        try:
            append_escalation(
                state_dir=state_dir,
                task_id="",
                phase="jarvis_preflight",
                reason_code="invalid_json_state",
                summary="Jarvis encountered an unhandled JarvisError.",
                details=[str(exc)],
                recommended_next_action="Inspect the error message and recent changes, repair the underlying issue, then rerun jarvis.py.",
            )
        except Exception:
            # If escalation writing itself fails, avoid masking the original error.
            pass
        print("JARVIS: an escalation record may have been written for this failure.", file=sys.stderr)
        raise SystemExit(1)

## FILE: scripts/generate_task_packet.py
from __future__ import annotations

import argparse
import json
import re
import sys
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

VALID_STATUSES = {
    "draft",
    "ready",
    "dispatched",
    "in_progress",
    "worker_complete",
    "qa_pass",
    "qa_fail",
    "blocked",
    "escalated",
    "done",
    "deferred",
}

DEFAULT_PROJECT_CONFIG = {
    "WCS": {
        "repo_path": r"C:\dev\wcsv2.0-new",
        "branch_prefix": "jarvis-task-",
        "default_qa_plan": [
            "Run npm run build",
            "Start local app with npm run dev",
            "Run Playwright smoke QA if available",
            "Verify the targeted change locally in the browser",
        ],
        "default_stop_conditions": [
            "Required file cannot be found",
            "Build fails for unrelated reasons",
            "Task scope expands beyond the targeted fix",
        ],
    },
    "N8N": {
        "repo_path": "",
        "branch_prefix": "jarvis-task-",
        "default_qa_plan": [
            "Validate workflow or prompt output against the task rubric",
            "Confirm no malformed JSON or broken node configuration",
        ],
        "default_stop_conditions": [
            "Required workflow file cannot be found",
            "Task scope expands beyond the targeted fix",
            "Quality cannot be verified with the current rubric",
        ],
    },
}

TASK_MD_TEMPLATE = """# TASK PACKET

## Header
- Task ID: {task_id}
- Project: {project}
- Title: {title}
- Bucket: {bucket}
- Priority: {priority}
- Risk: {risk}
- Status: {status}

## Repo
- Repo Path: `{repo_path}`
- Branch Name: `{branch_name}`

## Problem Summary
{problem_summary}

## Goal
{goal}

## Suspected Files
{suspected_files_md}

## Acceptance Criteria
{acceptance_criteria_md}

## QA Plan
{qa_plan_md}

## System Impact
{system_impact}

## Stop Conditions
{stop_conditions_md}

## Notes
{notes}
"""


def now_local() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


class PacketGenerationError(Exception):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PacketGenerationError(f"JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise PacketGenerationError(f"Invalid JSON in {path}: {exc}") from exc



def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")



def parse_notes_to_files(notes: str) -> list[str]:
    if not notes:
        return []
    cleaned = notes.replace("`", "").strip()
    parts = [part.strip() for part in re.split(r",|;", cleaned) if part.strip()]
    return parts



def humanize_title_to_problem(title: str) -> str:
    title = title.strip()
    if not title:
        return "Describe the current issue clearly before execution."
    return f"{title}."



def goal_from_title(title: str) -> str:
    if not title.strip():
        return "Complete the scoped task and verify the result."
    return f"Resolve: {title}, with the smallest safe change that satisfies QA."



def acceptance_from_backlog(item: dict[str, Any], suspected_files: list[str]) -> list[str]:
    project = item.get("project", "")
    title = item.get("title", "")
    criteria = [f"The scoped issue is resolved: {title}"] if title else ["The scoped issue is resolved"]
    if project == "WCS":
        criteria.extend([
            "App builds successfully with npm run build",
            "Local app can be opened for verification",
            "Targeted change is visible or behaves correctly on the relevant page/flow",
        ])
    elif project == "N8N":
        criteria.extend([
            "Workflow or prompt output passes the defined quality/rubric check",
            "No malformed JSON or broken node configuration is introduced",
        ])
    if suspected_files:
        criteria.append("Changes remain tightly limited to the suspected files unless a clearly related helper/config file must also be updated")
    return criteria



def system_impact_from_risk(project: str, risk: str, suspected_files: list[str]) -> str:
    base = {
        "low": "Low risk.",
        "medium": "Medium risk.",
        "high": "High risk.",
    }.get(risk, "Risk level not specified.")
    if suspected_files:
        scope = f" Primary expected scope: {', '.join(suspected_files)}."
    else:
        scope = " Scope should stay tightly bounded to the targeted issue."
    if project == "WCS":
        return base + " This should avoid unrelated production-facing behavior changes unless strictly necessary." + scope
    if project == "N8N":
        return base + " This should avoid unrelated workflow, credential, or publishing changes unless strictly necessary." + scope
    return base + scope



def bulletize(items: list[str], fallback: str) -> str:
    if not items:
        return f"- {fallback}"
    return "\n".join(f"- {item}" for item in items)



def build_packet_json(item: dict[str, Any], project_cfg: dict[str, Any], dispatch: bool) -> dict[str, Any]:
    task_id = item["task_id"]
    project = item["project"]
    notes = str(item.get("notes", "") or "")
    suspected_files = parse_notes_to_files(notes)
    ts = now_local()
    status = "dispatched" if dispatch else str(item.get("status", "ready") or "ready")
    if status not in VALID_STATUSES:
        raise PacketGenerationError(f"Task {task_id} has unsupported status: {status}")

    packet = {
        "task_id": task_id,
        "project": project,
        "title": str(item.get("title", "") or ""),
        "bucket": str(item.get("bucket", "") or ""),
        "priority": str(item.get("priority", "") or ""),
        "risk": str(item.get("risk", "") or ""),
        "status": status,
        "repo_path": project_cfg.get("repo_path", ""),
        "branch_name": f"{project_cfg.get('branch_prefix', 'jarvis-task-')}{task_id.lower()}",
        "problem_summary": humanize_title_to_problem(str(item.get("title", "") or "")),
        "goal": goal_from_title(str(item.get("title", "") or "")),
        "suspected_files": suspected_files,
        "acceptance_criteria": acceptance_from_backlog(item, suspected_files),
        "qa_plan": deepcopy(project_cfg.get("default_qa_plan", [])),
        "system_impact": system_impact_from_risk(project, str(item.get("risk", "") or ""), suspected_files),
        "stop_conditions": deepcopy(project_cfg.get("default_stop_conditions", [])),
        "notes": notes,
        "created_at": ts,
        "updated_at": ts,
    }
    return packet



def build_packet_markdown(packet: dict[str, Any]) -> str:
    suspected_files_md = bulletize(packet.get("suspected_files", []), "Confirm the target files before execution")
    acceptance_md = bulletize(packet.get("acceptance_criteria", []), "Add acceptance criteria before execution")
    qa_plan_md = bulletize(packet.get("qa_plan", []), "Add a QA plan before execution")
    stop_md = bulletize(packet.get("stop_conditions", []), "Add stop conditions before execution")
    notes = packet.get("notes") or "No additional notes."

    return TASK_MD_TEMPLATE.format(
        task_id=packet.get("task_id", ""),
        project=packet.get("project", ""),
        title=packet.get("title", ""),
        bucket=packet.get("bucket", ""),
        priority=packet.get("priority", ""),
        risk=packet.get("risk", ""),
        status=packet.get("status", ""),
        repo_path=packet.get("repo_path", ""),
        branch_name=packet.get("branch_name", ""),
        problem_summary=packet.get("problem_summary", ""),
        goal=packet.get("goal", ""),
        suspected_files_md=suspected_files_md,
        acceptance_criteria_md=acceptance_md,
        qa_plan_md=qa_plan_md,
        system_impact=packet.get("system_impact", ""),
        stop_conditions_md=stop_md,
        notes=notes,
    )



def create_blank_result(task_id: str) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "status": "draft",
        "executor": "",
        "summary": "",
        "files_changed": [],
        "commands_run": [],
        "issues_encountered": [],
        "notes": "",
        "completed_at": "",
    }



def create_blank_qa(task_id: str) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "status": "draft",
        "qa_tool": "",
        "summary": "",
        "checks_run": [],
        "checks_passed": [],
        "checks_failed": [],
        "artifacts": [],
        "notes": "",
        "completed_at": "",
    }



def create_blank_escalation(task_id: str) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "status": "draft",
        "reason": "",
        "details": "",
        "recommended_next_action": "",
        "created_at": "",
    }



def maybe_write(path: Path, content: str | dict[str, Any], *, force: bool) -> tuple[bool, str]:
    if path.exists() and not force:
        return False, f"SKIPPED (exists): {path}"
    if isinstance(content, str):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    else:
        save_json(path, content)
    return True, f"WROTE: {path}"



def update_backlog_status(backlog_items: list[dict[str, Any]], task_id: str, new_status: str) -> None:
    for item in backlog_items:
        if item.get("task_id") == task_id:
            item["status"] = new_status
            return
    raise PacketGenerationError(f"Task {task_id} not found while updating backlog status")



def render_master_backlog_md(backlog_items: list[dict[str, Any]]) -> str:
    lines = [
        "# MASTER_BACKLOG",
        "",
        "| Task ID | Project | Bucket | Priority | Risk | Status | Title | Notes |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in backlog_items:
        notes = str(item.get("notes", "") or "")
        lines.append(
            f"| {item.get('task_id','')} | {item.get('project','')} | {item.get('bucket','')} | {item.get('priority','')} | {item.get('risk','')} | {item.get('status','')} | {item.get('title','')} | {notes} |"
        )
    lines.append("")
    return "\n".join(lines)



def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Jarvis task packet files from master_backlog.json")
    parser.add_argument("--task", help="Task ID to generate, e.g. WCS-002")
    parser.add_argument("--workspace", help="Workspace root path. Defaults to script grandparent directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite packet/result/qa/escalation files if they already exist")
    parser.add_argument("--dispatch", action="store_true", help="Mark the backlog item as dispatched when generating files")
    parser.add_argument("--list-ready", action="store_true", help="List ready tasks and exit")
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    workspace = Path(args.workspace).resolve() if args.workspace else script_path.parent.parent
    state_dir = workspace / "state"
    tasks_dir = workspace / "tasks"
    results_dir = workspace / "results"
    qa_dir = workspace / "qa"
    logs_dir = workspace / "logs"
    backlog_json_path = state_dir / "master_backlog.json"
    backlog_md_path = state_dir / "MASTER_BACKLOG.md"

    backlog = load_json(backlog_json_path)
    if not isinstance(backlog, list):
        raise PacketGenerationError(f"Expected a JSON array in {backlog_json_path}")

    if args.list_ready:
        ready = [item for item in backlog if str(item.get("status", "")).lower() == "ready"]
        if not ready:
            print("No ready tasks found.")
            return 0
        print("Ready tasks:")
        for item in ready:
            print(f"- {item.get('task_id')}: {item.get('title')}")
        return 0

    if not args.task:
        parser.error("--task is required unless --list-ready is used")

    task_id = args.task.strip().upper()
    item = next((row for row in backlog if str(row.get("task_id", "")).upper() == task_id), None)
    if not item:
        raise PacketGenerationError(f"Task {task_id} not found in {backlog_json_path}")

    project = str(item.get("project", "") or "")
    project_cfg = DEFAULT_PROJECT_CONFIG.get(project, {
        "repo_path": "",
        "branch_prefix": "jarvis-task-",
        "default_qa_plan": ["Run the project-appropriate QA checks"],
        "default_stop_conditions": ["Task scope expands beyond the targeted fix"],
    })

    packet = build_packet_json(item, project_cfg, dispatch=args.dispatch)
    packet_md = build_packet_markdown(packet)

    task_json_path = tasks_dir / f"{task_id}_task.json"
    task_md_path = tasks_dir / f"{task_id}_task.md"
    worker_result_path = results_dir / f"{task_id}_worker_result.json"
    qa_result_path = qa_dir / f"{task_id}_qa_result.json"
    escalation_path = logs_dir / f"{task_id}_escalation.json"

    outputs = [
        maybe_write(task_json_path, packet, force=args.force),
        maybe_write(task_md_path, packet_md, force=args.force),
        maybe_write(worker_result_path, create_blank_result(task_id), force=args.force),
        maybe_write(qa_result_path, create_blank_qa(task_id), force=args.force),
        maybe_write(escalation_path, create_blank_escalation(task_id), force=args.force),
    ]

    if args.dispatch:
        update_backlog_status(backlog, task_id, "dispatched")
        save_json(backlog_json_path, backlog)
        backlog_md_path.write_text(render_master_backlog_md(backlog), encoding="utf-8")
        print(f"UPDATED backlog status to dispatched for {task_id}")
        print(f"RENDERED: {backlog_md_path}")

    for _, message in outputs:
        print(message)

    print("\nTask packet generation complete.")
    print(f"Task packet markdown: {task_md_path}")
    print(f"Task packet JSON:     {task_json_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PacketGenerationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)


## FILE: scripts/prepare_wcs_task_branch.py
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


class BranchPrepError(Exception):
    pass


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise BranchPrepError(f"Required JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise BranchPrepError(f"Invalid JSON in {path}: {exc}") from exc


def run_git(repo_path: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def normalize_task_id(task_id: str) -> str:
    task_id = task_id.strip().upper()
    if not task_id.startswith("WCS-"):
        raise BranchPrepError(f"Expected task id like WCS-009. Got: {task_id}")
    return task_id


def target_branch_name(task_id: str) -> str:
    return f"jarvis-task-{task_id.lower()}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare the correct WCS task branch before execution."
    )
    parser.add_argument("--task", required=True, help="Task id, e.g. WCS-009")
    parser.add_argument(
        "--workspace",
        help="Jarvis workspace root. Defaults to script grandparent directory.",
    )
    parser.add_argument(
        "--repo",
        help="Override WCS repo path. If omitted, use state/project_status_wcs.json",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    script_path = Path(__file__).resolve()
    workspace = Path(args.workspace).resolve() if args.workspace else script_path.parent.parent
    state_dir = workspace / "state"

    task_id = normalize_task_id(args.task)
    target_branch = target_branch_name(task_id)

    if args.repo:
        repo_path = Path(args.repo).resolve()
    else:
        project_status = read_json(state_dir / "project_status_wcs.json")
        repo_path = Path(project_status["repo_path"]).resolve()

    if not repo_path.exists():
        raise BranchPrepError(f"WCS repo path does not exist: {repo_path}")

    git_dir = repo_path / ".git"
    if not git_dir.exists():
        raise BranchPrepError(f"Path is not a git repo: {repo_path}")

    current_branch_result = run_git(repo_path, ["branch", "--show-current"])
    if current_branch_result.returncode != 0:
        raise BranchPrepError(current_branch_result.stderr.strip() or "Failed to detect current branch.")

    current_branch = current_branch_result.stdout.strip()

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        raise BranchPrepError(status_result.stderr.strip() or "Failed to inspect repo status.")

    dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
    is_dirty = bool(dirty_lines)

    if current_branch == target_branch:
        mode = "already_on_target_dirty" if is_dirty else "already_on_target_clean"
        print(f"MODE: {mode}")
        print(f"CURRENT_BRANCH: {current_branch}")
        print(f"TARGET_BRANCH: {target_branch}")
        print(f"DIRTY: {'true' if is_dirty else 'false'}")
        if dirty_lines:
            print("DIRTY_FILES:")
            for line in dirty_lines:
                print(line)
        return 0

    if is_dirty:
        raise BranchPrepError(
            "Refusing to switch branches because the WCS repo has uncommitted changes on the wrong branch.\n"
            f"Current branch: {current_branch}\n"
            f"Target branch: {target_branch}\n"
            "Dirty files:\n" + "\n".join(dirty_lines)
        )

    branch_exists_result = run_git(repo_path, ["branch", "--list", target_branch])
    if branch_exists_result.returncode != 0:
        raise BranchPrepError(branch_exists_result.stderr.strip() or "Failed to inspect branch list.")

    target_exists = bool(branch_exists_result.stdout.strip())

    if target_exists:
        switch_result = run_git(repo_path, ["switch", target_branch])
        if switch_result.returncode != 0:
            raise BranchPrepError(switch_result.stderr.strip() or f"Failed to switch to {target_branch}.")
        mode = "switched_to_existing_target"
    else:
        main_exists_result = run_git(repo_path, ["branch", "--list", "main"])
        if main_exists_result.returncode != 0:
            raise BranchPrepError(main_exists_result.stderr.strip() or "Failed to inspect main branch.")
        if not main_exists_result.stdout.strip():
            raise BranchPrepError("Cannot create target branch because local 'main' branch was not found.")

        create_result = run_git(repo_path, ["switch", "-c", target_branch, "main"])
        if create_result.returncode != 0:
            raise BranchPrepError(create_result.stderr.strip() or f"Failed to create {target_branch} from main.")
        mode = "created_new_target_from_main"

    print(f"MODE: {mode}")
    print(f"CURRENT_BRANCH: {current_branch}")
    print(f"TARGET_BRANCH: {target_branch}")
    print("DIRTY: false")
    print(f"REPO_PATH: {repo_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BranchPrepError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)

## FILE: scripts/render_master_backlog.py
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


## FILE: scripts/reconcile_task_outcome.py
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

FINAL_STATUSES = {
    "done",
    "blocked",
    "escalated",
    "worker_complete",
    "qa_fail",
}


def now_local() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


class ReconcileError(Exception):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ReconcileError(f"JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ReconcileError(f"Invalid JSON in {path}: {exc}") from exc


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def escape_md(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def normalize_text(value: Any) -> str:
    return str(value or "").strip()


def render_master_backlog_md(backlog_items: list[dict[str, Any]]) -> str:
    lines = [
        "# MASTER_BACKLOG",
        "",
        "| Task ID | Project | Bucket | Priority | Risk | Status | Title | Notes |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in backlog_items:
        lines.append(
            "| "
            + " | ".join(
                [
                    escape_md(item.get("task_id", "")),
                    escape_md(item.get("project", "")),
                    escape_md(item.get("bucket", "")),
                    escape_md(item.get("priority", "")),
                    escape_md(item.get("risk", "")),
                    escape_md(item.get("status", "")),
                    escape_md(item.get("title", "")),
                    escape_md(item.get("notes", "")),
                ]
            )
            + " |"
        )
    lines.append("")
    return "\n".join(lines)


def normalize_status(value: str) -> str:
    return str(value or "").strip().lower()


def decide_final_status(worker: dict[str, Any], qa: dict[str, Any], escalation: dict[str, Any]) -> str:
    worker_status = normalize_status(worker.get("status", ""))
    qa_status = normalize_status(qa.get("status", ""))
    escalation_status = normalize_status(escalation.get("status", ""))

    if escalation_status == "escalated":
        return "escalated"
    if worker_status == "escalated":
        return "escalated"
    if worker_status == "blocked":
        return "blocked"

    if worker_status != "worker_complete":
        raise ReconcileError(
            f"Worker result must have status 'worker_complete', 'blocked', or 'escalated'. Found: {worker_status or '<blank>'}"
        )

    if qa_status == "qa_pass":
        return "done"
    if qa_status == "qa_fail":
        return "blocked"
    if qa_status == "escalated":
        return "escalated"

    raise ReconcileError(
        f"QA result must have status 'qa_pass', 'qa_fail', or 'escalated'. Found: {qa_status or '<blank>'}"
    )


def update_backlog_status(backlog_items: list[dict[str, Any]], task_id: str, final_status: str) -> dict[str, Any]:
    for item in backlog_items:
        if str(item.get("task_id", "")).upper() == task_id.upper():
            item["status"] = final_status
            return item
    raise ReconcileError(f"Task {task_id} not found in backlog")


def run_git(repo_path: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def task_branch_name(task_id: str) -> str:
    return f"jarvis-task-{normalize_text(task_id).lower()}"


def load_repo_path_for_project(workspace: Path, project: str) -> Path:
    project_upper = normalize_text(project).upper()
    if project_upper == "WCS":
        status_path = workspace / "state" / "project_status_wcs.json"
    else:
        raise ReconcileError(f"Repo verification is not defined for project: {project_upper or '<blank>'}")

    status = load_json(status_path)
    if not isinstance(status, dict):
        raise ReconcileError(f"Expected JSON object in {status_path}")

    raw_repo_path = normalize_text(status.get("repo_path"))
    if not raw_repo_path:
        raise ReconcileError(f"Missing repo_path in {status_path}")

    repo_path = Path(raw_repo_path)
    if not repo_path.exists():
        raise ReconcileError(f"Configured repo path does not exist: {repo_path}")
    if not (repo_path / ".git").exists():
        raise ReconcileError(f"Configured repo path is not a git repository: {repo_path}")
    return repo_path


def detect_baseline_branch(repo_path: Path) -> str | None:
    for candidate in ("main", "master"):
        result = run_git(repo_path, ["branch", "--list", candidate])
        if result.returncode != 0:
            raise ReconcileError(result.stderr.strip() or f"Failed to inspect git branches in {repo_path}")
        if result.stdout.strip():
            return candidate
    return None


def verify_done_repo_state(workspace: Path, task: dict[str, Any]) -> dict[str, Any]:
    task_id = normalize_text(task.get("task_id")).upper()
    project = normalize_text(task.get("project")).upper()
    repo_path = load_repo_path_for_project(workspace, project)
    expected_branch = task_branch_name(task_id)

    current_branch_result = run_git(repo_path, ["branch", "--show-current"])
    if current_branch_result.returncode != 0:
        raise ReconcileError(current_branch_result.stderr.strip() or "Failed to detect current git branch.")
    current_branch = current_branch_result.stdout.strip()

    if current_branch != expected_branch:
        raise ReconcileError(
            "Refusing to mark task done because repo is on the wrong branch. "
            f"Current branch: {current_branch or '<blank>'}. Expected: {expected_branch}."
        )

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        raise ReconcileError(status_result.stderr.strip() or "Failed to inspect git status.")
    dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
    if dirty_lines:
        raise ReconcileError(
            "Refusing to mark task done because repo has uncommitted changes.\n"
            + "\n".join(dirty_lines)
        )

    baseline_branch = detect_baseline_branch(repo_path)
    commits_ahead = None
    if baseline_branch:
        ahead_result = run_git(repo_path, ["rev-list", "--count", f"{baseline_branch}..HEAD"])
        if ahead_result.returncode != 0:
            raise ReconcileError(
                ahead_result.stderr.strip()
                or f"Failed to compare {expected_branch} against {baseline_branch}."
            )
        try:
            commits_ahead = int(ahead_result.stdout.strip() or "0")
        except ValueError as exc:
            raise ReconcileError(
                f"Unexpected rev-list output while comparing {expected_branch} against {baseline_branch}: {ahead_result.stdout!r}"
            ) from exc

        if commits_ahead < 1:
            raise ReconcileError(
                "Refusing to mark task done because the task branch has no commits ahead of "
                f"{baseline_branch}. Expected at least one committed task change on {expected_branch}."
            )

    head_commit_result = run_git(repo_path, ["rev-parse", "--short", "HEAD"])
    if head_commit_result.returncode != 0:
        raise ReconcileError(head_commit_result.stderr.strip() or "Failed to read HEAD commit.")

    return {
        "repo_path": str(repo_path),
        "expected_branch": expected_branch,
        "current_branch": current_branch,
        "baseline_branch": baseline_branch or "",
        "commits_ahead_of_baseline": commits_ahead,
        "head_commit": head_commit_result.stdout.strip(),
        "verified_at": now_local(),
    }


def build_daily_review_entry(
    task: dict[str, Any],
    worker: dict[str, Any],
    qa: dict[str, Any],
    final_status: str,
    repo_verification: dict[str, Any] | None = None,
) -> str:
    task_id = task.get("task_id", "")
    title = task.get("title", "")
    worker_summary = (worker.get("summary") or "").strip()
    qa_summary = (qa.get("summary") or "").strip()
    files_changed = worker.get("files_changed") or []
    commands_run = worker.get("commands_run") or []

    lines = [
        f"### {task_id} — {final_status}",
        f"- Title: {title}",
    ]
    if worker_summary:
        lines.append(f"- Worker: {worker_summary}")
    if qa_summary:
        lines.append(f"- QA: {qa_summary}")
    if files_changed:
        lines.append(f"- Files changed: {', '.join(map(str, files_changed))}")
    if commands_run:
        lines.append(f"- Commands run: {', '.join(map(str, commands_run))}")
    if repo_verification:
        lines.append(f"- Repo path: {repo_verification.get('repo_path', '')}")
        lines.append(f"- Verified branch: {repo_verification.get('current_branch', '')}")
        baseline_branch = normalize_text(repo_verification.get("baseline_branch"))
        if baseline_branch:
            lines.append(
                f"- Commits ahead of {baseline_branch}: {repo_verification.get('commits_ahead_of_baseline', '')}"
            )
        lines.append(f"- HEAD commit: {repo_verification.get('head_commit', '')}")
        lines.append(f"- Branch verified at: {repo_verification.get('verified_at', '')}")
    lines.append(f"- Reconciled at: {now_local()}")
    lines.append("")
    return "\n".join(lines)


def append_daily_review(
    review_path: Path,
    task: dict[str, Any],
    worker: dict[str, Any],
    qa: dict[str, Any],
    final_status: str,
    repo_verification: dict[str, Any] | None = None,
) -> None:
    entry = build_daily_review_entry(task, worker, qa, final_status, repo_verification=repo_verification)
    if review_path.exists():
        existing = review_path.read_text(encoding="utf-8")
    else:
        today = datetime.now().strftime("%Y-%m-%d")
        existing = f"# DAILY_REVIEW\n\nDate: {today}\n\nSummary\n\nWins\n\nFailures / blockers\n\nNext step\n\n"

    task_id = str(task.get("task_id", ""))
    if f"### {task_id} —" in existing:
        return

    content = existing.rstrip() + "\n\n" + entry
    review_path.write_text(content, encoding="utf-8")


CURSOR_COMPLETION_CONTRACT = """When you finish the task, return your summary in this exact structure:

1. What changed
- Files changed:
- Short description of each change:

2. Commands run
- List each command exactly as run

3. Result
- Build result:
- Test result:
- QA result:

4. Issues encountered
- None
or
- List each issue clearly

5. Stop conditions
- State whether any stop condition was hit

6. Recommended worker_result.json fields
{
  \"status\": \"worker_complete\",
  \"summary\": \"...\",
  \"files_changed\": [\"...\"],
  \"commands_run\": [\"...\"],
  \"issues_encountered\": [],
  \"notes\": \"...\"
}

Do not add extra sections. Do not give broad advice unless asked."""


def main() -> int:
    parser = argparse.ArgumentParser(description="Reconcile task outcome from worker and QA JSON files")
    parser.add_argument("--task", required=False, help="Task ID to reconcile, e.g. WCS-002")
    parser.add_argument("--workspace", help="Workspace root path. Defaults to script grandparent directory.")
    parser.add_argument("--skip-review", action="store_true", help="Do not append an entry to DAILY_REVIEW.md")
    parser.add_argument("--print-cursor-contract", action="store_true", help="Print the recommended Cursor completion contract and exit")
    args = parser.parse_args()

    if args.print_cursor_contract:
        print(CURSOR_COMPLETION_CONTRACT)
        return 0

    if not args.task:
        parser.error("--task is required unless --print-cursor-contract is used")

    script_path = Path(__file__).resolve()
    workspace = Path(args.workspace).resolve() if args.workspace else script_path.parent.parent
    state_dir = workspace / "state"
    results_dir = workspace / "results"
    qa_dir = workspace / "qa"
    logs_dir = workspace / "logs"

    task_id = args.task.strip().upper()
    backlog_json_path = state_dir / "master_backlog.json"
    backlog_md_path = state_dir / "MASTER_BACKLOG.md"
    daily_review_path = state_dir / "DAILY_REVIEW.md"
    worker_result_path = results_dir / f"{task_id}_worker_result.json"
    qa_result_path = qa_dir / f"{task_id}_qa_result.json"
    escalation_path = logs_dir / f"{task_id}_escalation.json"

    backlog = load_json(backlog_json_path)
    if not isinstance(backlog, list):
        raise ReconcileError(f"Expected a JSON array in {backlog_json_path}")

    task = next((item for item in backlog if str(item.get("task_id", "")).upper() == task_id), None)
    if not task:
        raise ReconcileError(f"Task {task_id} not found in backlog")

    worker = load_json(worker_result_path)
    qa = load_json(qa_result_path)
    escalation = load_json(escalation_path) if escalation_path.exists() else {"status": "draft"}

    if str(worker.get("task_id", "")).upper() != task_id:
        raise ReconcileError(f"Worker result task_id mismatch in {worker_result_path}")
    if str(qa.get("task_id", "")).upper() != task_id:
        raise ReconcileError(f"QA result task_id mismatch in {qa_result_path}")

    final_status = decide_final_status(worker, qa, escalation)
    repo_verification = verify_done_repo_state(workspace, task) if final_status == "done" else None

    updated_task = update_backlog_status(backlog, task_id, final_status)
    save_json(backlog_json_path, backlog)
    backlog_md_path.write_text(render_master_backlog_md(backlog), encoding="utf-8")

    if not args.skip_review:
        append_daily_review(daily_review_path, updated_task, worker, qa, final_status, repo_verification=repo_verification)

    print(f"FINAL STATUS: {final_status}")
    if repo_verification:
        print("BRANCH VERIFIED: yes")
        print(f"REPO PATH: {repo_verification['repo_path']}")
        print(f"EXPECTED BRANCH: {repo_verification['expected_branch']}")
        print(f"CURRENT BRANCH: {repo_verification['current_branch']}")
        if repo_verification.get("baseline_branch"):
            print(
                f"COMMITS AHEAD OF {repo_verification['baseline_branch'].upper()}: "
                f"{repo_verification['commits_ahead_of_baseline']}"
            )
        print(f"HEAD COMMIT: {repo_verification['head_commit']}")
    print(f"UPDATED: {backlog_json_path}")
    print(f"RENDERED: {backlog_md_path}")
    if not args.skip_review:
        print(f"UPDATED: {daily_review_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ReconcileError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)


## FILE: scripts/stamp_result_timestamp.py
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

## FILE: scripts/pre_reconcile_check.py
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Tuple


ALLOWED_WORKER_STATUSES = {"worker_complete", "blocked", "escalated"}
ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


class CheckError(Exception):
    pass


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
        raise CheckError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise CheckError(f"Invalid JSON in {path}: {exc}") from exc


def run_git(repo_path: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only pre-reconcile readiness check for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016.",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def validate_task_id(task_id: str) -> str:
    task_id_norm = normalize_text(task_id).upper()
    if not task_id_norm.startswith("WCS-"):
        raise CheckError(f"Invalid task id (expected WCS-XXX): {task_id_norm}")
    suffix = task_id_norm.split("-", 1)[1]
    if not suffix.isdigit():
        raise CheckError(f"Invalid task id suffix (expected numeric): {task_id_norm}")
    return task_id_norm


def check_artifacts(workspace: Path, task_id: str, failures: list[str]) -> Tuple[Path, Path, Path]:
    task_json = workspace / "tasks" / f"{task_id}_task.json"
    worker_result = workspace / "results" / f"{task_id}_worker_result.json"
    qa_result = workspace / "qa" / f"{task_id}_qa_result.json"

    if not task_json.exists():
        failures.append(f"Missing task packet JSON: {task_json}")
    if not worker_result.exists():
        failures.append(f"Missing worker result JSON: {worker_result}")
    if not qa_result.exists():
        failures.append(f"Missing QA result JSON: {qa_result}")

    return task_json, worker_result, qa_result


def check_worker_result(path: Path, task_id: str, failures: list[str]) -> None:
    try:
        data = read_json(path)
    except CheckError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"Worker result must be a JSON object: {path}")
        return

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"Worker result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("Worker result status must not be 'draft'.")
    if status not in ALLOWED_WORKER_STATUSES:
        failures.append(
            f"Worker result status must be one of {sorted(ALLOWED_WORKER_STATUSES)}. Found: {status or '(blank)'}."
        )

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("Worker result completed_at must be present and non-blank.")


def check_qa_result(path: Path, task_id: str, failures: list[str]) -> None:
    try:
        data = read_json(path)
    except CheckError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"QA result must be a JSON object: {path}")
        return

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"QA result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("QA result status must not be 'draft'.")
    if status not in ALLOWED_QA_STATUSES:
        failures.append(
            f"QA result status must be one of {sorted(ALLOWED_QA_STATUSES)}. Found: {status or '(blank)'}."
        )

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("QA result completed_at must be present and non-blank.")


def resolve_repo_path(workspace: Path, failures: list[str]) -> Path | None:
    project_status_path = workspace / "state" / "project_status_wcs.json"
    try:
        data = read_json(project_status_path)
    except CheckError as exc:
        failures.append(str(exc))
        return None

    if not isinstance(data, dict):
        failures.append(f"project_status_wcs.json must be a JSON object: {project_status_path}")
        return None

    repo_raw = normalize_text(data.get("repo_path"))
    if not repo_raw:
        failures.append("project_status_wcs.json is missing repo_path.")
        return None

    repo_path = Path(repo_raw).resolve()
    if not repo_path.exists():
        failures.append(f"Repo path does not exist: {repo_path}")
        return None

    return repo_path


def check_repo_state(repo_path: Path, task_id: str, failures: list[str]) -> tuple[str | None, str | None, int | None]:
    expected_branch = f"jarvis-task-{task_id.lower()}"

    branch_result = run_git(repo_path, ["branch", "--show-current"])
    if branch_result.returncode != 0:
        failures.append(
            f"Failed to read current branch in repo {repo_path}: "
            f"{branch_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, None, None

    current_branch = normalize_text(branch_result.stdout)
    if not current_branch:
        failures.append(f"Current branch is empty in repo {repo_path}.")
    elif current_branch != expected_branch:
        failures.append(
            f"Current branch mismatch. Expected {expected_branch}, found {current_branch}."
        )

    status_result = run_git(repo_path, ["status", "--porcelain"])
    if status_result.returncode != 0:
        failures.append(
            f"Failed to inspect repo status in {repo_path}: "
            f"{status_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        dirty_lines = [line for line in status_result.stdout.splitlines() if line.strip()]
        if dirty_lines:
            failures.append(
                f"Repo working tree is not clean in {repo_path}. {len(dirty_lines)} changed path(s) detected."
            )

    base_branch = None
    for candidate in ["main", "master"]:
        rev_parse = run_git(repo_path, ["rev-parse", "--verify", candidate])
        if rev_parse.returncode == 0:
            base_branch = candidate
            break

    if base_branch is None:
        failures.append(f"Neither 'main' nor 'master' branch exists in repo {repo_path}.")
        return expected_branch, current_branch, None

    ahead_result = run_git(repo_path, ["rev-list", "--count", f"{base_branch}..{current_branch or 'HEAD'}"])
    if ahead_result.returncode != 0:
        failures.append(
            f"Failed to compute commits ahead of {base_branch} in {repo_path}: "
            f"{ahead_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, current_branch, None

    ahead_str = normalize_text(ahead_result.stdout)
    try:
        ahead_count = int(ahead_str or "0")
    except ValueError:
        failures.append(
            f"Unexpected rev-list output for {base_branch}..{current_branch or 'HEAD'} in {repo_path}: {ahead_str}"
        )
        return expected_branch, current_branch, None

    if ahead_count < 1:
        failures.append(
            f"Task branch must be ahead of {base_branch} by at least 1 commit. Found: {ahead_count}."
        )

    return expected_branch, current_branch, ahead_count


def main() -> int:
    args = parse_args()

    if not args.task:
        print("PRE-RECONCILE CHECK: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except CheckError as exc:
        print("PRE-RECONCILE CHECK: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: list[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    task_json, worker_result, qa_result = check_artifacts(workspace, task_id, failures)

    if worker_result.exists():
        check_worker_result(worker_result, task_id, failures)

    if qa_result.exists():
        check_qa_result(qa_result, task_id, failures)

    repo_path = resolve_repo_path(workspace, failures)
    expected_branch = None
    current_branch = None
    ahead_count: int | None = None

    if repo_path is not None:
        expected_branch, current_branch, ahead_count = check_repo_state(
            repo_path, task_id, failures
        )

    if failures:
        print("PRE-RECONCILE CHECK: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    print("PRE-RECONCILE CHECK: PASS")
    print(f"Task: {task_id}")
    if repo_path is not None and expected_branch is not None and current_branch is not None:
        print(f"Repo path: {repo_path}")
        print(f"Expected branch: {expected_branch}")
        print(f"Current branch: {current_branch}")
        if ahead_count is not None:
            print(f"Commits ahead of main/master: {ahead_count}")
    print("Passed checks:")
    print("- task, worker result, and QA result artifacts present")
    print("- worker result contract and completed_at valid")
    print("- QA result contract and completed_at valid")
    print("- repo path, branch, and clean working tree valid")
    print("- task branch ahead of main/master by at least 1 commit")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())



## FILE: scripts/post_reconcile_validate.py
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ALLOWED_WORKER_STATUSES = {"worker_complete", "blocked", "escalated"}
ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


class ValidationError(Exception):
    pass


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
        raise ValidationError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only post-reconcile validation for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def validate_task_id(task_id_raw: str) -> str:
    task_id = normalize_text(task_id_raw).upper()
    if not task_id.startswith("WCS-"):
        raise ValidationError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise ValidationError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def check_state_files_exist(workspace: Path, failures: list[str]) -> dict[str, Path]:
    state_dir = workspace / "state"
    paths = {
        "backlog_json": state_dir / "master_backlog.json",
        "backlog_md": state_dir / "MASTER_BACKLOG.md",
        "daily_review_md": state_dir / "DAILY_REVIEW.md",
    }
    for key, path in paths.items():
        if not path.exists():
            failures.append(f"Missing state file: {path}")
    return paths


def check_backlog_json(backlog_json_path: Path, task_id: str, failures: list[str]) -> dict[str, Any] | None:
    try:
        data = read_json(backlog_json_path)
    except ValidationError as exc:
        failures.append(str(exc))
        return None

    if not isinstance(data, list):
        failures.append(f"master_backlog.json root must be a list: {backlog_json_path}")
        return None

    matches: list[dict[str, Any]] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        if normalize_text(item.get("task_id")).upper() == task_id:
            matches.append(item)

    if len(matches) == 0:
        failures.append(f"No backlog entry found for task {task_id} in master_backlog.json.")
        return None
    if len(matches) > 1:
        failures.append(f"Expected exactly one backlog entry for {task_id}, found {len(matches)}.")
        return None

    record = matches[0]
    project = normalize_text(record.get("project")).upper()
    status = normalize_text(record.get("status")).lower()

    if project != "WCS":
        failures.append(
            f"Backlog entry for {task_id} has wrong project. Expected WCS, found {project or '(blank)'}."
        )
    if status != "done":
        failures.append(
            f"Backlog entry for {task_id} must have status 'done'. Found {status or '(blank)'}."
        )

    return record


def check_backlog_markdown(
    backlog_md_path: Path,
    task_id: str,
    title: str | None,
    failures: list[str],
) -> None:
    try:
        text = backlog_md_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        failures.append(f"Missing backlog markdown file: {backlog_md_path}")
        return
    except OSError as exc:
        failures.append(f"Failed to read backlog markdown {backlog_md_path}: {exc}")
        return

    if task_id not in text:
        failures.append(f"Task id {task_id} not found in MASTER_BACKLOG.md.")

    if title:
        if title not in text:
            failures.append(f"Task title not found in MASTER_BACKLOG.md: {title}")

    # Simple done indicator: look for a line containing both the task id and 'done' (case-insensitive).
    done_line_found = False
    for line in text.splitlines():
        if task_id in line and "done" in line.lower():
            done_line_found = True
            break
    if not done_line_found:
        failures.append(
            f"MASTER_BACKLOG.md does not show a simple 'done' indicator on the same line as {task_id}."
        )


def check_daily_review(daily_review_path: Path, task_id: str, failures: list[str]) -> None:
    try:
        text = daily_review_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        failures.append(f"Missing DAILY_REVIEW.md: {daily_review_path}")
        return
    except OSError as exc:
        failures.append(f"Failed to read DAILY_REVIEW.md {daily_review_path}: {exc}")
        return

    if task_id not in text:
        failures.append(f"Task id {task_id} not found in DAILY_REVIEW.md.")


def check_worker_result(worker_path: Path, task_id: str, failures: list[str]) -> None:
    if not worker_path.exists():
        failures.append(f"Missing worker result JSON: {worker_path}")
        return

    try:
        data = read_json(worker_path)
    except ValidationError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"Worker result must be a JSON object: {worker_path}")
        return

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"Worker result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status not in ALLOWED_WORKER_STATUSES:
        failures.append(
            f"Worker result status must be one of {sorted(ALLOWED_WORKER_STATUSES)}. Found: {status or '(blank)'}."
        )

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("Worker result completed_at must be present and non-blank.")


def check_qa_result(qa_path: Path, task_id: str, failures: list[str]) -> None:
    if not qa_path.exists():
        failures.append(f"Missing QA result JSON: {qa_path}")
        return

    try:
        data = read_json(qa_path)
    except ValidationError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"QA result must be a JSON object: {qa_path}")
        return

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"QA result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status not in ALLOWED_QA_STATUSES:
        failures.append(
            f"QA result status must be one of {sorted(ALLOWED_QA_STATUSES)}. Found: {status or '(blank)'}."
        )

    completed_at = normalize_text(data.get("completed_at"))
    if not completed_at:
        failures.append("QA result completed_at must be present and non-blank.")


def main() -> int:
    args = parse_args()

    if not args.task:
        print("POST-RECONCILE VALIDATION: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except ValidationError as exc:
        print("POST-RECONCILE VALIDATION: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: list[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    paths = check_state_files_exist(workspace, failures)

    backlog_record: dict[str, Any] | None = None
    title: str | None = None

    backlog_json_path = paths["backlog_json"]
    backlog_md_path = paths["backlog_md"]
    daily_review_path = paths["daily_review_md"]

    if backlog_json_path.exists():
        backlog_record = check_backlog_json(backlog_json_path, task_id, failures)
        if backlog_record is not None:
            title = normalize_text(backlog_record.get("title"))

    if backlog_md_path.exists():
        check_backlog_markdown(backlog_md_path, task_id, title, failures)

    if daily_review_path.exists():
        check_daily_review(daily_review_path, task_id, failures)

    worker_path = workspace / "results" / f"{task_id}_worker_result.json"
    qa_path = workspace / "qa" / f"{task_id}_qa_result.json"

    check_worker_result(worker_path, task_id, failures)
    check_qa_result(qa_path, task_id, failures)

    if failures:
        print("POST-RECONCILE VALIDATION: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    status = ""
    if backlog_record is not None:
        status = normalize_text(backlog_record.get("status"))

    print("POST-RECONCILE VALIDATION: PASS")
    print(f"Task: {task_id}")
    if title:
        print(f"Title: {title}")
    if status:
        print(f"Backlog status: {status}")
    print("Passed checks:")
    print("- backlog JSON contains one WCS backlog entry for this task with status done")
    print("- MASTER_BACKLOG.md shows the task id, title, and a done indicator")
    print("- DAILY_REVIEW.md includes the task id")
    print("- worker result exists with matching task_id, allowed status, and non-blank completed_at")
    print("- QA result exists with matching task_id, allowed status, and non-blank completed_at")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())



## FILE: scripts/worker_change_check.py
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple


class WorkerChangeError(Exception):
    pass


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
        raise WorkerChangeError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise WorkerChangeError(f"Invalid JSON in {path}: {exc}") from exc


def run_git(repo_path: Path, args: List[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only worker change boundary check for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    task_id = normalize_text(raw).upper()
    if not task_id.startswith("WCS-"):
        raise WorkerChangeError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise WorkerChangeError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def determine_expected_files(task_json_path: Path, failures: List[str]) -> Set[str]:
    try:
        data = read_json(task_json_path)
    except WorkerChangeError as exc:
        failures.append(str(exc))
        return set()

    if not isinstance(data, dict):
        failures.append(f"Task packet must be a JSON object: {task_json_path}")
        return set()

    expected: Set[str] = set()

    target_files = data.get("target_files")
    if isinstance(target_files, list):
        for item in target_files:
            path = normalize_text(item)
            if path:
                expected.add(path.replace("\\", "/"))

    if not expected:
        for key in ("target_file", "file_path", "file"):
            value = normalize_text(data.get(key))
            if value:
                expected.add(value.replace("\\", "/"))
                break

    if not expected:
        notes = normalize_text(data.get("notes"))
        if notes and ("\\" in notes or "/" in notes) and " " not in notes:
            expected.add(notes.replace("\\", "/"))

    if not expected:
        failures.append(
            f"Unable to determine expected file scope from task packet: {task_json_path}"
        )

    return expected


def resolve_repo_path(workspace: Path, failures: List[str]) -> Path | None:
    project_status_path = workspace / "state" / "project_status_wcs.json"
    try:
        data = read_json(project_status_path)
    except WorkerChangeError as exc:
        failures.append(str(exc))
        return None

    if not isinstance(data, dict):
        failures.append(f"project_status_wcs.json must be a JSON object: {project_status_path}")
        return None

    raw = normalize_text(data.get("repo_path"))
    if not raw:
        failures.append("project_status_wcs.json is missing repo_path.")
        return None

    repo_path = Path(raw).resolve()
    if not repo_path.exists():
        failures.append(f"Repo path does not exist: {repo_path}")
        return None

    return repo_path


def gather_changed_files(repo_path: Path, failures: List[str]) -> Set[str]:
    changed: Set[str] = set()

    status_result = run_git(repo_path, ["status", "--short"])
    if status_result.returncode != 0:
        failures.append(
            f"git status --short failed in {repo_path}: "
            f"{status_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        for line in status_result.stdout.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            parts = stripped.split(maxsplit=1)
            if len(parts) == 2:
                changed.add(parts[1].replace("\\", "/"))

    diff_result = run_git(repo_path, ["diff", "--name-only"])
    if diff_result.returncode != 0:
        failures.append(
            f"git diff --name-only failed in {repo_path}: "
            f"{diff_result.stderr.strip() or '(no stderr output)'}"
        )
    else:
        for line in diff_result.stdout.splitlines():
            path = normalize_text(line)
            if path:
                changed.add(path.replace("\\", "/"))

    return changed


def check_branch(repo_path: Path, task_id: str, failures: List[str]) -> Tuple[str, str | None]:
    expected_branch = f"jarvis-task-{task_id.lower()}"

    branch_result = run_git(repo_path, ["branch", "--show-current"])
    if branch_result.returncode != 0:
        failures.append(
            f"git branch --show-current failed in {repo_path}: "
            f"{branch_result.stderr.strip() or '(no stderr output)'}"
        )
        return expected_branch, None

    current_branch = normalize_text(branch_result.stdout)
    if not current_branch:
        failures.append(f"Current branch is empty in repo {repo_path}.")
    elif current_branch != expected_branch:
        failures.append(
            f"Current branch mismatch. Expected {expected_branch}, found {current_branch}."
        )

    return expected_branch, current_branch


def check_diff_sanity(repo_path: Path, changed_files: Set[str], failures: List[str]) -> None:
    if len(changed_files) > 3:
        failures.append(
            f"Too many changed files for a bounded task. Expected at most 3, found {len(changed_files)}."
        )

    for path in sorted(changed_files):
        diff_result = run_git(repo_path, ["diff", "--unified=0", "--", path])
        if diff_result.returncode != 0:
            failures.append(
                f"git diff --unified=0 failed for {path} in {repo_path}: "
                f"{diff_result.stderr.strip() or '(no stderr output)'}"
            )
            continue

        total_changes = 0
        for line in diff_result.stdout.splitlines():
            if not line:
                continue
            if line.startswith("@@"):
                continue
            if line.startswith("+++ ") or line.startswith("--- "):
                continue
            if line[0] in {"+", "-"}:
                total_changes += 1

        if total_changes > 40:
            failures.append(
                f"File {path} has too many changed lines for a bounded task. "
                f"Found {total_changes}, limit is 40."
            )


def main() -> int:
    args = parse_args()

    if not args.task:
        print("WORKER CHANGE CHECK: FAIL")
        print("Task: (missing)")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except WorkerChangeError as exc:
        print("WORKER CHANGE CHECK: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: List[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    task_json_path = workspace / "tasks" / f"{task_id}_task.json"
    expected_files = determine_expected_files(task_json_path, failures)

    repo_path = resolve_repo_path(workspace, failures)
    expected_branch = ""
    current_branch: str | None = None

    changed_files: Set[str] = set()
    if repo_path is not None:
        expected_branch, current_branch = check_branch(repo_path, task_id, failures)
        changed_files = gather_changed_files(repo_path, failures)

        if not changed_files:
            failures.append("No changed files detected in the WCS repo for this task.")

        if expected_files:
            for path in sorted(changed_files):
                if path not in expected_files:
                    failures.append(
                        f"Changed file {path} is outside the expected task scope: {sorted(expected_files)}."
                    )

        if changed_files:
            check_diff_sanity(repo_path, changed_files, failures)

    if failures:
        print("WORKER CHANGE CHECK: FAIL")
        print(f"Task: {task_id}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    print("WORKER CHANGE CHECK: PASS")
    print(f"Task: {task_id}")
    if repo_path is not None and expected_branch and current_branch:
        print(f"Repo path: {repo_path}")
        print(f"Expected branch: {expected_branch}")
        print(f"Current branch: {current_branch}")
    if expected_files:
        print(f"Expected file scope: {', '.join(sorted(expected_files))}")
    print(f"Actual changed files: {', '.join(sorted(changed_files))}")
    print("Passed checks:")
    print("- repo path and current branch resolved correctly")
    print("- changed files exist and are within expected task scope")
    print("- number of changed files is within the allowed limit")
    print("- per-file diff size is within the allowed limit")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())



## FILE: scripts/worker_result_validate.py
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, List, Set


ALLOWED_WORKER_STATUSES = {"worker_complete", "blocked", "escalated"}


class WorkerResultError(Exception):
    pass


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
        raise WorkerResultError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise WorkerResultError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only worker result schema validator for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    parser.add_argument(
        "--mode",
        choices=["pre-stamp", "post-stamp"],
        default="pre-stamp",
        help="Validation mode for completed_at (default: pre-stamp).",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    task_id = normalize_text(raw).upper()
    if not task_id.startswith("WCS-"):
        raise WorkerResultError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise WorkerResultError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def determine_expected_files(task_json_path: Path) -> Set[str]:
    expected: Set[str] = set()
    try:
        data = read_json(task_json_path)
    except WorkerResultError:
        return expected

    if not isinstance(data, dict):
        return expected

    target_files = data.get("target_files")
    if isinstance(target_files, list):
        for item in target_files:
            path = normalize_text(item)
            if path:
                expected.add(path.replace("\\", "/"))

    if not expected:
        for key in ("target_file", "file_path", "file"):
            value = normalize_text(data.get(key))
            if value:
                expected.add(value.replace("\\", "/"))
                break

    if not expected:
        notes = normalize_text(data.get("notes"))
        if notes and ("\\" in notes or "/" in notes) and " " not in notes:
            expected.add(notes.replace("\\", "/"))

    return expected


def check_worker_result(
    worker_path: Path,
    task_id: str,
    mode: str,
    expected_files: Set[str],
    failures: List[str],
) -> None:
    try:
        data = read_json(worker_path)
    except WorkerResultError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"Worker result must be a JSON object: {worker_path}")
        return

    # Required fields
    required_fields = [
        "task_id",
        "status",
        "executor",
        "summary",
        "files_changed",
        "commands_run",
        "issues_encountered",
        "notes",
        "completed_at",
    ]
    for field in required_fields:
        if field not in data:
            failures.append(f"Worker result missing required field: {field}")

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"Worker result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("Worker result status must not be 'draft'.")
    if status not in ALLOWED_WORKER_STATUSES:
        failures.append(
            f"Worker result status must be one of {sorted(ALLOWED_WORKER_STATUSES)}. Found: {status or '(blank)'}."
        )

    executor = normalize_text(data.get("executor"))
    if not executor:
        failures.append("Worker result executor must be present and non-blank.")

    summary = normalize_text(data.get("summary"))
    if not summary:
        failures.append("Worker result summary must be present and non-blank.")

    files_changed = data.get("files_changed")
    if not isinstance(files_changed, list):
        failures.append("Worker result files_changed must be a list.")
        files_changed_list: List[str] = []
    else:
        files_changed_list = [normalize_text(x) for x in files_changed]

    commands_run = data.get("commands_run")
    if not isinstance(commands_run, list):
        failures.append("Worker result commands_run must be a list.")

    issues_encountered = data.get("issues_encountered")
    if not isinstance(issues_encountered, list):
        failures.append("Worker result issues_encountered must be a list.")

    # notes field must exist (already checked) but may be blank or non-blank; no extra content rule

    if status == "worker_complete":
        if not files_changed_list:
            failures.append(
                "Worker result files_changed must contain at least one entry when status is worker_complete."
            )

    for entry in files_changed_list:
        if not entry:
            failures.append("Worker result files_changed contains a blank entry.")

    # Simple task-scope consistency if expected scope is known
    if expected_files:
        for entry in files_changed_list:
            normalized_entry = entry.replace("\\", "/")
            if normalized_entry and normalized_entry not in expected_files:
                failures.append(
                    f"Worker result files_changed entry {normalized_entry} is outside expected task scope: {sorted(expected_files)}."
                )

    completed_at_raw = normalize_text(data.get("completed_at"))
    if mode == "pre-stamp":
        if completed_at_raw:
            failures.append("In pre-stamp mode, worker result completed_at must be blank.")
    else:  # post-stamp
        if not completed_at_raw:
            failures.append("In post-stamp mode, worker result completed_at must be non-blank.")


def main() -> int:
    args = parse_args()

    if not args.task:
        print("WORKER RESULT VALIDATION: FAIL")
        print("Task: (missing)")
        print(f"Mode: {args.mode}")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except WorkerResultError as exc:
        print("WORKER RESULT VALIDATION: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print(f"Mode: {args.mode}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: List[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    worker_path = workspace / "results" / f"{task_id}_worker_result.json"
    task_json_path = workspace / "tasks" / f"{task_id}_task.json"

    if not worker_path.exists():
        failures.append(f"Missing worker result JSON: {worker_path}")

    expected_files = determine_expected_files(task_json_path)

    if worker_path.exists():
        check_worker_result(worker_path, task_id, args.mode, expected_files, failures)

    if failures:
        print("WORKER RESULT VALIDATION: FAIL")
        print(f"Task: {task_id}")
        print(f"Mode: {args.mode}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    # Best-effort display of key fields on pass
    data = read_json(worker_path)
    executor = normalize_text(data.get("executor"))
    status = normalize_text(data.get("status"))
    files_changed = data.get("files_changed") or []
    files_changed_display = [normalize_text(x) for x in files_changed if normalize_text(x)]

    print("WORKER RESULT VALIDATION: PASS")
    print(f"Task: {task_id}")
    print(f"Mode: {args.mode}")
    print(f"Executor: {executor}")
    print(f"Status: {status}")
    print(f"Files changed: {', '.join(files_changed_display) if files_changed_display else '(none)'}")
    print("Passed checks:")
    print("- worker result JSON exists and parses")
    print("- required worker result fields are present")
    print("- executor and summary are non-blank")
    print("- list fields (files_changed, commands_run, issues_encountered) have the correct types")
    print("- files_changed is non-empty for worker_complete (if applicable)")
    print("- completed_at matches the expected mode (pre-stamp or post-stamp)")
    if expected_files:
        print("- files_changed entries are within expected task scope")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())



## FILE: scripts/qa_result_validate.py
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, List


ALLOWED_QA_STATUSES = {"qa_pass", "qa_fail", "escalated"}


class QaResultError(Exception):
    pass


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
        raise QaResultError(f"Missing JSON file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise QaResultError(f"Invalid JSON in {path}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only QA result schema validator for a WCS task."
    )
    parser.add_argument(
        "--task",
        help="Task id like WCS-016 (required).",
    )
    parser.add_argument(
        "--workspace",
        help="Workspace path (defaults to jarvis-workspace root from script location).",
    )
    parser.add_argument(
        "--mode",
        choices=["pre-stamp", "post-stamp"],
        default="pre-stamp",
        help="Validation mode for completed_at (default: pre-stamp).",
    )
    return parser.parse_args()


def validate_task_id(raw: str) -> str:
    task_id = normalize_text(raw).upper()
    if not task_id.startswith("WCS-"):
        raise QaResultError(f"Invalid task id (expected WCS-XXX): {task_id}")
    suffix = task_id.split("-", 1)[1]
    if not suffix.isdigit():
        raise QaResultError(f"Invalid task id suffix (expected numeric): {task_id}")
    return task_id


def check_qa_result(
    qa_path: Path,
    task_id: str,
    mode: str,
    failures: List[str],
) -> None:
    try:
        data = read_json(qa_path)
    except QaResultError as exc:
        failures.append(str(exc))
        return

    if not isinstance(data, dict):
        failures.append(f"QA result must be a JSON object: {qa_path}")
        return

    required_fields = [
        "task_id",
        "status",
        "qa_tool",
        "summary",
        "checks_run",
        "checks_passed",
        "checks_failed",
        "artifacts",
        "notes",
        "completed_at",
    ]
    for field in required_fields:
        if field not in data:
            failures.append(f"QA result missing required field: {field}")

    actual_id = normalize_text(data.get("task_id")).upper()
    if actual_id != task_id:
        failures.append(
            f"QA result task_id mismatch. Expected {task_id}, found {actual_id or '(blank)'}."
        )

    status = normalize_text(data.get("status")).lower()
    if status == "draft":
        failures.append("QA result status must not be 'draft'.")
    if status not in ALLOWED_QA_STATUSES:
        failures.append(
            f"QA result status must be one of {sorted(ALLOWED_QA_STATUSES)}. Found: {status or '(blank)'}."
        )

    qa_tool = normalize_text(data.get("qa_tool"))
    if not qa_tool:
        failures.append("QA result qa_tool must be present and non-blank.")

    summary = normalize_text(data.get("summary"))
    if not summary:
        failures.append("QA result summary must be present and non-blank.")

    checks_run = data.get("checks_run")
    checks_passed = data.get("checks_passed")
    checks_failed = data.get("checks_failed")
    artifacts = data.get("artifacts")

    if not isinstance(checks_run, list):
        failures.append("QA result checks_run must be a list.")
        checks_run_list: List[str] = []
    else:
        checks_run_list = [normalize_text(x) for x in checks_run]

    if not isinstance(checks_passed, list):
        failures.append("QA result checks_passed must be a list.")
        checks_passed_list: List[str] = []
    else:
        checks_passed_list = [normalize_text(x) for x in checks_passed]

    if not isinstance(checks_failed, list):
        failures.append("QA result checks_failed must be a list.")
        checks_failed_list: List[str] = []
    else:
        checks_failed_list = [normalize_text(x) for x in checks_failed]

    if not isinstance(artifacts, list):
        failures.append("QA result artifacts must be a list.")
        artifacts_list: List[str] = []
    else:
        artifacts_list = [normalize_text(x) for x in artifacts]

    # notes must exist (checked above) but can be blank or non-blank; no extra content rule

    if status in {"qa_pass", "qa_fail"} and not checks_run_list:
        failures.append(
            "QA result checks_run must contain at least one entry when status is qa_pass or qa_fail."
        )

    for arr_name, arr in [
        ("checks_run", checks_run_list),
        ("checks_passed", checks_passed_list),
        ("checks_failed", checks_failed_list),
        ("artifacts", artifacts_list),
    ]:
        for entry in arr:
            if not isinstance(entry, str):
                failures.append(f"QA result {arr_name} contains a non-string entry.")
            elif not entry:
                failures.append(f"QA result {arr_name} contains a blank entry.")

    # Simple internal consistency
    if status == "qa_pass":
        if checks_failed_list:
            failures.append("QA result checks_failed must be empty when status is qa_pass.")
        if not checks_passed_list:
            failures.append("QA result checks_passed must contain at least one entry when status is qa_pass.")
    elif status == "qa_fail":
        if not checks_failed_list:
            failures.append("QA result checks_failed must contain at least one entry when status is qa_fail.")
    # status == escalated: no extra requirements for checks_passed / checks_failed beyond type and content shape

    completed_at_raw = normalize_text(data.get("completed_at"))
    if mode == "pre-stamp":
        if completed_at_raw:
            failures.append("In pre-stamp mode, QA result completed_at must be blank.")
    else:  # post-stamp
        if not completed_at_raw:
            failures.append("In post-stamp mode, QA result completed_at must be non-blank.")


def main() -> int:
    args = parse_args()

    if not args.task:
        print("QA RESULT VALIDATION: FAIL")
        print("Task: (missing)")
        print(f"Mode: {args.mode}")
        print("Failures:")
        print("- --task WCS-XXX is required.")
        return 1

    try:
        task_id = validate_task_id(args.task)
    except QaResultError as exc:
        print("QA RESULT VALIDATION: FAIL")
        print(f"Task: {normalize_text(args.task).upper()}")
        print(f"Mode: {args.mode}")
        print("Failures:")
        print(f"- {exc}")
        return 1

    if args.workspace:
        workspace = Path(args.workspace).resolve()
    else:
        script_path = Path(__file__).resolve()
        workspace = script_path.parent.parent

    failures: List[str] = []

    if not workspace.exists():
        failures.append(f"Workspace path does not exist: {workspace}")

    qa_path = workspace / "qa" / f"{task_id}_qa_result.json"

    if not qa_path.exists():
        failures.append(f"Missing QA result JSON: {qa_path}")

    if qa_path.exists():
        check_qa_result(qa_path, task_id, args.mode, failures)

    if failures:
        print("QA RESULT VALIDATION: FAIL")
        print(f"Task: {task_id}")
        print(f"Mode: {args.mode}")
        print("Failures:")
        for msg in failures:
            print(f"- {msg}")
        return 1

    data = read_json(qa_path)
    qa_tool = normalize_text(data.get("qa_tool"))
    status = normalize_text(data.get("status"))
    checks_run = data.get("checks_run") or []
    checks_run_display = [normalize_text(x) for x in checks_run if normalize_text(x)]

    print("QA RESULT VALIDATION: PASS")
    print(f"Task: {task_id}")
    print(f"Mode: {args.mode}")
    print(f"QA tool: {qa_tool}")
    print(f"Status: {status}")
    print(f"Checks run: {', '.join(checks_run_display) if checks_run_display else '(none)'}")
    print("Passed checks:")
    print("- QA result JSON exists and parses")
    print("- required QA result fields are present")
    print("- qa_tool and summary are non-blank")
    print("- list fields (checks_run, checks_passed, checks_failed, artifacts) have the correct types")
    print("- checks_run is non-empty for qa_pass/qa_fail (if applicable)")
    print("- internal consistency between status, checks_passed, and checks_failed")
    print("- completed_at matches the expected mode (pre-stamp or post-stamp)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

