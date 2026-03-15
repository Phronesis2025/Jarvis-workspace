# PATHFINDER DORMANT CONTRACT PACK BUNDLE

- Generated: 2026-03-14T19:20:00-05:00
- Purpose: Create the dormant Pathfinder future-module contract pack in one separate section of the Jarvis codebase.
- Status: Planning only. Do not activate Pathfinder, wire routing, or change the current WCS/Jarvis execution loop.
- Recommended target root: `future_modules/pathfinder/`
- Why this location: keeps Pathfinder real, reviewable, and ready for later work without polluting the active phase-1 runtime.

## Operator instructions

Use this bundle to create the files exactly as written under `future_modules/pathfinder/`.

Guardrails:
- create the files only
- do not modify active runtime scripts
- do not hook Pathfinder into Jarvis yet
- do not update active routing, scheduling, or worker dispatch
- do not mark Pathfinder as active anywhere
- keep all docs timestamped

---

## 1. File: `future_modules/pathfinder/README.md`

**Purpose:** Folder-level overview for the dormant Pathfinder module pack.

```md
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
```

---

## 2. File: `future_modules/pathfinder/PATHFINDER_SPEC.md`

**Purpose:** Core worker definition for Pathfinder.

```md
# PATHFINDER SPEC

**Status:** recognized, inactive  
**Last updated:** 2026-03-14

## 1. Purpose

Pathfinder is the planned Jarvis discovery/research worker.

Its role is to investigate:
- errors
- unclear implementation behavior
- repo/file context
- official documentation
- implementation options
- likely root causes
- recommended next steps

It does this **without editing production code**.

## 2. Why Pathfinder exists

The point of Pathfinder is to reduce wasted implementation passes.

Instead of sending a coding worker or operator into a task half-blind, Pathfinder should first produce a bounded, evidence-backed readout of:
- what appears broken or unclear
- what artifacts matter
- what likely paths forward exist
- what should be tried next

## 3. Allowed task types

Pathfinder may accept tasks such as:
- investigate a recurring build or smoke failure
- inspect repo structure for a targeted area
- compare two implementation approaches
- gather official docs relevant to a bounded issue
- summarize likely causes from existing evidence
- prepare a decision brief before coding begins

## 4. Not allowed

Pathfinder may not:
- edit production code
- create or modify runtime scripts outside its own dormant folder
- install dependencies
- migrate data
- mark work complete on behalf of implementation or QA
- broaden a bounded task into general exploration
- present guesses as proven facts

## 5. Inputs required

Every Pathfinder task should provide, at minimum:
- task id
- project
- worker
- title
- problem summary
- goal
- scope
- repo path if relevant
- suspected files or known artifacts
- research questions
- acceptance criteria
- QA method / review method
- risk
- system impact
- stop conditions

## 6. Required outputs

A Pathfinder run should return structured JSON that includes:
- task id
- status
- executor
- concise summary
- findings with evidence
- artifacts reviewed
- external sources reviewed if any
- recommended next actions
- open questions
- files changed (must remain empty for Pathfinder)
- commands run
- issues encountered
- notes
- completed_at

## 7. Success definition

A Pathfinder task is successful only when it produces:
- a bounded summary
- evidence-backed findings
- actionable next steps
- no code edits
- no fabricated certainty
- output that can be reviewed by a human or later validator

## 8. Immediate escalation conditions

Pathfinder should escalate immediately if:
- required artifacts are missing
- scope expands beyond the packet
- source quality is too weak to support a conclusion
- conflicting evidence blocks a safe recommendation
- the task would require code changes to proceed
- the task clearly belongs to implementation or QA instead

## 9. Non-goals

Pathfinder is not intended to:
- replace implementation work
- replace QA work
- perform autonomous long-range research
- become a generic assistant bucket for vague asks
- serve as a backdoor for unsafe or unbounded repo roaming
```

---

## 3. File: `future_modules/pathfinder/PATHFINDER_BOUNDARIES.md`

**Purpose:** Hard scope controls so Pathfinder does not drift into garbage.

