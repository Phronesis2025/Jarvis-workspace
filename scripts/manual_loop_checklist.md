# Manual WCS Proof Loop Checklist

## Before the fix
- [ ] Open `state/MASTER_BACKLOG.md`
- [ ] Confirm `WCS-001` is `ready`
- [ ] Create branch `jarvis-task-wcs-001`
- [ ] Open `tasks/WCS-001_task.md`
- [ ] Open repo in Cursor

## During the fix
- [ ] Apply only the targeted change
- [ ] Do not touch unrelated files
- [ ] Save changed files

## After the fix
- [ ] Run `npm run build`
- [ ] Fill `results/WCS-001_worker_result.json`
- [ ] Run local site with `npm run dev`
- [ ] Run QA for the home page
- [ ] Fill `qa/WCS-001_qa_result.json`
- [ ] Update `MASTER_BACKLOG.md` status to `done` or `escalated`
- [ ] Write summary into `DAILY_REVIEW.md`
