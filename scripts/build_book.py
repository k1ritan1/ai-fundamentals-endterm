#!/usr/bin/env python3
"""
Master Builder for USSC Daedalus Emergency Reboot Manual.
Assembles HTML shell, sidebar navigation, modular chapters, search modal, and simulation scripts into index.html.
"""

import sys
import os

# Import modules
from content.frontmatter import FRONTMATTER_HTML
from content.ch1 import CH1_HTML
from content.ch2 import CH2_HTML
from content.ch3 import CH3_HTML
from content.ch4 import CH4_HTML
from content.ch5 import CH5_HTML
from content.ch6 import CH6_HTML
from content.ch7 import CH7_HTML
from content.backmatter import BACKMATTER_HTML

TOPBAR_HTML = """
<header class="topbar">
  <div style="display: flex; align-items: center; gap: 0.75rem;">
    <button id="menu-toggle" class="menu-toggle" aria-label="Toggle navigation menu" aria-expanded="false">&#9776;</button>
    <a href="#overview" class="topbar-brand">
      <span class="status-beacon"></span>
      <span style="color: var(--accent-amber-bright);">USSC DAEDALUS</span>
      <span style="color: var(--text-muted);">//</span>
      <span>EMERGENCY MANUAL</span>
    </a>
  </div>
  <div class="topbar-telemetry-strip">
    <span class="telemetry-tag">STAGE 4 // DECK REBOOT</span>
    <span id="live-met-clock" class="telemetry-tag">MET: +142d 08:34:12</span>
    <span class="telemetry-tag" style="color: var(--status-nominal-bright);">INTEGRITY: 88.4%</span>
  </div>
  <div class="topbar-actions">
    <button id="panel-toggle-btn" class="btn-secondary" aria-label="Toggle navigation panel (Hotkey: [ )" title="Toggle navigation panel (Hotkey: [ )">
      <span id="panel-toggle-icon">&#x25F0;</span>
      <span id="panel-toggle-text">Panels: ON</span>
    </button>
    <button id="audio-toggle-btn" class="btn-secondary" aria-label="Toggle avionics sound effects">
      <span id="audio-icon">&#128263;</span>
      <span>SFX: OFF</span>
    </button>
    <button id="search-palette-btn" class="btn-secondary" aria-label="Open search index command palette">
      <span style="font-family: var(--font-mono); font-size: 0.76rem; color: var(--accent-amber-bright); font-weight: bold;">&#8984;K</span>
      <span>Search</span>
    </button>
    <button id="theme-toggle" class="btn-secondary" aria-label="Toggle Dark and Light theme">Theme: Dark HUD</button>
    <button id="fullscreen-btn" class="btn-secondary" aria-label="Toggle Fullscreen">&#x26F6; Fullscreen</button>
    <a href="presentation.html" class="btn-secondary" target="_blank" rel="noopener">Defense Deck</a>
    <a href="#submission-declaration" class="btn-primary">AI Declaration</a>
  </div>
</header>
"""

SIDEBAR_HTML = """
<nav class="sidebar" id="sidebar" aria-label="Manual Table of Contents">
  <div class="sidebar-progress-card">
    <div class="progress-header">
      <span>REBOOT SEQUENCE</span>
      <span style="color: var(--status-nominal-bright); font-weight: bold;">7/7 COMPLETE</span>
    </div>
    <div class="progress-bar-track">
      <div class="progress-bar-fill"></div>
    </div>
    <div class="sidebar-telemetry-grid">
      <div class="telemetry-cell">
        <span class="cell-label">CORE TEMP</span>
        <span class="cell-val">840 K</span>
      </div>
      <div class="telemetry-cell">
        <span class="cell-label">SRAM USAGE</span>
        <span class="cell-val">48 / 512 KB</span>
      </div>
      <div class="telemetry-cell">
        <span class="cell-label">BUS LATENCY</span>
        <span class="cell-val">2.4 ms</span>
      </div>
      <div class="telemetry-cell">
        <span class="cell-label">LINK</span>
        <span class="cell-val" style="color: var(--status-nominal-bright);">CAN-2.0B</span>
      </div>
    </div>
  </div>

  <div class="nav-group-title">Command Overview</div>
  <a href="#overview" class="nav-link active">
    <span class="nav-chapter-num">0.0</span>
    <span>Operational Briefing</span>
  </a>

  <div class="nav-group-title">Module 1: Navigation &amp; Hull Clearance</div>
  <a href="#chapter-1" class="nav-link">
    <span class="nav-chapter-num">CH 1</span>
    <span>Sensory Array &amp; Space Mapping</span>
    <span class="nav-status-pill">[ONLINE]</span>
  </a>
  <a href="#chapter-2" class="nav-link">
    <span class="nav-chapter-num">CH 2</span>
    <span>Breach Avoidance Routing</span>
    <span class="nav-status-pill">[ONLINE]</span>
  </a>

  <div class="nav-group-title">Module 2: Power &amp; Subsystem Defense</div>
  <a href="#chapter-3" class="nav-link">
    <span class="nav-chapter-num">CH 3</span>
    <span>Power Grid Allocation CSP</span>
    <span class="nav-status-pill">[ONLINE]</span>
  </a>
  <a href="#chapter-4" class="nav-link">
    <span class="nav-chapter-num">CH 4</span>
    <span>Subsystem Defense Protocols</span>
    <span class="nav-status-pill">[ONLINE]</span>
  </a>

  <div class="nav-group-title">Module 3: Environmental Control &amp; Tracking</div>
  <a href="#chapter-5" class="nav-link">
    <span class="nav-chapter-num">CH 5</span>
    <span>Reactor Coolant RL &amp; MDPs</span>
    <span class="nav-status-pill">[ONLINE]</span>
  </a>
  <a href="#chapter-6" class="nav-link">
    <span class="nav-chapter-num">CH 6</span>
    <span>Sensor Damage &amp; Tracking HMMs</span>
    <span class="nav-status-pill">[ONLINE]</span>
  </a>

  <div class="nav-group-title">Module 4: Diagnostics &amp; Core Reboot</div>
  <a href="#chapter-7" class="nav-link">
    <span class="nav-chapter-num">CH 7</span>
    <span>Autonomous Diagnostics &amp; Safety</span>
    <span class="nav-status-pill">[ONLINE]</span>
  </a>

  <div class="nav-group-title">Reference &amp; Verification</div>
  <a href="#master-bibliography" class="nav-link">
    <span class="nav-chapter-num">APP</span>
    <span>Hardware Specs &amp; Bibliography</span>
  </a>
  <a href="#submission-declaration" class="nav-link">
    <span class="nav-chapter-num">DOC</span>
    <span>Course AI Use Declaration</span>
  </a>
</nav>
"""

