# B1 WCS Defect Watcher v1 Spec

**Status:** design frozen, implementation-ready  
**Last updated:** 2026-03-19

## Purpose

B1 v1 is a bounded local website defect watcher. It detects visible defects on a configured live site, gathers evidence, filters noise, and produces **proposed defect packets** for operator review. Operator approval is required before any finding becomes an approved defect packet or backlog item.

## Naming (frozen)

| Term | Meaning |
|------|---------|
| **Watcher config** | Input JSON file; defines target site, routes, selectors, run settings |
| **Run result** | Watcher output; run_result.json plus evidence files |
| **Proposed defect packet** | Candidate packet created by watcher from evidence; stored in proposed_defect_packets/; pending operator approval |
| **Approved defect packet** | Only after operator explicitly approves; created by operator action, not by watcher |

The watcher creates proposed packets only. The watcher never auto-approves. The watcher never creates backlog items.

## Scope

- One target site at a time
- Bounded route list (no broad crawling)
- Read-only: no auto-fix, no auto-commit, no destructive actions
- Evidence: screenshots, console capture, route check results
- Output: run result + proposed defect packets for operator approval

## Non-goals (v1)

- Auto-fix or auto-remediation
- Broad multi-site orchestration
- Scheduling or cron integration
- Concurrency or parallel site checks
- Deep DOM analysis or visual regression (pixel diff)
- Automatic backlog insertion
- Auto-approval of any packet

## Runner/tooling (frozen)

- **v1 uses Playwright**
- **Reason:** Reuse proven WCS smoke/page-smoke browser approach

## First target site

- **URL:** https://www.wcsbasketball.site/
- **Project:** WCS (WCS Basketball)
- **Rationale:** Primary production site for the WCS project; bounded, known routes

## Intake source (frozen)

- **v1 watcher is launched by CLI with a config JSON file only**
- **Standard shape:** `python scripts/run_local_website_defect_watcher.py --config <path>`
- **Do not support multiple intake styles in v1**

## Detection surfaces for v1

| Surface | Description |
|---------|-------------|
| Homepage load failure | Target URL returns non-2xx or fails to load within timeout |
| Obvious console/runtime error | Uncaught JS error, critical failure in browser console (third-party noise filtered) |
| Missing critical section | A critical selector (e.g. nav, main content) is absent from DOM |
| Direct route reachability | Each allowed route is navigated to directly by URL; load success/failure is recorded. **v1 does not click nav links** — it verifies direct URL reachability only. |
| Obvious empty-state/content failure | Expected content area is empty when it should have content |
| Screenshot evidence | Optional capture for visual record; not used for automated comparison in v1 |

## Watcher config contract

**Schema: Watcher config** (input)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| watcher_id | string | yes | Identifier for this watcher instance |
| watcher_version | string | yes | Contract version (e.g. "1.0") |
| target_site | string | yes | Base URL (must be HTTPS for v1) |
| allowed_routes | array of string | yes | Routes watcher may visit; whitelist only |
| critical_routes | array of string | yes | Routes that must pass; failure = higher severity |
| critical_selectors | object | yes | Map route -> array of CSS selectors that must exist |
| run_mode | string | yes | "bounded" for v1 |
| max_routes | number | yes | Max routes to check per run |
| capture_screenshot | boolean | yes | Whether to capture screenshots |
| capture_console | boolean | yes | Whether to capture console errors |
| dedupe_window_hours | number | yes | Hours to suppress duplicate defects |
| output_dir | string | yes | Base path for run output (e.g. scratch/local_website_defect_watcher) |
| notes | string | no | Operator notes |

## Output layout (frozen)

All run output is written under:

```
<output_dir>/<watcher_id>/<run_id>/
├── run_result.json
├── screenshots/
├── console_errors.json
├── evidence_manifest.json
└── proposed_defect_packets/
    └── <finding_id>.json   (one file per proposed packet)
```

