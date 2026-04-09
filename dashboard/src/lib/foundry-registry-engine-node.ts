/**
 * Server-only: mirrors `run_engine` in `future_modules/the_foundry/engine/foundry_registry_engine.py`
 * (weighted score, dedupe, gates, caps, registry + queue writes) via FoundryStorage.
 */

import type { FoundryStorage } from "./foundry-storage";
import { foundryBlobPrefixes } from "./foundry-storage";

export class FoundryEngineError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "FoundryEngineError";
  }
}

const SOURCE_TYPE_ENUM = new Set(["article_text", "github_repo", "x_post_brief"]);
const SOURCE_LANE_ENUM = new Set(["article", "github", "x_post"]);
const REVIEW_STATUS_ENUM = new Set(["pending", "complete", "failed", "escalated"]);
const EXTRACTION_STATUS_ENUM = new Set(["not_started", "complete", "failed", "escalated"]);
const IDEA_KIND_ENUM = new Set([
  "pattern",
  "workflow",
  "component",
  "control",
  "architecture",
  "research_method",
  "data_method",
  "tooling",
]);
const RECOMMENDATION_ENUM = new Set([
  "discard",
  "watchlist",
  "research_next",
  "implement_soon",
  "queue_candidate",
]);

function utcNow(): string {
  return new Date().toISOString();
}

function normalizeText(value: string): string {
  return value.trim().toLowerCase().replace(/\s+/g, " ");
}

function isMissingOrVague(value: unknown): boolean {
  if (typeof value !== "string") return true;
  const cleaned = normalizeText(value);
  if (cleaned.length < 20) return true;
  const vagueMarkers = new Set(["tbd", "todo", "unclear", "unknown", "n/a", "none", "later"]);
  return vagueMarkers.has(cleaned);
}

function isIntegerScore(value: unknown): boolean {
  return typeof value === "number" && Number.isInteger(value) && value >= 0 && value <= 5;
}

function validateRequiredFields(record: Record<string, unknown>, requiredFields: string[], objectName: string): void {
  const missing = requiredFields.filter((field) => !(field in record));
  if (missing.length) {
    throw new FoundryEngineError(`${objectName} missing required fields: ${missing.join(", ")}`);
  }
}

function validateEnum(value: string, allowed: Set<string>, fieldName: string): void {
  if (!allowed.has(value)) {
    throw new FoundryEngineError(`Invalid enum value for ${fieldName}: ${JSON.stringify(value)}`);
  }
}

function validateScoreFields(candidate: Record<string, unknown>): void {
  const scoreFields = [
    "evidence_strength",
    "transferability",
    "expected_upside",
    "risk_reduction_value",
    "implementation_cost",
    "novelty",
    "dependency_burden",
    "confidence",
  ] as const;
  const badFields = scoreFields.filter((field) => !isIntegerScore(candidate[field]));
  if (badFields.length) {
    throw new FoundryEngineError(
      `Candidate ${String(candidate.candidate_id ?? "<unknown>")} has invalid 0-5 integer scoring fields: ${badFields.join(", ")}`
    );
  }
}

interface DedupeResult {
  status: string;
  reason: string;
  registry_match_id: string;
}

function computeWeightedScore(candidate: Record<string, unknown>): { weightedScore: number; breakdown: Record<string, number> } {
  const weightedTerms: Record<string, number> = {
    evidence_strength: (candidate.evidence_strength as number) * 0.22,
    transferability: (candidate.transferability as number) * 0.18,
    expected_upside: (candidate.expected_upside as number) * 0.16,
    risk_reduction_value: (candidate.risk_reduction_value as number) * 0.14,
    implementation_cost_inverted: (5 - (candidate.implementation_cost as number)) * 0.1,
    novelty: (candidate.novelty as number) * 0.08,
    dependency_burden_inverted: (5 - (candidate.dependency_burden as number)) * 0.07,
    confidence: (candidate.confidence as number) * 0.05,
  };
  const rawSum = Object.values(weightedTerms).reduce((a, b) => a + b, 0);
  let weightedScore = (rawSum / 5) * 100;
  weightedScore = Math.round(weightedScore * 10000) / 10000;
  weightedTerms.raw_sum = Math.round(rawSum * 10000) / 10000;
  weightedTerms.weighted_score = weightedScore;
  return { weightedScore, breakdown: weightedTerms };
}

