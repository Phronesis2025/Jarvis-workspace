/**
 * Data access layer — Supabase when configured, mock otherwise.
 */

import { readFile, readdir, stat } from "fs/promises";
import { basename, join } from "path";
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
  youtube_video?: number;
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
    extraction_path?: string | null;
  }>;
}

/** Extraction report shape (from extraction_report_*_api.json) */
export interface ExtractionReport {
  summary?: string;
  methods_tools_patterns?: Array<{ name: string; description?: string; category?: string }>;
  key_claims?: Array<{ claim: string; confidence?: string }>;
  hype_signals?: string[];
  open_questions?: string[];
  mentioned_symbols?: string[];
}

/**
 * Read extraction report from path. Returns null if file missing or invalid.
 */
export async function getExtractionReport(
  absPath: string | null | undefined
): Promise<ExtractionReport | null> {
  if (!absPath || !absPath.trim()) return null;
  try {
    const raw = await readFile(absPath, "utf-8");
    const data = JSON.parse(raw) as ExtractionReport;
    return data;
  } catch {
    return null;
  }
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
  extraction_path?: string | null;
  packet_path?: string | null;
}

/** Normalized summary for display (from run or sweep) */
export interface ResearchSwarmSummaryDisplay {
  run_id: string;
  started_at: string;
  success: number;
  partial: number;
  fail: number;
  skipped: number;
  github: number;
  article: number;
  youtube_video: number;
  unsupported: number;
  raw_from_list?: number;
  after_merge_dedup?: number;
  urls_file?: string | null;
  queries_file?: string | null;
  recurring_failures?: Array<{ reason: string; count: number }>;
}

/**
 * Read latest Phase A run or sweep summary from research_swarm outputs.
 * Prefers the most recent by filename (run or sweep).
 */
export async function getResearchSwarmLatestRun(): Promise<ResearchSwarmSummaryDisplay | null> {
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
    const runSummaries = files
      .filter((f) => f.startsWith("phase_a_run_summary_") && f.endsWith(".json"))
      .sort()
      .reverse();
    const sweepSummaries = files
      .filter((f) => f.startsWith("phase_a_sweep_summary_") && f.endsWith(".json"))
      .sort()
      .reverse();
    const all = [
      ...runSummaries.map((f) => ({ f, type: "run" as const })),
      ...sweepSummaries.map((f) => ({ f, type: "sweep" as const })),
    ].sort((a, b) => (b.f > a.f ? 1 : -1));
    if (all.length === 0) return null;
    const { f: chosen, type } = all[0];
    const raw = await readFile(join(outputsDir, chosen), "utf-8");
    const data = JSON.parse(raw);
    if (type === "sweep") {
      const d = data as Record<string, unknown>;
      return {
        run_id: (d.sweep_run_id as string) ?? (d.run_id as string) ?? chosen,
        started_at: (d.started_at as string) ?? "",
        success: (d.success_count as number) ?? 0,
        partial: (d.partial_count as number) ?? 0,
        fail: (d.fail_count as number) ?? 0,
        skipped: (d.skipped_count as number) ?? 0,
        github: 0,
        article: 0,
        youtube_video: 0,
        unsupported: 0,
        queries_file: d.query_file as string,
        recurring_failures: d.recurring_failures as Array<{ reason: string; count: number }>,
      };
    }
    const run = data as PhaseARunSummary;
    return {
      run_id: run.run_id ?? "",
      started_at: run.started_at ?? "",
      success: run.success ?? 0,
      partial: run.partial ?? 0,
      fail: run.fail ?? 0,
      skipped: (run.skipped_restricted ?? 0) + (run.skipped_unsupported ?? 0),
      github: run.github ?? 0,
      article: run.article ?? 0,
      youtube_video: run.youtube_video ?? 0,
      unsupported: (run.unsupported_video ?? 0) + (run.unsupported_other ?? 0),
      raw_from_list: run.raw_from_list,
      after_merge_dedup: run.after_merge_dedup,
      urls_file: run.urls_file,
      queries_file: run.queries_file,
      recurring_failures: run.recurring_failures,
    };
  } catch {
    return null;
  }
}

/**
 * Read all Phase A collection ledger rows.
 * Returns newest-first (most recent at index 0).
 * Collector and sweep runs both append to this ledger.
 */
