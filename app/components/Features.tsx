"use client";

import { useEffect, useRef, useState } from "react";
import { 
  Zap, 
  Brain, 
  Users, 
  Workflow, 
  Layers, 
  Shield,
  ArrowRight
} from "lucide-react";

export default function Features() {
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
    {
      icon: Zap,
      title: "Ship In Hours, Not Weeks",
      description: "Pre-built project scaffolds, specialist agents, and workflows take you from idea to LIVE in a single sitting.",
      color: "from-yellow-400 to-orange-500",
    },
    {
      icon: Brain,
      title: "Never Start From Scratch",
      description: "Every conversation starts exactly where you left off. Your context, brand voice, project history — all preserved.",
      color: "from-purple-400 to-pink-500",
    },
    {
      icon: Users,
      title: "Team Of AI Agents",
      description: "Deploy multiple agents in parallel. One builds, one writes, one reviews, one designs — all simultaneously.",
      color: "from-cyan-400 to-blue-500",
    },
    {
      icon: Workflow,
      title: "Battle-Tested Commands",
      description: "No guessing what to type. Run proven workflows refined over thousands of hours of real use.",
      color: "from-green-400 to-emerald-500",
    },
    {
      icon: Layers,
      title: "Everything Connected",
      description: "Stripe, Gmail, Calendar, Slack, Vercel, Supabase, Sendiio... all connected. One command does it all.",
      color: "from-pink-400 to-rose-500",
    },
    {
      icon: Shield,
      title: "Gets Smarter Over Time",
      description: "Persistent memory and self-improving loop. Month 3 is dramatically faster than month 1.",
      color: "from-indigo-400 to-violet-500",
    },
  ];

  return (
    <section ref={sectionRef} id="features" className="py-24 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div
          className={`text-center mb-16 transition-all duration-700 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          <h2 className="font-[family-name:var(--font-space)] text-3xl sm:text-4xl lg:text-5xl font-bold mb-6">
            What This Actually Means{" "}
            <span className="text-gradient">For You</span>
          </h2>
          <p className="text-gray-400 text-lg max-w-2xl mx-auto">
            This isn&apos;t theory. These are the exact capabilities that let you 
            ship projects in hours instead of weeks.
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((feature, index) => (
            <div
              key={feature.title}
              className={`group relative transition-all duration-700 ${
                isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
              }`}
              style={{ transitionDelay: `${index * 100}ms` }}
            >
              <div className="relative h-full glass rounded-2xl p-6 hover:bg-white/10 transition-all duration-300 overflow-hidden">
                {/* Hover gradient */}
                <div className={`absolute inset-0 bg-gradient-to-br ${feature.color} opacity-0 group-hover:opacity-5 transition-opacity duration-300`} />
                
                {/* Icon */}
                <div className={`w-12 h-12 rounded-xl bg-gradient-to-br ${feature.color} flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300`}>
                  <feature.icon className="w-6 h-6 text-white" />
                </div>

                {/* Content */}
                <h3 className="font-[family-name:var(--font-space)] text-xl font-bold mb-3 group-hover:text-cyan-400 transition-colors">
                  {feature.title}
                </h3>
                <p className="text-gray-400 text-sm leading-relaxed">
                  {feature.description}
                </p>

                {/* Arrow */}
                <div className="mt-4 flex items-center gap-2 text-cyan-400 opacity-0 group-hover:opacity-100 transition-opacity">
                  <span className="text-sm font-medium">Learn more</span>
                  <ArrowRight className="w-4 h-4" />
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