function dedupeCandidate(candidate: Record<string, unknown>, registryIdeas: Record<string, unknown>[]): DedupeResult {
  const duplicateGroupKey = candidate.duplicate_group_key;
  if (typeof duplicateGroupKey !== "string" || !duplicateGroupKey.trim()) {
    return { status: "needs_review", reason: "duplicate_group_key missing or blank", registry_match_id: "" };
  }

  const titleSig = normalizeText(String(candidate.title ?? ""));
  const categorySig = normalizeText(String(candidate.category ?? ""));
  const problemSig = normalizeText(String(candidate.problem_solved ?? ""));
  const patternSig = normalizeText(String(candidate.proposed_pattern ?? ""));

  if (!titleSig || !categorySig || !problemSig || !patternSig) {
    return { status: "needs_review", reason: "signature fields incomplete for deterministic dedupe", registry_match_id: "" };
  }

  const signature = `${titleSig}|${categorySig}|${problemSig}|${patternSig}`;
  const groupKey = normalizeText(duplicateGroupKey);

  for (const idea of registryIdeas) {
    if (normalizeText(String(idea.dedupe_key ?? "")) === groupKey) {
      return { status: "match", reason: "matched dedupe_key", registry_match_id: String(idea.idea_id ?? "") };
    }
  }

  for (const idea of registryIdeas) {
    const ideaSignature = `${normalizeText(String(idea.title ?? ""))}|${normalizeText(String(idea.category ?? ""))}|${normalizeText(String(idea.canonical_problem ?? ""))}|${normalizeText(String(idea.canonical_pattern ?? ""))}`;
    if (ideaSignature === signature) {
      return { status: "match", reason: "matched title/category/problem/pattern signature", registry_match_id: String(idea.idea_id ?? "") };
    }
  }

  if (groupKey.length < 6) {
    return { status: "needs_review", reason: "duplicate_group_key too weak for deterministic confidence", registry_match_id: "" };
  }
  return { status: "no_match", reason: "no deterministic match found", registry_match_id: "" };
}

function gateFailures(candidate: Record<string, unknown>, dedupe: DedupeResult): string[] {
  const failures: string[] = [];
  if ((candidate.evidence_strength as number) < 2) failures.push("evidence_strength_below_2");
  if ((candidate.transferability as number) < 2) failures.push("transferability_below_2");
  if (isMissingOrVague(candidate.implementation_implication)) failures.push("implementation_implication_missing_or_vague");
  if (dedupe.status === "needs_review") failures.push("dedupe_incomplete");
  return failures;
}

function antiHypeReasons(candidate: Record<string, unknown>, dedupe: DedupeResult): string[] {
  const reasons = new Set<string>();
  const claim = normalizeText(String(candidate.claim ?? ""));
  const summary = normalizeText(String(candidate.summary ?? ""));
  const vg = candidate.verification_gaps;
  const qualityNotes =
    Array.isArray(vg) && vg.every((x) => typeof x === "string") ? (vg as string[]).join(" ") : "";
  const noise = normalizeText(qualityNotes);

  if (claim.includes("hype") || summary.includes("hype")) reasons.add("mostly_hype");
  if (candidate.idea_kind === "tooling" && normalizeText(String(candidate.proposed_pattern ?? "")).length < 20) {
    reasons.add("bare_tool_mention");
  }
  if (isMissingOrVague(candidate.proposed_pattern)) reasons.add("unclear_method");
  if (dedupe.status === "needs_review") reasons.add("unresolved_duplicate");
  const weakNoiseMarkers = ["weak_source", "low_signal", "noisy"];
  if (weakNoiseMarkers.some((m) => noise.includes(m))) reasons.add("weak_source_quality_noise");
  return Array.from(reasons).sort();
}

function recommendationFromScore(score: number): string {
  if (score < 35) return "discard";
  if (score <= 49) return "watchlist";
  if (score <= 64) return "research_next";
  if (score <= 79) return "implement_soon";
  return "queue_candidate";
}

