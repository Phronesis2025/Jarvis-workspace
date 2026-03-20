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

/** Trust checkpoints derived from QA/worker evidence. WCS runs only. */
export interface OperatorCheckpoints {
  build?: { status: "pass" | "fail" | "unknown" };
  smoke?: { status: "pass" | "fail" | "unknown" };
  page_smoke?: {
    status: "pass" | "fail" | "skipped" | "unknown";
    route: string | null;
  };
  manual_check?: { status: "present" | "missing" | "unknown" };
  screenshot?: { status: "captured" | "missing" | "unknown" };
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
  operator_checkpoints: OperatorCheckpoints | null;
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

/** Module checklist item status */
export type ChecklistItemStatus =
  | "done"
  | "in_progress"
  | "not_started"
  | "deferred"
  | "blocked";

/** Single checklist item within a phase */
export interface ModuleChecklistItem {
  id: string;
  label: string;
  status: ChecklistItemStatus;
  notes?: string;
}

/** Phase within a module checklist */
export interface ModuleChecklistPhase {
  phase_id: string;
  phase_name: string;
  goal: string;
  status: ChecklistItemStatus;
  items: ModuleChecklistItem[];
}

/** Module build-path checklist */
export interface ModuleChecklist {
  module_id: string;
  module_name: string;
  purpose: string;
  status: ChecklistItemStatus;
  current_phase: string;
  current_step: string;
  final_version_definition: string;
  phases: ModuleChecklistPhase[];
}

/** Root structure of state/module_checklists.json */
export interface ModuleChecklistsData {
  generated_at: string;
  modules: ModuleChecklist[];
}
