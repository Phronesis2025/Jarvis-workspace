/**
 * Foundry scoring helpers (client-safe): weighted preview (Python-parity), manual validation,
 * heuristic prefill (legacy buckets only), bounded rubric-anchor proposal (Option A matrix).
 * Sidecar I/O: `foundry-scoring-persistence.ts`.
 */

import {
  type FoundryLane,
  RUBRIC_KEYS,
  type RubricDimensionKey,
  type IntakeHeuristicDimensions,
} from "./foundry-rubric-anchors";

export type { FoundryLane, RubricDimensionKey, IntakeHeuristicDimensions };
export { RUBRIC_KEYS } from "./foundry-rubric-anchors";
export { RUBRIC_ANCHORS, RUBRIC_ANCHOR_VERSION } from "./foundry-rubric-anchors";

export type FoundryScoringMode = "option_a_rubric_assisted" | "option_b_manual_matrix";

export { deriveBoundedRubricProposal } from "./foundry-rubric-proposal";

export interface FoundryScoringEvaluation {
  evaluation_id: string;
  idea_id: string;
  candidate_id: string;
  source_id: string;
  engine_run_id: string;
  scoring_mode_selected: FoundryScoringMode;
  evaluation_method: string;
  heuristic_prefill_scores: IntakeHeuristicDimensions | null;
  proposed_scores: IntakeHeuristicDimensions | null;
  final_scores: IntakeHeuristicDimensions;
  score_reasons: Record<RubricDimensionKey, string> | null;
  evidence_support: Record<RubricDimensionKey, string> | null;
  weighted_score: number;
  created_at: string;
  /** Optional: explicit rubric matrix version used for Option A proposal. */
  rubric_anchor_version?: string;
}

function clampInt0to5(n: number): number {
  const r = Math.round(n);
  if (r < 0) return 0;
  if (r > 5) return 5;
  return r;
}

function keywordHitCount(lc: string, keywords: readonly string[]): number {
  let hits = 0;
  for (const kw of keywords) {
    if (lc.includes(kw)) hits += 1;
  }
  return hits;
}

function snippetAroundKeyword(text: string, lc: string, keywords: readonly string[], maxLen: number): string {
  const lower = text.toLowerCase();
  for (const kw of keywords) {
    const idx = lower.indexOf(kw);
    if (idx >= 0) {
      const start = Math.max(0, idx - 40);
      return text.slice(start, start + maxLen).replace(/\s+/g, " ").trim();
    }
  }
  return text.slice(0, maxLen).replace(/\s+/g, " ").trim() || "—";
}

/** Mirrors `compute_weighted_score` in `future_modules/the_foundry/engine/foundry_registry_engine.py`. */
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

/** Legacy length/keyword bucket scores — prefill only; not the explicit rubric matrix. */
export function deriveIntakeHeuristicScores(lane: FoundryLane, rawInput: string): IntakeHeuristicDimensions {
  return deriveHeuristicPrefillAudit(lane, rawInput).final_scores;
}

/**
 * Deterministic structure/keyword buckets for dashboard prefill column only.
 * Labeled honestly in reasons — not rubric-matrix evaluation.
 */
