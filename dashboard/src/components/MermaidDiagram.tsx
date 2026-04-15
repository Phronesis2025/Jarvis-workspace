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
            primaryColor: "#171c2e",
            primaryTextColor: "#d8dfe8",
            primaryBorderColor: "#2a3142",
            lineColor: "#8be9f8",
            secondaryColor: "#141926",
            tertiaryColor: "#1f2534",
            background: "#0c0f17",
            mainBkg: "#171c2e",
            nodeBorder: "#2a3142",
            clusterBkg: "#141926",
            clusterBorder: "#2a3142",
            titleColor: "#8be9f8",
            edgeLabelBackground: "#171c2e",
            nodeTextColor: "#d8dfe8",
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
      <div className="rounded-lg border border-border bg-card p-3 text-sm text-warning">
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
