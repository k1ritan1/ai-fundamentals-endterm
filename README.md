# USSC Daedalus: Autonomous Subsystem Emergency Reboot Manual
**Course Title:** AIF1303 Artificial Intelligence Fundamentals  
**Academic Program:** Bachelor of Science in Physical AI and Robotics & AI / Machine Learning  
**Capstone Assessment:** Creative Project (40% of Final Course Grade)  
**Format:** Standalone Interactive Digital Book, Interactive Presentation Slide Deck, & Defense Dossier  

---

## 1. Project Overview & Creative Theme

This project delivers an interactive, mathematically rigorous, and creative AI textbook framed as the **Shipboard Emergency Reboot Manual** for the deep-space colony transport vessel *USSC Daedalus*.

Following primary fusion conduit failures and structural hull breaches in the Kepler Belt, the central cognitive executive is offline. Engineering personnel must execute emergency recovery protocols across four core shipboard modules, systematically deploying the foundational algorithms of Artificial Intelligence to restore autonomous navigation, power distribution, kinetic defense, reactor cooling, damage tracking, atmospheric diagnostics, and cognitive core persona alignment.

### Grounded Physical AI Focus
Unlike standard textbooks that treat algorithms as frictionless abstractions, every chapter evaluates methods under physical robotic realities:
- **Embedded Compute Budgets:** Microcontroller RAM limits (ARM Cortex-M7 with 512 KB SRAM, Xilinx UltraScale+ FPGAs, Nvidia Jetson Orin NPUs).
- **Hard Real-Time Latencies:** Fire-control cycle deadlines (40 ms), optical docking servo rates (30 ms), and telemetry filtering intervals (20 ms).
- **Physical Actuator Dynamics:** Motor gimbal slew rates (180 deg/s), non-linear thermal inertia, and valve delay hysteresis.
- **Sensor Noise & Failure:** Ultrasonic transducer noise, acoustic attenuation through bulkheads, and gas chromatograph drift.
- **Safety Criticality:** Hardware interlocks, Control Barrier Functions (CBFs), and cost-sensitive classification ensuring zero human crew fatalities.

---

## 2. Deliverables Directory

The repository contains four complete project deliverables satisfying all assignment requirements:

```
.
├── index.html                  # Deliverable 1: Complete 11,514-word interactive book with 7 live simulation engines
├── presentation.html           # Deliverable 2: 12-slide oral defense presentation with speaker notes
├── defense_guide.md            # Deliverable 3: 10-minute presentation script & 25-question oral defense Q&A bank
├── ai_use_declaration.md       # Deliverable 4: Official AI Use Declaration Form
├── css/
│   └── manual.css              # Industrial Spacecraft HUD stylesheet (WCAG AAA contrast, Dark/Light modes, Print PDF)
├── js/
│   └── simulations.js          # 7 Standalone interactive simulation engines
├── scripts/
│   ├── build_book.py           # Modular book compiler
│   ├── verify_book.py          # Automated compliance and anti-slop linter
│   └── content/                # Modular chapter sources (Ch 1 through Ch 7, Frontmatter, Backmatter)
└── README.md                   # Project documentation and evaluation guide
```

---

## 3. Syllabus Mapping & Chapter Architecture

The manual covers the complete 10-week curriculum of AIF1303 across 7 chapters (11,514 words across chapters, ~1,500 to 1,770 words each):

| Chapter | Syllabus Week | Technical Scope | Physical AI Subsystem | Interactive Simulation |
| :--- | :--- | :--- | :--- | :--- |
| **Chapter 1** | Weeks 1 to 2 | PEAS framework, state space, BFS, DFS, UCS, A* search, heuristic admissibility, consistency, and dominance proofs. | Exterior Hull Repair Crawler Alpha-1 | **Simulation 1.1:** 12x12 Hull Grid Pathfinder (BFS, DFS, UCS, A* with Manhattan/Euclidean heuristics) |
| **Chapter 2** | Week 3 | Local search (Hill Climbing, Simulated Annealing), CSP formalization, AC-3 arc consistency, Backtracking, MRV, and LCV. | Auxiliary Power Grid Matrix | **Simulation 2.1:** Subsystem Bus Allocation Sandbox (Backtracking AC-3 vs Local Hill Climbing) |
| **Chapter 3** | Week 4 | Adversarial zero-sum games, Minimax recursion, Alpha-Beta pruning proof, and Expectimax chance modeling. | Cargo Bay 3 Defense Sentry Turrets | **Simulation 3.1:** Adversarial Sentry Game Tree Visualizer (Minimax vs Alpha-Beta node cutoffs) |
| **Chapter 4** | Week 5 | Markov Decision Processes (MDPs), Bellman optimality, Value Iteration contraction, and Q-Learning. | Tokamak Reactor Coolant Loop | **Simulation 4.1:** Reactor Thermal Grid-World (Value Iteration heatmap vs live Q-Learning agent) |
| **Chapter 5** | Weeks 6 to 7 | Axioms of probability, Bayes' rule, Bayesian networks, d-separation, and HMM Forward Filtering. | Structural Backbone Sensor Mesh | **Simulation 5.1:** Sequential HMM Tracker (Forward belief filtering with noisy sensor updates) |
| **Chapter 6** | Week 8 | Utility theory (von Neumann-Morgenstern), MEU, Naive Bayes, Linear classifiers, and Cost-sensitive Confusion Matrix. | Habitation Ring Gas Chromatographs | **Simulation 6.1:** Atmospheric Fault Classifier & Confusion Matrix (Precision/Recall vs Safety Penalty) |
| **Chapter 7** | Weeks 9 to 10 | McCulloch-Pitts neurons, Perceptron learning, XOR barrier, MLPs, Backpropagation, Transformers (Self-Attention), AI Safety. | Docking Guidance Vision & AI Executive | **Simulation 7.1:** Docking Neural Classifier (Linear vs XOR) & Constitutional AI Command Sanitizer |

