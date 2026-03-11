# Jarvis Workspace Starter Pack

Drop this folder's contents into:

`C:\dev\jarvis-workspace`

## What this pack gives you

- starter workspace folders
- seeded WCS backlog from your top 10 issue list
- markdown + JSON sidecar files
- task / worker / QA / escalation templates
- Windows preflight check script
- first WCS task packet draft
- basic Playwright QA starter test file

## Your locked phase-1 decisions

- Runtime side: **Windows**
- Jarvis foreman: **Python**
- WCS execution: **semi-manual in Cursor**
- WCS QA: **Playwright**
- State: **Markdown + JSON sidecars**
- Max tasks per cycle: **1**
- Main branch direct edits: **never**

## What you do first

1. Copy this pack into `C:\dev\jarvis-workspace`
2. Run `scripts\preflight_check.ps1`
3. Open `state\MASTER_BACKLOG.md`
4. Start with task `WCS-001`
5. Open `tasks\WCS-001_task.md` in Cursor and do the fix
6. Fill `results\WCS-001_worker_result.json`
7. Run WCS locally with `npm run dev`
8. Run QA after the fix using Playwright
9. Update backlog/status using the provided files

## Notes

- WCS repo path: `C:\dev\wcsv2.0-new`
- Local URL: `http://localhost:3000`
- Install command: `npm install`
- Dev command: `npm run dev`
- Build command: `npm run build`
- Public pages to verify first:
  - `/`
  - `/about`
  - `/teams`

## Files you may need to edit manually

- `state\PROJECT_STATUS_WCS.md`
- `state\project_status_wcs.json`
- `tasks\WCS-001_task.md`
- `tasks\WCS-001_task.json`

## Next recommendation

Do **not** automate Jarvis yet.
Prove one boring manual loop first:
backlog -> task packet -> Cursor change -> worker result -> QA result -> backlog update