function enforceCaps(
  baseRecommendation: string,
  gateFailuresList: string[],
  antiHypeList: string[]
): { result: string; applied: string[] } {
  const applied: string[] = [];
  let result = baseRecommendation;

  const severeGateFailure = gateFailuresList.some((f) =>
    ["implementation_implication_missing_or_vague", "dedupe_incomplete"].includes(f)
  );
  if (severeGateFailure) {
    result = "discard";
    applied.push("severe_gate_failure_to_discard");
    return { result, applied };
  }

  if (gateFailuresList.length && !["discard", "watchlist"].includes(result)) {
    result = "watchlist";
    applied.push("hard_gate_cap_watchlist");
  }

  if (antiHypeList.length && !["discard", "watchlist"].includes(result)) {
    result = "watchlist";
    applied.push("anti_hype_cap_watchlist");
  }

  return { result, applied };
}

function mapRecommendationToRegistryStatus(recommendation: string): string {
  const m: Record<string, string> = {
    discard: "rejected",
    watchlist: "watchlist",
    research_next: "research_next",
    implement_soon: "implement_soon",
    queue_candidate: "queued",
  };
  return m[recommendation] ?? "watchlist";
}

const SOURCE_REQUIRED_FIELDS = [
  "source_id",
  "source_type",
  "source_lane",
  "input_mode",
  "title",
  "raw_input_ref",
  "processed_output_ref",
  "source_url_or_locator",
  "source_hash",
  "ingestion_method",
  "source_timestamp",
  "created_at",
  "reviewer_model",
  "review_version",
  "extraction_version",
  "review_status",
  "extraction_status",
  "review_summary",
  "key_claims",
  "quality_flags",
  "processing_notes",
  "candidate_ids",
] as const;

const CANDIDATE_REQUIRED_FIELDS = [
  "candidate_id",
  "source_id",
  "source_lane",
  "title",
  "summary",
  "category",
  "claim",
  "implementation_implication",
  "problem_solved",
  "proposed_pattern",
  "idea_kind",
  "confidence",
  "evidence_strength",
  "transferability",
  "expected_upside",
  "risk_reduction_value",
  "implementation_cost",
  "novelty",
  "dependency_burden",
  "needs_validation",
  "verification_gaps",
  "duplicate_group_key",
  "dedupe_confidence",
  "registry_match_id",
  "recommendation_state",
  "recommendation_reason",
  "extraction_method",
  "created_at",
] as const;

function pickFields(record: Record<string, unknown>, allowedFields: readonly string[]): Record<string, unknown> {
  const out: Record<string, unknown> = {};
  for (const field of allowedFields) {
    out[field] = record[field];
  }
  return out;
}

function validateSourceRecord(source: Record<string, unknown>): void {
  validateRequiredFields(source, [...SOURCE_REQUIRED_FIELDS], "Source Record");
  validateEnum(source.source_type as string, SOURCE_TYPE_ENUM, "source_type");
  validateEnum(source.source_lane as string, SOURCE_LANE_ENUM, "source_lane");
  validateEnum(source.review_status as string, REVIEW_STATUS_ENUM, "review_status");
  validateEnum(source.extraction_status as string, EXTRACTION_STATUS_ENUM, "extraction_status");
}

function validateCandidateIdea(candidate: Record<string, unknown>): void {
  validateRequiredFields(candidate, [...CANDIDATE_REQUIRED_FIELDS], "Candidate Idea");
  validateEnum(candidate.source_lane as string, SOURCE_LANE_ENUM, "source_lane");
  validateEnum(candidate.idea_kind as string, IDEA_KIND_ENUM, "idea_kind");
  validateEnum(candidate.recommendation_state as string, RECOMMENDATION_ENUM, "recommendation_state");
  validateScoreFields(candidate);
  const dc = candidate.dedupe_confidence;
  if (typeof dc !== "number" || dc < 0 || dc > 1) {
    throw new FoundryEngineError(
      `Candidate ${String(candidate.candidate_id ?? "<unknown>")} has invalid dedupe_confidence (expected 0..1 number).`
    );
  }
}

