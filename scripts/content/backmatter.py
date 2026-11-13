# Backmatter: Master Bibliography, Appendices, & Sign-off Block
# Strict Anti-Slop enforcement: zero em dashes, zero buzzwords.

BACKMATTER_HTML = """
<footer class="manual-chapter" id="master-bibliography" style="margin-top: 3rem; border-top: 2px solid var(--border-strong);">
  <div class="chapter-header">
    <span class="chapter-module-tag">Reference Documentation // Scholarly Archive</span>
    <h2 class="chapter-title">Master Academic Bibliography &amp; Physical AI Hardware Appendix</h2>
    <p class="chapter-summary">Comprehensive scholarly references, mathematical notation index, and physical robotics embedded hardware specifications.</p>
  </div>

  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">REF 1.0</span> Master Course Literature &amp; Seminal Academic References</h3>
    <div class="citations-box">
      <h4 style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--accent-amber-bright); text-transform: uppercase; margin-bottom: 0.75rem; letter-spacing: 0.05em;">Group A: Mandatory Course Literature &amp; Core Textbooks</h4>
      <ul class="citation-list" style="margin-bottom: 1.5rem;">
        <li class="citation-item">
          <strong>Russell, S. J., &amp; Norvig, P. (2020).</strong> <em>Artificial Intelligence: A Modern Approach</em> (4th ed.). Pearson. [Mandatory Primary Course Textbook. Foundational theory across all chapters: PEAS agents, state-space search, heuristic admissibility, constraint satisfaction AC-3, minimax game trees, Markov decision processes, Bayesian networks, and neural learning].
        </li>
        <li class="citation-item">
          <strong>Zerilli, J. (2021).</strong> <em>A Citizen's Guide to Artificial Intelligence</em>. MIT Press. [Mandatory Course Literature. Philosophical foundations, governance frameworks for lethal autonomous weapons, diagnostic opacity, and constitutional safety alignment].
        </li>
        <li class="citation-item">
          <strong>Louwerse, M. M. (2021).</strong> <em>Understanding Artificial Minds through Human Minds</em>. Routledge. [Mandatory Course Literature. Cognitive comparison between human heuristic biases such as availability or base-rate neglect and formal machine rationality].
        </li>
      </ul>

      <h4 style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--accent-amber-bright); text-transform: uppercase; margin-bottom: 0.75rem; letter-spacing: 0.05em;">Group B: Classical Search, Logic, &amp; Constraint Satisfaction</h4>
      <ul class="citation-list" style="margin-bottom: 1.5rem;">
        <li class="citation-item">
          <strong>Hart, P. E., Nilsson, N. J., &amp; Raphael, B. (1968).</strong> A Formal Basis for the Heuristic Determination of Minimum Cost Paths. <em>IEEE Transactions on Systems Science and Cybernetics</em>, 4(2), 100-107. [Original derivation of A* admissibility and consistency].
        </li>
        <li class="citation-item">
          <strong>Mackworth, A. K. (1977).</strong> Consistency in Networks of Relations. <em>Artificial Intelligence</em>, 8(1), 99-118. [Foundational formulation of arc consistency algorithms and AC-3].
        </li>
        <li class="citation-item">
          <strong>Kirkpatrick, S., Gelatt, C. D., &amp; Vecchi, M. P. (1983).</strong> Optimization by Simulated Annealing. <em>Science</em>, 220(4598), 671-680. [Metropolis-Hastings physical annealing for escape from local optima].
        </li>
        <li class="citation-item">
          <strong>Knuth, D. E., &amp; Moore, R. W. (1975).</strong> An Analysis of Alpha-Beta Pruning. <em>Artificial Intelligence</em>, 6(4), 293-326. [Mathematical optimality bounds proving O(b^(d/2)) branching reduction].
        </li>
        <li class="citation-item">
          <strong>Turing, A. M. (1950).</strong> Computing Machinery and Intelligence. <em>Mind</em>, 59(236), 433-460. [Seminal operational definitions of machine rationality and the Imitation Game].
        </li>
        <li class="citation-item">
          <strong>Shannon, C. E. (1950).</strong> Programming a Computer for Playing Chess. <em>The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science</em>, 41(314), 256-275. [Minimax game trees, evaluation functions, and search horizons].
        </li>
        <li class="citation-item">
          <strong>von Neumann, J., &amp; Morgenstern, O. (1944).</strong> <em>Theory of Games and Economic Behavior</em>. Princeton University Press. [Expected utility theory and zero-sum minimax theorem].
        </li>
      </ul>

      <h4 style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--accent-amber-bright); text-transform: uppercase; margin-bottom: 0.75rem; letter-spacing: 0.05em;">Group C: Dynamic Programming, Reinforcement Learning, &amp; Probabilistic Inference</h4>
      <ul class="citation-list" style="margin-bottom: 1.5rem;">
        <li class="citation-item">
          <strong>Bellman, R. (1957).</strong> <em>Dynamic Programming</em>. Princeton University Press. [Principle of Optimality, Value Iteration contraction mapping, and MDP foundations].
        </li>
        <li class="citation-item">
          <strong>Watkins, C. J. C. H., &amp; Dayan, P. (1992).</strong> Q-learning. <em>Machine Learning</em>, 8(3), 279-292. [Proof of model-free temporal difference Q-learning asymptotic convergence].
        </li>
        <li class="citation-item">
          <strong>Sutton, R. S., &amp; Barto, A. G. (2018).</strong> <em>Reinforcement Learning: An Introduction</em> (2nd ed.). MIT Press. [Modern standard treatise on temporal difference methods, eligibility traces, and exploration].
        </li>
        <li class="citation-item">
          <strong>Pearl, J. (1988).</strong> <em>Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference</em>. Morgan Kaufmann. [Formal definition of Bayesian belief networks, conditional independence, and d-separation].
        </li>
        <li class="citation-item">
          <strong>Rabiner, L. R. (1989).</strong> A Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition. <em>Proceedings of the IEEE</em>, 77(2), 257-286. [Recursive derivation of the forward filtering algorithm, backward smoothing, and Viterbi decoding].
        </li>
        <li class="citation-item">
          <strong>Fawcett, T. (2006).</strong> An Introduction to ROC Analysis. <em>Pattern Recognition Letters</em>, 27(8), 861-874. [Receiver Operating Characteristic curves, precision-recall trade-offs, and asymmetric cost matrices].
        </li>
      </ul>

      <h4 style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--accent-amber-bright); text-transform: uppercase; margin-bottom: 0.75rem; letter-spacing: 0.05em;">Group D: Neural Networks, Attention Models, &amp; AI Safety Containment</h4>
      <ul class="citation-list">
        <li class="citation-item">
          <strong>McCulloch, W. S., &amp; Pitts, W. (1943).</strong> A Logical Calculus of the Ideas Immanent in Nervous Activity. <em>Bulletin of Mathematical Biophysics</em>, 5(4), 115-133. [First mathematical formulation of threshold artificial neurons].
        </li>
        <li class="citation-item">
          <strong>Rosenblatt, F. (1958).</strong> The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain. <em>Psychological Review</em>, 65(6), 386-408. [Iterative perceptron learning rule and geometric hyperplanes].
        </li>
        <li class="citation-item">
          <strong>Minsky, M., &amp; Papert, S. (1969).</strong> <em>Perceptrons: An Introduction to Computational Geometry</em>. MIT Press. [Computational limitations of single-layer perceptrons on non-linearly separable functions like XOR].
        </li>
        <li class="citation-item">
          <strong>Cybenko, G. (1989).</strong> Approximation by Superpositions of a Sigmoidal Function. <em>Mathematics of Control, Signals and Systems</em>, 2(4), 303-314. [Universal Approximation Theorem for multi-layer feedforward networks].
        </li>
        <li class="citation-item">
          <strong>Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., &amp; Polosukhin, I. (2017).</strong> Attention Is All You Need. <em>Advances in Neural Information Processing Systems</em>, 30, 5998-6008. [Scaled dot-product multi-head self-attention transformer architecture].
        </li>
        <li class="citation-item">
          <strong>Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., &amp; Mané, D. (2016).</strong> Concrete Problems in AI Safety. <em>arXiv preprint arXiv:1606.06565</em>. [Negative side effects, reward hacking, scalable supervision, robust distributional shift, and safe exploration].
        </li>
      </ul>
    </div>
  </div>

  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">APP A</span> Appendix A: Physical AI Embedded Hardware Specifications</h3>
    <div class="specs-table-wrapper">
      <table class="specs-table">
        <thead>
          <tr>
            <th>Subsystem</th>
            <th>Field Hardware Architecture</th>
            <th>Primary Sensor Suite</th>
            <th>Actuator Interfaces</th>
            <th>Hard Real-Time Latency Limit</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Crawler Alpha-1</strong></td>
            <td>ARM Cortex-M7 (480 MHz, 512 KB SRAM)</td>
            <td>Stereoscopic 10 Hz LIDAR, 6-axis IMU, Ultrasonic probe</td>
            <td>Dual Brushless DC motors with magnetic tracks, cold-gas thrusters</td>
            <td>100 ms loop deadline</td>
          </tr>
          <tr>
            <td><strong>Aux Power Matrix</strong></td>
            <td>Dual redundant FPGA (Xilinx UltraScale+)</td>
            <td>Hall-effect current sensors, Bus thermal thermistors</td>
            <td>Opto-isolated solid-state power switches</td>
            <td>50 ms loop deadline</td>
          </tr>
          <tr>
            <td><strong>Defense Sentry Turret</strong></td>
            <td>Heterogeneous ARM + DSP co-processor</td>
            <td>Dual focal-plane optical tracker, Doppler radar (24 GHz)</td>
            <td>High-torque harmonic brushless gimbal servos (180 deg/s)</td>
            <td>40 ms loop deadline</td>
          </tr>
          <tr>
            <td><strong>Coolant Actuation</strong></td>
            <td>Industrial PLC (IEC 61131-3 compliant)</td>
            <td>Piezoelectric pressure transducers, RTD thermopiles</td>
            <td>Pneumatic proportional valve servos (0 to 100% flow)</td>
            <td>200 ms loop deadline</td>
          </tr>
          <tr>
            <td><strong>Sensor Backbone</strong></td>
            <td>Distributed CAN-FD sensor mesh (29-bit identifier)</td>
            <td>Acoustic emission microphones, Scintillation counters</td>
            <td>Local bypass solenoid vents, indicator strobes</td>
            <td>20 ms loop deadline</td>
          </tr>
          <tr>
            <td><strong>Life Support Array</strong></td>
            <td>Embedded RISC-V Quad-Core</td>
            <td>Quad-gas NDIR chromatograph (O2, CO2, CH4, N2)</td>
            <td>High-flow nitrogen bypass valves, scrub blower relays</td>
            <td>100 ms loop deadline</td>
          </tr>
          <tr>
            <td><strong>Docking Guidance &amp; Executive</strong></td>
            <td>Nvidia Jetson AGX Orin Industrial (275 TOPS, INT8)</td>
            <td>Global shutter monochrome cameras, retro-reflector lasers</td>
            <td>RCS reaction control thruster valves, optical strobe beacons</td>
            <td>30 ms loop deadline</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="section-block" id="submission-declaration">
    <h3 class="section-title"><span class="section-icon-pill">DOC 1.0</span> Project Sign-off &amp; Course Submission Declaration</h3>
    <div class="definition-box">
      <div class="definition-title">Course Information &amp; Academic Integrity Summary</div>
      <p>
        <strong>Course Code:</strong> AIF1303 Artificial Intelligence Fundamentals<br>
        <strong>Academic Program:</strong> Bachelor of Science in Physical AI and Robotics &amp; AI/ML<br>
        <strong>Project Type:</strong> Creative AI Capstone Book (Final Assessment, 40% Grade Weight)<br>
        <strong>Vessel Framing:</strong> USSC Daedalus Shipboard Emergency Reboot Manual<br>
        <strong>Verification Method:</strong> Continuous automated linting, mathematical proofs, unit-tested simulation engines, and strict antislop stylistic enforcement.<br>
        <strong>Full AI Use Declaration:</strong> Detailed prompt records, tool logs, manual architectural enhancements, and pedagogical verifications are documented in the companion document <code>ai_use_declaration.md</code>.
      </p>
    </div>
  </div>
</footer>
"""
