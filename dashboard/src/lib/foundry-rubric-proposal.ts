/**
 * Bounded rubric-anchor proposal for Option A: maps observable source signals to explicit 0–5 anchors.
 * Not LLM semantic truth; rules are deterministic and cite anchor levels in reasons.
 */

import {
  type FoundryLane,
  type IntakeHeuristicDimensions,
  type RubricDimensionKey,
  RUBRIC_KEYS,
  RUBRIC_ANCHORS,
  RUBRIC_ANCHOR_VERSION,
} from "./foundry-rubric-anchors";

export { RUBRIC_ANCHOR_VERSION };

function clamp0to5(n: number): number {
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

function sentenceCount(text: string): number {
  return (text.match(/[.!?](?:\s|$)/g) ?? []).length;
}

function paragraphBreaks(text: string): number {
  return (text.match(/\n\s*\n/g) ?? []).length;
}

function bulletCount(text: string): number {
  return (text.match(/^\s*[-*•]\s+/gm) ?? []).length + (text.match(/^\s*\d+[.)]\s+/gm) ?? []).length;
}

function hasQuantifiedUpside(text: string): boolean {
  return (
    /\d+\s*%/.test(text) ||
    /\$\s*\d/.test(text) ||
    /\d+\s*(ms|sec|s|min|hours?|days?)\b/i.test(text) ||
    /\d+x\b/i.test(text) ||
    /p\d{2,3}/i.test(text)
  );
}

function portabilitySignals(lc: string): number {
  return keywordHitCount(lc, [
    "reusable",
    "library",
    "framework",
    "pattern",
    "workflow",
    "abstraction",
    "api",
    "sdk",
    "plugin",
    "general-purpose",
    "portable",
    "drop-in",
    "interface",
  ]);
}

function upsideSignals(lc: string): number {
  return keywordHitCount(lc, [
    "faster",
    "latency",
    "throughput",
    "reduce cost",
    "cheaper",
    "scale",
    "efficiency",
    "roi",
    "slo",
    "optimize",
    "improve",
    "speedup",
    "gain",
  ]);
}

function riskSignals(lc: string): number {
  return keywordHitCount(lc, [
    "risk",
    "mitigat",
    "hedge",
    "circuit breaker",
    "limit order",
    "audit",
    "compliance",
    "incident",
    "failure mode",
    "drawdown",
    "monitor",
    "redundan",
    "control",
  ]);
}

function heavyScopeSignals(lc: string): number {
  return keywordHitCount(lc, [
    "kubernetes",
    "k8s",
    "microservice",
    "multi-team",
    "migration",
    "rewrite",
    "enterprise",
    "multi-cloud",
    "org-wide",
    "rollout",
    "program",
  ]);
}

function noveltySignals(lc: string): number {
  return keywordHitCount(lc, [
    "novel",
    "new approach",
    "first ",
    "unpublished",
    "state of the art",
    "sota",
    "breakthrough",
    "vs baseline",
    "compared to",
  ]);
}

function depSignals(lc: string): number {
  return keywordHitCount(lc, [
    "npm",
    "pip",
    "docker",
    "terraform",
    "kubernetes",
    "grpc",
    "kafka",
    "postgres",
    "aws",
    "gcp",
    "azure",
    "dependency",
    "dependencies",
  ]);
}

