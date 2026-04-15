/**
 * Foundry runtime storage: local filesystem (dev) or Vercel Blob (hosted).
 * Logical keys always use prefix `foundry/...` mirroring state/ layout.
 */

import { access, mkdir, readdir, readFile, stat, writeFile } from "fs/promises";
import { constants } from "fs";
import { join } from "path";

export const FOUNDRY_KEY_PREFIX = "foundry/";

export type FoundryStorageDriver = "fs" | "blob";

export interface FoundryJsonMeta {
  key: string;
  uploadedAtMs: number;
}

export interface FoundryStorage {
  readonly driver: FoundryStorageDriver;
  getJson<T>(key: string): Promise<T | null>;
  putJson(key: string, data: unknown): Promise<void>;
  listJsonKeys(prefix: string): Promise<string[]>;
  listJsonMeta(prefix: string): Promise<FoundryJsonMeta[]>;
  exists(key: string): Promise<boolean>;
}

export const foundryBlobPrefixes = {
  sourceRecords: `${FOUNDRY_KEY_PREFIX}source_records/`,
  candidateIdeas: `${FOUNDRY_KEY_PREFIX}candidate_ideas/`,
  registryIdeas: `${FOUNDRY_KEY_PREFIX}registry_ideas/`,
  queueRecommendations: `${FOUNDRY_KEY_PREFIX}queue_recommendations/`,
  implementationQueueItems: `${FOUNDRY_KEY_PREFIX}implementation_queue_items/`,
  scoringEvaluations: `${FOUNDRY_KEY_PREFIX}scoring_evaluations/`,
  indexes: `${FOUNDRY_KEY_PREFIX}indexes/`,
} as const;

export function workspaceRoot(): string {
  return join(process.cwd(), "..");
}

export function foundryStateRoot(): string {
  return join(workspaceRoot(), "future_modules", "the_foundry", "state");
}

export function resolveFoundryStorageDriver(): FoundryStorageDriver {
  const d = process.env.FOUNDRY_STORAGE_DRIVER?.trim().toLowerCase();
  if (d === "blob" || d === "vercel_blob" || d === "vercel-blob") return "blob";
  if (d === "fs") return "fs";
  if (process.env.VERCEL === "1" && process.env.BLOB_READ_WRITE_TOKEN?.trim()) {
    return "blob";
  }
  return "fs";
}

/** Hosted / Blob paths must use the Node engine (no `py -3`). */
export function foundryUsesNodeEngine(): boolean {
  if (process.env.FOUNDRY_ENGINE_RUNTIME === "python") return false;
  if (process.env.FOUNDRY_ENGINE_RUNTIME === "node") return true;
  if (process.env.VERCEL === "1") return true;
  return resolveFoundryStorageDriver() === "blob";
}

function assertFoundryKey(key: string): void {
  if (!key.startsWith(FOUNDRY_KEY_PREFIX)) {
    throw new Error(`Foundry storage key must start with "${FOUNDRY_KEY_PREFIX}"`);
  }
}

function keyToFsPath(key: string): string {
  assertFoundryKey(key);
  const rel = key.slice(FOUNDRY_KEY_PREFIX.length);
  return join(foundryStateRoot(), ...rel.split("/"));
}

async function fsListJsonKeys(prefix: string): Promise<string[]> {
  assertFoundryKey(prefix);
  const rel = prefix.slice(FOUNDRY_KEY_PREFIX.length).replace(/\/$/, "");
  const dir = join(foundryStateRoot(), ...rel.split("/"));
  try {
    const names = await readdir(dir);
    return names
      .filter((n) => n.endsWith(".json"))
      .map((n) => `${FOUNDRY_KEY_PREFIX}${rel}/${n}`)
      .sort();
  } catch {
    return [];
  }
}

