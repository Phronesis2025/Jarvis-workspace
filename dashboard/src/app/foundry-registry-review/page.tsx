import { getFoundryRegistryReviewData } from "@/lib/data";
import { FoundryRegistryReviewClient } from "@/components/FoundryRegistryReviewClient";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";

export default async function FoundryRegistryReviewPage() {
  const data = await getFoundryRegistryReviewData();

  if (data.ideas.length === 0) {
    return (
      <div className="space-y-4">
        <h2 className="text-xl font-semibold tracking-tight text-cyan-100">
          Master Idea Registry Review
        </h2>
        <div className="hud-panel p-4 text-sm text-amber-300">
          No registry ideas found in local Foundry state.
          <div className="mt-2 text-slate-400">
            Expected JSON files under: <span className="font-mono text-cyan-200">{data.dataRoot}/registry_ideas</span>
          </div>
        </div>
        {data.errors.length > 0 && (
          <div className="hud-panel p-4 text-sm text-amber-300">
            <div className="mb-2 font-semibold">State read errors</div>
            <ul className="list-disc space-y-1 pl-5">
              {data.errors.map((error) => (
                <li key={error}>{error}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <div className="flex flex-col gap-1">
        <h2 className="text-xl font-semibold tracking-tight text-cyan-100">
          Master Idea Registry Review
        </h2>
        <p className="text-sm text-slate-400">
          Read-only review surface for Foundry Registry Ideas from local JSON state.
        </p>
      </div>
      {data.errors.length > 0 && (
        <div className="rounded border border-amber-500/30 bg-amber-500/10 p-3 text-sm text-amber-200">
          <div className="mb-1 font-semibold">Partial data warning</div>
          <ul className="list-disc space-y-1 pl-5">
            {data.errors.map((error) => (
              <li key={error}>{error}</li>
            ))}
          </ul>
        </div>
      )}
      <FoundryRegistryReviewClient
        ideas={data.ideas}
        sourceLanesByIdeaId={data.sourceLanesByIdeaId}
        scoringEvaluationsByIdeaId={data.scoringEvaluationsByIdeaId}
      />
    </div>
  );
}
