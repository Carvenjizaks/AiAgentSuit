"use client";

import { useEffect, useRef, useState } from "react";
import { Check, Zap, Crown } from "lucide-react";

export default function Pricing() {
  const [isVisible, setIsVisible] = useState(false);
  const sectionRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
        }
      },
      { threshold: 0.1 }
    );

    if (sectionRef.current) {
      observer.observe(sectionRef.current);
    }

    return () => observer.disconnect();
  }, []);

  const features = [
    "Complete OpenClaw environment setup",
    "20+ pre-configured skills",
    "5 AI agent templates",
    "Multi-model support (Kimi, OpenAI, Claude)",
    "Content-to-cash pipelines",
    "Persistent memory system",
    "Battle-tested command library",
    "Stripe, Gmail, Vercel, Supabase integrations",
    "Project scaffolds & templates",
    "Live Suit-Up Session (Zoom)",
    "30-day Telegram support",
    "Lifetime updates",
  ];

  return (
    <section ref={sectionRef} id="pricing" className="py-24 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div
          className={`text-center mb-16 transition-all duration-700 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-cyan-500/20 to-purple-600/20 border border-cyan-500/30 text-sm mb-6">
            <Crown className="w-4 h-4 text-cyan-400" />
            <span className="text-cyan-400 font-medium">Limited Spots Available</span>
          </div>
          
          <h2 className="font-[family-name:var(--font-space)] text-3xl sm:text-4xl lg:text-5xl font-bold mb-6">
            One Setup.{" "}
            <span className="text-gradient">Unlimited Potential.</span>
          </h2>
          <p className="text-gray-400 text-lg max-w-2xl mx-auto">
            Everything you need to turn AI from a chatbot into a complete 
            business operating system.
          </p>
        </div>

        {/* Pricing Card */}
        <div
          className={`relative transition-all duration-700 delay-200 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          {/* Glow */}
          <div className="absolute -inset-1 bg-gradient-to-r from-cyan-500 to-purple-600 rounded-3xl blur-lg opacity-50" />
          
          <div className="relative glass rounded-3xl p-8 sm:p-12 overflow-hidden">
            {/* Background Pattern */}
            <div className="absolute inset-0 bg-gradient-to-br from-cyan-500/5 to-purple-600/5" />
            
            <div className="relative">
              {/* Top Section */}
              <div className="text-center mb-10">
                <h3 className="font-[family-name:var(--font-space)] text-2xl font-bold mb-2">
                  AI Agent Suit Complete
                </h3>
                <p className="text-gray-400">One-time investment. Lifetime value.</p>
              </div>

              {/* Price */}
              <div className="text-center mb-10">
                <div className="flex items-center justify-center gap-2 mb-2">
                  <span className="text-gray-500 line-through text-xl">$2,500</span>
                  <span className="px-3 py-1 rounded-full bg-green-500/20 text-green-400 text-sm font-medium">
                    Early Access
                  </span>
                </div>
                <div className="flex items-baseline justify-center gap-1">
                  <span className="text-4xl sm:text-5xl font-bold">$997</span>
                  <span className="text-gray-500">USD</span>
                </div>
                <p className="text-gray-500 text-sm mt-2">or R18,500 ZAR</p>
              </div>

              {/* CTA */}
              <div className="mb-10">
                <a
                  href="#"
                  className="group flex items-center justify-center gap-2 w-full py-4 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-semibold text-lg hover:opacity-90 transition-all glow-cyan"
                >
                  <Zap className="w-5 h-5" />
                  Get Instant Access
                </a>
                <p className="text-center text-gray-500 text-sm mt-3">
                  Only 10 spots available for this intake
                </p>
              </div>

              {/* Divider */}
              <div className="border-t border-white/10 my-8" />

              {/* Features */}
              <div className="grid sm:grid-cols-2 gap-4">
                {features.map((feature, index) => (
                  <div key={index} className="flex items-start gap-3">
                    <div className="w-5 h-5 rounded-full bg-cyan-500/20 flex items-center justify-center shrink-0 mt-0.5">
                      <Check className="w-3 h-3 text-cyan-400" />
                    </div>
                    <span className="text-gray-300 text-sm">{feature}</span>
                  </div>
                ))}
              </div>

              {/* Guarantee */}
              <div className="mt-10 p-4 rounded-2xl bg-white/5 text-center">
                <p className="text-sm text-gray-400">
                  <span className="text-white font-semibold">30-Day Guarantee:</span>{" "}
                  If you don&apos;t ship a project in your first 30 days, I&apos;ll personally 
                  jump on a call and build it with you.
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Trust Badges */}
        <div
          className={`mt-12 flex flex-wrap justify-center gap-6 transition-all duration-700 delay-400 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          <div className="flex items-center gap-2 text-gray-500 text-sm">
            <Check className="w-4 h-4 text-green-400" />
            <span>Secure Payment</span>
          </div>
          <div className="flex items-center gap-2 text-gray-500 text-sm">
            <Check className="w-4 h-4 text-green-400" />
            <span>Instant Delivery</span>
          </div>
          <div className="flex items-center gap-2 text-gray-500 text-sm">
            <Check className="w-4 h-4 text-green-400" />
            <span>30-Day Support</span>
          </div>
        </div>
      </div>
    </section>
  );
}
