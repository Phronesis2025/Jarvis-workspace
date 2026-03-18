/**
 * Mock data for dashboard when Supabase is not configured.
 * Allows pages to render before sync/export pipeline exists.
 */

import type {
  DashboardTaskState,
  DashboardRun,
  DashboardModuleStatus,
  DashboardPathfinderCase,
} from "./types";

export const mockTasks: DashboardTaskState[] = [
  {
    id: "1",
    task_id: "WCS-006",
    title: "Fix hero headline accessibility spacing/aria label",
    project: "WCS",
    module: "wcs",
    risk: "low",
    scope_hint: "src/components/Hero.tsx",
    status: "ready",
    last_result: null,
    updated_at: "2026-03-18T08:00:00Z",
    created_at: "2026-03-18T08:00:00Z",
  },
  {
    id: "2",
    task_id: "WCS-007",
    title: "Hide test site banner in production",
    project: "WCS",
    module: "wcs",
    risk: "low",
    scope_hint: "src/components/TestSiteBanner.tsx",
    status: "ready",
    last_result: null,
    updated_at: "2026-03-18T08:00:00Z",
    created_at: "2026-03-18T08:00:00Z",
  },
  {
    id: "3",
    task_id: "WCS-048",
    title: "Fix hero headline accessibility spacing/aria label",
    project: "WCS",
    module: "wcs",
    risk: "low",
    scope_hint: "src/app/schedules/page.tsx",
    status: "done",
    last_result: "worker_complete",
    updated_at: "2026-03-18T09:00:00Z",
    created_at: "2026-03-17T11:00:00Z",
  },
];

export const mockRuns: DashboardRun[] = [
  {
    id: "1",
    run_id: "PF-run-20260318-091232",
    module: "pathfinder",
    script_name: "run_pathfinder.py",
    task_ids: null,
    started_at: "2026-03-18T09:12:30Z",
    ended_at: "2026-03-18T09:12:32Z",
    outcome: "complete",
    stop_reason: null,
    llm_used: true,
    operator_checkpoints: null,
    created_at: "2026-03-18T09:12:32Z",
  },
  {
    id: "2",
    run_id: "WCS-048-cycle",
    module: "wcs",
    script_name: "run_one_task_cycle.py",
    task_ids: ["WCS-048"],
    started_at: "2026-03-17T11:27:00Z",
    ended_at: "2026-03-17T11:39:45Z",
    outcome: "complete",
    stop_reason: null,
    llm_used: false,
    operator_checkpoints: null,
    created_at: "2026-03-17T11:39:45Z",
  },
];

export const mockModuleStatus: DashboardModuleStatus[] = [
  {
    id: "1",
    module_id: "wcs",
    name: "WCS",
    status: "active",
    phase: "Phase 3",
    milestone_summary: "Foreman loop live; task cycles proven.",
    updated_at: "2026-03-18T09:00:00Z",
    created_at: "2026-03-18T09:00:00Z",
  },
  {
    id: "2",
    module_id: "pathfinder",
    name: "Pathfinder",
    status: "active",
    phase: "v1",
    milestone_summary: "Read-only discovery worker proven.",
    updated_at: "2026-03-18T09:00:00Z",
    created_at: "2026-03-18T09:00:00Z",
  },
];

export const mockPathfinderCases: DashboardPathfinderCase[] = [
  {
    id: "1",
    run_id: "PF-run-20260318-091232",
    intake_summary: "Schedules page empty-state shows generic placeholder; needs bounded improvement similar to WCS-048.",
    route: "/schedules",
    synthesis_source: "llm",
    confidence: "ready_for_implementation",
    likely_next_action: "Review findings and open implementation task if scope is clear.",
    backlog_candidate_title: "Improvement of Schedules Page Empty-State",
    omitted_reason: null,
    created_at: "2026-03-18T09:12:32Z",
  },
  {
    id: "2",
    run_id: "PF-run-20260318-091234",
    intake_summary: "Footer copyright year may need normalization across home and about pages. Context is limited.",
    route: "/",
    synthesis_source: "llm",
    confidence: "needs_more_context",
    likely_next_action: "Add evidence that directly addresses the intake topic, or verify scope manually.",
    backlog_candidate_title: null,
    omitted_reason: "Evidence does not directly address intake topic; artifacts contain only 1 of 4 topic terms.",
    created_at: "2026-03-18T09:12:34Z",
  },
];
