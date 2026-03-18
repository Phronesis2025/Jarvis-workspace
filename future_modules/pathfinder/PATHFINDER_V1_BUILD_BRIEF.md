# Pathfinder v1 Build Brief

## 1. Purpose

Pathfinder v1 is a read-only Jarvis discovery worker that investigates WCS defects and change requests before implementation. It answers what is actually happening, what artifacts matter, what the likely causes or options are, and what the safest next action is—without editing production code. The goal is to reduce wasted implementation cycles by producing a bounded, evidence-backed research brief that an operator or coding worker can use to decide the next step.

## 2. What v1 is

- Accepts a Pathfinder intake packet (minimal or full task packet) per run
- Performs read-only investigation of task artifacts, repo files in scope, and project docs
- Produces a structured research brief; optionally a draft backlog candidate; or an escalation record when blocked
- Findings must cite evidence; recommendations must be concrete and bounded
- `files_changed` is always empty
- Manual invocation only; no scheduling or unattended execution
- One task at a time; one repo/project per task
- Manual QA/review before any recommendation is acted on

## 3. What v1 is not

- Not a generic research agent or broad trend researcher
- Not a coding worker; does not edit production code, scripts, or dependencies
- Not a QA replacement; does not run tests or mark work complete
- Not autonomous; no task chaining, no automatic backlog generation
- Not scheduled; operator invokes explicitly
- No automatic creation of follow-up task packets or backlog items without operator review
- No broad repo-wide or multi-project scouting

## 4. Primary user flow

1. Operator creates a Pathfinder intake packet (minimal or full task packet) for a bounded WCS defect or change-request investigation.
2. Operator invokes Pathfinder via CLI with the packet path.
3. Pathfinder reads the packet, gathers evidence from allowed sources (workspace-relative paths by default), and synthesizes within scope.
4. Pathfinder produces:
   - **Primary:** A research brief (result JSON) with summary, findings with evidence, recommended next actions, and open questions; or
   - **Optional:** A draft backlog candidate when the brief supports it; or
   - **Fallback:** An escalation record when required artifacts are missing, scope would expand, evidence is too weak, or the task would require code edits.
5. Operator reviews the output manually.
6. Operator decides next step (e.g., accept draft backlog item, open implementation task, gather more info, escalate further).

## 5. Inputs

Pathfinder v1 accepts either a **minimal intake packet** or a **full task packet**.

### Minimal intake packet (primary for v1)

| Field | Required | Description |
|-------|----------|-------------|
| `issue_summary` | yes | Issue or change-request summary; clear, narrow description |
| `page_or_route` | optional | WCS page, route, or area (e.g., `/checkout`, product listing) |
| `evidence_paths` | optional | Paths to task/worker/QA artifacts to review (workspace-relative by default) |
| `suspected_files` | optional | File paths to prioritize (workspace-relative by default) |
| `severity` | optional | e.g., low, medium, high |
| `type` | optional | e.g., defect, change_request |

Paths are **workspace-relative by default**; absolute paths are allowed when provided.

### Full task packet (when available)

A full packet conforming to `pathfinder_task_packet.template.json` may be used when the operator has already created one. All fields from the template apply.

Input artifact: a single JSON file (minimal intake or full task packet).

## 6. Outputs

Pathfinder v1 produces:

| Output type | When | Artifact | Structure |
|-------------|------|----------|-----------|
| **Primary: Research brief** | Investigation completed with usable evidence | `pathfinder_result` JSON | `pathfinder_result.template.json` — summary, findings with evidence, artifacts_reviewed, recommended_next_actions, open_questions, files_changed (empty), commands_run, issues_encountered, notes |
| **Optional: Draft backlog candidate** | When the brief supports a concrete next step | Draft backlog item JSON | Bounded task/backlog candidate shape; operator reviews before acceptance |
| **Fallback: Escalation record** | Required artifacts missing, scope would expand, evidence too weak, or task would require code edits | `pathfinder_escalation_record` JSON | `pathfinder_escalation_record.template.json` — reason, evidence, recommended_next_action, pause_recommended |