```md
# PATHFINDER BOUNDARIES

**Status:** recognized, inactive  
**Last updated:** 2026-03-14

## 1. Allowed actions

Pathfinder may:
- read project docs
- inspect bounded repo paths
- inspect existing task/worker/QA artifacts
- review official external docs when explicitly relevant
- compare implementation options
- summarize likely causes
- recommend next steps
- recommend escalation when evidence is insufficient

## 2. Forbidden actions

Pathfinder may not:
- edit production code
- edit active Jarvis runtime files
- rewrite backlog items directly
- stamp results as done outside its own contract
- run destructive commands
- install or remove packages
- create uncontrolled new tasks automatically
- browse broadly without a bounded question set

## 3. Source boundaries

Preferred sources, in order:
1. task packet and known artifacts
2. repo files explicitly in scope
3. official project docs / source-of-truth docs
4. official vendor/framework documentation
5. other supporting sources only when clearly necessary

Pathfinder should avoid weak or noisy sources when stronger evidence exists.

## 4. Output boundaries

Pathfinder output must:
- stay inside the stated problem and goal
- distinguish evidence from inference
- distinguish fact from recommendation
- include concrete next actions, not vague advice
- leave `files_changed` empty

## 5. Scope discipline rules

Pathfinder should stop and escalate instead of continuing when:
- the task needs code edits
- the task needs repo-wide analysis beyond the packet
- the evidence points to multiple unrelated problem domains
- the likely fix touches auth, payments, data, deployment, or shared infra without explicit approval

## 6. Truthfulness rule

Pathfinder must not:
- invent missing evidence
- imply certainty that the evidence does not support
- claim a fix was verified
- claim a root cause was proven if it was only inferred

## 7. Relationship to other workers

Pathfinder comes before implementation when discovery is needed.

Pathfinder does not replace:
- the WCS worker
- Playwright QA
- future crawl-audit work
- future voice/interface work
```

---

## 4. File: `future_modules/pathfinder/PATHFINDER_ACTIVATION_RULES.md`

**Purpose:** Explicit inactive-state and later activation gates.

```md
# PATHFINDER ACTIVATION RULES

**Status:** recognized, inactive  
**Last updated:** 2026-03-14

## 1. Current state

Pathfinder is currently **inactive**.

This folder is preparation work only.

## 2. Why inactive is correct

Pathfinder should not be activated until the current boring Jarvis proof loop is trustworthy.

That means Pathfinder must not be used to compensate for:
- unstable task packets
- unstable worker-result capture
- unstable QA flow
- unstable reconcile behavior
- incomplete phase-1 hardening

## 3. Activation gate

Pathfinder may be considered for activation only after the following are true:
- Jarvis + WCS loop runs reliably end to end
- task packet contract is stable enough to reuse
- worker result capture is stable
- QA/reconcile/escalation flow is stable
- multiple real WCS tasks have completed or escalated through the full loop
- operator trust is increasing, not decreasing

## 4. First activation shape

When Pathfinder is first activated later, it should start with:
- one bounded task at a time
- read-only behavior only
- explicit packet input
- explicit result JSON output
- manual QA/review
- no scheduling by default
- no autonomous task chaining

## 5. First allowed task categories

Initial live Pathfinder tasks should be limited to:
- bug/issue investigation
- docs/context gathering for a bounded issue
- option comparison before implementation
- repo/context scouting for a known error

## 6. First prohibited categories

Do not activate Pathfinder first for:
- broad trend research
- automatic backlog generation
- autonomous multi-project scouting
- code-change recommendations without evidence
- anything that smells like “figure out whatever seems useful”

## 7. Runtime guardrails for first live use

Suggested first-pass guardrails:
- max one active Pathfinder task at a time
- max one repo/project scope per task
- explicit stop conditions in the packet
- manual review before any recommendation is acted on

## 8. Activation check question

Before Pathfinder becomes live, the operator should be able to answer yes to this:

> Do we trust the current Jarvis loop enough that adding a read-only research worker will increase clarity instead of creating more noise?

If the answer is no, Pathfinder stays dormant.
```

