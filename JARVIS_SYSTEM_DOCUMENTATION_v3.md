# JARVIS Multi-Agent Development System
## Master Documentation

**Version:** v3.0  
**Date:** March 9, 2026  
**Last updated:** 2026-03-12  
**Status:** Operating documentation for the rebuild; design-era baseline. For **current live hardened loop** (validation gates, stamping, reconcile, post-reconcile validation), see **JARVIS_LIVE_HANDOFF_BUNDLE.md** and **JARVIS_SCRIPT_PROCESS_REFERENCE.md**.  
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