export function deriveHeuristicPrefillAudit(lane: FoundryLane, rawInput: string): {
  final_scores: IntakeHeuristicDimensions;
  score_reasons: Record<RubricDimensionKey, string>;
  evidence_support: Record<RubricDimensionKey, string>;
} {
  const text = rawInput.trim();
  const lc = text.toLowerCase();
  const len = text.length;

  const paragraphBreaksCount = (text.match(/\n\s*\n/g) ?? []).length;
  const bulletLines = (text.match(/^\s*[-*•]\s+/gm) ?? []).length;
  const numberedLines = (text.match(/^\s*\d+[.)]\s+/gm) ?? []).length;
  const sentenceEnds = (text.match(/[.!?](?:\s|$)/g) ?? []).length;
  const structuredUnits = bulletLines + numberedLines;

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
    if (paragraphBreaksCount >= 2) bump += 1;
    if (structuredUnits >= 2) bump += 1;
    if (sentenceEnds >= 4) bump += 1;
    evidence_strength = clampInt0to5(evidence_strength + bump);
  }

  let transferability = lane === "github" ? 4 : lane === "article" ? 3 : 2;
  const portableKws = ["pattern", "workflow", "framework", "reusable", "general-purpose", "portable", "library"] as const;
  transferability += Math.min(2, keywordHitCount(lc, portableKws));
  if (len > 600) transferability += 1;
  transferability = clampInt0to5(transferability);

  const upsideKws = [
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
  ] as const;
  let expected_upside = Math.min(3, keywordHitCount(lc, upsideKws));
  expected_upside += len > 1200 ? 2 : len > 400 ? 1 : 0;
  expected_upside = clampInt0to5(expected_upside);

  const riskKws = [
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
  ] as const;
  let risk_reduction_value = Math.min(4, keywordHitCount(lc, riskKws));
  if (sentenceEnds >= 3) risk_reduction_value += 1;
  risk_reduction_value = clampInt0to5(risk_reduction_value);

  let implementation_cost = lane === "x_post" ? 3 : 2;
  const heavyKws = ["kubernetes", "microservice", "rewrite", "legacy", "migration", "multi-team", "enterprise"] as const;
  implementation_cost += Math.min(3, keywordHitCount(lc, heavyKws));
  if (structuredUnits >= 4) implementation_cost += 1;
  implementation_cost = clampInt0to5(implementation_cost);

  let novelty = lane === "x_post" ? 1 : 2;
  const novelKws = ["novel", "new approach", "first ", "state of the art", "sota", "unpublished", "breakthrough"] as const;
  novelty += Math.min(3, keywordHitCount(lc, novelKws));
  if (len < 120 && lane !== "github") novelty -= 1;
  novelty = clampInt0to5(novelty);

  let dependency_burden = lane === "github" ? 2 : 1;
  const depKws = ["dependency", "dependencies", "npm", "pip", "docker", "terraform", "cloud", "aws", "grpc"] as const;
  dependency_burden += Math.min(3, keywordHitCount(lc, depKws));
  if (lane === "github" && (text.match(/\//g) ?? []).length >= 5) dependency_burden += 1;
  dependency_burden = clampInt0to5(dependency_burden);

  let confidence = 1;
  confidence += len > 2000 ? 2 : len > 800 ? 1 : 0;
  if (paragraphBreaksCount >= 1) confidence += 1;
  if (lane === "github") confidence += 1;
  confidence = clampInt0to5(confidence);

  const final_scores: IntakeHeuristicDimensions = {
    confidence,
    evidence_strength,
    transferability,
    expected_upside,
    risk_reduction_value,
    implementation_cost,
    novelty,
    dependency_burden,
  };

  const prefix = "Heuristic prefill only (structure/keyword buckets; not explicit rubric matrix): ";

  const score_reasons: Record<RubricDimensionKey, string> = {
    evidence_strength:
      prefix +
      (lane === "github"
        ? `GitHub path segments; URL structure proxy (not repo quality).`
        : `Char length ${len}; paragraph breaks ${paragraphBreaksCount}; structured lines ${structuredUnits}; sentence ends ${sentenceEnds}.`),
    transferability:
      prefix + `Lane prior (${lane}); portable-pattern keyword hits ${keywordHitCount(lc, portableKws)}; len>600=${len > 600}.`,
    expected_upside:
      prefix +
      `Upside keyword hits (capped) ${Math.min(3, keywordHitCount(lc, upsideKws))}; length tier +${len > 1200 ? 2 : len > 400 ? 1 : 0}.`,
    risk_reduction_value:
      prefix +
      `Risk/control keyword hits (capped) ${Math.min(4, keywordHitCount(lc, riskKws))}; sentenceEnds>=3 → +${sentenceEnds >= 3 ? 1 : 0}.`,
    implementation_cost:
      prefix +
      `Lane base; heavy-scope keyword hits ${Math.min(3, keywordHitCount(lc, heavyKws))}; structuredUnits>=4 → +${structuredUnits >= 4 ? 1 : 0}.`,
    novelty: prefix + `Lane base; novelty keyword hits; short-text penalty if len<120 (non-GitHub).`,
    dependency_burden: prefix + `Lane base; dependency/cloud keyword hits; GitHub slash-density bump if applicable.`,
    confidence: prefix + `Length/structure coverage for adapter (not claim truth); paragraphBreaks>=1; github lane +1.`,
  };

  const evidence_support: Record<RubricDimensionKey, string> = {
    evidence_strength: lane === "github" ? text.slice(0, 120) : `len=${len} preview: ${text.slice(0, 100)}…`,
    transferability: snippetAroundKeyword(text, lc, [...portableKws], 100),
    expected_upside: snippetAroundKeyword(text, lc, [...upsideKws], 100),
    risk_reduction_value: snippetAroundKeyword(text, lc, [...riskKws], 100),
    implementation_cost: snippetAroundKeyword(text, lc, [...heavyKws], 100),
    novelty: snippetAroundKeyword(text, lc, [...novelKws], 100),
    dependency_burden: snippetAroundKeyword(text, lc, [...depKws], 100),
    confidence: text.slice(0, 120) || "—",
  };

  return { final_scores, score_reasons, evidence_support };
}

export function validateManualRubricScores(raw: unknown): IntakeHeuristicDimensions {
  if (raw === null || typeof raw !== "object" || Array.isArray(raw)) {
    throw new Error("Rubric scores object must be an object with eight 0..5 integers.");
  }
  const o = raw as Record<string, unknown>;
  const out: Partial<IntakeHeuristicDimensions> = {};
  for (const key of RUBRIC_KEYS) {
    const v = o[key];
    if (typeof v !== "number" || !Number.isInteger(v) || v < 0 || v > 5) {
      throw new Error(`Rubric scores.${key} must be an integer 0..5.`);
    }
    out[key] = v;
  }
  return out as IntakeHeuristicDimensions;
}

function emptyManualReasons(): Record<RubricDimensionKey, string> {
  return {
    confidence: "Operator manual matrix (Option B); not heuristic.",
    evidence_strength: "Operator manual matrix (Option B); not heuristic.",
    transferability: "Operator manual matrix (Option B); not heuristic.",
    expected_upside: "Operator manual matrix (Option B); not heuristic.",
    risk_reduction_value: "Operator manual matrix (Option B); not heuristic.",
    implementation_cost: "Operator manual matrix (Option B); not heuristic.",
    novelty: "Operator manual matrix (Option B); not heuristic.",
    dependency_burden: "Operator manual matrix (Option B); not heuristic.",
  };
}

function emptyManualEvidence(): Record<RubricDimensionKey, string> {
  const v = "— (manual matrix; no auto snippet)";
  return {
    confidence: v,
    evidence_strength: v,
    transferability: v,
    expected_upside: v,
    risk_reduction_value: v,
    implementation_cost: v,
    novelty: v,
    dependency_burden: v,
  };
}

export function buildManualAudit(): {
  score_reasons: Record<RubricDimensionKey, string>;
  evidence_support: Record<RubricDimensionKey, string>;
} {
  return {
    score_reasons: emptyManualReasons(),
    evidence_support: emptyManualEvidence(),
  };
}
