# JARVIS Multi-Agent Development System
## System Source of Truth

**Version:** v3.0  
**Date:** March 9, 2026  
**Last updated:** 2026-03-14  
**Last reviewed:** 2026-03-14  
**Status:** Authoritative decisions; design-era baseline. For **current live process and script list** (validators, stamping, reconcile gates), see **JARVIS_LIVE_HANDOFF_BUNDLE.md** and **JARVIS_SCRIPT_PROCESS_REFERENCE.md**.  
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

## 18A. Deferred Future Interface And Audit Options

### 18A.1 LiveKit
LiveKit is the leading future candidate for a Jarvis voice transport / realtime voice interface layer.

If used later, LiveKit is not Jarvis's brain and does not replace Jarvis core planning, orchestration, state, or execution flow.

Preferred layering if voice is activated later:
- speech-to-text
- intent/router layer
- Jarvis command adapter
- Jarvis core
- text-to-speech

Early voice support should stay read-only / low-risk:
- what's next
- summarize status
- read escalations
- read today's plan

Voice remains deferred in the current phase.

### 18A.2 LibreCrawl
LibreCrawl is a future optional crawl-audit companion, not a replacement for Playwright.

If used later, it should stay a bounded supporting audit layer for:
- broken links
- crawl coverage
- metadata issues
- content/asset discovery
- broad regression scanning

LibreCrawl evidence should feed QA/review, not decide task completion by itself. It should not be allowed to create noisy low-value alert spam.

Playwright remains the primary QA path in the current phase.

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
