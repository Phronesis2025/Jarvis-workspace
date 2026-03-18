import { getTasks, getRuns, getModuleStatus, getPathfinderCases } from "@/lib/data";
import { MermaidDiagram } from "@/components/MermaidDiagram";

function isToday(iso: string): boolean {
  const d = new Date(iso);
  const now = new Date();
  return d.getDate() === now.getDate() && d.getMonth() === now.getMonth() && d.getFullYear() === now.getFullYear();
}

function formatMetric(value: number | string, unavailable?: boolean) {
  if (unavailable) return <span className="text-slate-400">—</span>;
  return <span className="font-semibold text-slate-800">{value}</span>;
}

export default async function OverviewPage() {
  const [tasks, runs, modules, pathfinderCases] = await Promise.all([
    getTasks(),
    getRuns(100),
    getModuleStatus(),
    getPathfinderCases(100),
  ]);

  const today = new Date().toDateString();

  // Today-filtered
  const runsToday = runs.filter((r) => isToday(r.started_at));
  const wcsRunsToday = runsToday.filter((r) => r.module === "wcs");
  const pathfinderRunsToday = runsToday.filter((r) => r.module === "pathfinder");
  const tasksDoneToday = tasks.filter((t) => t.status === "done" && isToday(t.updated_at));
  const tasksBlockedToday = tasks.filter((t) => (t.status === "blocked" || t.status === "escalated") && isToday(t.updated_at));
  const pathfinderCasesToday = pathfinderCases.filter((c) => isToday(c.created_at));

  // Jarvis Core metrics (derived)
  const instructionsToday = runsToday.length; // proxy: each run = one instruction/cycle
  const tasksSelectedToday = wcsRunsToday.length + pathfinderRunsToday.filter((r) => r.task_ids?.length).length;
  const closuresToday = tasksDoneToday.length;
  const blockedEscalatedToday = tasksBlockedToday.length;

  // WCS metrics
  const wcsRunsAll = runs.filter((r) => r.module === "wcs");
  const wcsSuccessful = wcsRunsAll.filter((r) => (r.outcome ?? "").toLowerCase().includes("complete") || (r.outcome ?? "").toLowerCase().includes("worker_complete"));
  const lastSuccessfulWcs = wcsSuccessful[0];
  const buildPassRate = "—"; // unavailable
  const smokePassCount = "—"; // unavailable
  const pageSmokeCount = "—"; // unavailable

  // Pathfinder metrics
  const llmRuns = pathfinderCases.filter((c) => c.synthesis_source === "llm").length;
  const ruleBasedRuns = pathfinderCases.filter((c) => c.synthesis_source === "rule_based").length;
  const readyForImpl = pathfinderCases.filter((c) => c.confidence === "ready_for_implementation").length;
  const needsMoreContext = pathfinderCases.filter((c) => c.confidence === "needs_more_context").length;
  const pathfinderEscalations = 0; // unavailable - not in current schema
  const draftCandidatesCreated = pathfinderCases.filter((c) => c.backlog_candidate_title != null).length;

  // Operator attention
  const awaitingOperator = tasks.filter((t) => t.status === "awaiting_operator").length;
  const blocked = tasks.filter((t) => t.status === "blocked").length;
  const escalated = tasks.filter((t) => t.status === "escalated").length;

  const jarvisCore = modules.find((m) => m.module_id === "jarvis_core") ?? { name: "Jarvis Core", status: "active", milestone_summary: "Foreman loop live." };
  const wcsModule = modules.find((m) => m.module_id === "wcs") ?? { name: "WCS Code Module", status: "active", milestone_summary: "Task cycles proven." };
  const pathfinderModule = modules.find((m) => m.module_id === "pathfinder") ?? { name: "Pathfinder", status: "active", milestone_summary: "Read-only discovery worker." };

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-semibold text-slate-800">Overview</h2>

      {/* Today strip */}
      <section className="rounded-lg border border-slate-200 bg-slate-50 p-4">
        <h3 className="mb-3 text-sm font-medium text-slate-600">Today — {today}</h3>
        <div className="flex flex-wrap gap-4 text-sm">
          <span>Instructions: {formatMetric(instructionsToday)}</span>
          <span>Tasks run: {formatMetric(wcsRunsToday.length + pathfinderRunsToday.length)}</span>
          <span>Tasks closed: {formatMetric(closuresToday)}</span>
          <span>Pathfinder intakes: {formatMetric(pathfinderCasesToday.length)}</span>
          <span>Export freshness: <span className="text-slate-400">—</span></span>
          <span>System state: <span className="text-emerald-600 font-medium">operational</span></span>
        </div>
      </section>

      {/* Operator attention */}
      {(awaitingOperator > 0 || blocked > 0 || escalated > 0) && (
        <section className="rounded-lg border border-amber-200 bg-amber-50 p-4">
          <h3 className="mb-2 text-sm font-medium text-amber-800">Operator attention</h3>
          <div className="flex gap-4 text-sm">
            <span>Awaiting: {awaitingOperator}</span>
            <span>Blocked: {blocked}</span>
            <span>Escalated: {escalated}</span>
          </div>
        </section>
      )}

      {/* Jarvis Core */}
      <section className="rounded-lg border border-slate-200 bg-white p-5 shadow-sm">
        <div className="mb-4 flex items-center justify-between">
          <h3 className="text-lg font-semibold text-slate-800">Jarvis Core</h3>
          <span className={`rounded px-2 py-1 text-xs font-medium ${jarvisCore.status === "active" ? "bg-emerald-100 text-emerald-800" : "bg-slate-100 text-slate-600"}`}>
            {jarvisCore.status}
          </span>
        </div>
        <div className="mb-4 grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">
          <div><div className="text-xs text-slate-500">Instructions today</div><div>{formatMetric(instructionsToday)}</div></div>
          <div><div className="text-xs text-slate-500">Tasks selected today</div><div>{formatMetric(tasksSelectedToday)}</div></div>
          <div><div className="text-xs text-slate-500">Closures today</div><div>{formatMetric(closuresToday)}</div></div>
          <div><div className="text-xs text-slate-500">Blocked/escalated today</div><div>{formatMetric(blockedEscalatedToday)}</div></div>
          <div><div className="text-xs text-slate-500">Operating state</div><div className="text-emerald-600 text-sm font-medium">operational</div></div>
        </div>
        <div className="mb-4 rounded border border-slate-100 bg-slate-50/50 p-3 text-sm text-slate-600">
          <strong>Next steps:</strong> Run export when local state changes; review Task Board for ready work; run Pathfinder for new intakes.
        </div>
        <div className="rounded border border-slate-100 bg-white p-3">
          <div className="mb-2 text-xs font-medium text-slate-500">Jarvis flow</div>
          <MermaidDiagram code={`flowchart LR
    A[Backlog/Intake] --> B[Select Task]
    B --> C[Prepare Packet/Branch]
    C --> D[Launch Worker]
    D --> E[QA/Checkpoint]
    E --> F[Finalize/Reconcile]
    F --> G[Export Dashboard]`} />
        </div>
      </section>

      {/* WCS Code Module */}
      <section className="rounded-lg border border-slate-200 bg-white p-5 shadow-sm">
        <div className="mb-4 flex items-center justify-between">
          <h3 className="text-lg font-semibold text-slate-800">WCS Code Module</h3>
          <span className={`rounded px-2 py-1 text-xs font-medium ${wcsModule.status === "active" ? "bg-emerald-100 text-emerald-800" : "bg-slate-100 text-slate-600"}`}>
            {wcsModule.status}
          </span>
        </div>
        <div className="mb-4 grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">
          <div><div className="text-xs text-slate-500">Runs today</div><div>{formatMetric(wcsRunsToday.length)}</div></div>
          <div><div className="text-xs text-slate-500">Issues corrected</div><div>{formatMetric(tasks.filter((t) => t.status === "done").length)}</div></div>
          <div><div className="text-xs text-slate-500">Build pass rate</div><div>{formatMetric(buildPassRate, true)}</div></div>
          <div><div className="text-xs text-slate-500">Smoke pass count</div><div>{formatMetric(smokePassCount, true)}</div></div>
          <div><div className="text-xs text-slate-500">Page-smoke pass</div><div>{formatMetric(pageSmokeCount, true)}</div></div>
          <div><div className="text-xs text-slate-500">Last successful</div><div className="text-sm">{lastSuccessfulWcs ? lastSuccessfulWcs.run_id : "—"}</div></div>
        </div>
        <div className="mb-4 rounded border border-slate-100 bg-slate-50/50 p-3 text-sm text-slate-600">
          <strong>Next steps:</strong> Select ready task; run prep/launch; complete commit, QA, manual verification; finalize and reconcile.
        </div>
        <div className="rounded border border-slate-100 bg-white p-3">
          <div className="mb-2 text-xs font-medium text-slate-500">WCS execution flow</div>
          <MermaidDiagram code={`flowchart LR
    A[Task Selected] --> B[Branch Prep]
    B --> C[Cursor Execution]
    C --> D[Build/Smoke]
    D --> E[Manual Verification]
    E --> F[Finalize]
    F --> G[Reconcile]`} />
        </div>
      </section>

      {/* Pathfinder */}
      <section className="rounded-lg border border-slate-200 bg-white p-5 shadow-sm">
        <div className="mb-4 flex items-center justify-between">
          <h3 className="text-lg font-semibold text-slate-800">Pathfinder</h3>
          <span className={`rounded px-2 py-1 text-xs font-medium ${pathfinderModule.status === "active" ? "bg-emerald-100 text-emerald-800" : "bg-slate-100 text-slate-600"}`}>
            {pathfinderModule.status}
          </span>
        </div>
        <div className="mb-4 grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">
          <div><div className="text-xs text-slate-500">Intakes processed</div><div>{formatMetric(pathfinderCases.length)}</div></div>
          <div><div className="text-xs text-slate-500">LLM-assisted runs</div><div>{formatMetric(llmRuns)}</div></div>
          <div><div className="text-xs text-slate-500">Rule-based runs</div><div>{formatMetric(ruleBasedRuns)}</div></div>
          <div><div className="text-xs text-slate-500">Ready for impl</div><div>{formatMetric(readyForImpl)}</div></div>
          <div><div className="text-xs text-slate-500">Needs more context</div><div>{formatMetric(needsMoreContext)}</div></div>
          <div><div className="text-xs text-slate-500">Escalations</div><div>{pathfinderEscalations === 0 ? <span className="text-slate-400">—</span> : formatMetric(pathfinderEscalations)}</div></div>
          <div><div className="text-xs text-slate-500">Draft candidates</div><div>{formatMetric(draftCandidatesCreated)}</div></div>
        </div>
        <div className="mb-4 rounded border border-slate-100 bg-slate-50/50 p-3 text-sm text-slate-600">
          <strong>Next steps:</strong> Run Pathfinder on new intakes; review synthesis and draft backlog; open implementation task when scope is clear.
        </div>
        <div className="rounded border border-slate-100 bg-white p-3">
          <div className="mb-2 text-xs font-medium text-slate-500">Pathfinder flow</div>
          <MermaidDiagram code={`flowchart LR
    A[Intake Packet] --> B[Validate]
    B --> C[Gather Evidence]
    C --> D[Rule Checks]
    D --> E[Optional LLM Synthesis]
    E --> F[Validate Output]
    F --> G[Result / Draft Backlog / Escalation]`} />
        </div>
      </section>
    </div>
  );
}
