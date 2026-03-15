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
