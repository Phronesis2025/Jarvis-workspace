import { getModuleChecklists } from "@/lib/data";
import type {
  ModuleChecklist,
  ModuleChecklistPhase,
  ModuleChecklistItem,
  ChecklistItemStatus,
} from "@/lib/types";

export const dynamic = "force-dynamic";

function statusColor(s: ChecklistItemStatus): string {
  switch (s) {
    case "done":
      return "text-teal-400";
    case "in_progress":
      return "text-cyan-400";
    case "not_started":
      return "text-slate-500";
    case "blocked":
      return "text-amber-400";
    case "deferred":
      return "text-slate-500 italic";
    default:
      return "text-slate-400";
  }
}

function statusBadge(s: ChecklistItemStatus): string {
  switch (s) {
    case "done":
      return "border-teal-500/40 bg-teal-500/10 text-teal-400";
    case "in_progress":
      return "border-cyan-500/40 bg-cyan-500/10 text-cyan-400";
    case "not_started":
      return "border-slate-500/30 bg-slate-500/10 text-slate-400";
    case "blocked":
      return "border-amber-500/40 bg-amber-500/10 text-amber-400";
    case "deferred":
      return "border-slate-500/20 bg-slate-500/5 text-slate-500";
    default:
      return "border-slate-500/30 bg-slate-500/10 text-slate-400";
  }
}

function ChecklistItemRow({ item }: { item: ModuleChecklistItem }) {
  return (
    <div className="flex items-start gap-3 py-1.5">
      <span
        className={`mt-1.5 h-2 w-2 shrink-0 rounded-full ${
          item.status === "done"
            ? "bg-teal-400"
            : item.status === "in_progress" || item.status === "blocked"
              ? "bg-amber-400"
              : "bg-slate-600"
        }`}
      />
      <div className="min-w-0 flex-1">
        <span className={`text-sm ${statusColor(item.status)}`}>
          {item.label}
        </span>
        {item.notes && (
          <p className="mt-0.5 text-xs text-slate-500">{item.notes}</p>
        )}
      </div>
      <span
        className={`shrink-0 rounded border px-2 py-0.5 text-xs font-medium ${statusBadge(item.status)}`}
      >
        {item.status.replace("_", " ")}
      </span>
    </div>
  );
}

function PhaseBlock({
  phase,
  isCurrentPhase,
}: {
  phase: ModuleChecklistPhase;
  isCurrentPhase: boolean;
}) {
  const doneCount = phase.items.filter((i) => i.status === "done").length;
  const remaining =
    phase.items.length -
    phase.items.filter((i) => i.status === "done").length;

  return (
    <div
      className={`hud-panel p-4 ${isCurrentPhase ? "hud-panel-glow ring-1 ring-cyan-500/30" : ""}`}
    >
      <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
        <div>
          <h4 className="text-sm font-medium text-cyan-200">
            {phase.phase_name}
            {isCurrentPhase && (
              <span className="ml-2 text-xs text-cyan-400/80">
                (current phase)
              </span>
            )}
          </h4>
          <p className="mt-0.5 text-xs text-slate-500">{phase.goal}</p>
        </div>
        <div className="flex items-center gap-2">
          <span
            className={`rounded border px-2 py-0.5 text-xs ${statusBadge(phase.status)}`}
          >
            {phase.status.replace("_", " ")}
          </span>
          <span className="text-xs text-slate-500">
            {doneCount}/{phase.items.length}
          </span>
        </div>
      </div>
      <div className="space-y-0 divide-y divide-slate-700/50">
        {phase.items.map((item) => (
          <ChecklistItemRow key={item.id} item={item} />
        ))}
      </div>
      {remaining > 0 && (
        <p className="mt-2 text-xs text-slate-500">
          {remaining} item{remaining === 1 ? "" : "s"} remaining
        </p>
      )}
    </div>
  );
}

