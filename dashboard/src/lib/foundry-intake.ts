import { readFile, readdir, writeFile, mkdir } from "fs/promises";
import { join } from "path";
import { execFile } from "child_process";
import { promisify } from "util";
import type { FoundryRegistryIdea } from "@/lib/types";

const execFileAsync = promisify(execFile);

export type FoundryLane = "article" | "github" | "x_post";

export interface FoundryTopIdea {
  idea_id: string;
  title: string;
  category: string;
  status: string;
  weighted_score: number;
  supporting_source_count: number;
  confidence: number;
  expected_upside: number;
  implementation_cost: number;
  risk_reduction_value: number;
  last_updated: string;
}

export interface FoundryIntakeResult {
  status: "success";
  lane: FoundryLane;
  run_id: string;
  limitation_note: string;
  source_record: Record<string, unknown>;
  candidate_ideas: Array<Record<string, unknown>>;
  output_paths: Record<string, string>;
  top_10_lane_ideas: FoundryTopIdea[];
}

function workspaceRoot(): string {
  return join(process.cwd(), "..");
}

function foundryStateRoot(): string {
  return join(workspaceRoot(), "future_modules", "the_foundry", "state");
}

function normalize(value: string): string {
  return value.toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/^_+|_+$/g, "").slice(0, 80);
}

function nowIso(): string {
  return new Date().toISOString();
}

function runIdToken(): string {
  return new Date().toISOString().replace(/[-:]/g, "").replace(/\.\d{3}Z$/, "Z");
}

function laneMeta(lane: FoundryLane): { source_type: "article_text" | "github_repo" | "x_post_brief"; label: string } {
  if (lane === "article") return { source_type: "article_text", label: "Article Intake" };
  if (lane === "github") return { source_type: "github_repo", label: "GitHub Intake" };
  return { source_type: "x_post_brief", label: "X Post Intake" };
}

function validateInput(lane: FoundryLane, input: string): string | null {
  const trimmed = input.trim();
  if (!trimmed) return "Input is required.";
  if (lane === "github") {
    if (!/^https?:\/\/(www\.)?github\.com\/.+/i.test(trimmed)) {
      return "GitHub Intake requires a valid github.com URL.";
    }
  } else if (trimmed.length < 40) {
    return "Text input is too short for bounded local extraction (minimum 40 chars).";
  }
  return null;
}

function makeCandidateTitle(lane: FoundryLane, input: string): string {
  const trimmed = input.trim();
  if (lane === "github") return `GitHub pattern from ${trimmed.replace(/^https?:\/\//i, "")}`;
  return trimmed.split(/\s+/).slice(0, 8).join(" ");
}

/** 0–5 inclusive; deterministic rounding. */
function clampInt0to5(n: number): number {
  const r = Math.round(n);
  if (r < 0) return 0;
  if (r > 5) return 5;
  return r;
}

/** Count how many distinct keywords appear at least once (substring match). */
function keywordHitCount(lc: string, keywords: readonly string[]): number {
  let hits = 0;
  for (const kw of keywords) {
    if (lc.includes(kw)) hits += 1;
  }
  return hits;
}

/**
 * Coarse 0–5 integers from cheap local signals only (length, lane, bullets, keyword families).
 * Not semantic evaluation — same input always yields same scores.
 */
export type IntakeHeuristicDimensions = {
  confidence: number;
  evidence_strength: number;
  transferability: number;
  expected_upside: number;
  risk_reduction_value: number;
  implementation_cost: number;
  novelty: number;
  dependency_burden: number;
};

