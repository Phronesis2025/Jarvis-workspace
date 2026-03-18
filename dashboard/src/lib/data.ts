/**
 * Data access layer — Supabase when configured, mock otherwise.
 */

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