function ModuleSection({ module: m }: { module: ModuleChecklist }) {
  const totalItems = m.phases.reduce((sum, p) => sum + p.items.length, 0);
  const doneItems = m.phases.reduce(
    (sum, p) => sum + p.items.filter((i) => i.status === "done").length,
    0
  );
  const remainingItems = totalItems - doneItems;
  const currentPhase = m.phases.find((p) => p.phase_id === m.current_phase);

  return (
    <section className="space-y-4">
      <div className="hud-panel p-4">
        <div className="mb-3 flex flex-wrap items-start justify-between gap-3">
          <div>
            <h2 className="text-lg font-semibold text-cyan-100">
              {m.module_name}
            </h2>
            <p className="mt-1 text-sm text-slate-400">{m.purpose}</p>
          </div>
          <span
            className={`shrink-0 rounded border px-3 py-1.5 text-sm font-medium ${statusBadge(m.status)}`}
          >
            {m.status.replace("_", " ")}
          </span>
        </div>

        <div className="mb-4 grid grid-cols-1 gap-3 sm:grid-cols-2">
          <div className="rounded border border-cyan-500/20 bg-cyan-500/5 p-3">
            <div className="text-xs uppercase tracking-wider text-cyan-400/80">
              Current phase
            </div>
            <div className="mt-1 text-sm font-medium text-cyan-200">
              {currentPhase?.phase_name ?? m.current_phase}
            </div>
          </div>
          <div className="rounded border border-cyan-500/20 bg-cyan-500/5 p-3">
            <div className="text-xs uppercase tracking-wider text-cyan-400/80">
              Current step
            </div>
            <div className="mt-1 text-sm font-medium text-cyan-200">
              {m.current_step.replace(/_/g, " ")}
            </div>
          </div>
        </div>

        <div className="mb-4 rounded border border-slate-600/50 bg-slate-900/30 p-3">
          <div className="text-xs uppercase tracking-wider text-slate-500">
            Final version
          </div>
          <p className="mt-1 text-sm text-slate-300">
            {m.final_version_definition}
          </p>
        </div>

        <div className="mb-2 flex items-center gap-2 text-sm">
          <span className="text-teal-400">{doneItems} done</span>
          <span className="text-slate-500">•</span>
          <span className="text-amber-400/90">{remainingItems} remaining</span>
          <span className="text-slate-500">•</span>
          <span className="text-slate-500">{totalItems} total</span>
        </div>
      </div>

      <div className="space-y-4">
        {m.phases.map((phase) => (
          <PhaseBlock
            key={phase.phase_id}
            phase={phase}
            isCurrentPhase={phase.phase_id === m.current_phase}
          />
        ))}
      </div>
    </section>
  );
}

export default async function ChecklistsPage() {
  const data = await getModuleChecklists();

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-semibold tracking-tight text-cyan-100">
          Module Checklists
        </h1>
        <p className="mt-1 text-sm text-slate-400">
          Build-path view for each module. Rendered from{" "}
          <code className="rounded bg-slate-800 px-1.5 py-0.5 font-mono text-xs text-cyan-300">
            state/module_checklists.json
          </code>
          .
        </p>
      </div>

      {!data ? (
        <div className="hud-panel p-6">
          <p className="text-amber-400/90">
            Checklist data unavailable. Run the dashboard locally with the
            Jarvis workspace so{" "}
            <code className="rounded bg-slate-800 px-1 py-0.5 font-mono text-xs">
              state/module_checklists.json
            </code>{" "}
            can be read.
          </p>
        </div>
      ) : (
        <>
          {data.generated_at && (
            <p className="text-xs text-slate-500">
              Generated: {new Date(data.generated_at).toISOString()}
            </p>
          )}
          <div className="space-y-10">
            {data.modules.map((m) => (
              <ModuleSection key={m.module_id} module={m} />
            ))}
          </div>
        </>
      )}
    </div>
  );
}