SEARCH_MODAL_HTML = """
<div id="search-modal-backdrop" class="search-modal-backdrop" role="dialog" aria-modal="true" aria-label="Command search palette">
  <div class="search-modal">
    <div class="search-input-wrapper">
      <span style="font-family: var(--font-mono); color: var(--accent-amber-bright); margin-right: 0.6rem; font-weight: bold;">&gt;</span>
      <input type="text" id="search-palette-input" class="search-input" placeholder="Search chapters, algorithms, formulas, hardware specs (e.g. A*, AC-3, HMM, Bellman, FP16)..." aria-label="Search manual documentation">
      <button id="search-close-btn" class="btn-secondary" style="padding: 0.2rem 0.5rem;" aria-label="Close search modal">ESC</button>
    </div>
    <ul id="search-results-list" class="search-results-list" role="listbox">
      <!-- Populated dynamically via JS search index -->
    </ul>
  </div>
</div>
"""

MATH_INIT_SCRIPT = """
  <script>
    window.retriggerMathRendering = function() {
      if (typeof renderMathInElement === 'function' && typeof katex !== 'undefined') {
        try {
          const opts = {
            delimiters: [
              {left: '$$', right: '$$', display: true},
              {left: String.fromCharCode(92) + '[', right: String.fromCharCode(92) + ']', display: true},
              {left: '$', right: '$', display: false},
              {left: String.fromCharCode(92) + '(', right: String.fromCharCode(92) + ')', display: false}
            ],
            ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
            throwOnError: false
          };
          renderMathInElement(document.body, opts);
          // Explicitly scan all tables, table cells, headers, and badges
          document.querySelectorAll('table, th, td, .specs-table th, .specs-table td, .diagram-header span, .diagram-caption, .formula-label, .definition-box').forEach(function(el) {
            renderMathInElement(el, opts);
          });
        } catch (e) {
          console.warn('Math typesetting caught error:', e);
        }
      }
    };
  </script>
"""

HTML_TEMPLATE = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark" class="dark-hud">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>USSC Daedalus: Autonomous Subsystem Emergency Reboot Manual (AIF1303)</title>
  <meta name="description" content="AI Fundamentals EndTerm Capstone Manual. Complete engineering guide covering PEAS, search, CSPs, minimax, MDPs, Q-learning, Bayesian networks, HMMs, classification, neural nets, and AI safety.">
  <link rel="stylesheet" href="css/manual.css">
  
  {MATH_INIT_SCRIPT}

  <!-- KaTeX for crisp mathematical typography (local offline with fallback) -->
  <link rel="stylesheet" href="vendor/katex/katex.min.css">
  <script defer src="vendor/katex/katex.min.js"></script>
  <script defer src="vendor/katex/auto-render.min.js"
    onload="window.retriggerMathRendering && window.retriggerMathRendering();"></script>
</head>
<body>
  {TOPBAR_HTML}
  {SEARCH_MODAL_HTML}

  <div class="app-container">
    {SIDEBAR_HTML}

    <main class="main-content">
      {FRONTMATTER_HTML}
      {CH1_HTML}
      {CH2_HTML}
      {CH3_HTML}
      {CH4_HTML}
      {CH5_HTML}
      {CH6_HTML}
      {CH7_HTML}
      {BACKMATTER_HTML}
    </main>
  </div>

  <button id="panel-restore-btn" class="panel-restore-pill" aria-label="Restore navigation panel" title="Restore navigation panel (Hotkey: [ )">
    <span class="pill-icon">&#x25F0;</span>
    <span>RESTORE PANELS</span>
    <span class="pill-hotkey">[</span>
  </button>

  <script src="js/simulations.js"></script>
</body>
</html>
"""

def build():
    output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "index.html"))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE)
    print(f"Successfully assembled book to {output_path}")

if __name__ == "__main__":
    build()