- **run_result.json** — Full run result schema (see below)
- **screenshots/** — Screenshot files named `{route_slug}.png` (route "/" → "root", "/schedules" → "schedules")
- **console_errors.json** — Array of console error objects
- **evidence_manifest.json** — Array of `{evidence_type, path, note, finding_id}`; consolidated evidence list
- **proposed_defect_packets/** — Proposed defect packet JSON files only; no approved canonical packets here

## Dedupe persistence (frozen)

- **Location:** `state/local_website_defect_watcher_dedupe.json`
- **Contents:** `duplicate_key` history with `last_seen` timestamps
- **Format:** `{ "duplicate_key": "last_seen_iso8601", ... }`
- **Simple for v1**

## Run result schema (frozen)

**File:** `run_result.json`

| Field | Type | Description |
|-------|------|-------------|
| run_id | string | Unique run identifier |
| watcher_id | string | From config |
| watcher_version | string | From config |
| target_site | string | From config |
| started_at | string | ISO 8601 |
| completed_at | string | ISO 8601 |
| status | string | "completed", "partial", "failed" |
| findings | array | Array of finding objects (schema below) |
| checked_routes | array | Array of route check objects (schema below) |
| screenshots | array | Array of screenshot objects (schema below) |
| console_errors | array | Array of console error objects (schema below) |
| proposed_packet_count | number | Count of proposed defect packets written |
| recommended_action | string | "review", "dismiss", "escalate" |
| requires_operator_review | boolean | True when findings exist |

### findings[] schema

| Field | Type | Description |
|-------|------|-------------|
| finding_id | string | Unique id (e.g. B1-FND-20260319-001) |
| defect_type | string | load_failure, console_error, missing_critical_section, broken_nav, empty_content |
| severity | string | low, medium, high, critical |
| summary | string | One-line summary |
| affected_route | string | Route where defect was found |
| critical | boolean | True if route is in critical_routes |
| evidence | array | Array of evidence objects (schema below) |
| duplicate_key | string | For deduplication |
| recommended_followup | string | Suggested next step |
| requires_operator_review | boolean | Always true for findings |

### findings[].evidence[] schema

| Field | Type | Description |
|-------|------|-------------|
| evidence_type | string | screenshot, console_error, selector_missing |
| path | string | Relative path to evidence file or selector |
| note | string | Brief note |

### checked_routes[] schema

| Field | Type | Description |
|-------|------|-------------|
| route | string | Route path (e.g. /, /schedules) |
| checked_at | string | ISO 8601 |
| load_status | string | pass, fail, timeout |
| nav_status | string | pass, fail, skipped. **v1:** Always pass when route loads; no nav-link clicking. |
| critical_selector_status | string | pass, fail, skipped |
| screenshot_path | string \| null | Path to screenshot if captured |

### screenshots[] schema

| Field | Type | Description |
|-------|------|-------------|
| path | string | Relative path to screenshot file |
| route | string | Route where captured |
| captured_at | string | ISO 8601 |
| purpose | string | evidence, route_check |

### console_errors[] schema

| Field | Type | Description |
|-------|------|-------------|
| route | string | Route where error occurred |
| level | string | error, warning |
| message | string | Error message |
| captured_at | string | ISO 8601 |

## Proposed defect packet schema (frozen)

**Location:** `proposed_defect_packets/<finding_id>.json`

| Field | Type | Description |
|-------|------|-------------|
| packet_id | string | Same as finding_id for proposed packets |
| source | string | watcher_id |
| target_site | string | Site where defect was observed |
| defect_type | string | Same as finding |
| severity | string | Same as finding |
| summary | string | Same as finding |
| affected_route | string | Same as finding |
| reproduction_hint | string | How to reproduce |
| evidence | array | Same shape as findings[].evidence |
| duplicate_key | string | For deduplication |
| recommended_followup | string | Same as finding |
| operator_status | string | Always "pending_review" for proposed packets |

**Note:** Approved defect packets are created by operator action (separate flow). They may add operator_status: approved_defect_packet or approved_backlog_candidate. The watcher never writes approved packets.

## Operator gate (frozen)

- **Watcher may create proposed packet JSON only**
- **Watcher may never auto-create real backlog items**
- **Watcher may never auto-approve a packet**
- **Operator outcomes (explicit):**

| Outcome | Meaning |
|---------|---------|
| dismissed_noise | Operator marks as noise; no packet promoted; may update dedupe |
| informational_only | Operator acknowledges; no backlog item |
| approved_defect_packet | Operator approves; approved packet written (by operator flow); ready for backlog candidate |
| approved_backlog_candidate | Operator approves and requests backlog insertion (operator flow) |

## Noise filtering rules

1. **Transient third-party warnings** — Ads, analytics, or third-party script warnings do not automatically count as defects. Console messages containing supabase, websocket, realtime, analytics, advertisement, gtag, facebook, google-analytics, or third-party are filtered.
2. **One-off flaky load** — Single load failure on non-critical route requires rerun before packet creation; if route is in critical_routes, one failure may create proposed packet.
3. **Cosmetic variance** — Layout drift, font differences, or minor visual variance without functional break do not become a packet.
4. **Duplicate suppression** — Same duplicate_key within dedupe_window_hours is suppressed; check state/local_website_defect_watcher_dedupe.json.

## Duplicate suppression rules

- `duplicate_key` = `{route}:{defect_type}:{normalized_summary}` (max 80 chars for summary part)
- Normalized summary: lowercase, trim, collapse whitespace
- Check state/local_website_defect_watcher_dedupe.json; if key exists and last_seen within window, suppress
- On new finding, update dedupe file with current timestamp

## Severity rules

| Severity | Criteria |
|----------|----------|
| critical | Homepage load failure; critical route completely broken |
| high | Critical route missing critical section |
| medium | Non-critical route missing section; console error on critical route |
| low | Non-critical route minor issue |

## Recommended v1 execution flow

1. Load watcher config from `--config <path>`; validate schema.
2. Create run_id; create output dir `<output_dir>/<watcher_id>/<run_id>/`.
3. Load dedupe state from state/local_website_defect_watcher_dedupe.json.
4. For each route in allowed_routes up to max_routes:
   - Navigate to target_site + route (Playwright)
   - Check load success
   - Check critical selectors if route in critical_routes
   - Capture screenshot if capture_screenshot
   - Capture console errors if capture_console
   - Build checked_routes entry
5. Apply noise filtering and duplicate suppression.
6. Build findings array; for each finding, write proposed packet to proposed_defect_packets/.
7. Write run_result.json, console_errors.json, evidence_manifest.json.
8. Update state/local_website_defect_watcher_dedupe.json.
9. Print summary; exit.

## Example defect scenarios for WCS

- **Homepage load failure:** https://www.wcsbasketball.site/ returns 500 or times out.
- **Missing critical section:** Route loads but a configured critical selector (e.g. nav, main) is absent from DOM.
- **Direct route unreachable:** Navigating to a route by URL fails (load_status fail/timeout). v1 does not verify nav-link clicking.
- **Empty content:** Expected content area is empty when it should have content.
- **Console error:** Uncaught TypeError on page load (third-party noise such as Supabase/WebSocket is filtered).

## Test plan for v1

1. **Happy path:** All routes load; no findings; run result shows status "completed", empty findings.
2. **Load failure:** Simulate or use unreachable URL; verify finding created with severity critical.
3. **Missing selector:** Use test page with missing critical selector; verify finding and proposed packet.
4. **Noise filtering:** Inject third-party warning; verify it does not become a defect.
5. **Deduplication:** Run twice with same defect within window; verify second run suppresses.
6. **Output layout:** Verify all files written to correct paths.
7. **Operator review:** Operator flow (out of scope for watcher) approves; verify approved packet created elsewhere.

## Future extension notes

- Add more sites via config array (one site per run in v1).
- Optional scheduling (cron, n8n) after v1 proven.
- Visual regression (pixel diff) as optional detection surface.
- Direct backlog insertion when operator approves with approved_backlog_candidate.
