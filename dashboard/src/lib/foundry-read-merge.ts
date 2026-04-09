/**
 * Merge repo-local Foundry state seeds with runtime storage (Vercel Blob) for dashboard reads.
 * When driver is `fs`, only storage is used (same on-disk tree). When `blob`, seed JSON is overlaid then runtime wins.
 */

import { readdir, readFile } from "fs/promises";
import { join } from "path";
import type { FoundryRegistryIdea } from "./types";
import type { FoundryLane } from "./foundry-rubric-anchors";
import { parseFoundryIdea } from "./foundry-registry-parse";
import type { FoundryStorage } from "./foundry-storage";
import { foundryBlobPrefixes, foundryStateRoot } from "./foundry-storage";

export async function loadMergedRegistryIdeas(
  store: FoundryStorage,
  errors: string[]
): Promise<FoundryRegistryIdea[]> {
  const byId = new Map<string, FoundryRegistryIdea>();

  if (store.driver === "blob") {
    const seedDir = join(foundryStateRoot(), "registry_ideas");
    try {
      const files = await readdir(seedDir);
      for (const fileName of files.filter((f) => f.endsWith(".json"))) {
        try {
          const raw = JSON.parse(await readFile(join(seedDir, fileName), "utf-8"));
          const idea = parseFoundryIdea(raw);
          if (idea) byId.set(idea.idea_id, idea);
          else errors.push(`Malformed registry idea skipped (seed): ${fileName}`);
        } catch {
          errors.push(`Malformed registry idea skipped (seed): ${fileName}`);
        }
      }
    } catch {
      /* no seed dir */
    }
  }

  try {
    const keys = await store.listJsonKeys(foundryBlobPrefixes.registryIdeas);
    for (const key of keys) {
      try {
        const raw = await store.getJson<unknown>(key);
        const idea = parseFoundryIdea(raw);
        if (idea) byId.set(idea.idea_id, idea);
        else errors.push(`Malformed registry idea skipped: ${key}`);
      } catch {
        errors.push(`Malformed registry idea skipped: ${key}`);
      }
    }
  } catch (e) {
    errors.push(`Registry storage list failed: ${e instanceof Error ? e.message : String(e)}`);
  }

  return Array.from(byId.values());
}

export async function loadMergedSourceLaneBySourceId(
  store: FoundryStorage,
  errors: string[]
): Promise<Record<string, FoundryLane>> {
  const map: Record<string, FoundryLane> = {};

  if (store.driver === "blob") {
    const sourceDir = join(foundryStateRoot(), "source_records");
    try {
      const sourceFiles = await readdir(sourceDir);
      for (const fileName of sourceFiles.filter((f) => f.endsWith(".json"))) {
        try {
          const raw = JSON.parse(await readFile(join(sourceDir, fileName), "utf-8")) as Record<string, unknown>;
          if (
            typeof raw.source_id === "string" &&
            (raw.source_lane === "article" || raw.source_lane === "github" || raw.source_lane === "x_post")
          ) {
            map[raw.source_id] = raw.source_lane;
          }
        } catch {
          errors.push(`Malformed source record skipped (seed): ${fileName}`);
        }
      }
    } catch {
      /* */
    }
  }

  try {
    const keys = await store.listJsonKeys(foundryBlobPrefixes.sourceRecords);
    for (const key of keys) {
      try {
        const raw = await store.getJson<Record<string, unknown>>(key);
        if (
          raw &&
          typeof raw.source_id === "string" &&
          (raw.source_lane === "article" || raw.source_lane === "github" || raw.source_lane === "x_post")
        ) {
          map[raw.source_id] = raw.source_lane;
        }
      } catch {
        errors.push(`Malformed source record skipped: ${key}`);
      }
    }
  } catch (e) {
    errors.push(`Source storage list failed: ${e instanceof Error ? e.message : String(e)}`);
  }

  return map;
}
