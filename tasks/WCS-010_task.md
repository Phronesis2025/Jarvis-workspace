# TASK PACKET

## Header
- Task ID: WCS-010
- Project: WCS
- Title: Show fallback message instead of hiding TodaysEvents on error
- Bucket: broken
- Priority: P2
- Risk: medium
- Status: ready

## Repo
- Repo Path: `C:\dev\wcsv2.0-new`
- Branch Name: `jarvis-task-wcs-010`

## Problem Summary
Show fallback message instead of hiding TodaysEvents on error.

## Goal
Resolve: Show fallback message instead of hiding TodaysEvents on error, with the smallest safe change that satisfies QA.

## Suspected Files
- src/components/TodaysEvents.tsx

## Acceptance Criteria
- The scoped issue is resolved: Show fallback message instead of hiding TodaysEvents on error
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
Medium risk. This should avoid unrelated production-facing behavior changes unless strictly necessary. Primary expected scope: src/components/TodaysEvents.tsx.

## Stop Conditions
- Required file cannot be found
- Build fails for unrelated reasons
- Task scope expands beyond the targeted fix

## Notes
src/components/TodaysEvents.tsx
