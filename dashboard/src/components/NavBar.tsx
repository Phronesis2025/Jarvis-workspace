"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const navItems = [
  { href: "/", label: "Overview" },
  { href: "/tasks", label: "Task Board" },
  { href: "/runs", label: "Recent Runs" },
  { href: "/pathfinder", label: "Pathfinder" },
] as const;

export function NavBar() {
  const pathname = usePathname();

  return (
    <nav className="flex flex-wrap gap-1 sm:gap-2">
      {navItems.map(({ href, label }) => {
        const isActive =
          href === "/"
            ? pathname === "/"
            : pathname.startsWith(href);
        return (
          <Link
            key={href}
            href={href}
            className={`rounded-md px-3 py-2 text-sm font-medium transition-colors ${
              isActive
                ? "bg-cyan-500/15 text-cyan-200 ring-1 ring-cyan-500/40 shadow-[0_0_12px_rgba(34,211,238,0.15)]"
                : "text-slate-400 hover:bg-slate-800/50 hover:text-cyan-100"
            }`}
            aria-current={isActive ? "page" : undefined}
          >
            {label}
          </Link>
        );
      })}
    </nav>
  );
}
