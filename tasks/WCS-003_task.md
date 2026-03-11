# TASK PACKET

## Header
- Task ID: WCS-003
- Project: WCS
- Title: Add timeout/fallback handling for long loading states
- Bucket: broken
- Priority: P1
- Risk: medium
- Status: dispatched

## Repo
- Repo Path: `C:\dev\wcsv2.0-new`
- Branch Name: `jarvis-task-wcs-003`

## Problem Summary
Add timeout/fallback handling for long loading states.

## Goal
Resolve: Add timeout/fallback handling for long loading states, with the smallest safe change that satisfies QA.

## Suspected Files
- TodaysEvents.tsx
- LogoMarquee.tsx

## Acceptance Criteria
- The scoped issue is resolved: Add timeout/fallback handling for long loading states
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
Medium risk. This should avoid unrelated production-facing behavior changes unless strictly necessary. Primary expected scope: TodaysEvents.tsx, LogoMarquee.tsx.

## Stop Conditions
- Required file cannot be found
- Build fails for unrelated reasons
- Task scope expands beyond the targeted fix

## Notes
TodaysEvents.tsx, LogoMarquee.tsx
