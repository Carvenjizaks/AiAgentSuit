"use client";

import { useEffect, useRef, useState } from "react";
import { ArrowRight, Sparkles } from "lucide-react";

export default function CTA() {
  const [isVisible, setIsVisible] = useState(false);
  const sectionRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
        }
      },
      { threshold: 0.3 }
    );

    if (sectionRef.current) {
      observer.observe(sectionRef.current);
    }

    return () => observer.disconnect();
  }, []);

  return (
    <section ref={sectionRef} className="py-24 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto">
        <div
          className={`relative transition-all duration-700 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          {/* Background Glow */}
          <div className="absolute -inset-4 bg-gradient-to-r from-cyan-500/20 via-purple-600/20 to-pink-500/20 rounded-3xl blur-2xl" />
          
          <div className="relative glass rounded-3xl p-8 sm:p-12 lg:p-16 text-center overflow-hidden">
            {/* Decorative Elements */}
            <div className="absolute top-0 left-0 w-32 h-32 bg-cyan-500/10 rounded-full blur-3xl" />
            <div className="absolute bottom-0 right-0 w-40 h-40 bg-purple-600/10 rounded-full blur-3xl" />
            
            {/* Content */}
            <div className="relative">
              <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-cyan-500/20 to-purple-600/20 border border-cyan-500/30 text-sm mb-8">
                <Sparkles className="w-4 h-4 text-cyan-400" />
                <span className="text-cyan-400 font-medium">Only 10 Spots Available</span>
              </div>

              <h2 className="font-[family-name:var(--font-space)] text-3xl sm:text-4xl lg:text-5xl font-bold mb-6">
                Ready To Turn AI Into{" "}
                <span className="text-gradient">Your Competitive Edge?</span>
              </h2>

              <p className="text-gray-400 text-lg max-w-2xl mx-auto mb-10">
                Stop experimenting. Start shipping. The AI Agent Suit is the difference 
                between playing with AI and actually building with it.
              </p>

              <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
                <a
                  href="#pricing"
                  className="group inline-flex items-center gap-2 px-8 py-4 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-semibold text-lg hover:opacity-90 transition-all glow-cyan"
                >
                  Get The AI Agent Suit
                  <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                </a>
              </div>

              <p className="text-gray-500 text-sm mt-6">
                Join 50+ founders, creators, and agencies already shipping faster.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
