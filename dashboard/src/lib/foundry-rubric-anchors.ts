/**
 * Foundry 8-dimension matrix: explicit 0–5 anchors (auditable, bounded).
 * Scoring code maps observable source signals to these levels; this file is the rubric truth surface.
 */

export type FoundryLane = "article" | "github" | "x_post";

export const RUBRIC_KEYS = [
  "confidence",
  "evidence_strength",
  "transferability",
  "expected_upside",
  "risk_reduction_value",
  "implementation_cost",
  "novelty",
  "dependency_burden",
] as const;

export type RubricDimensionKey = (typeof RUBRIC_KEYS)[number];

export type IntakeHeuristicDimensions = Record<RubricDimensionKey, number>;

/** Version string written to preview/sidecar metadata paths that consume anchors. */
export const RUBRIC_ANCHOR_VERSION = "foundry_explicit_matrix_v1_2026-04-09";

/**
 * Per dimension: anchor text for scores 0,1,2,3,4,5 (inclusive).
 * Evaluator must cite which level is claimed and why (bounded rules in foundry-rubric-proposal.ts).
 */
export const RUBRIC_ANCHORS: Record<RubricDimensionKey, readonly [string, string, string, string, string, string]> = {
  confidence: [
    "0 — Scorer has almost no textual basis to assign any dimension (empty or noise).",
    "1 — Sparse text; high uncertainty for any structured read of the source.",
    "2 — Enough text to read a single surface claim; many dimensions remain underspecified.",
    "3 — Moderate coverage; several concrete fragments support partial reads across dimensions.",
    "4 — Broad coverage (length/structure); most dimensions can be read without large gaps.",
    "5 — Rich, structured source; dimensions can be read with explicit hooks (sections, lists, metrics, or repo path).",
  ],
  evidence_strength: [
    "0 — No substantive content (empty/whitespace only).",
    "1 — Fragments or title-only class material; no sustained argument or artifact description.",
    "2 — Short coherent passage OR bare repo URL with minimal path context.",
    "3 — Multiple sentences or bullets with at least one concrete detail (step, file, API, metric, or named component).",
    "4 — Sustained detail: several concrete specifics OR clear multi-part structure supporting claims.",
    "5 — Dense substantiation: multiple independent specifics (metrics, repro steps, interfaces, or deep repo path + descriptive scope).",
  ],
  transferability: [
    "0 — Purely local/one-off; no hint of reuse beyond the exact story.",
    "1 — Mostly anecdotal; portability not discussed and not inferable.",
    "2 — Implicit general lesson; weak signals of reuse (generic wording only).",
    "3 — Clear pattern or module named; plausible reuse in similar contexts.",
    "4 — Explicit reusable workflow, library, API, or cross-context pattern language.",
    "5 — Strong portability: abstraction, interface contract, or “drop-in” integration described.",
  ],
  expected_upside: [
    "0 — No benefit language or outcome implied.",
    "1 — Vague benefit (“better”, “improved”) without object or magnitude.",
    "2 — Directional benefit tied to a vague target (speed, cost, quality) without measure.",
    "3 — Specific benefit class (latency, throughput, risk, toil) named once.",
    "4 — Multiple benefit classes or a benefit tied to a concrete mechanism.",
    "5 — Quantified or sharply bounded upside (numbers, SLO-class targets, or explicit before/after framing).",
  ],
  risk_reduction_value: [
    "0 — No risk, safety, control, or failure-mode content.",
    "1 — Casual mention of “risk” without mitigation story.",
    "2 — Identifies a risk class (operational, model, market, compliance) without controls.",
    "3 — Names a control or safeguard (audit, limit, circuit breaker, hedge, validation) once.",
    "4 — Multiple controls or a traceable mitigation path.",
    "5 — Systematic risk posture: monitoring, limits, redundancy, or governance tied to concrete triggers.",
  ],
  implementation_cost: [
    "0 — Trivial integration (config flip, single call, docs-only).",
    "1 — Small localized change; no new infra.",
    "2 — Moderate engineering: multi-file or small service touch.",
    "3 — Notable scope: new component, pipeline stage, or recurring operational load.",
    "4 — Heavy engineering: multi-service, migration, or large test matrix implied.",
    "5 — Program-scale: org/process change, multi-team rollout, or major platform commitment.",
  ],
  novelty: [
    "0 — Pure boilerplate or generic advice with no distinctive mechanism.",
    "1 — Familiar pattern restated; no new hook.",
    "2 — Minor twist on a known pattern.",
    "3 — Distinct mechanism or composition not boilerplate.",
    "4 — Claims comparative edge vs baseline approach (speed, cost, robustness).",
    "5 — Strong novelty signals: first-of-class, unpublished method, or sharp departure from defaults (bounded; not semantic truth).",
  ],
  dependency_burden: [
    "0 — No external deps implied; standalone narrative or URL only.",
    "1 — Light touch on one external system or package class.",
    "2 — Several deps or one heavyweight class (cloud SDK, broker, cluster).",
    "3 — Multiple heavyweight classes or orchestration (containers + cloud + data plane).",
    "4 — Broad stack implied (multi-cloud, mesh, large polyglot graph).",
    "5 — Extreme coupling: many moving services/vendors with hard coordination implied.",
  ],
};
