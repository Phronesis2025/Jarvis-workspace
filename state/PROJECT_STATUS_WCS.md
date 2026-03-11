# PROJECT_STATUS_WCS

## Repo
- Path: `C:\dev\wcsv2.0-new`

## Commands
- Install: `npm install`
- Dev: `npm run dev`
- Build: `npm run build`

## Local URL
- `http://localhost:3000`

## Public pages to verify first
- `/`
- `/about`
- `/teams`

## Deployment
- GitHub push triggers Vercel redeploy

## Known issue buckets
- broken
- ugly
- incomplete
- optimization

## First known tasks
- testimonial typo
- stats section showing 0
- loading states that never resolve
- empty Around the WCS section
- non-functional footer email signup
- hero headline accessibility
- production test banner
- unclear navbar Coaches link
- LogoMarquee response handling
- TodaysEvents silent failure

## Open checks still needed
- confirm Python version on Windows
- confirm Node version on Windows
- confirm Playwright install in WCS repo
- confirm whether `data-testid` selectors already exist

## Scout Defect Intake

Public Scout v1 is now integrated with automatic scout-result normalization.

Current flow:
- run_wcs_scout.py executes Playwright public route scout
- public_scout_results.json is written to the timestamped log folder
- normalize_scout_to_backlog.py runs automatically after scout
- known scout noise is filtered through scout_noise_rules.json
- valid new defects can be inserted into master_backlog.json
- MASTER_BACKLOG.md is refreshed from backlog JSON when inserts occur

Validation completed:
- clean run no-op path proven
- synthetic failure insertion path proven
- duplicate suppression path proven
