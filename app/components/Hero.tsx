"use client";

import { useEffect, useState } from "react";
import { ArrowRight, Play, Sparkles, Bot, Zap, Cpu } from "lucide-react";

export default function Hero() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  return (
    <section className="relative min-h-screen flex items-center justify-center pt-20 pb-16 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto w-full">
        <div className="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">
          {/* Left Content */}
          <div
            className={`space-y-8 transition-all duration-1000 ${
              isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
            }`}
          >
            {/* Badge */}
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full glass text-sm">
              <Sparkles className="w-4 h-4 text-cyan-400" />
              <span className="text-gray-300">Powered by AI</span>
              <span className="px-2 py-0.5 rounded-full bg-cyan-500/20 text-cyan-400 text-xs font-medium">
                v2.0
              </span>
            </div>

            {/* Headline */}
            <h1 className="font-[family-name:var(--font-space)] text-4xl sm:text-5xl lg:text-6xl xl:text-7xl font-bold leading-[1.1]">
              Your Complete{" "}
              <span className="text-gradient">AI Command</span>{" "}
              Center
            </h1>

            {/* Subheadline */}
            <p className="text-lg sm:text-xl text-gray-400 max-w-xl leading-relaxed">
              Pre-configured AI environment with 20+ skills, multi-agent orchestration,
              and content-to-cash pipelines. Deploy in 10 minutes, ship projects in hours.
            </p>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4">
              <a
                href="#pricing"
                className="group inline-flex items-center justify-center gap-2 px-8 py-4 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-semibold text-lg hover:opacity-90 transition-all glow-cyan"
              >
                Get The Suit
                <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </a>
              <a
                href="#proof"
                className="inline-flex items-center justify-center gap-2 px-8 py-4 rounded-full glass text-white font-semibold text-lg hover:bg-white/10 transition-all"
              >
                <Play className="w-5 h-5" />
                See What&apos;s Possible
              </a>
            </div>

            {/* Trust Indicators */}
            <div className="flex flex-wrap items-center gap-6 pt-4">
              <div className="flex items-center gap-2 text-sm text-gray-500">
                <div className="flex -space-x-2">
                  {[1, 2, 3, 4].map((i) => (
                    <div
                      key={i}
                      className="w-8 h-8 rounded-full bg-gradient-to-br from-gray-700 to-gray-800 border-2 border-[#0a0a0f]"
                    />
                  ))}
                </div>
                <span>50+ early adopters</span>
              </div>
              <div className="h-4 w-px bg-gray-800 hidden sm:block" />
              <div className="flex items-center gap-2 text-sm text-gray-500">
                <span className="text-yellow-500">★★★★★</span>
                <span>4.9/5 rating</span>
              </div>
            </div>
          </div>

          {/* Right Content - Visual */}
          <div
            className={`relative transition-all duration-1000 delay-300 ${
              isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
            }`}
          >
            {/* Main Card */}
            <div className="relative">
              {/* Glow effect */}
              <div className="absolute -inset-4 bg-gradient-to-r from-cyan-500/20 to-purple-600/20 rounded-3xl blur-2xl" />
              
              {/* Card */}
              <div className="relative glass rounded-3xl p-6 sm:p-8 overflow-hidden">
                {/* Header */}
                <div className="flex items-center justify-between mb-6">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-400 to-purple-600 flex items-center justify-center">
                      <Bot className="w-5 h-5 text-white" />
                    </div>
                    <div>
                      <div className="font-semibold">AI Agent Suit</div>
                      <div className="text-xs text-gray-500">Active • 5 agents running</div>
                    </div>
                  </div>
                  <div className="flex gap-2">
                    <div className="w-3 h-3 rounded-full bg-red-500/80" />
                    <div className="w-3 h-3 rounded-full bg-yellow-500/80" />
                    <div className="w-3 h-3 rounded-full bg-green-500/80" />
                  </div>
                </div>

                {/* Terminal Content */}
                <div className="space-y-3 font-mono text-sm">
                  <div className="flex items-start gap-3">
                    <span className="text-cyan-400">➜</span>
                    <span className="text-gray-300">~</span>
                    <span className="text-purple-400">openclaw</span>
                    <span className="text-gray-500">skills:list</span>
                  </div>
                  
                  <div className="pl-6 space-y-1 text-gray-400">
                    <div>✓ letterman-skill</div>
                    <div>✓ poststream-social</div>
                    <div>✓ video-cue</div>
                    <div>✓ seo-content-writer</div>
                    <div>✓ article-cue</div>
                    <div className="text-gray-600">+ 15 more...</div>
                  </div>

                  <div className="flex items-start gap-3 pt-2">
                    <span className="text-cyan-400">➜</span>
                    <span className="text-gray-300">~</span>
                    <span className="text-purple-400">agent</span>
                    <span className="text-gray-500">deploy --all</span>
                  </div>

                  <div className="pl-6 space-y-1">
                    <div className="flex items-center gap-2 text-green-400">
                      <Zap className="w-3 h-3" />
                      <span>Content Agent: ACTIVE</span>
                    </div>
                    <div className="flex items-center gap-2 text-green-400">
                      <Cpu className="w-3 h-3" />
                      <span>SEO Agent: ACTIVE</span>
                    </div>
                    <div className="flex items-center gap-2 text-green-400">
                      <Bot className="w-3 h-3" />
                      <span>Social Agent: ACTIVE</span>
                    </div>
                  </div>

                  <div className="flex items-center gap-2 pt-4 text-gray-500">
                    <span className="animate-pulse">▋</span>
                    <span>Waiting for command...</span>
                  </div>
                </div>

                {/* Stats Bar */}
                <div className="mt-6 pt-6 border-t border-white/10 grid grid-cols-3 gap-4">
                  <div>
                    <div className="text-2xl font-bold text-cyan-400">20+</div>
                    <div className="text-xs text-gray-500">Skills</div>
                  </div>
                  <div>
                    <div className="text-2xl font-bold text-purple-400">5</div>
                    <div className="text-xs text-gray-500">Agents</div>
                  </div>
                  <div>
                    <div className="text-2xl font-bold text-pink-400">10m</div>
                    <div className="text-xs text-gray-500">Setup</div>
                  </div>
                </div>
              </div>

              {/* Floating Elements */}
              <div className="absolute -top-4 -right-4 w-20 h-20 rounded-2xl bg-gradient-to-br from-purple-600 to-pink-600 flex items-center justify-center animate-float glow-purple">
                <Sparkles className="w-8 h-8 text-white" />
              </div>
              
              <div className="absolute -bottom-6 -left-6 glass rounded-xl p-4 animate-float" style={{ animationDelay: '1s' }}>
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-green-500/20 flex items-center justify-center">
                    <Zap className="w-5 h-5 text-green-400" />
                  </div>
                  <div>
                    <div className="text-sm font-medium">Project Shipped</div>
                    <div className="text-xs text-gray-500">Just now</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
