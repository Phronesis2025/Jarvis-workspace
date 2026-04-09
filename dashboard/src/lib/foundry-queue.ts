import { readFile, readdir, stat } from "fs/promises";
import { join } from "path";
import type { FoundryRegistryIdea } from "@/lib/types";
import {
  createFoundryStorage,
  foundryBlobPrefixes,
  foundryStateRoot,
} from "@/lib/foundry-storage";
import type { FoundryStorage } from "@/lib/foundry-storage";

const QUEUE_REC_DIR = "queue_recommendations";
const PERSISTED_DIR = "implementation_queue_items";

export type FoundryQueueOperatorApproval = "pending" | "approved" | "rejected";
export type FoundryQueueStatus =
  | "proposed"
  | "ready"
  | "in_design"
  | "in_build"
  | "blocked"
  | "done"
  | "dropped";

/** Locked Implementation Queue Item v1 shape (matches Foundry contract). */
export interface FoundryImplementationQueueItem {
  queue_id: string;
  idea_id: string;
  queue_rank: number;
  priority_band: string;
  why_now: string;
  required_resources: string[];
  expected_build_output: string;
  owner: string;
  operator_approval_state: FoundryQueueOperatorApproval;
  approval_notes: string;
  target_module: string;
  effort_estimate: string;
  dependency_status: string;
  source_confidence_snapshot: number;
  success_criteria: string[];
  next_action: string;
  status: FoundryQueueStatus;
  blockers: string[];
  created_at: string;
  last_updated: string;
}

export interface FoundryQueueRow extends FoundryImplementationQueueItem {
  idea_title: string | null;
  idea_summary: string | null;
  idea_registry_status: string | null;
  /** Batch file stem when item came from recommendations only */
  source_run_id?: string;
  persisted_locally: boolean;
}

export interface FoundryImplementationQueueData {
  items: FoundryQueueRow[];
  errors: string[];
  warnings: string[];
  dataRoot: string;
}

const APPROVAL: FoundryQueueOperatorApproval[] = ["pending", "approved", "rejected"];
const STATUSES: FoundryQueueStatus[] = [
  "proposed",
  "ready",
  "in_design",
  "in_build",
  "blocked",
  "done",
  "dropped",
];

function isRecord(v: unknown): v is Record<string, unknown> {
  return v !== null && typeof v === "object" && !Array.isArray(v);
}

function validateQueueItem(raw: unknown): FoundryImplementationQueueItem | null {
  if (!isRecord(raw)) {
    return null;
  }
  const r = raw;
  if (typeof r.queue_id !== "string" || !r.queue_id.trim()) return null;
  if (typeof r.idea_id !== "string" || !r.idea_id.trim()) return null;
  if (typeof r.queue_rank !== "number" || r.queue_rank < 1 || !Number.isInteger(r.queue_rank)) return null;
  if (typeof r.priority_band !== "string" || !r.priority_band.trim()) return null;
  if (typeof r.why_now !== "string" || !r.why_now.trim()) return null;
  if (!Array.isArray(r.required_resources) || r.required_resources.some((x) => typeof x !== "string")) return null;
  if (typeof r.expected_build_output !== "string" || !r.expected_build_output.trim()) return null;
  if (typeof r.owner !== "string" || !r.owner.trim()) return null;
  if (typeof r.operator_approval_state !== "string" || !APPROVAL.includes(r.operator_approval_state as FoundryQueueOperatorApproval))
    return null;
  if (typeof r.approval_notes !== "string") return null;
  if (typeof r.target_module !== "string" || !r.target_module.trim()) return null;
  if (typeof r.effort_estimate !== "string" || !r.effort_estimate.trim()) return null;
  if (typeof r.dependency_status !== "string" || !r.dependency_status.trim()) return null;
  if (typeof r.source_confidence_snapshot !== "number" || r.source_confidence_snapshot < 0 || r.source_confidence_snapshot > 5)
    return null;
  if (!Array.isArray(r.success_criteria) || r.success_criteria.some((x) => typeof x !== "string")) return null;
  if (typeof r.next_action !== "string" || !r.next_action.trim()) return null;
  if (typeof r.status !== "string" || !STATUSES.includes(r.status as FoundryQueueStatus)) return null;
  if (!Array.isArray(r.blockers) || r.blockers.some((x) => typeof x !== "string")) return null;
  if (typeof r.created_at !== "string" || !r.created_at.trim()) return null;
  if (typeof r.last_updated !== "string" || !r.last_updated.trim()) return null;

  return {
    queue_id: r.queue_id,
    idea_id: r.idea_id,
    queue_rank: r.queue_rank,
    priority_band: r.priority_band,
    why_now: r.why_now,
    required_resources: r.required_resources as string[],
    expected_build_output: r.expected_build_output,
    owner: r.owner,
    operator_approval_state: r.operator_approval_state as FoundryQueueOperatorApproval,
    approval_notes: r.approval_notes,
    target_module: r.target_module,
    effort_estimate: r.effort_estimate,
    dependency_status: r.dependency_status,
    source_confidence_snapshot: r.source_confidence_snapshot,
    success_criteria: r.success_criteria as string[],
    next_action: r.next_action,
    status: r.status as FoundryQueueStatus,
    blockers: r.blockers as string[],
    created_at: r.created_at,
    last_updated: r.last_updated,
  };
}

