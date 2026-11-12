# USSC Daedalus: Autonomous Subsystem Emergency Reboot Manual
## Design System & Avionics Component Architecture Rules (MIL-STD-1472 / AIF-1303)

This rules document governs the visual hierarchy, component architecture, design tokens, and technical implementation for the *USSC Daedalus Emergency Reboot Manual* web application and companion defense deck.

---

## 1. Token Definitions

All visual tokens are defined as CSS Custom Properties in `css/manual.css` under the `:root` pseudo-class (Dark HUD) and `[data-theme="light"]` attribute selector (Diagnostic Cleanroom).

### 1.1 Color Tokens
```css
:root {
  /* Core Slate & Charcoal Canvas (60% Dominant Surface) */
  --bg-primary: #0f141c;              /* Deep space cockpit hull */
  --bg-surface: #151b26;              /* Primary instrumentation panel */
  --bg-surface-elevated: #1d2535;     /* Card elevation and code well */
  --bg-surface-subtle: #252f42;       /* Selected items and hovers */
  
  /* Precision Structural Borders (1px Technical Partitioning) */
  --border-subtle: #283347;          /* Standard divider lines */
  --border-strong: #3b4a63;          /* Interactive component bezels */
  --border-accent: #d97706;          /* Active focus indicator */
  
  /* Readout Typography (Strict WCAG AAA / AA Contrast) */
  --text-primary: #e6edf3;           /* High-luminance digital readout */
  --text-secondary: #94a3b8;         /* Subsystem prose and descriptions */
  --text-muted: #64748b;             /* De-emphasized metadata and timestamps */
  
  /* Functional Alert Accents (Applied with Intention: Max 10% Surface) */
  --accent-amber: #d97706;           /* Primary tactical accent (Warning / Active) */
  --accent-amber-bright: #f59e0b;    /* High-intensity illuminated state */
  --accent-amber-bg: rgba(217, 119, 6, 0.12); /* Subtle backlit tint */
  
  --accent-cobalt: #2563eb;          /* Secondary navigation / diagnostic blue */
  --accent-cobalt-bright: #3b82f6;   /* Active flight path marker */
  --accent-cobalt-bg: rgba(37, 99, 235, 0.12);
  
  /* Subsystem Telemetry LED States */
  --status-nominal: #059669;         /* Subsystem restored / test passed */
  --status-nominal-bright: #10b981;  /* Blinking beacon pulse */
  --status-nominal-bg: rgba(16, 185, 129, 0.12);
  
  --status-critical: #dc2626;        /* System failure / hull breach alert */
  --status-critical-bright: #ef4444; /* Emergency strobe color */
  --status-critical-bg: rgba(239, 68, 68, 0.14);
}

/* Clinical Laboratory Light Mode */
[data-theme="light"] {
  --bg-primary: #f8fafc;
  --bg-surface: #ffffff;
  --bg-surface-elevated: #f1f5f9;
  --bg-surface-subtle: #e2e8f0;
  
  --border-subtle: #cbd5e1;
  --border-strong: #94a3b8;
  --border-accent: #b45309;
  
  --text-primary: #0f172a;           /* Deep ink navy (Contrast > 14:1) */
  --text-secondary: #334155;
  --text-muted: #475569;
  
  --accent-amber: #b45309;
  --accent-amber-bright: #d97706;
  --accent-amber-bg: rgba(180, 83, 9, 0.08);
  
  --status-nominal: #047857;
  --status-critical: #b91c1c;
  --status-critical-bg: #fff1f2;
}
```

### 1.2 Typography Tokens
```css
:root {
  /* Technical Monospace: KaTeX math, registers, pseudo-code, telemetry */
  --font-mono: "JetBrains Mono", Consolas, "SF Mono", Menlo, ui-monospace, monospace;
  
  /* Precision Clean Sans: UI controls, headings, body reading copy */
  --font-sans: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  
  /* Fluid Scale */
  --text-xs: 0.72rem;     /* Micro telemetry stamps and hardware specs */
  --text-sm: 0.82rem;     /* Code snippets, table cells, captions */
  --text-base: 0.95rem;   /* Main reading prose */
  --text-lg: 1.15rem;     /* Section sub-headers */
  --text-xl: 1.45rem;     /* Section titles */
  --text-2xl: 1.85rem;    /* Chapter headings */
}
```

