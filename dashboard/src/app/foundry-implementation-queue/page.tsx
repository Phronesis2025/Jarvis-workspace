import { FoundryImplementationQueueClient } from "@/components/FoundryImplementationQueueClient";
import { getFoundryImplementationQueueData } from "@/lib/foundry-queue";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";

export default async function FoundryImplementationQueuePage() {
  const data = await getFoundryImplementationQueueData();

  return (
    <div className="space-y-4">
      <div className="flex flex-col gap-1">
        <h2 className="text-xl font-semibold tracking-tight text-cyan-100">Implementation Queue</h2>
        <p className="text-sm text-slate-400">
          Local Foundry queue from <span className="font-mono text-cyan-200/80">queue_recommendations/*.json</span>
          , with operator edits in{" "}
          <span className="font-mono text-cyan-200/80">implementation_queue_items/*.json</span>.
        </p>
      </div>

      {data.warnings.length > 0 && (
        <div className="rounded border border-amber-500/30 bg-amber-500/10 p-3 text-sm text-amber-200">
          <div className="mb-1 font-semibold">Notice</div>
          <ul className="list-disc space-y-1 pl-5">
            {data.warnings.map((w) => (
              <li key={w}>{w}</li>
            ))}
          </ul>
        </div>
      )}

      {data.errors.length > 0 && (
        <div className="rounded border border-red-500/30 bg-red-500/10 p-3 text-sm text-red-200">
          <div className="mb-1 font-semibold">Data issues</div>
          <ul className="list-disc space-y-1 pl-5">
            {data.errors.map((e) => (
              <li key={e}>{e}</li>
            ))}
          </ul>
        </div>
      )}

      {data.items.length === 0 ? (
        <div className="hud-panel p-6 text-sm text-slate-400">
          <p className="text-amber-200/90">No implementation queue items loaded.</p>
          <p className="mt-2">
            Batch files: <span className="font-mono">{data.dataRoot}/queue_recommendations/</span>
          </p>
          <p className="mt-1 text-xs text-slate-500">
            Items are produced when the local engine recommends <code className="text-cyan-300">queue_candidate</code> with all
            gates passed. Empty batches are normal until then.
          </p>
        </div>
      ) : (
        <FoundryImplementationQueueClient initialItems={data.items} />
      )}
    </div>
  );
}