async function readJson<T>(path: string): Promise<T | null> {
  try {
    return JSON.parse(await readFile(path, "utf-8")) as T;
  } catch {
    return null;
  }
}

async function loadQueueBatchEntries(
  store: FoundryStorage,
  errors: string[],
  warnings: string[]
): Promise<Array<{ label: string; mtime: number; raw: unknown }>> {
  const entries: Array<{ label: string; mtime: number; raw: unknown }> = [];

  if (store.driver === "blob") {
    const recDir = join(foundryStateRoot(), QUEUE_REC_DIR);
    try {
      const names = await readdir(recDir);
      for (const name of names.filter((n) => n.endsWith(".json"))) {
        const p = join(recDir, name);
        const st = await stat(p);
        const raw = await readJson<unknown>(p);
        if (raw) entries.push({ label: name, mtime: st.mtimeMs, raw });
      }
    } catch {
      /* no local seed */
    }
  }

  try {
    const metas = await store.listJsonMeta(foundryBlobPrefixes.queueRecommendations);
    for (const { key, uploadedAtMs } of metas) {
      const raw = await store.getJson<unknown>(key);
      if (raw) entries.push({ label: key, mtime: uploadedAtMs, raw });
    }
  } catch {
    warnings.push("Queue recommendations storage list failed; no batch queue items loaded.");
  }

  entries.sort((a, b) => b.mtime - a.mtime);
  return entries;
}

async function loadRegistryContext(
  store: FoundryStorage,
  ideaId: string
): Promise<{ title: string | null; summary: string | null; status: string | null }> {
  const key = `${foundryBlobPrefixes.registryIdeas}${ideaId}.json`;
  let data = await store.getJson<FoundryRegistryIdea>(key);
  if (!data && store.driver === "blob") {
    data = await readJson<FoundryRegistryIdea>(join(foundryStateRoot(), "registry_ideas", `${ideaId}.json`));
  }
  if (!data) return { title: null, summary: null, status: null };
  return {
    title: typeof data.title === "string" ? data.title : null,
    summary: typeof data.summary === "string" ? data.summary : null,
    status: typeof data.status === "string" ? data.status : null,
  };
}

async function loadPersistedQueueRaw(
  store: FoundryStorage,
  queueId: string
): Promise<unknown | null> {
  const key = `${foundryBlobPrefixes.implementationQueueItems}${queueId}.json`;
  const fromStore = await store.getJson<unknown>(key);
  if (fromStore !== null) return fromStore;
  if (store.driver === "blob") {
    return readJson<unknown>(join(foundryStateRoot(), PERSISTED_DIR, `${queueId}.json`));
  }
  return null;
}

/**
 * Merge queue items from all batch files (newest file wins per queue_id),
 * then overlay persisted copies from implementation_queue_items/ when present.
 * With Vercel Blob, repo-local seeds are merged under runtime keys (runtime wins on key collision).
 */