### 1.3 Layout & Elevation Tokens
```css
:root {
  --sidebar-width: 300px;
  --topbar-height: 60px;
  --content-max-width: 980px;
  --prose-max-width: 720px; /* Ergonomic 68ch line length cap */
  
  --radius-xs: 2px;
  --radius-sm: 3px;
  --radius-md: 4px;
  
  --shadow-hud: 0 4px 16px rgba(0, 0, 0, 0.45);
  --shadow-modal: 0 16px 48px rgba(0, 0, 0, 0.75);
  --focus-ring: 2px solid var(--accent-amber-bright);
}
```

---

## 2. Component Library

### 2.1 Mission Control Topbar HUD (`<header class="topbar">`)
- **Structure**: Left (Brand & live pulsing LED indicator), Center (Ship registry & telemetry clock), Right (Command search `Cmd+K`, theme toggle, deck link, declaration link).
- **Aesthetic**: Glassmorphism HUD (`rgba(15, 20, 28, 0.92)` with `backdrop-filter: blur(8px)`), sub-pixel bottom border, live Mission Elapsed Time counter (`MET: +142d 08:34:12`).

### 2.2 Flight Management System (FMS) Sidebar (`<nav class="sidebar">`)
- **Structure**: Subsystem recovery tracker (7/7 progress meter), hierarchical module categories, chapter links with status pills (`[ONLINE]`, `[RECOV]`, `[DIAG]`).
- **Interactive State**: Active item marked with illuminated 3px flight-director amber bar, subtle gradient fill, and glowing chapter number badge.

### 2.3 Subsystem Directive Hero Header (`<div class="chapter-hero">`)
- **Structure**: Military declassified stamp, subsystem identifier badge (`PROTOCOL: NAV-PEAS-01`), primary failure telemetry summary table, and chapter title.

### 2.4 System Emergency Briefing (`<div class="briefing-callout">`)
- **Structure**: Urgent in-universe incident report with red hazard border, timestamp stamp, and critical alarm beacon.
- **Rules**: High narrative urgency, strictly 0 em dashes, pure text with zero distracting decorative images.

### 2.5 Blueprint Mathematical Cards (`<div class="math-block">`)
- **Structure**: Dark blueprint background with subtle 16px grid lines, formula classification pill (`EQUATION 1.1 // A* EVALUATION`), centered KaTeX formula, and parameter breakdown legend.
- **Rendering**: Delimiters configured as `$$...$$` (display) and `\(...\)` (inline) using KaTeX auto-render without integrity blockades.

### 2.6 Avionics Console Code Container (`<div class="code-container">`)
- **Structure**: Terminal title bar with 3 window status dots, execution target pill (`TARGET: ARM CORTEX-M7 SRAM`), copy algorithm button, line numbering, and syntax color highlighting.
- **Telemetry Footer**: Asymmetric performance matrix displaying time complexity, space complexity, completeness, and admissibility criteria.

### 2.7 Oscilloscope Image Frames (`<figure class="diagram-frame">`)
- **Structure**: Dark bezel housing with corner crosshair ticks (`+`), diagnostic channel header (`OPTICAL SENSOR FEED // CH-01-A`), explicit dimension image, and formal academic caption.

### 2.8 Glass Cockpit Simulation Modules (`<div class="sim-container">`)
- **Structure**: Tactical control bar with tactile segmented algorithm switches and sliders, high-DPI canvas or responsive SVG tree, and digital flight telemetry instruments updating in real-time.

### 2.9 Quick Search Command Palette (`<div class="search-modal">`)
- **Structure**: High-contrast modal dialog triggered via `Cmd+K` / `Ctrl+K`, real-time filter across 32 subsystem entries, keyboard navigation (`ArrowUp`, `ArrowDown`, `Enter`, `Escape`), and smooth anchor scrolling.

---

## 3. Frameworks & Libraries

