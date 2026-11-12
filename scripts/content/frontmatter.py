# Frontmatter and System Architecture for USSC Daedalus Emergency Reboot Manual

FRONTMATTER_HTML = """
<header class="manual-header" id="overview">
  <div class="topbar-badge">STANDARD OPERATING PROCEDURE // CLASSIFIED ENGINEERING MANUAL</div>
  <h1 class="manual-title">USSC DAEDALUS: Autonomous Subsystem Emergency Reboot Manual</h1>
  <p class="manual-subtitle">Field Engineering Handbook for Physical AI Systems in Deep-Space Transit</p>
  
  <div class="manual-meta-grid">
    <div class="meta-item">
      <span class="meta-label">Course Registry</span>
      <span class="meta-val">AIF1303 AI Fundamentals</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">Academic Program</span>
      <span class="meta-val">B.S. Physical AI &amp; Robotics</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">Curriculum Cycle</span>
      <span class="meta-val">10-Week EndTerm Capstone (40%)</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">Colony Vessel ID</span>
      <span class="meta-val">USSC Daedalus (Registry NX-842)</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">Subsystem Status</span>
      <span class="meta-val" style="color: var(--status-critical-bright);">CRITICAL REBOOT REQUIRED</span>
    </div>
    <div class="meta-item">
      <span class="meta-label">Verification Standard</span>
      <span class="meta-val">ISO/IEC 22989 &amp; Russell-Norvig AIMA</span>
    </div>
  </div>

  <div class="definition-box" style="margin-top: 1.5rem;">
    <div class="definition-title">Operational Context &amp; Purpose of this Manual</div>
    <p>
      At 03:42 shipboard standard time during transit through the Kepler Belt, the colony transport vessel <em>USSC Daedalus</em> sustained secondary debris impacts, triggering emergency isolations across the primary reactor, environmental scrubbers, docking arrays, and autonomous routing conduits. The primary cognitive executive suffered memory corruption and was brought offline.
    </p>
    <p>
      This manual serves as the definitive engineering recovery protocol. It translates core principles of Artificial Intelligence into emergency field procedures. Each module details the mathematical formulation, algorithmic execution, and physical hardware constraints required to restore autonomous functionality. Physical AI principles are embedded throughout: every algorithm must execute on resource-constrained embedded field controllers, account for motor torque and sensor noise, and adhere to life-critical safety margins.
    </p>
  </div>

  <div class="specs-table-wrapper" style="margin-top: 1.5rem;">
    <table class="specs-table">
      <thead>
        <tr>
          <th>Subsystem Module</th>
          <th>Syllabus Mapping</th>
          <th>Physical AI Subsystem</th>
          <th>Core Algorithmic Protocols</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Module 1: Navigation &amp; Clearance</strong></td>
          <td>Weeks 1 to 3</td>
          <td>Exterior Hull Crawler Robotics &amp; Power Grid</td>
          <td>PEAS, State Space, BFS, DFS, UCS, A* Search, Hill Climbing, Simulated Annealing, CSP (AC-3, Backtracking)</td>
        </tr>
        <tr>
          <td><strong>Module 2: Hostile Intrusion &amp; Contention</strong></td>
          <td>Week 4</td>
          <td>Cargo Bay Defense Sentry Turrets</td>
          <td>Adversarial Game Trees, Minimax, Alpha-Beta Pruning, Expectimax under Hazard</td>
        </tr>
        <tr>
          <td><strong>Module 3: Environmental Control &amp; Tracking</strong></td>
          <td>Weeks 5 to 7</td>
          <td>Tokamak Fusion Coolant &amp; Hull Sensor Mesh</td>
          <td>Markov Decision Processes (MDPs), Bellman Optimality, Q-Learning, Bayes' Rule, Bayesian Networks, HMM Forward Filtering</td>
        </tr>
        <tr>
          <td><strong>Module 4: Crew Diagnostics &amp; Core Reboot</strong></td>
          <td>Weeks 8 to 10</td>
          <td>Gas Chromatograph Arrays, Optical Docking, &amp; AI Core</td>
          <td>Utility Theory, Naive Bayes, Linear Classifiers, Perceptrons, MLPs, Backpropagation, Transformers (Self-Attention), AI Safety</td>
        </tr>
      </tbody>
    </table>
  </div>
</header>
"""