function buildRegistryIdea(
  candidate: Record<string, unknown>,
  weightedScore: number,
  breakdown: Record<string, number>,
  recommendation: string
): Record<string, unknown> {
  const now = utcNow();
  return {
    idea_id: `idea_${String(candidate.candidate_id)}`,
    title: candidate.title,
    summary: candidate.summary,
    category: candidate.category,
    canonical_problem: candidate.problem_solved,
    canonical_pattern: candidate.proposed_pattern,
    dedupe_key: candidate.duplicate_group_key,
    source_refs: [candidate.source_id],
    supporting_source_count: 1,
    contradicting_source_count: 0,
    confidence: candidate.confidence,
    evidence_strength: candidate.evidence_strength,
    transferability: candidate.transferability,
    expected_upside: candidate.expected_upside,
    risk_reduction_value: candidate.risk_reduction_value,
    implementation_cost: candidate.implementation_cost,
    novelty: candidate.novelty,
    dependency_burden: candidate.dependency_burden,
    score_breakdown: breakdown,
    weighted_score: weightedScore,
    status: mapRecommendationToRegistryStatus(recommendation),
    review_state: "pending_review",
    promotion_reason: candidate.recommendation_reason,
    review_notes: "",
    implementation_notes: "",
    dependencies: [],
    related_ideas: [],
    queue_eligibility: recommendation === "queue_candidate",
    queue_reason: recommendation === "queue_candidate" ? "eligible_by_score_and_gates" : "not_queue_candidate",
    first_seen_at: candidate.created_at,
    created_at: now,
    last_updated: now,
  };
}

function buildQueueItem(registryIdea: Record<string, unknown>, queueRank: number): Record<string, unknown> {
  const now = utcNow();
  const ws = registryIdea.weighted_score as number;
  return {
    queue_id: `queue_${String(registryIdea.idea_id)}`,
    idea_id: registryIdea.idea_id,
    queue_rank: queueRank,
    priority_band: ws >= 90 ? "high" : "medium",
    why_now: "Scored 80+ with all hard gates passed.",
    required_resources: [],
    expected_build_output: "Design/build plan for approved registry idea",
    owner: "unassigned",
    operator_approval_state: "pending",
    approval_notes: "",
    target_module: "stock_module",
    effort_estimate: "tbd",
    dependency_status: "unknown",
    source_confidence_snapshot: Number(registryIdea.confidence),
    success_criteria: ["Operator confirms design intent and acceptance criteria."],
    next_action: "Operator review",
    status: "proposed",
    blockers: [],
    created_at: now,
    last_updated: now,
  };
}

function engineRunId(): string {
  const d = new Date();
  const y = d.getUTCFullYear();
  const m = String(d.getUTCMonth() + 1).padStart(2, "0");
  const day = String(d.getUTCDate()).padStart(2, "0");
  const h = String(d.getUTCHours()).padStart(2, "0");
  const min = String(d.getUTCMinutes()).padStart(2, "0");
  const s = String(d.getUTCSeconds()).padStart(2, "0");
  return `${y}${m}${day}T${h}${min}${s}Z`;
}

export interface FoundryEngineManifest {
  run_id: string;
  source_id: string;
  counts: {
    candidate_ideas: number;
    registry_ideas_generated: number;
    queue_recommendations_generated: number;
  };
  output_paths: Record<string, string>;
}