- **Markup**: Pure semantic HTML5 (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`).
- **Styles**: Vanilla Modern CSS3 with Custom Properties, CSS Grid, Flexbox, and media queries (`@media print`, `@media (max-width: 1024px)`). Zero heavyweight CSS framework overhead (no Bootstrap, no Tailwind runtime).
- **Mathematics**: KaTeX v0.16.8 (with auto-render extension). Script loading is structured to eliminate race conditions, loaded locally from `vendor/katex/` for instant offline reliability.
- **Interactive Computing**: Vanilla ES6+ JavaScript modules. All 7 simulations calculate real mathematical logic (A* priority queues, AC-3 constraint propagation, alpha-beta cutoffs, Q-learning Bellman updates, HMM forward filtering).

---

## 4. Asset Management

- **Image Manifest**: All 11 assigned academic diagrams are referenced with exact HTTPS URLs, embedded inside `.diagram-frame` containers with explicit `width`, `height`, and descriptive `alt` tags.
- **Local Fallbacks & Verification**: Local verification harness (`scripts/verify_book.py`) confirms all assets are accounted for and render within accessible contrast boundaries.
- **Vector Graphics**: SVGs utilized for tactical tree nodes, crosshairs, and glyphs to guarantee sharp fidelity at any DPI scale.

---

## 5. Icon & Glyph System

- **Design Rule**: Monochrome technical glyphs with functional status accents. No generic pastel icons.
- **Glyph Inventory**:
  - `▲` / `▼`: Tactical status beacons and sorting direction.
  - `+` / `✛`: Oscilloscope coordinate crosshairs.
  - `●`: Pulsing LED state indicators (Green: Restored, Amber: Contested, Red: Critical).
  - `⎋` / `⌘K`: Keyboard hotkey caps.
  - `[` `]`: Segmented bracketed telemetry tags (e.g. `[SEC 1.1]`, `[AIMA-4]`).

---

## 6. Styling Approach & Anti-Slop Enforcement

- **Strict Rule R-02 (Zero Em Dashes)**:
  Under no circumstances may the em dash character (Unicode \\u2014) be used in code, comments, CSS content strings, or prose. Use colons, commas, parentheses, or periods.
- **Strict Rule R-16 (Zero AI Slop Buzzwords)**:
  Marketing filler (*delve*, *showcase*, *elevate*, *game-changer*, *seamless*, *cutting-edge*, *revolutionary*, *tapestry*) is strictly prohibited. Use precise engineering language.
- **Contrast Ratios**: Minimum 4.5:1 for body copy (WCAG AA) and 7:1 for critical telemetry (WCAG AAA).
- **Dial Settings**:
  - `ENERGY: 2` (Calm, authoritative, military command center).
  - `RHYTHM: 2` (Structured, asymmetric telemetry layout with predictable cadence).
  - `MOTION: 1` (Restrained functional motion: 180ms UI transitions, subtle status beacon pulses).

---

## 7. Project Structure & File Map

```
ai-fundamentals-endrerm/
├── index.html                   # Master interactive book manual (11,600+ words, 7 chapters)
├── presentation.html            # Defense presentation deck (12 slides, speaker pop-out, fullscreen)
├── defense_guide.md             # 10-minute presentation script & 25 examination Q&As
├── ai_use_declaration.md        # Course AI declaration of integrity & prompt logs
├── DESIGN_SYSTEM.md             # This comprehensive architecture & design token document
├── README.md                    # Project manual and architecture documentation
├── css/
│   └── manual.css               # Complete MIL-STD avionics design system & light/dark tokens
├── js/
│   └── simulations.js           # 7 deterministic simulation engines & command search palette
├── vendor/
│   └── katex/                   # Local offline KaTeX engine (zero CDN race conditions)
│       ├── katex.min.js
│       ├── auto-render.min.js
│       └── katex.min.css
└── scripts/
    ├── build_book.py            # Automated compiler assembling modules into index.html
    ├── verify_book.py           # Automated audit tool (words, citations, anti-slop, math)
    └── content/                 # Modular 5-part academic chapter content generators
        ├── frontmatter.py
        ├── ch1.py ... ch7.py
        └── backmatter.py
```
