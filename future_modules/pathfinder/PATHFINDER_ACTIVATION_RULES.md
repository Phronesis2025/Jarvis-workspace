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
