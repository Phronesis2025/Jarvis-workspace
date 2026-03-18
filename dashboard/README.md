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

3. Add env vars to your deployment (see below).

## Local run

```bash
cd dashboard
npm install
npm run dev
```

Open [http://localhost:3001](http://localhost:3001). The app uses mock data when Supabase env vars are absent.

## Vercel deployment

1. Push the repo to GitHub.
2. Import the project in Vercel (or connect existing).
3. Set root directory to `dashboard` if the dashboard lives in a subfolder.
4. Add environment variables in Vercel project settings:
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
5. Deploy. Vercel will build with `next build` and serve with `next start`.

## Pages

- **Overview:** Module-centered operations summary (Jarvis Core, WCS Code Module, Pathfinder) with metrics, next steps, and Mermaid process diagrams.
- **Task Board:** Tasks grouped by status (ready, running, awaiting operator, blocked, escalated, done).
- **Recent Runs:** Table of run_id, module, script, outcome, llm_used, etc.
- **Pathfinder:** Table of Pathfinder cases with synthesis_source, confidence, backlog candidate.

## Data flow (v1)

Data is read from Supabase. Populate it by running the export script from the workspace root:

```bash
# Set SUPABASE_URL (or NEXT_PUBLIC_SUPABASE_URL) and SUPABASE_SERVICE_KEY (or SUPABASE_SERVICE_ROLE_KEY)
python scripts/export_dashboard_data.py
```

The exporter reads local Jarvis source-of-truth files and upserts into the dashboard tables. One-way only; never mutates Jarvis files.
