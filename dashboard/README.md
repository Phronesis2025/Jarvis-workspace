# Jarvis Dashboard v1

Read-only web dashboard for Jarvis system progress and workflow. Deploys on Vercel.

## Architecture

- **Source of truth:** Local Jarvis JSON/Markdown files remain authoritative.
- **Dashboard:** Read-only. Supabase is the read model / dashboard data store only.
- **No write-back:** No editing, scheduling, or command execution from the UI.

## Required env vars

| Variable | Description |
|----------|-------------|
| `NEXT_PUBLIC_SUPABASE_URL` | Supabase project URL |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Supabase anonymous (public) key |

If these are not set, the dashboard uses mock data so pages can render before the sync/export pipeline exists.

## Supabase setup

1. Create a Supabase project at [supabase.com](https://supabase.com).
2. Run the schema in the SQL editor:

   ```bash
   # Copy contents of supabase/schema.sql and run in Supabase SQL editor
   ```

   The schema includes RLS policies so the dashboard (anon key) can SELECT from dashboard tables. The exporter writes with the service role key (bypasses RLS).

3. Add env vars to your deployment (see below).

## Local run

```bash
cd dashboard
npm install
npm run dev
```

Open [http://localhost:3001](http://localhost:3001). The app uses mock data when Supabase env vars are absent.

## Verification

- **Lint:** Runs non-interactively and passes (`npm run lint`).
- **Build:** May be environment-blocked on some Windows setups due to Next.js trace-file locking (EPERM on `.next` or `.next-build/trace`). Do not overclaim build success when environment-blocked.
- **Local dev:** `npm run dev` on port 3001 serves the dashboard with correct shell/styling. Overview and Module Checklists both render as expected. Use `npm run dev` for local development; `npm run start` serves the production build (if build succeeds) and may behave differently.

## Troubleshooting

- **Overview stale data:** The Overview route uses `fetchCache = "force-no-store"` so Supabase reads are not cached. If Overview shows old values, restart the dev server and run a fresh export (`python scripts/export_dashboard_data.py` from the workspace root). **Overview is now trustworthy enough for live workflow monitoring** after restart and export refresh; exporter/live activity can be observed through the current read-only dashboard surfaces.

## Vercel deployment

1. Push the repo to GitHub.
2. Import the project in Vercel (or connect existing).
3. Set root directory to `dashboard` if the dashboard lives in a subfolder.
4. Add environment variables in Vercel project settings:
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
5. Deploy. Vercel will build with `next build` and serve with `next start`.

## Pages

- **Overview:** Module-centered operations summary (Jarvis Core, WCS Code Module, Pathfinder, B1 Local Website Defect Watcher) with metrics, next steps, and Mermaid process diagrams. WCS module card includes a compact "Latest WCS run trust" section (build, smoke, page-smoke, route, stop reason). B1 module section shows bounded read-only watcher status, first site, proof summary, and a separate B1 process chart (Watcher Config → Route Checks → Evidence Capture → Noise Filter/Dedupe → Proposed Defect Packets → Operator Review). Exporter health surface shows dry-run availability, dry-run proof status, and live export as separate proof surface.
- **Task Board:** Tasks grouped by status (ready, running, awaiting operator, blocked, escalated, done).
- **Recent Runs:** Table of run_id, module, script, outcome, trust (B/S/P for WCS runs), stop_reason, llm_used, etc.
- **Pathfinder:** Table of Pathfinder cases with synthesis_source, confidence, backlog candidate.
- **Module Checklists:** Route `/checklists`. Read-only build-path view per module. Canonical source: `state/module_checklists.json` (and `state/MODULE_CHECKLISTS.md` for human view). Page shows module name, purpose, status, current phase/step, final version definition, phase-by-phase checklist, done vs remaining counts. Renders from canonical JSON when dashboard runs locally with workspace state; shows "unavailable" when file cannot be read (e.g. deployed without workspace). Local dev rendering verified (Overview and Checklists both render with correct shell/styling when `npm run dev` on port 3001).

## Exporter verification

Run `python scripts/export_dashboard_data.py --dry-run` from the workspace root to verify payload and env health without Supabase writes. Safe mode gathers local data and prints a summary; no client import or writes.

## Data flow (v1)

Data is read from Supabase. Populate it by running the export script from the workspace root:

```bash
# Set SUPABASE_URL (or NEXT_PUBLIC_SUPABASE_URL) and SUPABASE_SERVICE_KEY (or SUPABASE_SERVICE_ROLE_KEY)
python scripts/export_dashboard_data.py
```

The exporter reads local Jarvis source-of-truth files and upserts into the dashboard tables. For WCS runs, it derives and populates trust checkpoints (build, smoke, page-smoke, route, manual_check, screenshot) and stop_reason from qa_result, worker_result, task packet, and escalations. It also records the last export time in `dashboard_export_log` for the Overview "Last dashboard update" field. One-way only; never mutates Jarvis files.
