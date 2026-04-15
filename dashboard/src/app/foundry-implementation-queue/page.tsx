import { FoundryImplementationQueueClient } from "@/components/FoundryImplementationQueueClient";
import { getFoundryImplementationQueueData } from "@/lib/foundry-queue";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";

export default async function FoundryImplementationQueuePage() {
  const data = await getFoundryImplementationQueueData();

  return (
    <div className="space-y-4">
      <div className="flex flex-col gap-1">
        <h2 className="text-xl font-semibold tracking-tight text-foreground">Implementation Queue</h2>
        <p className="text-sm text-muted-foreground">
          Local Foundry queue from <span className="font-mono text-primary/80">queue_recommendations/*.json</span>
          , with operator edits in{" "}
          <span className="font-mono text-primary/80">implementation_queue_items/*.json</span>.
        </p>
      </div>

      {data.warnings.length > 0 && (
        <div className="rounded-lg border border-warning/20 bg-warning/15 p-3 text-sm text-warning">
          <div className="mb-1 font-semibold">Notice</div>
          <ul className="list-disc space-y-1 pl-5">
            {data.warnings.map((w) => (
              <li key={w}>{w}</li>
            ))}
          </ul>
        </div>
      )}

      {data.errors.length > 0 && (
        <div className="rounded-lg border border-destructive/20 bg-destructive/15 p-3 text-sm text-destructive">
          <div className="mb-1 font-semibold">Data issues</div>
          <ul className="list-disc space-y-1 pl-5">
            {data.errors.map((e) => (
              <li key={e}>{e}</li>
            ))}
          </ul>
        </div>
      )}

      {data.items.length === 0 ? (
        <div className="hud-panel p-6 text-sm text-muted-foreground">
          <p className="text-warning">No implementation queue items loaded.</p>
          <p className="mt-2">
            Batch files: <span className="font-mono">{data.dataRoot}/queue_recommendations/</span>
          </p>
          <p className="mt-1 text-xs text-muted-foreground">
            Items are produced when the local engine recommends <code className="text-primary">queue_candidate</code> with all
            gates passed. Empty batches are normal until then.
          </p>
        </div>
      ) : (
        <FoundryImplementationQueueClient initialItems={data.items} />
      )}
    </div>
  );
}
