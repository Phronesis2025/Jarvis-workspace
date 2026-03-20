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
