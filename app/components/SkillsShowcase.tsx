"use client";

import { useEffect, useRef, useState } from "react";
import { 
  FileText, 
  Video, 
  Share2, 
  Mail, 
  Search, 
  PenTool,
  BarChart3,
  Plane,
  FileSpreadsheet,
  ShoppingCart,
  Funnel,
  Magnet,
  Code,
  Sparkles
} from "lucide-react";

export default function SkillsShowcase() {
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

  const skills = [
    { icon: FileText, name: "Letterman", category: "Content", description: "Newsletter & article publishing" },
    { icon: Video, name: "VideoCue", category: "Content", description: "Video pipeline & clipping" },
    { icon: Share2, name: "PostStream", category: "Social", description: "Social media automation" },
    { icon: Mail, name: "Sendiio", category: "Marketing", description: "Email & SMS campaigns" },
    { icon: Search, name: "SEO Writer", category: "Content", description: "Search-optimized articles" },
    { icon: PenTool, name: "AEO Optimizer", category: "SEO", description: "AI search engine optimization" },
    { icon: BarChart3, name: "Data Analyst", category: "Analytics", description: "Data visualization & insights" },
    { icon: Plane, name: "Travel Planner", category: "Utility", description: "Trip research & itineraries" },
    { icon: FileSpreadsheet, name: "Spreadsheet Auto", category: "Productivity", description: "Automated data tasks" },
    { icon: ShoppingCart, name: "Affiliate Promo", category: "Marketing", description: "Launch promotion system" },
    { icon: Funnel, name: "Sales Funnel", category: "Marketing", description: "High-converting copy" },
    { icon: Magnet, name: "Lead Magnet", category: "Marketing", description: "Ebook & guide creation" },
    { icon: Code, name: "Web Scraper", category: "Dev", description: "Data extraction tools" },
    { icon: Sparkles, name: "Skill Creator", category: "Meta", description: "Build custom skills" },
  ];

  const categories = [...new Set(skills.map(s => s.category))];

  return (
    <section ref={sectionRef} id="skills" className="py-24 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div
          className={`text-center mb-16 transition-all duration-700 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          <h2 className="font-[family-name:var(--font-space)] text-3xl sm:text-4xl lg:text-5xl font-bold mb-6">
            20+ Specialist{" "}
            <span className="text-gradient">Skills Loaded</span>
          </h2>
          <p className="text-gray-400 text-lg max-w-2xl mx-auto">
            Every skill is pre-configured and ready to deploy. From content creation 
            to marketing automation — it&apos;s all included.
          </p>
        </div>

        {/* Category Pills */}
        <div
          className={`flex flex-wrap justify-center gap-3 mb-12 transition-all duration-700 delay-100 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          {categories.map((category) => (
            <span
              key={category}
              className="px-4 py-2 rounded-full glass text-sm text-gray-300 hover:bg-white/10 transition-colors cursor-pointer"
            >
              {category}
            </span>
          ))}
        </div>

        {/* Skills Grid */}
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
          {skills.map((skill, index) => (
            <div
              key={skill.name}
              className={`group transition-all duration-700 ${
                isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
              }`}
              style={{ transitionDelay: `${index * 50}ms` }}
            >
              <div className="glass rounded-xl p-4 hover:bg-white/10 transition-all duration-300 group-hover:scale-105">
                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-cyan-500/20 to-purple-600/20 flex items-center justify-center shrink-0 group-hover:from-cyan-500 group-hover:to-purple-600 transition-all">
                    <skill.icon className="w-5 h-5 text-cyan-400 group-hover:text-white transition-colors" />
                  </div>
                  <div>
                    <h3 className="font-semibold text-sm mb-1 group-hover:text-cyan-400 transition-colors">
                      {skill.name}
                    </h3>
                    <p className="text-xs text-gray-500">{skill.description}</p>
                    <span className="inline-block mt-2 text-[10px] px-2 py-0.5 rounded-full bg-white/5 text-gray-400">
                      {skill.category}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Bottom Note */}
        <div
          className={`mt-12 text-center transition-all duration-700 delay-500 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          <p className="text-gray-500 text-sm">
            Plus: Multi-model support (Kimi, OpenAI, Claude) • Sub-agent orchestration • ACP harness • Custom skill builder
          </p>
        </div>
      </div>
    </section>
  );
}
