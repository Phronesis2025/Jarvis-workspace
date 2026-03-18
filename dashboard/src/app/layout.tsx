import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = {
  title: "Jarvis Dashboard",
  description: "Read-only dashboard for Jarvis system progress and workflow",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-slate-50 text-slate-900 antialiased">
        <header className="border-b border-slate-200 bg-white">
          <div className="mx-auto max-w-7xl px-4 py-3 sm:px-6">
            <h1 className="text-lg font-semibold text-slate-800">
              Jarvis Dashboard
            </h1>
            <nav className="mt-2 flex gap-4 text-sm">
              <Link
                href="/"
                className="text-slate-600 hover:text-slate-900 underline-offset-2 hover:underline"
              >
                Overview
              </Link>
              <Link
                href="/tasks"
                className="text-slate-600 hover:text-slate-900 underline-offset-2 hover:underline"
              >
                Task Board
              </Link>
              <Link
                href="/runs"
                className="text-slate-600 hover:text-slate-900 underline-offset-2 hover:underline"
              >
                Recent Runs
              </Link>
              <Link
                href="/pathfinder"
                className="text-slate-600 hover:text-slate-900 underline-offset-2 hover:underline"
              >
                Pathfinder
              </Link>
            </nav>
          </div>
        </header>
        <main className="mx-auto max-w-7xl px-4 py-6 sm:px-6">{children}</main>
      </body>
    </html>
  );
}
