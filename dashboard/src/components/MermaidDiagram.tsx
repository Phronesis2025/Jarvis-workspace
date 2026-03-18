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
          theme: "neutral",
          securityLevel: "loose",
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
      <div className="rounded border border-amber-200 bg-amber-50 p-3 text-sm text-amber-800">
        Diagram unavailable: {error}
      </div>
    );
  }
  return (
    <div
      ref={containerRef}
      className="mermaid-container flex justify-center overflow-x-auto py-2 [&_svg]:max-w-full"
    />
  );
}
