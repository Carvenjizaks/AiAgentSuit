"use client";

import { useEffect, useRef, useState } from "react";
import { ChevronDown } from "lucide-react";

export default function FAQ() {
  const [isVisible, setIsVisible] = useState(false);
  const [openIndex, setOpenIndex] = useState<number | null>(0);
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

  const faqs = [
    {
      question: "What exactly is the AI Agent Suit?",
      answer: "It's a complete, pre-configured OpenClaw environment with 20+ skills, 5 AI agent templates, and all integrations set up. Think of it as cloning my entire AI workspace onto your machine. One command installs everything.",
    },
    {
      question: "Do I need to be technical to use this?",
      answer: "Basic command line familiarity helps, but you don't need to be a developer. The Suit-Up Session walks you through everything step by step. Most users are shipping projects within 24 hours of setup.",
    },
    {
      question: "What models does it support?",
      answer: "The Suit is model-agnostic. It works with Kimi (Moonshot), OpenAI (GPT-4, GPT-3.5), and Claude. You're not locked into any single provider — use the best model for each task.",
    },
    {
      question: "How is this different from just using ChatGPT or Claude?",
      answer: "ChatGPT and Claude are chatbots. The Suit is a complete operating system. It has persistent memory, parallel agents, 20+ specialized skills, and direct integrations with your tools. It's the difference between a calculator and a spreadsheet.",
    },
    {
      question: "What kind of projects can I build?",
      answer: "Newsletters, landing pages, client websites, social media campaigns, email sequences, data analysis, travel itineraries, lead magnets, sales funnels — if it involves content, code, or creativity, the Suit can handle it.",
    },
    {
      question: "Is this a subscription?",
      answer: "No. It's a one-time purchase. You get the complete setup, lifetime updates to the skills, and 30 days of direct support via Telegram.",
    },
    {
      question: "What do I need to get started?",
      answer: "A computer (Mac, Windows, or Linux), an OpenClaw installation, and API keys for the AI models you want to use (Kimi, OpenAI, or Claude). The Suit-Up Session covers all of this.",
    },
    {
      question: "Can I get a refund?",
      answer: "Yes. If you go through the setup, attend the Suit-Up Session, and still can't ship a project in 30 days, I'll refund you in full. But I'll also personally help you build something first.",
    },
  ];

  return (
    <section ref={sectionRef} id="faq" className="py-24 px-4 sm:px-6 lg:px-8">
      <div className="max-w-3xl mx-auto">
        {/* Header */}
        <div
          className={`text-center mb-16 transition-all duration-700 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          <h2 className="font-[family-name:var(--font-space)] text-3xl sm:text-4xl lg:text-5xl font-bold mb-6">
            Questions?{" "}
            <span className="text-gradient">Answered.</span>
          </h2>
          <p className="text-gray-400 text-lg">
            Everything you need to know before getting started.
          </p>
        </div>

        {/* FAQ List */}
        <div className="space-y-4">
          {faqs.map((faq, index) => (
            <div
              key={index}
              className={`transition-all duration-700 ${
                isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
              }`}
              style={{ transitionDelay: `${index * 50}ms` }}
            >
              <div
                className={`glass rounded-2xl overflow-hidden transition-all duration-300 ${
                  openIndex === index ? "bg-white/10" : "hover:bg-white/5"
                }`}
              >
                <button
                  onClick={() => setOpenIndex(openIndex === index ? null : index)}
                  className="w-full flex items-center justify-between p-6 text-left"
                >
                  <span className="font-semibold pr-4">{faq.question}</span>
                  <ChevronDown
                    className={`w-5 h-5 text-cyan-400 shrink-0 transition-transform duration-300 ${
                      openIndex === index ? "rotate-180" : ""
                    }`}
                  />
                </button>
                <div
                  className={`overflow-hidden transition-all duration-300 ${
                    openIndex === index ? "max-h-96" : "max-h-0"
                  }`}
                >
                  <p className="px-6 pb-6 text-gray-400 leading-relaxed">
                    {faq.answer}
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