---

## 4. Structured 5-Part Section Pattern per Chapter

Every chapter adheres strictly to the required five-part structure:
1. **System Emergency Briefing (~150 words):** In-universe spacecraft failure scenario and operational urgency.
2. **Theoretical Foundation & Mathematical Formulation (~600+ words):** Rigorous academic definitions, LaTeX equations, variables, and theorems.
3. **Algorithmic Execution / Pseudo-code (~500+ words):** Step-by-step logic, data structures, complexity tables ($O$-notation), and physical robotics constraints.
4. **Interactive Simulation Module (~200 words + embedded widget):** Playable canvas or interactive controls directly connected to the mathematical formulation.
5. **Academic Post-Mortem & Citations (~150 words):** Real-world scholarly literature citations synthesizing foundational theory with physical operations.

---

## 5. Mandatory Academic Literature Integration

All required course texts are cited, discussed, and synthesized across every chapter:
- **Russell, S. J., & Norvig, P. (2020).** *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. (Cited 8 times across Chapters 1, 2, 3, 4, 5, 6, 7, and Bibliography).
- **Zerilli, J. (2021).** *A Citizen's Guide to Artificial Intelligence*. MIT Press. (Cited 5 times across Chapters 1, 3, 6, 7, and Bibliography).
- **Louwerse, M. M. (2021).** *Understanding Artificial Minds through Human Minds*. Routledge. (Cited 6 times across Chapters 1, 2, 4, 5, 7, and Bibliography).
- **Foundational Seminal Literature:** Hart, Nilsson, & Raphael (1968); Kirkpatrick et al. (1983); Knuth & Moore (1975); Bellman (1957); Watkins & Dayan (1992); Pearl (1988); Rabiner (1989); McCulloch & Pitts (1943); Minsky & Papert (1969); Vaswani et al. (2017); Amodei et al. (2016).

---

## 6. Anti-Slop Stylistic & Architectural Compliance

This project was built under strict adherence to the Anti-Slop design and copywriting filters:
- **Rule R-02 (Zero Em Dashes):** Verified zero occurrences of the em dash character (``) across all project files.
- **Rule R-16 (Zero Buzzwords):** Zero empty marketing buzzwords (*delve*, *showcase*, *elevate*, *game-changer*, *seamless*, *cutting-edge*, *revolutionary*, *tapestry*).
- **Rule R-21 & R-34 (Dual Working Themes):** 100% functional Dark HUD Mode and Light Laboratory Mode with verified contrast ratios exceeding WCAG AA standards.
- **Rule R-26 & R-32 (Accessible Interactivity):** Every button and slider is operable, displays `cursor: pointer`, maintains `:focus-visible` styling, and functions with keyboard navigation.
- **Print / PDF Layout:** Includes a complete `@media print` stylesheet with clean page breaks, unclipped code blocks, and crisp black-and-white typography for generating a 35-page PDF manual.

---

## 7. How to Run & Verify

### Viewing the Interactive Book
Open `index.html` directly in any modern web browser, or launch a local static server:
```bash
python3 -m http.server 8000
```
Navigate to `http://localhost:8000` to interact with the full book and its 7 simulation engines.

### Viewing the Oral Defense Presentation Deck
Open `presentation.html` in any browser:
- Use **Left/Right Arrow keys**, **Space**, or on-screen buttons to change slides.
- Press **N** or click **Speaker Notes** to toggle the oral presentation talking points drawer.
- Click **Return to Interactive Book** to jump to the text.

### Deploying to Render.com
This repository includes a `render.yaml` specification for immediate static site deployment:
1. Connect this GitHub repository on [dashboard.render.com](https://dashboard.render.com).
2. Create a new **Static Site** (or select **Blueprint** to use `render.yaml`).
3. Set the build settings:
   - **Build Command:** `python3 scripts/build_book.py`
   - **Publish Directory:** `.`
4. Deploy. Render serves both `index.html` (the interactive reboot manual) and `presentation.html` (the companion defense slide deck) on a public HTTPS URL.

### Running the Automated Verification Audit
Run the automated verification script to audit word counts, section headers, anti-slop rules, and literature citations:
```bash
python3 scripts/verify_book.py index.html
```

---

## 8. Academic Integrity Certification

All conceptual architectures, mathematical derivations, simulation logic, and oral defense guides have been verified for technical correctness and academic honesty. Complete AI tool version records, prompt sequences, manual refinements, and validation methodologies are documented in `ai_use_declaration.md`.