Pathfinder v1 does **not**:
- Emit a production code change
- Directly create a final implementation commit
- Create backlog items or task packets without operator review

## 7. Boundaries

- **Read-only:** Pathfinder must not edit any production code, runtime scripts, or dependencies.
- **Bounded scope:** Pathfinder must not expand beyond the packet’s stated scope, research_questions, or allowed_sources.
- **Evidence discipline:** Pathfinder must not invent evidence, imply certainty without support, or claim a root cause is proven when it is only inferred.
- **Empty files_changed:** `files_changed` must always be an empty array.
- **Escalate, don’t guess:** When stop_conditions are met, Pathfinder must produce an escalation record, not a speculative result.
- **No auth/payments/data/deployment:** Pathfinder must not recommend changes to auth, payments, data, deployment, or shared infra without explicit approval (and v1 should avoid these domains entirely).
- **Subordinate to Jarvis:** Pathfinder does not replace WCS, Playwright QA, or any existing worker.

## 8. First proof target

**Scenario:** A visible WCS issue or change request is reported—e.g., checkout button not responding on the payment page, or product listing filters missing on the category page. The operator creates a minimal Pathfinder intake packet with `issue_summary`, `page_or_route` (e.g., `/checkout` or product listing), and optionally `evidence_paths` (e.g., `results/WCS-048_worker_result.json`) and `suspected_files`. Pathfinder runs via CLI, gathers evidence from the named artifacts and files (workspace-relative), and produces a research brief with 1–3 evidence-backed findings and concrete recommended next actions—or an escalation record if it cannot proceed. Optionally, when the brief supports it, Pathfinder emits a draft backlog candidate for operator review. The operator sees a visible, user-facing issue flow from intake to bounded research output.

**Success criterion:** The operator can say: “I can see what was reviewed, why the findings were made, what should happen next, and that no code was changed.”

## 9. Recommended file set for v1

| File | Purpose |
|------|---------|
| `future_modules/pathfinder/README.md` | Overview (existing) |
| `future_modules/pathfinder/PATHFINDER_V1_BUILD_BRIEF.md` | This brief |
| `future_modules/pathfinder/templates/pathfinder_intake.template.json` | Minimal intake contract (new) |
| `future_modules/pathfinder/templates/pathfinder_task_packet.template.json` | Full task packet contract (existing) |
| `future_modules/pathfinder/templates/pathfinder_result.template.json` | Output contract for research brief (existing) |
| `future_modules/pathfinder/templates/pathfinder_escalation_record.template.json` | Output contract for escalation (existing) |
| `future_modules/pathfinder/examples/pathfinder_intake.example.json` | Example minimal intake (new) |
| `future_modules/pathfinder/examples/pathfinder_task_packet.example.json` | Example full packet (existing) |
| `future_modules/pathfinder/examples/pathfinder_result.example.json` | Example good result (existing) |
| `future_modules/pathfinder/examples/pathfinder_bad_result.example.json` | Example bad result (existing) |
| `scripts/pathfinder_run.py` (or equivalent) | CLI entry point: load intake/packet, run investigation, write result, optional draft backlog, or escalation |
| `scripts/pathfinder_result_validate.py` | Validate result JSON against contract and QA rules |

Minimal additions: intake template, intake example, run script, validator. Reuse existing result/escalation templates and examples.

## 10. Implementation defaults (resolved)

| Decision | Default |
|----------|---------|
| **Invocation** | CLI first; operator runs `pathfinder_run` with packet path |
| **Path resolution** | Workspace-relative by default; absolute paths allowed when provided |
| **Investigation core** | Rule-based gathering + bounded synthesis; not free-form autonomous research |

No open questions remain that materially block implementation.
