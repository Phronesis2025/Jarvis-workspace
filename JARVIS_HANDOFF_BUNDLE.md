# JARVIS_HANDOFF_BUNDLE.md

## Purpose

This bundle is the minimum source-of-truth handoff for continuing the current local-first Jarvis rebuild without restarting from theory.

The next chat should:
- treat this bundle as the primary handoff context
- ask clarifying questions first
- request any missing files before proposing the next build step

---

## CONTEXT ANCHOR

We are continuing an existing local-first Jarvis rebuild project. Do not restart from theory. Pick up from the current working state and continue the build.

Project intent:
- Build a local-first multi-agent system.
- Jarvis is a Python foreman/orchestrator, not the main coding agent.
- State uses JSON as source of truth and Markdown as rendered human view.
- WCS website is the first active project.
- Cursor is the current semi-manual coding worker.
- Playwright is the QA layer.
- Parent login area is deferred for now.
- Voice is deferred for later phases.
- n8n worker comes later after WCS foundation is stronger.

Current architecture decisions:
- Phase 1 runtime: simple Python scripts
- State: markdown + JSON sidecars
- WCS task flow:
  backlog -> Jarvis select -> task packet -> correct task branch prep -> Cursor worker -> QA result -> reconcile
- Keep scope tight.
- Prefer boring, durable build steps over flashy architecture.
- Do not derail into broad redesign unless clearly necessary.

What is already working:
- `render_master_backlog.py`
- `generate_task_packet.py`
- `reconcile_task_outcome.py`
- `overnight_health_check.py`
- `run_wcs_scout.py`
- `normalize_scout_to_backlog.py`
- `prepare_wcs_task_branch.py`
- `stamp_result_timestamp.py`
- `jarvis.py` now does:
  - select one valid WCS task
  - write/update daily plan + run log
  - generate task packet
  - prepare/switch the WCS repo to the correct task branch

What has been proven:
- `MASTER_BACKLOG.md` is rendered from `master_backlog.json`
- task packets can be generated automatically
- task outcomes can be reconciled automatically
- overnight health check passes
- Public Scout v1 works
- defect-to-backlog normalizer works and is integrated into the scout loop
- wrong-branch execution risk was reduced by adding task-branch preparation
- live tasks have gone through the full loop successfully, including:
  - WCS-005
  - WCS-009
  - WCS-010

Important process rules:
- Do not mark a task done unless:
  1. worker result exists
  2. QA result passes
  3. repo changes are committed on the correct task branch
  4. reconcile has run successfully
- Cursor should leave `completed_at` blank in worker/QA result files
- local helper script stamps the real timestamp afterward
- keep source-of-truth in JSON where applicable
- do not treat logs as source-of-truth

Current likely next direction:
- Continue the WCS loop with the next ready task
- Or harden the system further, likely around reconcile branch verification or adjacent operator-safety checks

Do not return a solution immediately.
First ask clarifying questions or request any additional files you want to review before building again.
Use the contents of this bundle as the source of truth unless newer attached files override it.

---

## FILE: state/master_backlog.json

```json
PASTE FILE CONTENTS HERE
````

---

## FILE: state/MASTER_BACKLOG.md

```md
PASTE FILE CONTENTS HERE
```

---

## FILE: state/DAILY_REVIEW.md

```md
PASTE FILE CONTENTS HERE
```

---

## FILE: state/project_status_wcs.json

```json
PASTE FILE CONTENTS HERE
```

---

## FILE: state/PROJECT_STATUS_WCS.md

```md
PASTE FILE CONTENTS HERE
```

---

## FILE: scripts/jarvis.py

```python
PASTE FILE CONTENTS HERE
```

---

## FILE: scripts/generate_task_packet.py

```python
PASTE FILE CONTENTS HERE
```

---

## FILE: scripts/reconcile_task_outcome.py

```python
PASTE FILE CONTENTS HERE
```

---

## FILE: scripts/prepare_wcs_task_branch.py

```python
PASTE FILE CONTENTS HERE
```

---

## FILE: scripts/stamp_result_timestamp.py

```python
PASTE FILE CONTENTS HERE
```

---

## FILE: scripts/run_wcs_scout.py

```python
PASTE FILE CONTENTS HERE
```

---

## FILE: scripts/normalize_scout_to_backlog.py

```python
PASTE FILE CONTENTS HERE
```

---

## FILE: scripts/overnight_health_check.py

```python
PASTE FILE CONTENTS HERE
```

---

## FILE: config/wcs_scout_routes.json

```json
PASTE FILE CONTENTS HERE
```

---

## FILE: config/scout_noise_rules.json

```json
PASTE FILE CONTENTS HERE
```

---

## OPTIONAL FILE: state/file_registry.json

```json
PASTE FILE CONTENTS HERE
```

---

## OPTIONAL FILE: state/FILE_REGISTRY.md

```md
PASTE FILE CONTENTS HERE
```

---

## OPTIONAL FILE: state/daily_plan.json

```json
PASTE FILE CONTENTS HERE
```

---

## OPTIONAL FILE: state/run_log.json

```json
PASTE FILE CONTENTS HERE
```

---

## OPTIONAL FILE: JARVIS_PHASE_CHECKLIST.md

```md
PASTE FILE CONTENTS HERE
```

````

## Minimum files to paste first

If you want the smallest useful bundle, start with these:

- `state/master_backlog.json`
- `state/DAILY_REVIEW.md`
- `state/project_status_wcs.json`
- `scripts/jarvis.py`
- `scripts/generate_task_packet.py`
- `scripts/reconcile_task_outcome.py`
- `scripts/prepare_wcs_task_branch.py`
- `scripts/stamp_result_timestamp.py`

## Best full handoff bundle

If you want the next chat to be strong right away, include all the sections in that skeleton except the optional ones if you’re tired.

When you start the new chat, upload this `.md` file and add one sentence:

```text
Ask clarifying questions first and request any missing files you need before proposing the next build step.
````