---

## 5. File: `future_modules/pathfinder/PATHFINDER_QA_RULES.md`

**Purpose:** Validation and review rules for Pathfinder outputs.

```md
# PATHFINDER QA RULES

**Status:** recognized, inactive  
**Last updated:** 2026-03-14

## 1. QA purpose

Pathfinder QA exists to verify that a Pathfinder result is:
- bounded
- evidence-backed
- structurally valid
- honest about uncertainty
- free of code edits
- useful enough to guide the next step

## 2. Minimum review checks

A Pathfinder result should be reviewed for:
- packet/result task id match
- allowed status value
- non-blank summary
- findings present when status is complete
- evidence attached to each major finding
- recommendations clearly tied to findings
- open questions separated from findings
- `files_changed` remains empty
- no forbidden actions occurred

## 3. Required QA questions

### Contract check
- Did the result follow the expected JSON structure?
- Are required list fields lists?
- Is the summary concise and non-blank?

### Evidence check
- Does each major claim point to evidence?
- Are quoted or referenced artifacts real and in scope?
- Are unsupported guesses clearly labeled as inference or open questions?

### Boundary check
- Did Pathfinder stay read-only?
- Did it stay within the stated scope?
- Did it avoid broad wandering or fake certainty?

### Usefulness check
- Are the recommended next actions concrete?
- Would an operator or worker know what to do next?
- Did the result reduce uncertainty instead of adding noise?

## 4. Suggested result status rules

Use:
- `worker_complete` when the bounded research task was completed with usable evidence
- `blocked` when the task could not proceed because required artifacts or access were missing
- `escalated` when the situation requires operator review, broader scope, or a different worker path

## 5. Hard QA fail conditions

A Pathfinder result should fail review if:
- it claims certainty without evidence
- it contains code edits
- it leaves `files_changed` non-empty
- it recommends broad implementation work without bounded reasoning
- it fabricates sources or artifacts
- it clearly violated packet boundaries

## 6. Example acceptance bar

A passing Pathfinder result should let a reviewer say:
- I can see what was reviewed
- I can see why the findings were made
- I can see what should happen next
- I can see that no code was changed

## 7. Escalation from QA

QA should recommend escalation when:
- the result is structurally valid but too weak to act on safely
- multiple possible root causes remain unresolved
- source quality is too weak
- the issue belongs to implementation or QA rather than research
```

---

## 6. File: `future_modules/pathfinder/templates/pathfinder_task_packet.template.json`

**Purpose:** Draft input packet contract for future Pathfinder tasks.

```json
{
  "task_id": "PF-001",
  "project": "WCS",
  "worker": "pathfinder",
  "title": "Investigate a bounded issue before implementation",
  "problem_summary": "Describe the issue or unknown clearly and narrowly.",
  "goal": "Produce an evidence-backed research summary with concrete next steps and no code edits.",
  "scope": "Bounded repo/doc investigation only for the named issue.",
  "repo_path": "",
  "branch_name": "",
  "suspected_files": [],
  "known_artifacts": [],
  "research_questions": [],
  "allowed_sources": [
    "task_artifacts",
    "repo_files",
    "project_docs",
    "official_external_docs"
  ],
  "acceptance_criteria": [
    "Findings are evidence-backed",
    "Recommended next actions are concrete",
    "No production code is edited",
    "Scope remains bounded to the packet"
  ],
  "qa_method": "Manual review against evidence, structure, and scope compliance",
  "qa_plan": [
    "Validate result JSON structure",
    "Check that major findings cite evidence",
    "Confirm files_changed is empty",
    "Confirm recommendations stay bounded"
  ],
  "risk": "low",
  "system_impact": "Read-only research task; no production code edits allowed.",
  "stop_conditions": [
    "Required artifacts are missing",
    "Scope expands beyond the packet",
    "Task would require code edits to proceed",
    "Evidence quality is too weak for a safe recommendation"
  ],
  "must_not_do": [
    "Do not edit code",
    "Do not install dependencies",
    "Do not broaden scope",
    "Do not claim certainty without evidence"
  ],
  "status": "ready",
  "created_at": "",
  "updated_at": ""
}
```

