/**
 * Shared Foundry registry idea JSON validation (dashboard + merge loaders).
 */

import type { FoundryRegistryIdea } from "./types";

function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

export function parseFoundryIdea(raw: unknown): FoundryRegistryIdea | null {
  if (!isRecord(raw)) return null;
  const requiredString = [
    "idea_id",
    "title",
    "summary",
    "category",
    "canonical_problem",
    "canonical_pattern",
    "dedupe_key",
    "status",
    "review_state",
    "promotion_reason",
    "review_notes",
    "implementation_notes",
    "queue_reason",
    "first_seen_at",
    "created_at",
    "last_updated",
  ] as const;
  for (const key of requiredString) {
    if (typeof raw[key] !== "string") return null;
  }

  const requiredNumber = [
    "supporting_source_count",
    "contradicting_source_count",
    "confidence",
    "evidence_strength",
    "transferability",
    "expected_upside",
    "risk_reduction_value",
    "implementation_cost",
    "novelty",
    "dependency_burden",
    "weighted_score",
  ] as const;
  for (const key of requiredNumber) {
    if (typeof raw[key] !== "number" || Number.isNaN(raw[key])) return null;
  }

  const stringArrayKeys = ["source_refs", "dependencies", "related_ideas"] as const;
  for (const key of stringArrayKeys) {
    if (!Array.isArray(raw[key]) || raw[key].some((v) => typeof v !== "string")) return null;
  }

  if (!isRecord(raw.score_breakdown)) return null;
  if (typeof raw.queue_eligibility !== "boolean") return null;

  return {
    idea_id: raw.idea_id as string,
    title: raw.title as string,
    summary: raw.summary as string,
    category: raw.category as string,
    canonical_problem: raw.canonical_problem as string,
    canonical_pattern: raw.canonical_pattern as string,
    dedupe_key: raw.dedupe_key as string,
    source_refs: raw.source_refs as string[],
    supporting_source_count: raw.supporting_source_count as number,
    contradicting_source_count: raw.contradicting_source_count as number,
    confidence: raw.confidence as number,
    evidence_strength: raw.evidence_strength as number,
    transferability: raw.transferability as number,
    expected_upside: raw.expected_upside as number,
    risk_reduction_value: raw.risk_reduction_value as number,
    implementation_cost: raw.implementation_cost as number,
    novelty: raw.novelty as number,
    dependency_burden: raw.dependency_burden as number,
    score_breakdown: raw.score_breakdown as Record<string, number>,
    weighted_score: raw.weighted_score as number,
    status: raw.status as FoundryRegistryIdea["status"],
    review_state: raw.review_state as FoundryRegistryIdea["review_state"],
    promotion_reason: raw.promotion_reason as string,
    review_notes: raw.review_notes as string,
    implementation_notes: raw.implementation_notes as string,
    dependencies: raw.dependencies as string[],
    related_ideas: raw.related_ideas as string[],
    queue_eligibility: raw.queue_eligibility as boolean,
    queue_reason: raw.queue_reason as string,
    first_seen_at: raw.first_seen_at as string,
    created_at: raw.created_at as string,
    last_updated: raw.last_updated as string,
  };
}
