import { readFile, writeFile, mkdir } from "fs/promises";
import { join } from "path";
import { execFile } from "child_process";
import { promisify } from "util";
import {
  createFoundryStorage,
  foundryBlobPrefixes,
  foundryStateRoot,
  foundryUsesNodeEngine,
  workspaceRoot,
} from "@/lib/foundry-storage";
import { runFoundryRegistryEngineNode } from "@/lib/foundry-registry-engine-node";
import { loadMergedRegistryIdeas, loadMergedSourceLaneBySourceId } from "@/lib/foundry-read-merge";
import {
  buildManualAudit,
  computeIntakeWeightedScorePreview,
  deriveBoundedRubricProposal,
  deriveHeuristicPrefillAudit,
  type FoundryScoringMode,
  type IntakeHeuristicDimensions,
  validateManualRubricScores,
  type FoundryScoringEvaluation,
} from "@/lib/foundry-scoring";
import { RUBRIC_KEYS, type FoundryLane } from "@/lib/foundry-rubric-anchors";
import { writeScoringEvaluationSidecar } from "@/lib/foundry-scoring-persistence";

const execFileAsync = promisify(execFile);

export type { FoundryLane };

export type { FoundryScoringMode, IntakeHeuristicDimensions };
export { deriveIntakeHeuristicScores, computeIntakeWeightedScorePreview } from "@/lib/foundry-scoring";

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

