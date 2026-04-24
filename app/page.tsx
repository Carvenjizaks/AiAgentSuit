"use client";

import { useEffect, useState } from "react";
import Hero from "./components/Hero";
import BeforeAfter from "./components/BeforeAfter";
import Features from "./components/Features";
import Proof from "./components/Proof";
import SkillsShowcase from "./components/SkillsShowcase";
import Pricing from "./components/Pricing";
import FAQ from "./components/FAQ";
import CTA from "./components/CTA";
import Footer from "./components/Footer";
import Navigation from "./components/Navigation";

export default function Home() {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) return null;

  return (
    <main className="relative min-h-screen overflow-x-hidden">
      {/* Background Effects */}
      <div className="fixed inset-0 z-0">
        <div className="absolute inset-0 bg-[#0a0a0f]" />
        <div className="absolute inset-0 grid-pattern opacity-50" />
        
        {/* Gradient orbs */}
        <div className="absolute top-0 left-1/4 w-[600px] h-[600px] bg-purple-600/20 rounded-full blur-[150px] animate-pulse-glow" />
        <div className="absolute top-1/3 right-0 w-[500px] h-[500px] bg-cyan-500/15 rounded-full blur-[130px] animate-pulse-glow" style={{ animationDelay: '1s' }} />
        <div className="absolute bottom-0 left-1/3 w-[700px] h-[700px] bg-pink-600/10 rounded-full blur-[180px] animate-pulse-glow" style={{ animationDelay: '2s' }} />
      </div>

      {/* Content */}
      <div className="relative z-10">
        <Navigation />
        <Hero />
        <BeforeAfter />
        <Features />
        <Proof />
        <SkillsShowcase />
        <Pricing />
        <FAQ />
        <CTA />
        <Footer />
      </div>
    </main>
  );
}
