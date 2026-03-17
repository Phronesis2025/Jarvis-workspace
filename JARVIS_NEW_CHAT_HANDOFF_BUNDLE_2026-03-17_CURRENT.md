# JARVIS NEW CHAT HANDOFF — 2026-03-17

**Read this file first when continuing the Jarvis rebuild in a new chat.**

- **Last updated:** 2026-03-17
- **Purpose:** Self-contained handoff for new chat; reflects current live truth only.

---

## 1. Paths

| Role | Path |
|------|------|
| **Jarvis workspace root** | `C:\dev\jarvis-workspace` |
| **WCS repo root** | `C:\dev\wcsv2.0-new` |

---

## 2. Core Identity

- **Jarvis** is the foreman/orchestrator. It coordinates task selection, packet generation, worker routing, verification, and logging. It is not the main builder.
- **Cursor** is the current execution surface for the coding worker. The WCS worker runs through Cursor.
- **WCS** (website) is the first active proof domain.

---

## 3. What Is Proven

| Capability | Status |
|------------|--------|
| **Core loop** | Proven |
| **Strict launch path** | Proven |
| **One-task wrapper** (`run_one_task_cycle.py`) | Proven |
| **Full-cycle wrapper mechanical path** (`run_one_task_full_cycle.py`) | Proven |
| **`--finalize`** (resume mode for post after manual verification) | Proven |
| **Screenshot artifact support** | Proven |

The wrapper family can truthfully close a single task end-to-end via: mechanical path (prep, strict launch, diff review, commit, build, managed dev server, smoke, screenshot capture) → honest manual-check stop → `--finalize` for post.

---

## 4. Proof Tasks and What Each Proved

| Task | What it proved |
|------|----------------|
| **WCS-041** | Strict real-Agent `--launch-cursor` success path; Hero.tsx |
| **WCS-046** | One-command single-task wrapper (`run_one_task_cycle.py`); ClientTeams.tsx |
| **WCS-031** | About page flow; about/page.tsx |
| **WCS-048** | Schedules page flow; schedules/page.tsx |
| **WCS-061** | Full-cycle wrapper mechanical path (prep through screenshot capture); Footer.tsx; honest stop before manual verification |
| **WCS-008** | Full-cycle + `--finalize`; screenshot artifact support; Navbar.tsx; wrapper can close a single task end-to-end |

**WCS-033 was a bad proof target** (empty-state visibility; target not visible in default local app state). Its proof debris was cleaned up. **Do not treat WCS-033 as proof.**

---

## 5. Current Process Position (Plain Language)

We are past single-task proof. The full-cycle wrapper (`run_one_task_full_cycle.py`) can run one task from prep through post when the operator provides `--confirm-commit` and `--manual-check`. The flow stops honestly before manual verification; the operator then runs with `--finalize` to complete post (which includes reconcile). No batching or scheduling is live yet. The next logical build target is a **sequential single-command multi-task runner**: run one task after another in sequence, not concurrently.

---

## 6. Known Gaps and Constraints

- **Current smoke test** is limited and should be improved later, especially for page-specific task coverage.
- **No batching or scheduling** is live yet.
- **Next target:** Sequential single-task execution across multiple tasks (one after another), not concurrency.

---

## 7. Project Constraints and Preferences

- **Before every Cursor prompt,** provide the exact model to use (e.g. `composer-1.5`).
- **Keep prompts tight and constrained.**
- **Prefer boring, durable steps** over flashy redesign.

---

## 8. Key Scripts

| Script | Role |
|--------|------|
| `scripts/run_one_task_full_cycle.py` | Full single-task closeout; supports `--finalize` for post-only |
| `scripts/run_one_task_cycle.py` | Prep + optional launch; prints remaining operator steps |
| `scripts/run_wcs_operator_entrypoint.py` | Thin wrapper for `prep` and `post` |
| `scripts/select_next_ready_task.py` | Selects next eligible ready task from backlog |
| `scripts/reconcile_task_outcome.py` | Updates backlog from worker/QA results |

---

## 9. State Files

- `state/master_backlog.json` — machine-readable backlog
- `state/MASTER_BACKLOG.md` — rendered backlog
- `state/file_registry.json` — file registry (source of truth)
- `state/FILE_REGISTRY.md` — rendered registry
- `tasks/<TASK_ID>_task.json` — task packet per task

---

## 10. Further Reading

- `JARVIS_LIVE_HANDOFF_BUNDLE.md` — detailed live state
- `JARVIS_TASK_EXECUTION_CHECKLIST.md` — operator checklist
- `JARVIS_SCRIPT_PROCESS_REFERENCE.md` — script reference