export interface FoundryIntakeScoringEvaluationPayload {
  evaluation_id: string;
  scoring_mode_selected: FoundryScoringMode;
  evaluation_method: string;
  final_scores: IntakeHeuristicDimensions;
  heuristic_prefill_scores: IntakeHeuristicDimensions | null;
  proposed_scores: IntakeHeuristicDimensions | null;
  score_reasons: Record<string, string> | null;
  evidence_support: Record<string, string> | null;
  weighted_score: number;
  sidecar_path: string;
  /** Explicit rubric matrix version for Option A proposals. */
  rubric_anchor_version?: string;
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
  scoring_evaluation: FoundryIntakeScoringEvaluationPayload;
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

export function validateFoundryIntakeInput(lane: FoundryLane, input: string): string | null {
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

/** Pure preview for Option A: heuristic prefill + explicit-anchor proposal (no engine I/O). */
export function buildFoundryOptionAPreview(lane: FoundryLane, input: string): {
  status: "success";
  lane: FoundryLane;
  rubric_anchor_version: string;
  proposal_evaluation_method: string;
  heuristic_prefill_scores: IntakeHeuristicDimensions;
  proposed_scores: IntakeHeuristicDimensions;
  score_reasons: Record<string, string>;
  evidence_support: Record<string, string>;
} {
  const err = validateFoundryIntakeInput(lane, input);
  if (err) {
    throw new Error(err);
  }
  const prefill = deriveHeuristicPrefillAudit(lane, input);
  const proposal = deriveBoundedRubricProposal(lane, input);
  return {
    status: "success",
    lane,
    rubric_anchor_version: proposal.anchor_version,
    proposal_evaluation_method: proposal.evaluation_method,
    heuristic_prefill_scores: prefill.final_scores,
    proposed_scores: proposal.proposed_scores,
    score_reasons: proposal.score_reasons,
    evidence_support: proposal.evidence_support,
  };
}

function makeCandidateTitle(lane: FoundryLane, input: string): string {
  const trimmed = input.trim();
  if (lane === "github") return `GitHub pattern from ${trimmed.replace(/^https?:\/\//i, "")}`;
  return trimmed.split(/\s+/).slice(0, 8).join(" ");
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

function buildInputPacket(
  lane: FoundryLane,
  rawInput: string,
  finalScores: IntakeHeuristicDimensions,
  mode: FoundryScoringMode
): {
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

  const quality_flags =
    mode === "option_b_manual_matrix"
      ? ["bounded_local_extraction_v1", "operator_manual_rubric_matrix_v1", "needs_validation"]
      : [
          "bounded_local_extraction_v1",
          "deterministic_rubric_assisted_v1",
          "deterministic_keyword_heuristic_scores_v1",
          "needs_validation",
        ];

  const processing_notes =
    mode === "option_b_manual_matrix"
      ? "Operator supplied eight rubric integers (Option B); engine applies locked weighted formula only."
      : "Option A: deterministic rubric-assisted scoring (length/lane/structure/keyword families) with per-dimension audit strings; not semantic truth.";

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
    reviewer_model: mode === "option_b_manual_matrix" ? "operator_manual_rubric_v1" : "bounded_rubric_assisted_adapter_v1",
    review_version: "v1",
    extraction_version: "v1",
    review_status: "complete",
    extraction_status: "complete",
    review_summary: rawSummary || "No summary extracted.",
    key_claims: [rawSummary || "No claim extracted."],
    quality_flags,
    processing_notes,
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
      confidence: finalScores.confidence,
      evidence_strength: finalScores.evidence_strength,
      transferability: finalScores.transferability,
      expected_upside: finalScores.expected_upside,
      risk_reduction_value: finalScores.risk_reduction_value,
      implementation_cost: finalScores.implementation_cost,
      novelty: finalScores.novelty,
      dependency_burden: finalScores.dependency_burden,
      needs_validation: true,
      verification_gaps: ["bounded_local_extraction", "source_needs_manual_review"],
      duplicate_group_key: normalize(`${lane}_${title}`) || `${lane}_candidate`,
      dedupe_confidence: 0.5,
      registry_match_id: "",
      recommendation_state: "watchlist",
      recommendation_reason: "seed_value_will_be_overwritten_by_engine",
      extraction_method:
        mode === "option_b_manual_matrix" ? "operator_manual_matrix_v1" : "deterministic_rubric_assisted_v1",
      created_at: createdAt,
    },
  ];

  return { source_record, candidate_ideas, sourceId, candidateId };
}

async function readJsonFile<T>(path: string): Promise<T | null> {
  try {
    return JSON.parse(await readFile(path, "utf-8")) as T;
  } catch {
    return null;
  }
}

export async function getTopIdeasForLane(lane: FoundryLane): Promise<FoundryTopIdea[]> {
  const store = await createFoundryStorage();
  const mergeErrors: string[] = [];
  const ideas = await loadMergedRegistryIdeas(store, mergeErrors);
  const sourceLaneBySourceId = await loadMergedSourceLaneBySourceId(store, mergeErrors);
  void mergeErrors;

  const rows: FoundryTopIdea[] = [];
  for (const idea of ideas) {
    const ideaLanes = new Set(
      (idea.source_refs ?? [])
        .map((sourceId) => sourceLaneBySourceId[sourceId])
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
  }

  return rows.sort((a, b) => b.weighted_score - a.weighted_score).slice(0, 10);
}

export interface RunFoundryLaneIntakeOptions {
  scoring_mode: FoundryScoringMode;
  manual_rubric_scores?: unknown;
  /** Option A: operator-locked 0..5 integers; omit to accept proposal exactly (smoke/tests only). */
  option_a_locked_rubric_scores?: unknown;
}

function toPayload(doc: FoundryScoringEvaluation, sidecarPath: string): FoundryIntakeScoringEvaluationPayload {
  return {
    evaluation_id: doc.evaluation_id,
    scoring_mode_selected: doc.scoring_mode_selected,
    evaluation_method: doc.evaluation_method,
    final_scores: doc.final_scores,
    heuristic_prefill_scores: doc.heuristic_prefill_scores,
    proposed_scores: doc.proposed_scores,
    score_reasons: doc.score_reasons,
    evidence_support: doc.evidence_support,
    weighted_score: doc.weighted_score,
    sidecar_path: sidecarPath,
    rubric_anchor_version: doc.rubric_anchor_version,
  };
}

export async function runFoundryLaneIntake(
  lane: FoundryLane,
  input: string,
  options: RunFoundryLaneIntakeOptions
): Promise<FoundryIntakeResult> {
  const validationError = validateFoundryIntakeInput(lane, input);
  if (validationError) {
    throw new Error(validationError);
  }

  const mode = options.scoring_mode;
  let finalScores: IntakeHeuristicDimensions;
  let heuristicPrefill: IntakeHeuristicDimensions | null = null;
  let proposed: IntakeHeuristicDimensions | null = null;
  let scoreReasons: FoundryScoringEvaluation["score_reasons"] = null;
  let evidenceSupport: FoundryScoringEvaluation["evidence_support"] = null;
  let evaluationMethod: string;
  let rubricAnchorVersion: string | undefined;

  if (mode === "option_a_rubric_assisted") {
    const prefillAudit = deriveHeuristicPrefillAudit(lane, input);
    heuristicPrefill = { ...prefillAudit.final_scores };

    const rubricProposal = deriveBoundedRubricProposal(lane, input);
    proposed = { ...rubricProposal.proposed_scores };
    rubricAnchorVersion = rubricProposal.anchor_version;

    const locked =
      options.option_a_locked_rubric_scores !== undefined
        ? validateManualRubricScores(options.option_a_locked_rubric_scores)
        : { ...rubricProposal.proposed_scores };

    finalScores = locked;
    scoreReasons = { ...rubricProposal.score_reasons };
    evidenceSupport = { ...rubricProposal.evidence_support };
    for (const k of RUBRIC_KEYS) {
      if (finalScores[k] !== rubricProposal.proposed_scores[k]) {
        scoreReasons[k] = `${rubricProposal.score_reasons[k]} | Operator locked at ${finalScores[k]} (proposed ${rubricProposal.proposed_scores[k]}).`;
      }
    }
    evaluationMethod = "bounded_explicit_rubric_anchor_operator_locked_v1";
  } else {
    if (options.manual_rubric_scores === undefined) {
      throw new Error("option_b_manual_matrix requires manual_rubric_scores (all eight integers 0..5).");
    }
    finalScores = validateManualRubricScores(options.manual_rubric_scores);
    heuristicPrefill = null;
    proposed = { ...finalScores };
    const manual = buildManualAudit();
    scoreReasons = manual.score_reasons;
    evidenceSupport = manual.evidence_support;
    evaluationMethod = "operator_manual_matrix_v1";
  }

  const store = await createFoundryStorage();
  const usedNode = foundryUsesNodeEngine();
  const stateRoot = foundryStateRoot();
  const wsRoot = workspaceRoot();

  const { source_record, candidate_ideas, sourceId, candidateId } = buildInputPacket(lane, input, finalScores, mode);
  const packet = { source_record, candidate_ideas };

  let manifest: { run_id: string; output_paths: Record<string, string> };
  let packetPathRel = "";
  const manifestPath = join(stateRoot, "indexes", "foundry_registry_manifest.json");

  if (usedNode) {
    manifest = await runFoundryRegistryEngineNode(wsRoot, packet, store);
  } else {
    const packetDir = join(stateRoot, "indexes", "intake_packets");
    await mkdir(packetDir, { recursive: true });
    const packetRunId = runIdToken();
    const packetPath = join(packetDir, `intake_${lane}_${packetRunId}.json`);
    packetPathRel = packetPath;
    await writeFile(packetPath, JSON.stringify(packet, null, 2) + "\n", "utf-8");

    const scriptPath = join(wsRoot, "future_modules", "the_foundry", "scripts", "run_foundry_registry_engine.py");
    try {
      await execFileAsync("py", ["-3", scriptPath, "--input", packetPath, "--workspace-root", wsRoot], {
        cwd: wsRoot,
      });
    } catch (error) {
      const reason = error instanceof Error ? error.message : "Unknown engine invocation failure.";
      throw new Error(`Foundry engine run failed: ${reason}`);
    }

    const fromDisk = await readJsonFile<{ run_id: string; output_paths: Record<string, string> }>(manifestPath);
    if (!fromDisk) {
      throw new Error("Foundry engine did not write manifest (foundry_registry_manifest.json).");
    }
    manifest = fromDisk;
  }

  const sourceRecordPath = join(wsRoot, manifest.output_paths.source_record);
  const candidatePath = join(stateRoot, "candidate_ideas", `${candidateId}.json`);

  const writtenSourceRecord =
    (await store.getJson<Record<string, unknown>>(`${foundryBlobPrefixes.sourceRecords}${sourceId}.json`)) ??
    (await readJsonFile<Record<string, unknown>>(sourceRecordPath));
  const writtenCandidate =
    (await store.getJson<Record<string, unknown>>(`${foundryBlobPrefixes.candidateIdeas}${candidateId}.json`)) ??
    (await readJsonFile<Record<string, unknown>>(candidatePath));

  if (!writtenSourceRecord || !writtenCandidate) {
    throw new Error("Foundry engine did not produce expected source/candidate records.");
  }

  const previewScore = weightedScoreFromCandidateRecord(writtenCandidate);
  const candidateForResponse =
    previewScore !== undefined ? { ...writtenCandidate, weighted_score: previewScore } : writtenCandidate;

  const { relativePath, evaluation } = await writeScoringEvaluationSidecar(
    {
      candidateId,
      sourceId,
      engineRunId: manifest.run_id,
      mode,
      heuristicPrefill,
      proposed,
      finalScores,
      scoreReasons,
      evidenceSupport,
      evaluationMethod,
      rubricAnchorVersion: mode === "option_a_rubric_assisted" ? rubricAnchorVersion : undefined,
    },
    store
  );

  const top10 = await getTopIdeasForLane(lane);

  const limitation_note =
    mode === "option_a_rubric_assisted"
      ? "Option A: explicit 0–5 rubric anchors → proposed scores + source-tied reasons/snippets; operator locks final integers before engine run. Heuristic prefill is separate (legacy buckets). Not semantic AI truth. Saved under scoring_evaluations/."
      : "Option B: operator manual rubric matrix (0–5 integers). Engine applies the locked weighted formula only. Mode and values saved under scoring_evaluations/. Human review still required.";

  return {
    status: "success",
    lane,
    run_id: manifest.run_id,
    limitation_note,
    source_record: writtenSourceRecord,
    candidate_ideas: [candidateForResponse],
    output_paths: {
      intake_packet: usedNode ? "(node-engine; no local packet file)" : packetPathRel.replace(/\\/g, "/"),
      source_record: sourceRecordPath.replace(/\\/g, "/"),
      candidate_idea: candidatePath.replace(/\\/g, "/"),
      manifest: manifestPath.replace(/\\/g, "/"),
      scoring_evaluation: relativePath.replace(/\\/g, "/"),
    },
    top_10_lane_ideas: top10,
    scoring_evaluation: toPayload(evaluation, relativePath),
  };
}
