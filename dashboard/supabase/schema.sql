-- Jarvis Dashboard v1 — minimal read-only schema
-- Run in Supabase SQL editor or via migration

-- Task state for Task Board
CREATE TABLE IF NOT EXISTS dashboard_task_state (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  task_id text NOT NULL,
  title text NOT NULL,
  project text NOT NULL,
  module text,
  risk text,
  scope_hint text,
  status text NOT NULL CHECK (status IN ('ready', 'running', 'awaiting_operator', 'blocked', 'escalated', 'done')),
  last_result text,
  updated_at timestamptz NOT NULL DEFAULT now(),
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(task_id)
);

CREATE INDEX IF NOT EXISTS idx_task_state_status ON dashboard_task_state(status);
CREATE INDEX IF NOT EXISTS idx_task_state_project ON dashboard_task_state(project);
CREATE INDEX IF NOT EXISTS idx_task_state_updated ON dashboard_task_state(updated_at DESC);

-- Runs for Recent Runs page
CREATE TABLE IF NOT EXISTS dashboard_runs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  run_id text NOT NULL,
  module text NOT NULL,
  script_name text NOT NULL,
  task_ids text[],
  started_at timestamptz NOT NULL,
  ended_at timestamptz,
  outcome text,
  stop_reason text,
  llm_used boolean DEFAULT false,
  operator_checkpoints jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_runs_started ON dashboard_runs(started_at DESC);
CREATE INDEX IF NOT EXISTS idx_runs_module ON dashboard_runs(module);

-- Module status for Overview
CREATE TABLE IF NOT EXISTS dashboard_module_status (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  module_id text NOT NULL UNIQUE,
  name text NOT NULL,
  status text NOT NULL,
  phase text,
  milestone_summary text,
  updated_at timestamptz NOT NULL DEFAULT now(),
  created_at timestamptz NOT NULL DEFAULT now()
);

-- Pathfinder cases for Pathfinder page
CREATE TABLE IF NOT EXISTS dashboard_pathfinder_cases (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  run_id text NOT NULL,
  intake_summary text,
  route text,
  synthesis_source text CHECK (synthesis_source IN ('llm', 'rule_based')),
  confidence text,
  likely_next_action text,
  backlog_candidate_title text,
  omitted_reason text,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_pathfinder_created ON dashboard_pathfinder_cases(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_pathfinder_synthesis ON dashboard_pathfinder_cases(synthesis_source);