function scoreEvidenceStrength(lane: FoundryLane, text: string, lc: string, len: number): { s: number; why: string; ev: string } {
  if (!text.trim()) {
    return { s: 0, why: "Anchor 0: no substantive text.", ev: "—" };
  }
  if (lane === "github") {
    const pathPart = lc.replace(/^https?:\/\/(www\.)?github\.com\//i, "");
    const segments = pathPart.split("/").filter(Boolean).length;
    const slashDensity = (text.match(/\//g) ?? []).length;
    let s = 2;
    if (segments >= 3) s = 3;
    if (segments >= 4 || slashDensity >= 5) s = 4;
    if (segments >= 5 && len > 40) s = 5;
    s = clamp0to5(s);
    const anchorIdx = s;
    return {
      s,
      why: `Anchor ${anchorIdx}: GitHub path segments=${segments}, slash markers=${slashDensity} (${RUBRIC_ANCHORS.evidence_strength[anchorIdx].slice(0, 72)}…)`,
      ev: text.slice(0, 140),
    };
  }
  const bullets = bulletCount(text);
  const paras = paragraphBreaks(text);
  const sentences = sentenceCount(text);
  const metrics = hasQuantifiedUpside(text);
  let s = 1;
  if (len >= 120 && sentences >= 2) s = 2;
  if ((len >= 400 && sentences >= 3) || bullets >= 2 || paras >= 1) s = 3;
  if ((len >= 1200 && (paras >= 2 || bullets >= 3)) || (metrics && len >= 500)) s = 4;
  if (len >= 3500 && paras >= 2 && sentences >= 8) s = 5;
  s = clamp0to5(s);
  return {
    s,
    why: `Anchor ${s}: len=${len}, sentences≈${sentences}, paragraphs=${paras}, bullets=${bullets}, quantified=${metrics}. ${RUBRIC_ANCHORS.evidence_strength[s].slice(0, 64)}…`,
    ev: text.slice(0, 140) || "—",
  };
}

function scoreTransferability(lane: FoundryLane, text: string, lc: string, len: number): { s: number; why: string; ev: string } {
  const p = portabilitySignals(lc);
  let base = lane === "github" ? 3 : lane === "article" ? 2 : 2;
  let s = base + Math.min(2, Math.floor(p / 2)) + (len > 800 ? 1 : 0);
  s = clamp0to5(s);
  const kws = [
    "reusable",
    "library",
    "framework",
    "pattern",
    "workflow",
    "abstraction",
    "api",
    "sdk",
    "plugin",
    "general-purpose",
    "portable",
    "drop-in",
    "interface",
  ] as const;
  return {
    s,
    why: `Anchor ${s}: lane=${lane}; portability keyword families hit≈${p}; long_text=${len > 800 ? "yes" : "no"}. ${RUBRIC_ANCHORS.transferability[s].slice(0, 64)}…`,
    ev: snippetAroundKeyword(text, lc, kws, 120),
  };
}

function scoreExpectedUpside(text: string, lc: string, len: number): { s: number; why: string; ev: string } {
  const u = upsideSignals(lc);
  const q = hasQuantifiedUpside(text);
  let s = Math.min(3, Math.ceil(u / 2));
  if (len > 400) s += 1;
  if (len > 1200) s += 1;
  if (q) s += 1;
  s = clamp0to5(s);
  const kws = [
    "faster",
    "latency",
    "throughput",
    "reduce cost",
    "scale",
    "efficiency",
    "roi",
    "optimize",
    "improve",
    "speedup",
    "gain",
  ] as const;
  return {
    s,
    why: `Anchor ${s}: upside keyword hits=${u}; quantified tokens=${q}; length tier applied. ${RUBRIC_ANCHORS.expected_upside[s].slice(0, 64)}…`,
    ev: snippetAroundKeyword(text, lc, kws, 120),
  };
}

function scoreRiskReduction(text: string, lc: string, len: number): { s: number; why: string; ev: string } {
  const r = riskSignals(lc);
  let s = Math.min(4, r);
  if (sentenceCount(text) >= 4 && r >= 1) s += 1;
  if (len > 2000 && r >= 2) s += 1;
  s = clamp0to5(s);
  const kws = ["risk", "mitigat", "audit", "compliance", "circuit breaker", "monitor", "failure mode"] as const;
  return {
    s,
    why: `Anchor ${s}: risk/control keyword hits=${r}; text length factor. ${RUBRIC_ANCHORS.risk_reduction_value[s].slice(0, 64)}…`,
    ev: snippetAroundKeyword(text, lc, kws, 120),
  };
}

function scoreImplementationCost(lane: FoundryLane, text: string, lc: string): { s: number; why: string; ev: string } {
  const h = heavyScopeSignals(lc);
  const bullets = bulletCount(text);
  let s = lane === "x_post" ? 3 : 2;
  s += Math.min(3, h);
  if (bullets >= 4) s += 1;
  s = clamp0to5(s);
  const kws = ["kubernetes", "microservice", "migration", "rewrite", "multi-team", "enterprise"] as const;
  return {
    s,
    why: `Anchor ${s}: heavy-scope signals=${h}; structured bullets=${bullets}; lane=${lane}. ${RUBRIC_ANCHORS.implementation_cost[s].slice(0, 64)}…`,
    ev: snippetAroundKeyword(text, lc, kws, 120),
  };
}

function scoreNovelty(lane: FoundryLane, text: string, lc: string, len: number): { s: number; why: string; ev: string } {
  const n = noveltySignals(lc);
  let s = lane === "x_post" ? 1 : 2;
  s += Math.min(3, n);
  if (len < 120 && lane !== "github") s -= 1;
  s = clamp0to5(s);
  const kws = ["novel", "new approach", "first ", "unpublished", "sota", "breakthrough", "vs baseline"] as const;
  return {
    s,
    why: `Anchor ${s}: novelty keyword hits=${n}; short-text penalty if applicable. ${RUBRIC_ANCHORS.novelty[s].slice(0, 64)}…`,
    ev: snippetAroundKeyword(text, lc, kws, 120),
  };
}

function scoreDependencyBurden(lane: FoundryLane, text: string, lc: string): { s: number; why: string; ev: string } {
  const d = depSignals(lc);
  let s = lane === "github" ? 2 : 1;
  s += Math.min(3, Math.ceil(d / 2));
  if (lane === "github" && (text.match(/\//g) ?? []).length >= 5) s += 1;
  s = clamp0to5(s);
  const kws = ["npm", "docker", "terraform", "aws", "grpc", "kafka", "dependency"] as const;
  return {
    s,
    why: `Anchor ${s}: dependency/cloud keyword families≈${d}; github slash density considered. ${RUBRIC_ANCHORS.dependency_burden[s].slice(0, 64)}…`,
    ev: snippetAroundKeyword(text, lc, kws, 120),
  };
}

function scoreConfidence(lane: FoundryLane, text: string, len: number): { s: number; why: string; ev: string } {
  const paras = paragraphBreaks(text);
  let s = 1;
  if (len > 800) s += 1;
  if (len > 2000) s += 1;
  if (paras >= 1) s += 1;
  if (lane === "github") s += 1;
  s = clamp0to5(s);
  return {
    s,
    why: `Anchor ${s}: coverage proxy len=${len}, paragraph breaks=${paras}, lane=${lane}. ${RUBRIC_ANCHORS.confidence[s].slice(0, 64)}…`,
    ev: text.slice(0, 120) || "—",
  };
}

export interface BoundedRubricProposal {
  proposed_scores: IntakeHeuristicDimensions;
  score_reasons: Record<RubricDimensionKey, string>;
  evidence_support: Record<RubricDimensionKey, string>;
  anchor_version: string;
  evaluation_method: "bounded_explicit_rubric_anchor_proposal_v1";
}

/**
 * Deterministic proposal: each dimension score is chosen as the best-fitting explicit anchor level
 * using the rules above (source-grounded snippets; not claim verification).
 */
export function deriveBoundedRubricProposal(lane: FoundryLane, rawInput: string): BoundedRubricProposal {
  const text = rawInput.trim();
  const lc = text.toLowerCase();
  const len = text.length;

  const ev = scoreEvidenceStrength(lane, text, lc, len);
  const tr = scoreTransferability(lane, text, lc, len);
  const up = scoreExpectedUpside(text, lc, len);
  const rk = scoreRiskReduction(text, lc, len);
  const ic = scoreImplementationCost(lane, text, lc);
  const nv = scoreNovelty(lane, text, lc, len);
  const db = scoreDependencyBurden(lane, text, lc);
  const cf = scoreConfidence(lane, text, len);

  const proposed_scores: IntakeHeuristicDimensions = {
    confidence: cf.s,
    evidence_strength: ev.s,
    transferability: tr.s,
    expected_upside: up.s,
    risk_reduction_value: rk.s,
    implementation_cost: ic.s,
    novelty: nv.s,
    dependency_burden: db.s,
  };

  const score_reasons: Record<RubricDimensionKey, string> = {
    confidence: cf.why,
    evidence_strength: ev.why,
    transferability: tr.why,
    expected_upside: up.why,
    risk_reduction_value: rk.why,
    implementation_cost: ic.why,
    novelty: nv.why,
    dependency_burden: db.why,
  };

  const evidence_support: Record<RubricDimensionKey, string> = {
    confidence: cf.ev,
    evidence_strength: ev.ev,
    transferability: tr.ev,
    expected_upside: up.ev,
    risk_reduction_value: rk.ev,
    implementation_cost: ic.ev,
    novelty: nv.ev,
    dependency_burden: db.ev,
  };

  return {
    proposed_scores,
    score_reasons,
    evidence_support,
    anchor_version: RUBRIC_ANCHOR_VERSION,
    evaluation_method: "bounded_explicit_rubric_anchor_proposal_v1",
  };
}

export function emptyScores(): IntakeHeuristicDimensions {
  return Object.fromEntries(RUBRIC_KEYS.map((k) => [k, 0])) as IntakeHeuristicDimensions;
}
