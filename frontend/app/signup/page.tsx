import Link from "next/link";
import { GalleryVerticalEnd } from "lucide-react";

import { SignupForm } from "@/components/signup-form";

export default function SignupPage() {
  return (
    <main className="signup-page dark grid min-h-svh lg:grid-cols-2">
      <section className="signup-panel flex min-h-svh flex-col gap-4 px-6 py-6 md:px-10 md:py-8">
        <header className="signup-brand flex justify-center md:justify-start">
          <Link href="/" className="flex items-center gap-2 font-medium">
            <span className="flex size-6 items-center justify-center rounded-md bg-primary text-primary-foreground">
              <GalleryVerticalEnd className="size-4" aria-hidden="true" />
            </span>
            FastAPI Shop
          </Link>
        </header>

        <div className="flex flex-1 items-center justify-center py-8">
          <div className="w-full max-w-xs">
            <SignupForm />
          </div>
        </div>
      </section>

      <aside className="signup-art relative hidden overflow-hidden lg:block" aria-hidden="true">
        <div className="signup-art-glow" />
        <div className="signup-art-orbit signup-art-orbit-outer" />
        <div className="signup-art-orbit signup-art-orbit-inner" />
        <div className="signup-art-core">
          <GalleryVerticalEnd />
        </div>
        <div className="signup-art-caption">A better way to shop.</div>
      </aside>
    </main>
  );
}
