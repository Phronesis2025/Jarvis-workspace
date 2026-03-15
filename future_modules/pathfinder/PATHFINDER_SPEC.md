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
