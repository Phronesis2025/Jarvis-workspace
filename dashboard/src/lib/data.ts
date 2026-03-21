/**
 * Data access layer — Supabase when configured, mock otherwise.
 */

import { readFile } from "fs/promises";
import { join } from "path";
import { supabase, hasSupabase } from "./supabase";
import {
  mockTasks,
  mockRuns,
  mockModuleStatus,
  mockPathfinderCases,
} from "./mock-data";
import type {
  DashboardTaskState,
  DashboardRun,
  DashboardModuleStatus,
  DashboardPathfinderCase,
  DashboardExportLog,
  ModuleChecklistsData,
} from "./types";

export async function getTasks(): Promise<DashboardTaskState[]> {
  if (hasSupabase() && supabase) {
    const { data, error } = await supabase
      .from("dashboard_task_state")
      .select("*")
      .order("updated_at", { ascending: false });
    if (error) return mockTasks;
    return (data ?? []) as DashboardTaskState[];
  }
  return mockTasks;
}

export async function getRuns(limit = 50): Promise<DashboardRun[]> {
  if (hasSupabase() && supabase) {
    const { data, error } = await supabase
      .from("dashboard_runs")
      .select("*")
      .order("started_at", { ascending: false })
      .limit(limit);
    if (error) return mockRuns;
    return (data ?? []) as DashboardRun[];
  }
  return mockRuns;
}

export async function getModuleStatus(): Promise<DashboardModuleStatus[]> {
  if (hasSupabase() && supabase) {
    const { data, error } = await supabase
      .from("dashboard_module_status")
      .select("*")
      .order("module_id");
    if (error) return mockModuleStatus;
    return (data ?? []) as DashboardModuleStatus[];
  }
  return mockModuleStatus;
}

export async function getPathfinderCases(
  limit = 50
): Promise<DashboardPathfinderCase[]> {
  if (hasSupabase() && supabase) {
    const { data, error } = await supabase
      .from("dashboard_pathfinder_cases")
      .select("*")
      .order("created_at", { ascending: false })
      .limit(limit);
    if (error) return mockPathfinderCases;
    return (data ?? []) as DashboardPathfinderCase[];
  }
  return mockPathfinderCases;
}

/** Last successful dashboard export. Returns null when unavailable (e.g. mock mode, table empty). */
export async function getLastExportTime(): Promise<DashboardExportLog | null> {
  if (hasSupabase() && supabase) {
    const { data, error } = await supabase
      .from("dashboard_export_log")
      .select("*")
      .eq("id", "latest")
      .maybeSingle();
    if (error || !data) return null;
    return data as DashboardExportLog;
  }
  return null;
}

/**
 * Read module checklists from canonical state file.
 * Works when dashboard runs from workspace (e.g. cwd is dashboard/, state is ../state/).
 * Returns null when file is unavailable (e.g. deployed without workspace state).
 */
export async function getModuleChecklists(): Promise<ModuleChecklistsData | null> {
  try {
    const workspaceRoot = join(process.cwd(), "..");
    const filePath = join(workspaceRoot, "state", "module_checklists.json");
    const raw = await readFile(filePath, "utf-8");
    const data = JSON.parse(raw) as ModuleChecklistsData;
    if (!data?.modules || !Array.isArray(data.modules)) return null;
    return data;
  } catch {
    return null;
  }
}

/** Phase A run summary shape (from phase_a_run_summary_*.json) */
export interface PhaseARunSummary {
  run_id: string;
  started_at: string;
  urls_file: string | null;
  queries_file: string | null;
  discovery_queries_used: Array<{ query: string; source_class: string; found: number }>;
  raw_from_list: number;
  after_merge_dedup: number;
  github: number;
  article: number;
  unsupported_video: number;
  unsupported_other: number;
  processed: number;
  success: number;
  partial: number;
  fail: number;
  skipped_restricted: number;
  skipped_unsupported: number;
  recurring_failures: Array<{ reason: string; count: number }>;
  results?: Array<{
    source_url: string;
    source_class: string;
    outcome: string;
    usefulness?: string;
    failure_reason?: string | null;
  }>;
}

/** Ledger row shape (phase_a_collection_ledger.jsonl) */
export interface PhaseALedgerRow {
  run_id: string;
  timestamp: string;
  source_url: string;
  source_class: string;
  input_origin: string;
  outcome: string;
  failure_reason?: string | null;
  usefulness?: string;
}

/**
 * Read latest Phase A run summary from research_swarm outputs.
 * Returns null when no summary files exist.
 */
export async function getResearchSwarmLatestRun(): Promise<PhaseARunSummary | null> {
  try {
    const { readdir } = await import("fs/promises");
    const workspaceRoot = join(process.cwd(), "..");
    const outputsDir = join(
      workspaceRoot,
      "future_modules",
      "research_swarm",
      "outputs"
    );
    const files = await readdir(outputsDir);
    const summaries = files
      .filter((f) => f.startsWith("phase_a_run_summary_") && f.endsWith(".json"))
      .sort()
      .reverse();
    if (summaries.length === 0) return null;
    const raw = await readFile(join(outputsDir, summaries[0]), "utf-8");
    return JSON.parse(raw) as PhaseARunSummary;
  } catch {
    return null;
  }
}

/**
 * Read latest N rows from Phase A collection ledger.
 * Returns empty array when ledger unavailable.
 */
export async function getResearchSwarmLedgerRows(
  limit = 25
): Promise<PhaseALedgerRow[]> {
  try {
    const workspaceRoot = join(process.cwd(), "..");
    const ledgerPath = join(
      workspaceRoot,
      "future_modules",
      "research_swarm",
      "outputs",
      "phase_a_collection_ledger.jsonl"
    );
    const raw = await readFile(ledgerPath, "utf-8");
    const lines = raw
      .trim()
      .split("\n")
      .filter((l) => l.trim());
    const rows: PhaseALedgerRow[] = [];
    for (let i = lines.length - 1; i >= 0 && rows.length < limit; i--) {
      try {
        rows.push(JSON.parse(lines[i]) as PhaseALedgerRow);
      } catch {
        /* skip malformed */
      }
    }
    return rows;
  } catch {
    return [];
  }
}
