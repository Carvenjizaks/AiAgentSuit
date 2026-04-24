"use client";

import { useEffect, useRef, useState } from "react";
import { 
  Rocket, 
  Layout, 
  Key, 
  Gem, 
  Globe, 
  Plus,
  Clock,
  CheckCircle2
} from "lucide-react";

export default function Proof() {
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

  const builds = [
    {
      icon: Rocket,
      title: "AI Voice Assistant",
      description: "Full Jarvis-style voice system. One dashboard, speak naturally, AI responds in your voice.",
      time: "4 hours",
    },
    {
      icon: Layout,
      title: "Command Center Dashboard",
      description: "Real-time business nerve center. Shows deadlines, priorities, and revenue opportunities.",
      time: "6 hours",
    },
    {
      icon: Key,
      title: "License Key System",
      description: "Complete product protection. Automated key generation, validation, and delivery.",
      time: "3 hours",
    },
    {
      icon: Globe,
      title: "4 Client Websites",
      description: "Four complete professional sites. Designed, built, and deployed alongside everything else.",
      time: "12 hours",
    },
    {
      icon: Gem,
      title: "Diamond Comparison Site",
      description: "Natural vs lab-grown diamond platform. Full site, live and working.",
      time: "5 hours",
    },
    {
      icon: Plus,
      title: "+ More In The Demo",
      description: "See the full list live. This is just what fits on the page.",
      time: "48 hrs total",
      highlight: true,
    },
  ];

  return (
    <section ref={sectionRef} id="proof" className="py-24 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div
          className={`text-center mb-16 transition-all duration-700 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full glass text-sm mb-6">
            <Clock className="w-4 h-4 text-cyan-400" />
            <span className="text-gray-300">48 Hours. One Person. No Developers.</span>
          </div>
          
          <h2 className="font-[family-name:var(--font-space)] text-3xl sm:text-4xl lg:text-5xl font-bold mb-6">
            What I Built Using{" "}
            <span className="text-gradient">This Setup</span>
          </h2>
          <p className="text-gray-400 text-lg max-w-2xl mx-auto">
            This is NOT theory. Here&apos;s what shipped in under 2 days using 
            the AI Agent Suit with multi-agent orchestration.
          </p>
        </div>

        {/* Builds Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {builds.map((build, index) => (
            <div
              key={build.title}
              className={`group relative transition-all duration-700 ${
                isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
              }`}
              style={{ transitionDelay: `${index * 100}ms` }}
            >
              <div className={`relative h-full rounded-2xl p-6 overflow-hidden transition-all duration-300 ${
                build.highlight 
                  ? "bg-gradient-to-br from-cyan-500/20 to-purple-600/20 border border-cyan-500/30" 
                  : "glass hover:bg-white/10"
              }`}>
                {/* Icon & Time */}
                <div className="flex items-start justify-between mb-4">
                  <div className={`w-12 h-12 rounded-xl flex items-center justify-center ${
                    build.highlight 
                      ? "bg-gradient-to-br from-cyan-400 to-purple-600" 
                      : "bg-white/10"
                  }`}>
                    <build.icon className="w-6 h-6 text-white" />
                  </div>
                  <div className="flex items-center gap-1 text-xs font-medium">
                    <Clock className="w-3 h-3 text-gray-500" />
                    <span className={build.highlight ? "text-cyan-400" : "text-gray-500"}>
                      {build.time}
                    </span>
                  </div>
                </div>

                {/* Content */}
                <h3 className="font-[family-name:var(--font-space)] text-lg font-bold mb-2">
                  {build.title}
                </h3>
                <p className="text-gray-400 text-sm leading-relaxed">
                  {build.description}
                </p>

                {/* Highlight indicator */}
                {build.highlight && (
                  <div className="absolute top-4 right-4">
                    <div className="flex items-center gap-1 text-xs text-cyan-400">
                      <CheckCircle2 className="w-3 h-3" />
                      <span>Live Demo</span>
                    </div>
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>

        {/* Bottom CTA */}
        <div
          className={`mt-12 text-center transition-all duration-700 delay-700 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          <p className="text-gray-400 mb-6">
            That&apos;s the difference between using AI like everyone else... 
            and having it set up like a <span className="text-white font-semibold">WEAPON</span>.
          </p>
          <a
            href="#pricing"
            className="inline-flex items-center gap-2 px-8 py-4 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-semibold hover:opacity-90 transition-opacity glow-cyan"
          >
            Get The Same Setup
          </a>
        </div>
      </div>
    </section>
  );
}
