"use client";

import { useEffect, useRef, useState } from "react";

/** Client component to render a Mermaid flowchart. Uses unique ID per instance. */
export function MermaidDiagram({ code }: { code: string }) {
  const containerRef = useRef<HTMLDivElement>(null);
  const idRef = useRef(`mermaid-${Math.random().toString(36).slice(2, 9)}`);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!code || !containerRef.current) return;
    let active = true;
    setError(null);
    import("mermaid")
      .then(({ default: mermaid }) => {
        mermaid.initialize({
          startOnLoad: false,
          theme: "base",
          securityLevel: "loose",
          themeVariables: {
            primaryColor: "#0f172a",
            primaryTextColor: "#e2e8f0",
            primaryBorderColor: "#22d3ee",
            lineColor: "#22d3ee",
            secondaryColor: "#1e293b",
            tertiaryColor: "#334155",
            background: "#020617",
            mainBkg: "#0f172a",
            nodeBorder: "#22d3ee",
            clusterBkg: "#0f172a",
            clusterBorder: "#22d3ee",
            titleColor: "#22d3ee",
            edgeLabelBackground: "#0f172a",
            nodeTextColor: "#e2e8f0",
          },
        });
        return mermaid.render(idRef.current, code);
      })
      .then(({ svg }) => {
        if (active && containerRef.current) {
          containerRef.current.innerHTML = svg;
        }
      })
      .catch((err) => {
        if (active) setError(String(err?.message ?? err));
      });
    return () => {
      active = false;
    };
  }, [code]);

  if (error) {
    return (
      <div className="rounded border border-cyan-500/30 bg-slate-900/50 p-3 text-sm text-amber-400">
        Diagram unavailable: {error}
      </div>
    );
  }
  return (
    <div
      ref={containerRef}
      className="mermaid-container flex justify-center overflow-x-auto py-2 [&_svg]:max-w-full [&_svg]:opacity-90"
    />
  );
}
