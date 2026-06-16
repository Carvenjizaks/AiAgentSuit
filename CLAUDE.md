# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Warning: Unfamiliar Next.js Version

This project uses Next.js 14 with the App Router. APIs, conventions, and file structure may differ from training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.

## Commands

```bash
npm run dev      # Start development server (localhost:3000)
npm run build    # Production build
npm start        # Start production server
npm run lint     # Run ESLint
```

There are no tests in this project.

## Architecture

This is a **single-page marketing website** — one route (`app/page.tsx`), no API routes, no backend. All content is rendered client-side.

### Page Structure

`app/page.tsx` is a `"use client"` component that renders all sections in order: Navigation → Hero → BeforeAfter → Features → Proof → SkillsShowcase → Pricing → FAQ → CTA → Footer. It guards against hydration mismatches with a `useState`/`useEffect` mount check that returns `null` until client-side.

Each section is its own component in `app/components/`. Navigation uses anchor links to section IDs (`#features`, `#pricing`, etc.) — there is no client-side router navigation.

### Design System

All visual conventions are established via Tailwind utilities defined in `app/globals.css`:

- **Colors**: cyan (`#22d3ee`), purple (`#a855f7`), pink (`#ec4899`) on a near-black background (`#0a0a0f`)
- **`.text-gradient`**: Gradient text spanning cyan → purple → pink using `bg-clip-text`
- **`.glass` / `.glass-dark`**: Frosted glass cards via `bg-white/5 backdrop-blur-xl border border-white/10`
- **`.glow-cyan` / `.glow-purple`**: Box-shadow glow effects
- **Animations**: `gradient-shift` (8s), `float` (6s, -20px Y), `pulse-glow` (3s opacity) — all defined as `@keyframes` in globals.css

Icon library is `lucide-react`. Do not introduce other icon libraries.

### Animation Pattern

Components use `IntersectionObserver` (via `useRef` + `useEffect`) to trigger reveal animations on scroll. Staggered delays are applied via inline `transitionDelay` styles. This pattern is consistent across Features, Hero, and other sections — follow it when adding new animated sections.

### Fonts

Two fonts loaded via `next/font/google` in `app/layout.tsx`: Inter (body) and Space Grotesk (headings). Available as CSS variables `--font-inter` and `--font-space`, applied to `<body>` as Tailwind classes.

### Configuration Notes

- `next.config.js` has `images.unoptimized: true` — keep this for static export compatibility
- ESLint uses v9 flat config (`eslint.config.mjs`) — do not create `.eslintrc.*` files
- No Prettier configured; maintain existing code style manually
