"use client";

import { Zap, Mail, GitFork, X } from "lucide-react";

export default function Footer() {
  const currentYear = new Date().getFullYear();

  const footerLinks = {
    Product: [
      { label: "Features", href: "#features" },
      { label: "Skills", href: "#skills" },
      { label: "Pricing", href: "#pricing" },
      { label: "FAQ", href: "#faq" },
    ],
    Resources: [
      { label: "Documentation", href: "#" },
      { label: "GitHub", href: "https://github.com/Carvenjizaks/AiAgentSuit" },
      { label: "Docs", href: "#" },
    ],
    Company: [
      { label: "About", href: "#" },
      { label: "Contact", href: "#" },
      { label: "Terms", href: "#" },
      { label: "Privacy", href: "#" },
    ],
  };

  const socialLinks = [
    { icon: X, href: "#", label: "X" },
    { icon: GitFork, href: "https://github.com/Carvenjizaks/AiAgentSuit", label: "GitHub" },
    { icon: Mail, href: "mailto:hello@aiagentsuit.com", label: "Email" },
  ];

  return (
    <footer className="py-16 px-4 sm:px-6 lg:px-8 border-t border-white/5">
      <div className="max-w-7xl mx-auto">
        <div className="grid md:grid-cols-2 lg:grid-cols-5 gap-12 mb-12">
          {/* Brand */}
          <div className="lg:col-span-2">
            <a href="#" className="flex items-center gap-2 mb-4">
              <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-400 to-purple-600 flex items-center justify-center">
                <Zap className="w-5 h-5 text-white" />
              </div>
              <span className="font-[family-name:var(--font-space)] font-bold text-xl">
                AI Agent<span className="text-cyan-400">Suit</span>
              </span>
            </a>
            <p className="text-gray-400 text-sm max-w-xs mb-6">
              Pre-configured AI environment with 20+ skills and multi-agent
              orchestration. Deploy in 10 minutes.
            </p>
            <div className="flex items-center gap-4">
              {socialLinks.map((social) => (
                <a
                  key={social.label}
                  href={social.href}
                  className="w-10 h-10 rounded-full glass flex items-center justify-center text-gray-400 hover:text-white hover:bg-white/10 transition-all"
                  aria-label={social.label}
                >
                  <social.icon className="w-5 h-5" />
                </a>
              ))}
            </div>
          </div>

          {/* Links */}
          {Object.entries(footerLinks).map(([category, links]) => (
            <div key={category}>
              <h3 className="font-semibold mb-4">{category}</h3>
              <ul className="space-y-3">
                {links.map((link) => (
                  <li key={link.label}>
                    <a
                      href={link.href}
                      className="text-gray-400 text-sm hover:text-white transition-colors"
                    >
                      {link.label}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        {/* Bottom */}
        <div className="pt-8 border-t border-white/5 flex flex-col sm:flex-row items-center justify-between gap-4">
          <p className="text-gray-500 text-sm">
            © {currentYear} AI Agent Suit. All rights reserved.
          </p>
          <p className="text-gray-600 text-sm">
            Built with{" "}
            <span className="text-gray-500">AI</span>
          </p>
        </div>
      </div>
    </footer>
  );
}
