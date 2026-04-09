"use client";

import { useEffect, useMemo, useState } from "react";
import { useRouter } from "next/navigation";
import type { FoundryQueueRow } from "@/lib/foundry-queue";

interface Props {
  initialItems: FoundryQueueRow[];
}

const APPROVAL_OPTIONS = ["pending", "approved", "rejected"] as const;
const STATUS_OPTIONS = [
  "proposed",
  "ready",
  "in_design",
  "in_build",
  "blocked",
  "done",
  "dropped",
] as const;

function searchHaystack(row: FoundryQueueRow): string {
  const blockers = row.blockers.join(" ");
  return [
    row.idea_title ?? "",
    row.idea_id,
    row.why_now,
    row.expected_build_output,
    blockers,
  ]
    .join(" ")
    .toLowerCase();
}

export function FoundryImplementationQueueClient({ initialItems }: Props) {
  const router = useRouter();
  const [items, setItems] = useState<FoundryQueueRow[]>(initialItems);
  const [approvalFilter, setApprovalFilter] = useState<string>("all");
  const [statusFilter, setStatusFilter] = useState<string>("all");
  const [priorityFilter, setPriorityFilter] = useState<string>("all");
  const [search, setSearch] = useState("");
  const [selectedId, setSelectedId] = useState<string>(initialItems[0]?.queue_id ?? "");
  const [saveStatus, setSaveStatus] = useState<"idle" | "saving" | "error">("idle");
  const [saveMessage, setSaveMessage] = useState("");

  const priorityBands = useMemo(() => {
    const s = new Set(items.map((i) => i.priority_band));
    return Array.from(s).sort();
  }, [items]);

  const filtered = useMemo(() => {
    const q = search.trim().toLowerCase();
    return items.filter((row) => {
      if (approvalFilter !== "all" && row.operator_approval_state !== approvalFilter) return false;
      if (statusFilter !== "all" && row.status !== statusFilter) return false;
      if (priorityFilter !== "all" && row.priority_band !== priorityFilter) return false;
      if (q && !searchHaystack(row).includes(q)) return false;
      return true;
    });
  }, [items, approvalFilter, statusFilter, priorityFilter, search]);

  const selected = useMemo(() => {
    return filtered.find((r) => r.queue_id === selectedId) ?? filtered[0] ?? null;
  }, [filtered, selectedId]);

  useEffect(() => {
    if (filtered.length === 0) return;
    if (!filtered.some((r) => r.queue_id === selectedId)) {
      setSelectedId(filtered[0].queue_id);
    }
  }, [filtered, selectedId]);

  const summary = useMemo(() => {
    return {
      total: items.length,
      ready: items.filter((i) => i.status === "ready").length,
      blocked: items.filter((i) => i.status === "blocked").length,
      pendingApproval: items.filter((i) => i.operator_approval_state === "pending").length,
    };
  }, [items]);

  const [formApproval, setFormApproval] = useState("");
  const [formNotes, setFormNotes] = useState("");
  const [formStatus, setFormStatus] = useState("");
  const [formNext, setFormNext] = useState("");
  const [formBlockers, setFormBlockers] = useState("");

  useEffect(() => {
    const row = items.find((r) => r.queue_id === selectedId);
    if (!row) return;
    setFormApproval(row.operator_approval_state);
    setFormNotes(row.approval_notes);
    setFormStatus(row.status);
    setFormNext(row.next_action);
    setFormBlockers(row.blockers.join("\n"));
    setSaveStatus("idle");
    setSaveMessage("");
  }, [selectedId, items]);

  async function onSave(e: React.FormEvent) {
    e.preventDefault();
    if (!selected) return;
    setSaveStatus("saving");
    setSaveMessage("");
    const blockers = formBlockers
      .split("\n")
      .map((l) => l.trim())
      .filter(Boolean);

    try {
      const res = await fetch("/api/foundry/queue-item", {
        method: "PATCH",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
          queue_id: selected.queue_id,
          operator_approval_state: formApproval,
          approval_notes: formNotes,
          status: formStatus,
          next_action: formNext,
          blockers,
        }),
      });
      const data = (await res.json()) as { status: string; message?: string; item?: FoundryQueueRow };
      if (!res.ok || data.status !== "success" || !data.item) {
        throw new Error(data.message ?? "Save failed.");
      }
      setItems((prev) =>
        prev.map((r) =>
          r.queue_id === data.item!.queue_id
            ? {
                ...data.item!,
                idea_title: r.idea_title,
                idea_summary: r.idea_summary,
                idea_registry_status: r.idea_registry_status,
                source_run_id: r.source_run_id,
                persisted_locally: true,
              }
            : r
        )
      );
      setSaveStatus("idle");
      router.refresh();
    } catch (err) {
      setSaveStatus("error");
      setSaveMessage(err instanceof Error ? err.message : "Save failed.");
    }
  }

  return (
    <div className="space-y-6">
      <section className="grid grid-cols-2 gap-3 sm:grid-cols-4">
        <div className="hud-metric p-3">
          <div className="text-xs uppercase tracking-wider text-slate-500">Total queue items</div>
          <div className="mt-1 text-xl font-semibold text-cyan-200">{summary.total}</div>
        </div>
        <div className="hud-metric p-3">
          <div className="text-xs uppercase tracking-wider text-slate-500">Ready</div>
          <div className="mt-1 text-xl font-semibold text-cyan-200">{summary.ready}</div>
        </div>
        <div className="hud-metric p-3">
          <div className="text-xs uppercase tracking-wider text-slate-500">Blocked</div>
          <div className="mt-1 text-xl font-semibold text-cyan-200">{summary.blocked}</div>
        </div>
        <div className="hud-metric p-3">
          <div className="text-xs uppercase tracking-wider text-slate-500">Pending approval</div>
          <div className="mt-1 text-xl font-semibold text-cyan-200">{summary.pendingApproval}</div>
        </div>
      </section>

      <section className="hud-panel p-4">
        <div className="grid grid-cols-1 gap-3 md:grid-cols-2 lg:grid-cols-4">
          <label className="space-y-1 text-sm">
            <span className="text-slate-400">Operator approval</span>
            <select
              value={approvalFilter}
              onChange={(e) => setApprovalFilter(e.target.value)}
              className="w-full rounded border border-cyan-500/20 bg-slate-950 px-2 py-2 text-slate-200"
            >
              <option value="all">all</option>
              {APPROVAL_OPTIONS.map((o) => (
                <option key={o} value={o}>
                  {o}
                </option>
              ))}
            </select>
          </label>
          <label className="space-y-1 text-sm">
            <span className="text-slate-400">Status</span>
            <select
              value={statusFilter}
              onChange={(e) => setStatusFilter(e.target.value)}
              className="w-full rounded border border-cyan-500/20 bg-slate-950 px-2 py-2 text-slate-200"
            >
              <option value="all">all</option>
              {STATUS_OPTIONS.map((o) => (
                <option key={o} value={o}>
                  {o}
                </option>
              ))}
            </select>
          </label>
          <label className="space-y-1 text-sm">
            <span className="text-slate-400">Priority band</span>
            <select
              value={priorityFilter}
              onChange={(e) => setPriorityFilter(e.target.value)}
              className="w-full rounded border border-cyan-500/20 bg-slate-950 px-2 py-2 text-slate-200"
            >
              <option value="all">all</option>
              {priorityBands.map((p) => (
                <option key={p} value={p}>
                  {p}
                </option>
              ))}
            </select>
          </label>
          <label className="space-y-1 text-sm">
            <span className="text-slate-400">Search</span>
            <input
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="title, idea, why now, output, blockers"
              className="w-full rounded border border-cyan-500/20 bg-slate-950 px-2 py-2 text-slate-200 placeholder:text-slate-500"
            />
          </label>
        </div>
      </section>

      <section className="grid grid-cols-1 gap-6 lg:grid-cols-2">
        <div className="hud-panel overflow-x-auto p-0">
          <table className="min-w-full divide-y divide-cyan-500/10">
            <thead>
              <tr>
                {[
                  "rank",
                  "idea",
                  "priority",
                  "why now",
                  "expected output",
                  "resources",
                  "approval",
                  "status",
                  "blockers",
                  "confidence",
                  "created",
                  "updated",
                ].map((h) => (
                  <th key={h} className="px-2 py-2 text-left text-xs font-medium uppercase text-slate-400">
                    {h}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody className="divide-y divide-cyan-500/5">
              {filtered.map((row) => {
                const active = selected?.queue_id === row.queue_id;
                return (
                  <tr
                    key={row.queue_id}
                    onClick={() => setSelectedId(row.queue_id)}
                    className={`cursor-pointer text-sm ${active ? "bg-cyan-500/10" : "hover:bg-slate-900/70"}`}
                  >
                    <td className="whitespace-nowrap px-2 py-2 text-slate-200">{row.queue_rank}</td>
                    <td className="max-w-[180px] truncate px-2 py-2 text-slate-200">
                      {row.idea_title ?? row.idea_id}
                    </td>
                    <td className="whitespace-nowrap px-2 py-2 text-slate-400">{row.priority_band}</td>
                    <td className="max-w-[140px] truncate px-2 py-2 text-slate-400">{row.why_now}</td>
                    <td className="max-w-[140px] truncate px-2 py-2 text-slate-400">{row.expected_build_output}</td>
                    <td className="max-w-[100px] truncate px-2 py-2 text-slate-500">
                      {row.required_resources.length ? row.required_resources.join(", ") : "—"}
                    </td>
                    <td className="whitespace-nowrap px-2 py-2 text-slate-400">{row.operator_approval_state}</td>
                    <td className="whitespace-nowrap px-2 py-2 text-slate-400">{row.status}</td>
                    <td className="max-w-[100px] truncate px-2 py-2 text-amber-200/80">
                      {row.blockers.length ? row.blockers.join("; ") : "—"}
                    </td>
                    <td className="whitespace-nowrap px-2 py-2 text-cyan-200">{row.source_confidence_snapshot}</td>
                    <td className="whitespace-nowrap px-2 py-2 text-xs text-slate-500">
                      {new Date(row.created_at).toLocaleString()}
                    </td>
                    <td className="whitespace-nowrap px-2 py-2 text-xs text-slate-500">
                      {new Date(row.last_updated).toLocaleString()}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
          {filtered.length === 0 && (
            <p className="p-4 text-sm text-amber-300">No queue items match the current filters.</p>
          )}
        </div>

        <div className="space-y-4">
          {!selected ? (
            <div className="hud-panel p-4 text-sm text-slate-500">Select a queue item for details.</div>
          ) : (
            <>
              <div className="hud-panel p-4 text-sm text-slate-300">
                <h3 className="text-lg font-semibold text-cyan-100">
                  {selected.idea_title ?? selected.idea_id}
                </h3>
                <p className="mt-1 text-xs text-slate-500">
                  queue_id: <span className="font-mono text-cyan-200/80">{selected.queue_id}</span> · idea_id:{" "}
                  <span className="font-mono text-cyan-200/80">{selected.idea_id}</span>
                </p>
                {selected.source_run_id && (
                  <p className="mt-1 text-xs text-slate-500">Source batch run_id: {selected.source_run_id}</p>
                )}
                {selected.persisted_locally && (
                  <p className="mt-1 text-xs text-teal-400/90">Operator edits persisted locally (implementation_queue_items/).</p>
                )}
                <div className="mt-3 space-y-2">
                  <div>
                    <span className="text-slate-500">Why now:</span> {selected.why_now}
                  </div>
                  <div>
                    <span className="text-slate-500">Expected build output:</span> {selected.expected_build_output}
                  </div>
                  <div>
                    <span className="text-slate-500">Required resources:</span>{" "}
                    {selected.required_resources.length ? selected.required_resources.join(", ") : "—"}
                  </div>
                  <div>
                    <span className="text-slate-500">Target module:</span> {selected.target_module}
                  </div>
                  <div>
                    <span className="text-slate-500">Effort estimate:</span> {selected.effort_estimate}
                  </div>
                  <div>
                    <span className="text-slate-500">Dependency status:</span> {selected.dependency_status}
                  </div>
                  <div>
                    <span className="text-slate-500">Source confidence snapshot:</span> {selected.source_confidence_snapshot}
                  </div>
                  <div>
                    <span className="text-slate-500">Success criteria:</span>
                    <ul className="mt-1 list-disc pl-5">
                      {selected.success_criteria.map((c, i) => (
                        <li key={i}>{c}</li>
                      ))}
                    </ul>
                  </div>
                  <div>
                    <span className="text-slate-500">Next action:</span> {selected.next_action || "—"}
                  </div>
                  <div>
                    <span className="text-slate-500">Status:</span> {selected.status}
                  </div>
                  <div>
                    <span className="text-slate-500">Operator approval:</span> {selected.operator_approval_state}
                  </div>
                  <div>
                    <span className="text-slate-500">Approval notes:</span> {selected.approval_notes || "—"}
                  </div>
                  <div>
                    <span className="text-slate-500">Blockers:</span>
                    {selected.blockers.length ? (
                      <ul className="mt-1 list-disc pl-5">
                        {selected.blockers.map((b, i) => (
                          <li key={i}>{b}</li>
                        ))}
                      </ul>
                    ) : (
                      <span className="text-slate-500"> —</span>
                    )}
                  </div>
                  <div>
                    <span className="text-slate-500">Created:</span> {new Date(selected.created_at).toLocaleString()}
                  </div>
                  <div>
                    <span className="text-slate-500">Last updated:</span> {new Date(selected.last_updated).toLocaleString()}
                  </div>
                </div>
                <div className="mt-4 border-t border-cyan-500/10 pt-3">
                  <div className="text-xs font-medium uppercase tracking-wider text-slate-500">Registry context</div>
                  {selected.idea_summary ? (
                    <p className="mt-1 text-slate-400">{selected.idea_summary}</p>
                  ) : (
                    <p className="mt-1 text-slate-500">No matching registry idea file or summary unavailable.</p>
                  )}
                  {selected.idea_registry_status && (
                    <p className="mt-1 text-xs text-slate-500">Registry status: {selected.idea_registry_status}</p>
                  )}
                </div>
              </div>

              <form onSubmit={onSave} className="hud-panel space-y-3 p-4">
                <h4 className="text-xs font-medium uppercase tracking-wider text-cyan-400/80">Operator updates (local JSON)</h4>
                <label className="block text-sm">
                  <span className="text-slate-400">operator_approval_state</span>
                  <select
                    value={formApproval}
                    onChange={(e) => setFormApproval(e.target.value)}
                    className="mt-1 w-full rounded border border-cyan-500/20 bg-slate-950 px-2 py-2 text-slate-200"
                  >
                    {APPROVAL_OPTIONS.map((o) => (
                      <option key={o} value={o}>
                        {o}
                      </option>
                    ))}
                  </select>
                </label>
                <label className="block text-sm">
                  <span className="text-slate-400">status</span>
                  <select
                    value={formStatus}
                    onChange={(e) => setFormStatus(e.target.value)}
                    className="mt-1 w-full rounded border border-cyan-500/20 bg-slate-950 px-2 py-2 text-slate-200"
                  >
                    {STATUS_OPTIONS.map((o) => (
                      <option key={o} value={o}>
                        {o}
                      </option>
                    ))}
                  </select>
                </label>
                <label className="block text-sm">
                  <span className="text-slate-400">next_action</span>
                  <input
                    value={formNext}
                    onChange={(e) => setFormNext(e.target.value)}
                    className="mt-1 w-full rounded border border-cyan-500/20 bg-slate-950 px-2 py-2 text-slate-200"
                  />
                </label>
                <label className="block text-sm">
                  <span className="text-slate-400">approval_notes</span>
                  <textarea
                    value={formNotes}
                    onChange={(e) => setFormNotes(e.target.value)}
                    rows={3}
                    className="mt-1 w-full rounded border border-cyan-500/20 bg-slate-950 px-2 py-2 text-slate-200"
                  />
                </label>
                <label className="block text-sm">
                  <span className="text-slate-400">blockers (one per line)</span>
                  <textarea
                    value={formBlockers}
                    onChange={(e) => setFormBlockers(e.target.value)}
                    rows={3}
                    className="mt-1 w-full rounded border border-cyan-500/20 bg-slate-950 px-2 py-2 text-slate-200"
                  />
                </label>
                {saveStatus === "error" && <p className="text-sm text-amber-300">{saveMessage}</p>}
                <button
                  type="submit"
                  disabled={saveStatus === "saving"}
                  className="rounded-full bg-cyan-600 px-4 py-2 text-sm font-semibold text-white disabled:opacity-60"
                >
                  {saveStatus === "saving" ? "Saving…" : "Save to local queue item JSON"}
                </button>
              </form>
            </>
          )}
        </div>
      </section>
    </div>
  );
}