export async function getResearchSwarmAllLedgerRows(): Promise<PhaseALedgerRow[]> {
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
    for (let i = lines.length - 1; i >= 0; i--) {
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

/** Stock symbol review summary shape (from stock_symbol_review_summary.json) */
export interface StockSymbolReviewSummary {
  generated_from?: string;
  report_count?: number;
  symbol_count?: number;
  symbols?: Array<{
    symbol: string;
    occurrence_count: number;
    source_count: number;
    example_source_urls?: string[];
    example_packet_ids?: string[];
    stock_relevant_sources?: number;
    all_sources_stock_relevant?: boolean;
  }>;
}

/** Draft watchlist packet shape (from draft_watchlist_packet_from_rs.json) */
export interface DraftWatchlistPacket {
  packet_id?: string;
  created_at?: string;
  symbols?: string[];
  watch_reason?: string;
  time_horizon?: string;
  risk_tolerance?: string;
  notes?: string;
}

/**
 * Read stock symbol review summary from research_swarm outputs.
 * Returns null when file is missing or invalid.
 */
export async function getStockSymbolReviewSummary(): Promise<StockSymbolReviewSummary | null> {
  try {
    const workspaceRoot = join(process.cwd(), "..");
    const path = join(
      workspaceRoot,
      "future_modules",
      "research_swarm",
      "outputs",
      "stock_symbol_review_summary.json"
    );
    const raw = await readFile(path, "utf-8");
    return JSON.parse(raw) as StockSymbolReviewSummary;
  } catch {
    return null;
  }
}

/**
 * Read draft watchlist packet from research_swarm outputs.
 * Returns null when file is missing or invalid.
 */
export async function getDraftWatchlistPacket(): Promise<DraftWatchlistPacket | null> {
  try {
    const workspaceRoot = join(process.cwd(), "..");
    const path = join(
      workspaceRoot,
      "future_modules",
      "research_swarm",
      "outputs",
      "draft_watchlist_packet_from_rs.json"
    );
    const raw = await readFile(path, "utf-8");
    return JSON.parse(raw) as DraftWatchlistPacket;
  } catch {
    return null;
  }
}

/** Stock research brief shape (from stock_research_brief_*.json) */
export interface StockResearchBrief {
  report_id?: string;
  packet_id?: string;
  created_at?: string;
  symbols?: string[];
  briefs?: Array<{
    symbol: string;
    thesis_or_watch_reason?: string;
    catalyst_summary?: string;
    risk_summary?: string;
    evidence_sources?: Array<{ type?: string; title?: string; date?: string; url?: string }>;
    open_questions?: string[];
    confidence_band?: string;
    review_recommendation?: string;
  }>;
}

const STOCK_MODULE_OUTPUTS_SEGMENTS = [
  "future_modules",
  "stock_module",
  "outputs",
] as const;

const STOCK_RESEARCH_BRIEF_PREFIX = "stock_research_brief_";
const RISK_GATE_REVIEW_PREFIX = "risk_gate_review_";

/**
 * Absolute path to the newest stock_research_brief_*.json by mtime, or null.
 */
async function getLatestStockResearchBriefFilePath(): Promise<string | null> {
  try {
    const workspaceRoot = join(process.cwd(), "..");
    const outputsDir = join(workspaceRoot, ...STOCK_MODULE_OUTPUTS_SEGMENTS);
    const entries = await readdir(outputsDir, { withFileTypes: true });
    const briefFiles = entries.filter(
      (e) =>
        e.isFile() &&
        e.name.startsWith(STOCK_RESEARCH_BRIEF_PREFIX) &&
        e.name.endsWith(".json")
    );
    if (briefFiles.length === 0) return null;
    const withStat = await Promise.all(
      briefFiles.map(async (e) => {
        const p = join(outputsDir, e.name);
        const s = await stat(p);
        return { path: p, mtime: s.mtimeMs };
      })
    );
    withStat.sort((a, b) => b.mtime - a.mtime);
    return withStat[0].path;
  } catch {
    return null;
  }
}

/**
 * Read the most recent stock research brief from stock_module outputs.
 * Returns null when no brief file exists or read fails.
 */
export async function getLatestStockResearchBrief(): Promise<StockResearchBrief | null> {
  try {
    const path = await getLatestStockResearchBriefFilePath();
    if (!path) return null;
    const raw = await readFile(path, "utf-8");
    return JSON.parse(raw) as StockResearchBrief;
  } catch {
    return null;
  }
}

/** One row in risk_gate_review.flags */
export interface RiskGateFlagRow {
  symbol: string;
  rule: string;
  description: string;
}

/** Risk gate review JSON (risk_gate_review_*.json), paired by filename suffix with the brief */
export interface RiskGateReview {
  review_id?: string;
  report_id?: string;
  created_at?: string;
  overall_status?: "pass" | "caution" | "flag";
  flags?: RiskGateFlagRow[];
  summary?: string;
}

/**
 * Load risk_gate_review_<suffix>.json for the same suffix as the latest
 * stock_research_brief_<suffix>.json (by mtime). Returns null if the paired
 * file is missing or invalid.
 */
export async function getRiskGateReviewForLatestBrief(): Promise<RiskGateReview | null> {
  try {
    const briefPath = await getLatestStockResearchBriefFilePath();
    if (!briefPath) return null;
    const name = basename(briefPath);
    if (
      !name.startsWith(STOCK_RESEARCH_BRIEF_PREFIX) ||
      !name.endsWith(".json")
    ) {
      return null;
    }
    const stem = name.slice(0, -".json".length);
    const suffix = stem.startsWith(STOCK_RESEARCH_BRIEF_PREFIX)
      ? stem.slice(STOCK_RESEARCH_BRIEF_PREFIX.length)
      : stem;
    const workspaceRoot = join(process.cwd(), "..");
    const outputsDir = join(workspaceRoot, ...STOCK_MODULE_OUTPUTS_SEGMENTS);
    const riskPath = join(outputsDir, `${RISK_GATE_REVIEW_PREFIX}${suffix}.json`);
    const raw = await readFile(riskPath, "utf-8");
    return JSON.parse(raw) as RiskGateReview;
  } catch {
    return null;
  }
}

export interface StockBriefReviewPair {
  /** Suffix after `stock_research_brief_` used for pairing with risk gate filename */
  suffix: string;
  /** Absolute path to stock_research_brief_<suffix>.json */
  briefPath: string;
  /** The parsed research brief JSON */
  brief: StockResearchBrief;
  /** Absolute path to risk_gate_review_<suffix>.json when it exists */
  riskGatePath: string | null;
  /** Parsed risk gate review JSON when it exists */
  riskGate: RiskGateReview | null;

  /** Selector fields derived from brief JSON (first symbol in `briefs[]`) */
  symbol: string;
  createdAt: string | null;
  confidenceBand: string | null;
}

/**
 * List available stock brief outputs and pair each with its matching
 * risk gate review output (paired by filename suffix).
 *
 * Returns newest-first (by brief file mtime).
 */
export async function getAvailableStockBriefReviewPairs(): Promise<StockBriefReviewPair[]> {
  try {
    const workspaceRoot = join(process.cwd(), "..");
    const outputsDir = join(workspaceRoot, ...STOCK_MODULE_OUTPUTS_SEGMENTS);
    const entries = await readdir(outputsDir, { withFileTypes: true });
    const briefFiles = entries.filter(
      (e) =>
        e.isFile() &&
        e.name.startsWith(STOCK_RESEARCH_BRIEF_PREFIX) &&
        e.name.endsWith(".json")
    );

    const withStat = await Promise.all(
      briefFiles.map(async (e) => {
        const briefPath = join(outputsDir, e.name);
        const s = e.name.slice(0, -".json".length);
        const suffix = s.startsWith(STOCK_RESEARCH_BRIEF_PREFIX)
          ? s.slice(STOCK_RESEARCH_BRIEF_PREFIX.length)
          : s;

        const st = await stat(briefPath);

        let brief: StockResearchBrief | null = null;
        try {
          const raw = await readFile(briefPath, "utf-8");
          brief = JSON.parse(raw) as StockResearchBrief;
        } catch {
          brief = null;
        }

        const first = brief?.briefs?.[0];
        const symbol = first?.symbol ?? "—";
        const createdAt = (brief?.created_at ?? null) as string | null;
        const confidenceBand = (first?.confidence_band ?? null) as string | null;

        const riskGatePath = join(outputsDir, `${RISK_GATE_REVIEW_PREFIX}${suffix}.json`);
        let riskGate: RiskGateReview | null = null;
        try {
          const raw = await readFile(riskGatePath, "utf-8");
          riskGate = JSON.parse(raw) as RiskGateReview;
        } catch {
          riskGate = null;
        }

        return {
          mtimeMs: st.mtimeMs,
          item: {
            suffix,
            briefPath,
            brief: brief ?? { briefs: [] },
            riskGatePath: riskGate ? riskGatePath : null,
            riskGate,
            symbol,
            createdAt,
            confidenceBand,
          } as StockBriefReviewPair,
        };
      })
    );

    withStat.sort((a, b) => b.mtimeMs - a.mtimeMs);
    return withStat.map((x) => x.item);
  } catch {
    return [];
  }
}

/**
 * Derive most useful links from ledger: outcome=success, usefulness=useful.
 * Dedupes by source_url; newest successful useful row wins.
 */
export function deriveMostUsefulFromLedger(
  rows: PhaseALedgerRow[]
): PhaseALedgerRow[] {
  const byUrl = new Map<string, PhaseALedgerRow>();
  for (const r of rows) {
    if (r.outcome !== "success" || (r.usefulness ?? "") !== "useful") continue;
    const url = (r.source_url || "").trim();
    if (!url) continue;
    const existing = byUrl.get(url);
    if (!existing || r.timestamp > existing.timestamp) {
      byUrl.set(url, r);
    }
  }
  return Array.from(byUrl.values()).sort(
    (a, b) => (b.timestamp > a.timestamp ? 1 : -1)
  );
}