export function deriveIntakeHeuristicScores(lane: FoundryLane, rawInput: string): IntakeHeuristicDimensions {
  const text = rawInput.trim();
  const lc = text.toLowerCase();
  const len = text.length;

  const paragraphBreaks = (text.match(/\n\s*\n/g) ?? []).length;
  const bulletLines = (text.match(/^\s*[-*•]\s+/gm) ?? []).length;
  const numberedLines = (text.match(/^\s*\d+[.)]\s+/gm) ?? []).length;
  const sentenceEnds = (text.match(/[.!?](?:\s|$)/g) ?? []).length;
  const structuredUnits = bulletLines + numberedLines;

  // evidence_strength: material + light structure (not “truth of claims”)
  let evidence_strength = 1;
  if (lane === "github") {
    const pathPart = lc.replace(/^https?:\/\/(www\.)?github\.com\//i, "");
    const segments = pathPart.split("/").filter(Boolean).length;
    evidence_strength = clampInt0to5(2 + Math.min(3, Math.floor(segments / 2)));
  } else {
    if (len >= 3500) evidence_strength = 5;
    else if (len >= 1800) evidence_strength = 4;
    else if (len >= 900) evidence_strength = 3;
    else if (len >= 300) evidence_strength = 2;
    else evidence_strength = 1;
    let bump = 0;
    if (paragraphBreaks >= 2) bump += 1;
    if (structuredUnits >= 2) bump += 1;
    if (sentenceEnds >= 4) bump += 1;
    evidence_strength = clampInt0to5(evidence_strength + bump);
  }

  // transferability: lane prior + “portable pattern” language
  let transferability = lane === "github" ? 4 : lane === "article" ? 3 : 2;
  transferability += Math.min(
    2,
    keywordHitCount(lc, ["pattern", "workflow", "framework", "reusable", "general-purpose", "portable", "library"])
  );
  if (len > 600) transferability += 1;
  transferability = clampInt0to5(transferability);

  // expected_upside
  const upsideHits = keywordHitCount(lc, [
    "improve",
    "faster",
    "speedup",
    "reduce cost",
    "scale",
    "optimize",
    "efficiency",
    "gain",
    "roi",
    "latency",
    "throughput",
  ]);
  let expected_upside = Math.min(3, upsideHits);
  expected_upside += len > 1200 ? 2 : len > 400 ? 1 : 0;
  expected_upside = clampInt0to5(expected_upside);

  // risk_reduction_value
  const riskHits = keywordHitCount(lc, [
    "risk",
    "mitigate",
    "hedge",
    "safety",
    "control",
    "audit",
    "compliance",
    "incident",
    "loss",
    "drawdown",
    "failure mode",
  ]);
  let risk_reduction_value = Math.min(4, riskHits);
  if (sentenceEnds >= 3) risk_reduction_value += 1;
  risk_reduction_value = clampInt0to5(risk_reduction_value);

  // implementation_cost: higher = more expensive (engine inverts in formula)
  let implementation_cost = lane === "x_post" ? 3 : 2;
  implementation_cost += Math.min(
    3,
    keywordHitCount(lc, ["kubernetes", "microservice", "rewrite", "legacy", "migration", "multi-team", "enterprise"])
  );
  if (structuredUnits >= 4) implementation_cost += 1;
  implementation_cost = clampInt0to5(implementation_cost);

  // novelty
  let novelty = lane === "x_post" ? 1 : 2;
  novelty += Math.min(
    3,
    keywordHitCount(lc, ["novel", "new approach", "first ", "state of the art", "sota", "unpublished", "breakthrough"])
  );
  if (len < 120 && lane !== "github") novelty -= 1;
  novelty = clampInt0to5(novelty);

  // dependency_burden: higher = heavier deps (engine inverts)
  let dependency_burden = lane === "github" ? 2 : 1;
  dependency_burden += Math.min(
    3,
    keywordHitCount(lc, ["dependency", "dependencies", "npm", "pip", "docker", "terraform", "cloud", "aws", "grpc"])
  );
  if (lane === "github" && (text.match(/\//g) ?? []).length >= 5) dependency_burden += 1;
  dependency_burden = clampInt0to5(dependency_burden);

  // confidence: faith in adapter/heuristic coverage given volume + structure (not model certainty)
  let confidence = 1;
  confidence += len > 2000 ? 2 : len > 800 ? 1 : 0;
  if (paragraphBreaks >= 1) confidence += 1;
  if (lane === "github") confidence += 1;
  confidence = clampInt0to5(confidence);

  return {
    confidence,
    evidence_strength,
    transferability,
    expected_upside,
    risk_reduction_value,
    implementation_cost,
    novelty,
    dependency_burden,
  };
}

/** Mirrors `compute_weighted_score` in `foundry_registry_engine.py` (unchanged formula). */
export function computeIntakeWeightedScorePreview(dims: IntakeHeuristicDimensions): number {
  const rawSum =
    dims.evidence_strength * 0.22 +
    dims.transferability * 0.18 +
    dims.expected_upside * 0.16 +
    dims.risk_reduction_value * 0.14 +
    (5 - dims.implementation_cost) * 0.1 +
    dims.novelty * 0.08 +
    (5 - dims.dependency_burden) * 0.07 +
    dims.confidence * 0.05;
  return Math.round((rawSum / 5) * 100 * 10000) / 10000;
}

function weightedScoreFromCandidateRecord(candidate: Record<string, unknown>): number | undefined {
  const keys = [
    "evidence_strength",
    "transferability",
    "expected_upside",
    "risk_reduction_value",
    "implementation_cost",
    "novelty",
    "dependency_burden",
    "confidence",
  ] as const;
  const dims: Partial<IntakeHeuristicDimensions> = {};
  for (const k of keys) {
    const v = candidate[k];
    if (typeof v !== "number" || !Number.isInteger(v)) return undefined;
    dims[k] = v;
  }
  return computeIntakeWeightedScorePreview(dims as IntakeHeuristicDimensions);
}

function buildInputPacket(lane: FoundryLane, rawInput: string): {
  source_record: Record<string, unknown>;
  candidate_ideas: Array<Record<string, unknown>>;
  sourceId: string;
  candidateId: string;
} {
  const runId = runIdToken();
  const createdAt = nowIso();
  const sourceId = `src_${lane}_${runId}`;
  const candidateId = `cand_${lane}_${runId}_001`;
  const title = makeCandidateTitle(lane, rawInput);
  const { source_type } = laneMeta(lane);
  const rawSummary = rawInput.trim().slice(0, 280);
  const scores = deriveIntakeHeuristicScores(lane, rawInput);

  const source_record = {
    source_id: sourceId,
    source_type,
    source_lane: lane,
    input_mode: "dashboard_manual_intake",
    title,
    raw_input_ref: `inline:${sourceId}`,
    processed_output_ref: `foundry://bounded_local_extraction/${sourceId}`,
    source_url_or_locator: lane === "github" ? rawInput.trim() : `inline://${sourceId}`,
    source_hash: `hash_${normalize(rawInput).slice(0, 24)}`,
    ingestion_method: "dashboard_form_submit",
    source_timestamp: createdAt,
    created_at: createdAt,
    reviewer_model: "bounded_local_adapter_v1",
    review_version: "v1",
    extraction_version: "v1",
    review_status: "complete",
    extraction_status: "complete",
    review_summary: rawSummary || "No summary extracted.",
    key_claims: [rawSummary || "No claim extracted."],
    quality_flags: [
      "bounded_local_extraction_v1",
      "deterministic_keyword_heuristic_scores_v1",
      "needs_validation",
    ],
    processing_notes:
      "Deterministic local intake: candidate text fields from raw input; eight scoring dimensions from bounded keyword/length/structure heuristic (not LLM, not semantic truth).",
    candidate_ids: [candidateId],
  };

  const candidate_ideas = [
    {
      candidate_id: candidateId,
      source_id: sourceId,
      source_lane: lane,
      title,
      summary: rawSummary || "No summary extracted.",
      category: lane === "github" ? "tooling" : "research_method",
      claim: rawSummary || "No claim extracted.",
      implementation_implication:
        "Bounded local candidate extracted from intake input; requires operator review before promotion decisions.",
      problem_solved: "Transforms raw intake into structured candidate for registry review.",
      proposed_pattern: "Intake -> deterministic adapter -> local registry engine -> review page.",
      idea_kind: lane === "github" ? "tooling" : "workflow",
      confidence: scores.confidence,
      evidence_strength: scores.evidence_strength,
      transferability: scores.transferability,
      expected_upside: scores.expected_upside,
      risk_reduction_value: scores.risk_reduction_value,
      implementation_cost: scores.implementation_cost,
      novelty: scores.novelty,
      dependency_burden: scores.dependency_burden,
      needs_validation: true,
      verification_gaps: ["bounded_local_extraction", "source_needs_manual_review"],
      duplicate_group_key: normalize(`${lane}_${title}`) || `${lane}_candidate`,
      dedupe_confidence: 0.5,
      registry_match_id: "",
      recommendation_state: "watchlist",
      recommendation_reason: "seed_value_will_be_overwritten_by_engine",
      extraction_method: "bounded_local_adapter_v1",
      created_at: createdAt,
    },
  ];

  return { source_record, candidate_ideas, sourceId, candidateId };
}

async function readJson<T>(path: string): Promise<T> {
  return JSON.parse(await readFile(path, "utf-8")) as T;
}

export async function getTopIdeasForLane(lane: FoundryLane): Promise<FoundryTopIdea[]> {
  const stateRoot = foundryStateRoot();
  const registryDir = join(stateRoot, "registry_ideas");
  const sourceDir = join(stateRoot, "source_records");
  const sourceLaneById = new Map<string, FoundryLane>();

  try {
    const sourceFiles = await readdir(sourceDir);
    for (const file of sourceFiles.filter((f) => f.endsWith(".json"))) {
      try {
        const item = await readJson<Record<string, unknown>>(join(sourceDir, file));
        if (typeof item.source_id === "string" && (item.source_lane === "article" || item.source_lane === "github" || item.source_lane === "x_post")) {
          sourceLaneById.set(item.source_id, item.source_lane);
        }
      } catch {
        // Ignore malformed source files for top-10 view.
      }
    }
  } catch {
    return [];
  }

  const rows: FoundryTopIdea[] = [];
  try {
    const registryFiles = await readdir(registryDir);
    for (const file of registryFiles.filter((f) => f.endsWith(".json"))) {
      try {
        const idea = await readJson<FoundryRegistryIdea>(join(registryDir, file));
        const ideaLanes = new Set(
          (idea.source_refs ?? [])
            .map((sourceId) => sourceLaneById.get(sourceId))
            .filter((v): v is FoundryLane => Boolean(v))
        );
        if (!ideaLanes.has(lane)) continue;
        rows.push({
          idea_id: idea.idea_id,
          title: idea.title,
          category: idea.category,
          status: idea.status,
          weighted_score: idea.weighted_score,
          supporting_source_count: idea.supporting_source_count,
          confidence: idea.confidence,
          expected_upside: idea.expected_upside,
          implementation_cost: idea.implementation_cost,
          risk_reduction_value: idea.risk_reduction_value,
          last_updated: idea.last_updated,
        });
      } catch {
        // Ignore malformed registry files for top-10 view.
      }
    }
  } catch {
    return [];
  }

  return rows.sort((a, b) => b.weighted_score - a.weighted_score).slice(0, 10);
}

export async function runFoundryLaneIntake(lane: FoundryLane, input: string): Promise<FoundryIntakeResult> {
  const validationError = validateInput(lane, input);
  if (validationError) {
    throw new Error(validationError);
  }

  const stateRoot = foundryStateRoot();
  const packetDir = join(stateRoot, "indexes", "intake_packets");
  await mkdir(packetDir, { recursive: true });

  const { source_record, candidate_ideas, sourceId, candidateId } = buildInputPacket(lane, input);
  const packet = { source_record, candidate_ideas };
  const runId = runIdToken();
  const packetPath = join(packetDir, `intake_${lane}_${runId}.json`);
  await writeFile(packetPath, JSON.stringify(packet, null, 2) + "\n", "utf-8");

  const scriptPath = join(workspaceRoot(), "future_modules", "the_foundry", "scripts", "run_foundry_registry_engine.py");
  try {
    await execFileAsync(
      "py",
      ["-3", scriptPath, "--input", packetPath, "--workspace-root", workspaceRoot()],
      { cwd: workspaceRoot() }
    );
  } catch (error) {
    const reason = error instanceof Error ? error.message : "Unknown engine invocation failure.";
    throw new Error(`Foundry engine run failed: ${reason}`);
  }

  const manifestPath = join(stateRoot, "indexes", "foundry_registry_manifest.json");
  const manifest = await readJson<{ run_id: string; output_paths: Record<string, string> }>(manifestPath);
  const sourceRecordPath = join(workspaceRoot(), manifest.output_paths.source_record);
  const candidatePath = join(stateRoot, "candidate_ideas", `${candidateId}.json`);

  const writtenSourceRecord = await readJson<Record<string, unknown>>(sourceRecordPath);
  const writtenCandidate = await readJson<Record<string, unknown>>(candidatePath);
  const previewScore = weightedScoreFromCandidateRecord(writtenCandidate);
  const candidateForResponse =
    previewScore !== undefined ? { ...writtenCandidate, weighted_score: previewScore } : writtenCandidate;
  const top10 = await getTopIdeasForLane(lane);

  return {
    status: "success",
    lane,
    run_id: manifest.run_id,
    limitation_note:
      "Scores use a bounded deterministic heuristic (length, lane, bullets, simple keyword families). Same input → same numbers. Not semantic ranking; operator review still required.",
    source_record: writtenSourceRecord,
    candidate_ideas: [candidateForResponse],
    output_paths: {
      intake_packet: packetPath.replace(/\\/g, "/"),
      source_record: sourceRecordPath.replace(/\\/g, "/"),
      candidate_idea: candidatePath.replace(/\\/g, "/"),
      manifest: manifestPath.replace(/\\/g, "/"),
    },
    top_10_lane_ideas: top10,
  };
}