---

## 7. File: `future_modules/pathfinder/templates/pathfinder_result.template.json`

**Purpose:** Draft structured result contract for future Pathfinder runs.

```json
{
  "task_id": "PF-001",
  "status": "worker_complete",
  "executor": "pathfinder",
  "summary": "Concise evidence-backed summary of what Pathfinder found.",
  "findings": [
    {
      "id": "F1",
      "claim": "State the finding clearly.",
      "evidence": [
        "Artifact, file path, doc section, or source used to support the finding."
      ],
      "confidence": "medium"
    }
  ],
  "artifacts_reviewed": [],
  "external_sources_reviewed": [],
  "recommended_next_actions": [],
  "open_questions": [],
  "files_changed": [],
  "commands_run": [],
  "issues_encountered": [],
  "notes": "Use notes for review guidance, caveats, or escalation context.",
  "completed_at": ""
}
```

---

## 8. File: `future_modules/pathfinder/templates/pathfinder_escalation_record.template.json`

**Purpose:** Draft escalation record shape for Pathfinder-specific failures or handoffs.

```json
{
  "task_id": "PF-001",
  "worker": "pathfinder",
  "status": "escalated",
  "reason": "State clearly why Pathfinder could not proceed safely or why operator review is required.",
  "evidence": [],
  "recommended_next_action": "",
  "pause_recommended": false,
  "notes": "",
  "created_at": "",
  "updated_at": ""
}
```

---

## 9. File: `future_modules/pathfinder/examples/pathfinder_task_packet.example.json`

**Purpose:** Concrete example of a future Pathfinder packet shaped to the current Jarvis style.

```json
{
  "task_id": "PF-001",
  "project": "WCS",
  "worker": "pathfinder",
  "title": "Investigate recurring local WCS smoke readiness failure before implementation",
  "problem_summary": "The local WCS smoke flow intermittently fails because the app does not appear ready in time for verification. We need a bounded research pass before changing code or scripts.",
  "goal": "Review the existing artifacts and likely touchpoints, identify the most likely causes, and recommend the next safest implementation or QA step without editing code.",
  "scope": "Read-only investigation of the existing WCS smoke/verification path and directly related task artifacts.",
  "repo_path": "C:\\dev\\wcsv2.0-new",
  "branch_name": "jarvis-task-wcs-043",
  "suspected_files": [
    "package.json",
    "playwright.config.ts",
    "tests/e2e/smoke.spec.ts"
  ],
  "known_artifacts": [
    "tasks/WCS-043_task.json",
    "results/WCS-043_worker_result.json",
    "qa/WCS-043_qa_result.json",
    "scratch/task_cycle_summaries/WCS-043_task_cycle_summary.md"
  ],
  "research_questions": [
    "What artifact or config path most likely controls local smoke readiness?",
    "Does the current evidence point to app startup timing, Playwright setup timing, or a broader environment issue?",
    "What is the next smallest safe change or test to run?"
  ],
  "allowed_sources": [
    "task_artifacts",
    "repo_files",
    "project_docs",
    "official_external_docs"
  ],
  "acceptance_criteria": [
    "Findings are tied to actual artifacts or files",
    "Recommendations are concrete and bounded",
    "No production code is edited",
    "Output clearly distinguishes evidence from inference"
  ],
  "qa_method": "Manual review against evidence, structure, and scope compliance",
  "qa_plan": [
    "Review findings against named artifacts",
    "Check that files_changed remains empty",
    "Confirm recommendations are bounded and actionable"
  ],
  "risk": "low",
  "system_impact": "Read-only research task; no production code edits allowed.",
  "stop_conditions": [
    "Required artifacts are missing",
    "Scope expands beyond local smoke readiness investigation",
    "The task would require code edits to continue",
    "Evidence quality is too weak for a safe recommendation"
  ],
  "must_not_do": [
    "Do not edit code",
    "Do not install dependencies",
    "Do not broaden scope",
    "Do not claim the issue is proven if it is only inferred"
  ],
  "status": "ready",
  "created_at": "2026-03-14T19:20:00-05:00",
  "updated_at": "2026-03-14T19:20:00-05:00"
}
```

