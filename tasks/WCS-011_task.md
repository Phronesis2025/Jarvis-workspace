# TASK PACKET

## Header
- Task ID: WCS-011
- Project: WCS
- Title: Stabilize local Playwright smoke QA for home page
- Bucket: broken
- Priority: P1
- Risk: low
- Status: dispatched

## Repo
- Repo Path: `C:\dev\wcsv2.0-new`
- Branch Name: `jarvis-task-wcs-011`

## Problem Summary
Stabilize local Playwright smoke QA for home page.

## Goal
Resolve: Stabilize local Playwright smoke QA for home page, with the smallest safe change that satisfies QA.

## Suspected Files
- tests/e2e
- playwright config
- global setup for http://localhost:3000

## Acceptance Criteria
- The scoped issue is resolved: Stabilize local Playwright smoke QA for home page
- App builds successfully with npm run build
- Local app can be opened for verification
- Targeted change is visible or behaves correctly on the relevant page/flow
- Changes remain tightly limited to the suspected files unless a clearly related helper/config file must also be updated

## QA Plan
- Run npm run build
- Start local app with npm run dev
- Run Playwright smoke QA if available
- Verify the targeted change locally in the browser

## System Impact
Low risk. This should avoid unrelated production-facing behavior changes unless strictly necessary. Primary expected scope: tests/e2e, playwright config, global setup for http://localhost:3000.

## Stop Conditions
- Required file cannot be found
- Build fails for unrelated reasons
- Task scope expands beyond the targeted fix

## Notes
tests/e2e, playwright config, global setup for http://localhost:3000
