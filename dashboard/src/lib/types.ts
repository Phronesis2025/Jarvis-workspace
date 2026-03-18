/** Dashboard row types — match Supabase schema */

export type TaskStatus =
  | "ready"
  | "running"
  | "awaiting_operator"
  | "blocked"
  | "escalated"
  | "done";

export interface DashboardTaskState {
  id: string;
  task_id: string;
  title: string;
  project: string;
  module: string | null;
  risk: string | null;
  scope_hint: string | null;
  status: TaskStatus;
  last_result: string | null;
  updated_at: string;
  created_at: string;
}

export interface DashboardRun {
  id: string;
  run_id: string;
  module: string;
  script_name: string;
  task_ids: string[] | null;
  started_at: string;
  ended_at: string | null;
  outcome: string | null;
  stop_reason: string | null;
  llm_used: boolean;
  operator_checkpoints: unknown;
  created_at: string;
}

export interface DashboardModuleStatus {
  id: string;
  module_id: string;
  name: string;
  status: string;
  phase: string | null;
  milestone_summary: string | null;
  updated_at: string;
  created_at: string;
}

export interface DashboardPathfinderCase {
  id: string;
  run_id: string;
  intake_summary: string | null;
  route: string | null;
  synthesis_source: "llm" | "rule_based" | null;
  confidence: string | null;
  likely_next_action: string | null;
  backlog_candidate_title: string | null;
  omitted_reason: string | null;
  created_at: string;
}

export interface DashboardExportLog {
  id: string;
  exported_at: string;
  task_count: number | null;
  run_count: number | null;
  module_count: number | null;
  pathfinder_count: number | null;
}
