import type { Metadata } from "next";
import "./globals.css";
import { NavBar } from "@/components/NavBar";
import { AppTopBar } from "@/components/AppTopBar";

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
      <body className="min-h-screen bg-background text-foreground antialiased">
        <div className="min-h-screen lg:grid lg:grid-cols-[280px_minmax(0,1fr)]">
          <aside className="border-b border-border bg-background lg:sticky lg:top-0 lg:h-screen lg:border-b-0 lg:border-r">
            <NavBar />
          </aside>
          <div className="min-w-0">
            <AppTopBar />
            <main className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
              {children}
            </main>
          </div>
        </div>
      </body>
    </html>
  );
}