export async function getFoundryImplementationQueueData(): Promise<FoundryImplementationQueueData> {
  const store = await createFoundryStorage();
  const stateRoot = foundryStateRoot();
  const persistDir = join(stateRoot, PERSISTED_DIR);
  const errors: string[] = [];
  const warnings: string[] = [];
  const fromBatches = new Map<string, { item: FoundryImplementationQueueItem; runId: string }>();

  const batchEntries = await loadQueueBatchEntries(store, errors, warnings);
  if (batchEntries.length === 0 && store.driver === "fs") {
    try {
      await stat(join(foundryStateRoot(), QUEUE_REC_DIR));
    } catch {
      warnings.push("Queue recommendations folder missing or unreadable; no batch queue items loaded.");
    }
  }

  for (const { label, raw } of batchEntries) {
    if (!isRecord(raw)) {
      errors.push(`Malformed queue batch (not an object): ${label}`);
      continue;
    }
    const runId =
      typeof raw.run_id === "string"
        ? raw.run_id
        : label.replace(/^queue_recommendations_|\.json$/g, "").replace(/.*\//, "");
    const items = raw.items;
    if (!Array.isArray(items)) {
      errors.push(`Malformed queue batch (missing items array): ${label}`);
      continue;
    }
    for (let i = 0; i < items.length; i++) {
      const validated = validateQueueItem(items[i]);
      if (!validated) {
        errors.push(`Invalid queue item in ${label} at index ${i}`);
        continue;
      }
      if (!fromBatches.has(validated.queue_id)) {
        fromBatches.set(validated.queue_id, { item: validated, runId });
      }
    }
  }

  const allIds = new Set<string>(fromBatches.keys());

  try {
    const persistedKeys = await store.listJsonKeys(foundryBlobPrefixes.implementationQueueItems);
    for (const key of persistedKeys) {
      const base = key.split("/").pop() ?? "";
      const id = base.replace(/\.json$/, "");
      if (id) allIds.add(id);
    }
  } catch {
    /* */
  }

  if (store.driver === "blob") {
    try {
      const persistedNames = await readdir(persistDir);
      for (const name of persistedNames.filter((n) => n.endsWith(".json"))) {
        allIds.add(name.replace(/\.json$/, ""));
      }
    } catch {
      /* */
    }
  }

  const sortedQueueIds = Array.from(allIds).sort((a, b) => a.localeCompare(b));
  const rows: FoundryQueueRow[] = [];

  for (const queueId of sortedQueueIds) {
    const persistedRaw = await loadPersistedQueueRaw(store, queueId);
    let canonical: FoundryImplementationQueueItem | null = null;
    let persistedLocally = false;
    let sourceRunId: string | undefined;

    if (persistedRaw !== null) {
      canonical = validateQueueItem(persistedRaw);
      if (canonical) {
        persistedLocally = true;
      } else {
        errors.push(`Malformed persisted queue item: ${queueId}.json`);
      }
    }

    if (!canonical) {
      const batch = fromBatches.get(queueId);
      if (batch) {
        canonical = batch.item;
        sourceRunId = batch.runId;
      }
    }

    if (!canonical) continue;

    const reg = await loadRegistryContext(store, canonical.idea_id);
    rows.push({
      ...canonical,
      idea_title: reg.title,
      idea_summary: reg.summary,
      idea_registry_status: reg.status,
      source_run_id: sourceRunId,
      persisted_locally: persistedLocally,
    });
  }

  rows.sort((a, b) => a.queue_rank - b.queue_rank || a.queue_id.localeCompare(b.queue_id));

  if (rows.length === 0 && fromBatches.size === 0 && errors.length === 0) {
    warnings.push(
      "No queue items found. Engine writes batches to queue_recommendations/; items appear when candidates score as queue_candidate."
    );
  }

  return {
    items: rows,
    errors,
    warnings,
    dataRoot: `../future_modules/the_foundry/state`,
  };
}

export interface FoundryQueueItemPatch {
  operator_approval_state?: FoundryQueueOperatorApproval;
  approval_notes?: string;
  status?: FoundryQueueStatus;
  blockers?: string[];
  next_action?: string;
}

export async function updateFoundryQueueItem(
  queueId: string,
  patch: FoundryQueueItemPatch
): Promise<{ item: FoundryImplementationQueueItem }> {
  const trimmedId = queueId.trim();
  if (!trimmedId) {
    throw new Error("queue_id is required.");
  }

  const data = await getFoundryImplementationQueueData();
  const current = data.items.find((r) => r.queue_id === trimmedId);
  if (!current) {
    throw new Error(`Unknown queue_id: ${trimmedId}`);
  }

  const next: FoundryImplementationQueueItem = {
    queue_id: current.queue_id,
    idea_id: current.idea_id,
    queue_rank: current.queue_rank,
    priority_band: current.priority_band,
    why_now: current.why_now,
    required_resources: [...current.required_resources],
    expected_build_output: current.expected_build_output,
    owner: current.owner,
    operator_approval_state: patch.operator_approval_state ?? current.operator_approval_state,
    approval_notes: patch.approval_notes !== undefined ? patch.approval_notes : current.approval_notes,
    target_module: current.target_module,
    effort_estimate: current.effort_estimate,
    dependency_status: current.dependency_status,
    source_confidence_snapshot: current.source_confidence_snapshot,
    success_criteria: [...current.success_criteria],
    next_action: patch.next_action !== undefined ? patch.next_action : current.next_action,
    status: patch.status ?? current.status,
    blockers: patch.blockers !== undefined ? [...patch.blockers] : [...current.blockers],
    created_at: current.created_at,
    last_updated: new Date().toISOString(),
  };

  if (typeof next.approval_notes !== "string") {
    throw new Error("approval_notes must be a string.");
  }
  if (typeof next.next_action !== "string" || !next.next_action.trim()) {
    throw new Error("next_action must be a non-empty string.");
  }
  if (!APPROVAL.includes(next.operator_approval_state)) {
    throw new Error("Invalid operator_approval_state.");
  }
  if (!STATUSES.includes(next.status)) {
    throw new Error("Invalid status.");
  }

  const validated = validateQueueItem(next);
  if (!validated) {
    throw new Error("Updated item failed contract validation.");
  }

  const store = await createFoundryStorage();
  await store.putJson(`${foundryBlobPrefixes.implementationQueueItems}${trimmedId}.json`, validated);

  return { item: validated };
}
