"use client";

import { useEffect, useRef, useState } from "react";
import { X, Check } from "lucide-react";

export default function BeforeAfter() {
  const [isVisible, setIsVisible] = useState(false);
  const sectionRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
        }
      },
      { threshold: 0.2 }
    );

    if (sectionRef.current) {
      observer.observe(sectionRef.current);
    }

    return () => observer.disconnect();
  }, []);

  const beforeItems = [
    "One chat window, endless context switching",
    "You type everything manually",
    "No memory between sessions",
    "No project structure",
    "Generic AI responses",
    "One task at a time",
    "You figure out prompts yourself",
    "No integrations",
    "Hours to get anything done",
    "Starts from zero every conversation",
  ];

  const afterItems = [
    "20+ specialist skills loaded",
    "5 AI agents ready to deploy",
    "Persistent memory across projects",
    "Pre-built project scaffolds",
    "Custom rules that match YOUR voice",
    "Multiple agents working in PARALLEL",
    "Battle-tested commands built in",
    "Live integrations (Stripe, Gmail, Vercel, Supabase...)",
    "Full projects shipped in MINUTES",
    "Picks up exactly where you left off",
  ];

  return (
    <section ref={sectionRef} id="before-after" className="py-24 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div
          className={`text-center mb-16 transition-all duration-700 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          <h2 className="font-[family-name:var(--font-space)] text-3xl sm:text-4xl lg:text-5xl font-bold mb-6">
            The Difference Is{" "}
            <span className="text-gradient">Everything</span>
          </h2>
          <p className="text-gray-400 text-lg max-w-2xl mx-auto">
            Stop using AI like everyone else. This is what happens when you have a 
            complete system instead of just a chatbot.
          </p>
        </div>

        {/* Comparison Grid */}
        <div className="grid lg:grid-cols-2 gap-8">
          {/* Before */}
          <div
            className={`transition-all duration-700 delay-100 ${
              isVisible ? "opacity-100 translate-x-0" : "opacity-0 -translate-x-10"
            }`}
          >
            <div className="glass-dark rounded-3xl p-8 h-full border-red-500/20">
              <div className="flex items-center gap-3 mb-8">
                <div className="w-12 h-12 rounded-2xl bg-red-500/10 flex items-center justify-center">
                  <X className="w-6 h-6 text-red-500" />
                </div>
                <div>
                  <h3 className="font-[family-name:var(--font-space)] text-xl font-bold text-red-400">
                    BEFORE
                  </h3>
                  <p className="text-sm text-gray-500">Using AI the hard way</p>
                </div>
              </div>

              <ul className="space-y-4">
                {beforeItems.map((item, index) => (
                  <li key={index} className="flex items-start gap-3">
                    <X className="w-5 h-5 text-red-500/60 mt-0.5 shrink-0" />
                    <span className="text-gray-400">{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* After */}
          <div
            className={`transition-all duration-700 delay-200 ${
              isVisible ? "opacity-100 translate-x-0" : "opacity-0 translate-x-10"
            }`}
          >
            <div className="glass rounded-3xl p-8 h-full border-cyan-500/20 relative overflow-hidden">
              {/* Glow */}
              <div className="absolute -top-20 -right-20 w-40 h-40 bg-cyan-500/20 rounded-full blur-3xl" />
              
              <div className="flex items-center gap-3 mb-8 relative">
                <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-cyan-400 to-purple-600 flex items-center justify-center">
                  <Check className="w-6 h-6 text-white" />
                </div>
                <div>
                  <h3 className="font-[family-name:var(--font-space)] text-xl font-bold text-cyan-400">
                    WITH THE SUIT
                  </h3>
                  <p className="text-sm text-gray-500">AI as a weapon</p>
                </div>
              </div>

              <ul className="space-y-4 relative">
                {afterItems.map((item, index) => (
                  <li key={index} className="flex items-start gap-3">
                    <Check className="w-5 h-5 text-cyan-400 mt-0.5 shrink-0" />
                    <span className="text-white">{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