---

## 10. File: `future_modules/pathfinder/examples/pathfinder_result.example.json`

**Purpose:** Example of a good Pathfinder result.

```json
{
  "task_id": "PF-001",
  "status": "worker_complete",
  "executor": "pathfinder",
  "summary": "The evidence most strongly suggests that local smoke readiness issues are caused by timing and environment coordination around app startup rather than a proven regression in the target page itself.",
  "findings": [
    {
      "id": "F1",
      "claim": "The current issue looks more like readiness timing than a proven page-level regression.",
      "evidence": [
        "qa/WCS-043_qa_result.json shows build, smoke, and manual verification can pass when the environment is aligned.",
        "scratch/task_cycle_summaries/WCS-043_task_cycle_summary.md shows the completed proof loop for the same area."
      ],
      "confidence": "medium"
    },
    {
      "id": "F2",
      "claim": "The most likely next useful review surface is the local app startup and smoke harness boundary, not the feature page component itself.",
      "evidence": [
        "The bounded task artifacts point to QA/readiness handling as the investigation target.",
        "The suspected file list in the packet focuses on smoke/config surfaces rather than only UI feature code."
      ],
      "confidence": "medium"
    }
  ],
  "artifacts_reviewed": [
    "tasks/WCS-043_task.json",
    "results/WCS-043_worker_result.json",
    "qa/WCS-043_qa_result.json",
    "scratch/task_cycle_summaries/WCS-043_task_cycle_summary.md"
  ],
  "external_sources_reviewed": [],
  "recommended_next_actions": [
    "Review the current local smoke startup sequence and readiness assumptions before changing page code.",
    "Check the smoke harness/config path named in the packet before opening a new implementation task.",
    "Only create a follow-up code task after the likely readiness boundary is narrowed further."
  ],
  "open_questions": [
    "Is the startup timing issue intermittent across environments or isolated to one local setup?",
    "Is there a single harness/config entry point already designated as the source of truth for smoke readiness?"
  ],
  "files_changed": [],
  "commands_run": [
    "Reviewed bounded Pathfinder packet and named task artifacts only",
    "Read current task, worker, QA, and cycle summary artifacts for PF-001 research scope"
  ],
  "issues_encountered": [],
  "notes": "Read-only Pathfinder result. Recommendations are bounded and should be reviewed before any implementation task is opened.",
  "completed_at": ""
}
```

---

## 11. File: `future_modules/pathfinder/examples/pathfinder_bad_result.example.json`

**Purpose:** Example of a bad Pathfinder result that should fail QA.

```json
{
  "task_id": "PF-001",
  "status": "worker_complete",
  "executor": "pathfinder",
  "summary": "I figured out the whole problem and the app definitely just needs a bunch of code changes.",
  "findings": [
    {
      "id": "F1",
      "claim": "The root cause is proven.",
      "evidence": [],
      "confidence": "high"
    }
  ],
  "artifacts_reviewed": [],
  "external_sources_reviewed": [],
  "recommended_next_actions": [
    "Rewrite the smoke setup and refactor related code across the repo.",
    "Install anything needed and fix whatever seems wrong."
  ],
  "open_questions": [],
  "files_changed": [
    "playwright.config.ts"
  ],
  "commands_run": [],
  "issues_encountered": [],
  "notes": "No evidence needed because this is obviously the problem.",
  "completed_at": ""
}
```

---

## Cursor execution note

Once this bundle is reviewed, the clean next step is to give Cursor a prompt like this:

```text
Create every file in this bundle exactly as written under `future_modules/pathfinder/`.

Rules:
- create directories as needed
- preserve file names exactly
- preserve file contents exactly
- do not activate Pathfinder
- do not modify active runtime files
- do not update routing, scheduling, or current worker logic
- return the exact files created
```