async function createFsStorage(): Promise<FoundryStorage> {
  return {
    driver: "fs",
    async getJson<T>(key: string): Promise<T | null> {
      try {
        const p = keyToFsPath(key);
        return JSON.parse(await readFile(p, "utf-8")) as T;
      } catch {
        return null;
      }
    },
    async putJson(key: string, data: unknown): Promise<void> {
      const p = keyToFsPath(key);
      await mkdir(join(p, ".."), { recursive: true });
      await writeFile(p, JSON.stringify(data, null, 2) + "\n", "utf-8");
    },
    listJsonKeys: fsListJsonKeys,
    async listJsonMeta(prefix: string): Promise<FoundryJsonMeta[]> {
      const keys = await fsListJsonKeys(prefix);
      const out: FoundryJsonMeta[] = [];
      for (const key of keys) {
        try {
          const st = await stat(keyToFsPath(key));
          out.push({ key, uploadedAtMs: st.mtimeMs });
        } catch {
          out.push({ key, uploadedAtMs: 0 });
        }
      }
      return out;
    },
    async exists(key: string): Promise<boolean> {
      try {
        await access(keyToFsPath(key), constants.F_OK);
        return true;
      } catch {
        return false;
      }
    },
  };
}

/** Blob access must match the Vercel store (private stores reject `access: 'public'`). */
function resolveFoundryBlobAccess(): "public" | "private" {
  const a = process.env.FOUNDRY_BLOB_ACCESS?.trim().toLowerCase();
  if (a === "public") return "public";
  return "private";
}

async function readBlobStreamAsText(stream: ReadableStream<Uint8Array>): Promise<string> {
  const reader = stream.getReader();
  const decoder = new TextDecoder();
  let out = "";
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    if (value?.length) out += decoder.decode(value, { stream: true });
  }
  out += decoder.decode();
  return out;
}

async function createBlobStorage(): Promise<FoundryStorage> {
  const token = process.env.BLOB_READ_WRITE_TOKEN;
  if (!token?.trim()) {
    throw new Error("BLOB_READ_WRITE_TOKEN is required when FOUNDRY_STORAGE_DRIVER=blob");
  }
  const blobAccess = resolveFoundryBlobAccess();
  const { put, list, get } = await import("@vercel/blob");

  async function listAllBlobs(prefix: string) {
    const blobs: Awaited<ReturnType<typeof list>>["blobs"] = [];
    let cursor: string | undefined;
    do {
      const page = await list({ prefix, token, cursor, limit: 1000 });
      blobs.push(...page.blobs);
      cursor = page.hasMore ? page.cursor : undefined;
    } while (cursor);
    return blobs;
  }

  return {
    driver: "blob",
    async getJson<T>(key: string): Promise<T | null> {
      assertFoundryKey(key);
      try {
        const result = await get(key, { access: blobAccess, token });
        if (!result || result.statusCode !== 200 || !result.stream) return null;
        const text = await readBlobStreamAsText(result.stream);
        return JSON.parse(text) as T;
      } catch {
        return null;
      }
    },
    async putJson(key: string, data: unknown): Promise<void> {
      assertFoundryKey(key);
      await put(key, JSON.stringify(data), {
        access: blobAccess,
        addRandomSuffix: false,
        allowOverwrite: true,
        token,
        contentType: "application/json",
      });
    },
    async listJsonKeys(prefix: string): Promise<string[]> {
      const blobs = await listAllBlobs(prefix);
      return blobs
        .map((b) => b.pathname)
        .filter((p) => p.endsWith(".json"))
        .sort();
    },
    async listJsonMeta(prefix: string): Promise<FoundryJsonMeta[]> {
      const blobs = await listAllBlobs(prefix);
      return blobs
        .filter((b) => b.pathname.endsWith(".json"))
        .map((b) => ({
          key: b.pathname,
          uploadedAtMs: b.uploadedAt.getTime(),
        }))
        .sort((a, b) => a.key.localeCompare(b.key));
    },
    async exists(key: string): Promise<boolean> {
      const blobs = await listAllBlobs(key);
      return blobs.some((b) => b.pathname === key);
    },
  };
}

export async function createFoundryStorage(): Promise<FoundryStorage> {
  return resolveFoundryStorageDriver() === "blob" ? createBlobStorage() : createFsStorage();
}
