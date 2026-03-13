# Jarvis Multi-Agent Development System
## Product Requirements Document (PRD)

**Version:** 3.0  
**Date:** March 9, 2026  
**Last updated:** 2026-03-12  
**Status:** Rebuild baseline; design-era. For **current live execution loop and scripts**, see **JARVIS_LIVE_HANDOFF_BUNDLE.md** and **JARVIS_SCRIPT_PROCESS_REFERENCE.md**.  
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