export async function runFoundryRegistryEngineNode(
  wsRoot: string,
  payload: { source_record: Record<string, unknown>; candidate_ideas: Record<string, unknown>[] },
  store: FoundryStorage
): Promise<FoundryEngineManifest> {
  const sourceRecord = payload.source_record;
  const candidateIdeas = payload.candidate_ideas;
  if (!sourceRecord || typeof sourceRecord !== "object") {
    throw new FoundryEngineError("Input must include object field `source_record`.");
  }
  if (!Array.isArray(candidateIdeas) || !candidateIdeas.every((item) => item && typeof item === "object")) {
    throw new FoundryEngineError("Input must include array field `candidate_ideas` of objects.");
  }

  validateSourceRecord(sourceRecord);
  const expectedIds = candidateIdeas.map((c) => c.candidate_id);
  if (JSON.stringify(sourceRecord.candidate_ids) !== JSON.stringify(expectedIds)) {
    throw new FoundryEngineError("source_record.candidate_ids must exactly match candidate_ideas[].candidate_id order.");
  }

  const regKeys = await store.listJsonKeys(foundryBlobPrefixes.registryIdeas);
  const existingRegistry: Record<string, unknown>[] = [];
  for (const key of regKeys) {
    const loaded = await store.getJson<Record<string, unknown>>(key);
    if (loaded && typeof loaded === "object") existingRegistry.push(loaded);
  }

  const processedCandidates: Record<string, unknown>[] = [];
  const generatedRegistry: Record<string, unknown>[] = [];
  const generatedQueue: Record<string, unknown>[] = [];
  const candidateAssessments: Record<string, unknown>[] = [];

  for (const candidate of candidateIdeas) {
    validateCandidateIdea(candidate);
    if (candidate.source_id !== sourceRecord.source_id) {
      throw new FoundryEngineError(
        `Candidate ${String(candidate.candidate_id)} source_id mismatch vs source_record.source_id.`
      );
    }

    const { weightedScore, breakdown } = computeWeightedScore(candidate);
    const dedupe = dedupeCandidate(candidate, [...existingRegistry, ...generatedRegistry]);
    const failures = gateFailures(candidate, dedupe);
    const hype = antiHypeReasons(candidate, dedupe);
    const base = recommendationFromScore(weightedScore);
    const { result: recommendation, applied: caps } = enforceCaps(base, failures, hype);

    const reasonParts = [`base=${base}`, `score=${weightedScore}`, `dedupe=${dedupe.status}`];
    if (failures.length) reasonParts.push(`gate_failures=${failures.join(",")}`);
    if (hype.length) reasonParts.push(`anti_hype=${hype.join(",")}`);
    if (caps.length) reasonParts.push(`caps=${caps.join(",")}`);

    const candidateClean = pickFields(candidate, CANDIDATE_REQUIRED_FIELDS) as Record<string, unknown>;
    candidateClean.recommendation_state = recommendation;
    candidateClean.recommendation_reason = reasonParts.join(" | ");
    candidateClean.registry_match_id = dedupe.registry_match_id;
    processedCandidates.push(candidateClean);

    candidateAssessments.push({
      candidate_id: candidate.candidate_id,
      weighted_score: weightedScore,
      score_breakdown: breakdown,
      dedupe_result: {
        status: dedupe.status,
        reason: dedupe.reason,
        registry_match_id: dedupe.registry_match_id,
      },
      gate_failures: failures,
      anti_hype_reasons: hype,
      base_recommendation: base,
      final_recommendation: recommendation,
      caps_applied: caps,
    });

    const registryIdea = buildRegistryIdea(candidateClean, weightedScore, breakdown, recommendation);
    generatedRegistry.push(registryIdea);
    if (recommendation === "queue_candidate" && !failures.length && !hype.length) {
      generatedQueue.push(buildQueueItem(registryIdea, generatedQueue.length + 1));
    }
  }

  const srcId = String(sourceRecord.source_id);
  await store.putJson(`${foundryBlobPrefixes.sourceRecords}${srcId}.json`, sourceRecord);

  for (const c of processedCandidates) {
    await store.putJson(`${foundryBlobPrefixes.candidateIdeas}${String(c.candidate_id)}.json`, c);
  }

  for (const reg of generatedRegistry) {
    await store.putJson(`${foundryBlobPrefixes.registryIdeas}${String(reg.idea_id)}.json`, reg);
  }

  const runId = engineRunId();
  const queueKey = `${foundryBlobPrefixes.queueRecommendations}queue_recommendations_${runId}.json`;
  await store.putJson(queueKey, { run_id: runId, items: generatedQueue });

  const assessmentKey = `${foundryBlobPrefixes.indexes}candidate_assessments_${runId}.json`;
  await store.putJson(assessmentKey, { run_id: runId, items: candidateAssessments });

  const stateRel = "future_modules/the_foundry/state";
  const sourceRelPath = `${stateRel}/source_records/${srcId}.json`;
  const manifest: FoundryEngineManifest = {
    run_id: runId,
    source_id: srcId,
    counts: {
      candidate_ideas: processedCandidates.length,
      registry_ideas_generated: generatedRegistry.length,
      queue_recommendations_generated: generatedQueue.length,
    },
    output_paths: {
      source_record: sourceRelPath,
      candidate_ideas_dir: `${stateRel}/candidate_ideas`,
      registry_ideas_dir: `${stateRel}/registry_ideas`,
      queue_recommendation_file: `${stateRel}/queue_recommendations/queue_recommendations_${runId}.json`,
      candidate_assessment_file: `${stateRel}/indexes/candidate_assessments_${runId}.json`,
    },
  };

  const manifestKey = `${foundryBlobPrefixes.indexes}foundry_registry_manifest.json`;
  await store.putJson(manifestKey, manifest);

  void wsRoot;
  return manifest;
}
