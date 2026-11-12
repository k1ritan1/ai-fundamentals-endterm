# Chapter 5: Structural Damage Localization & Sequential Sensor Inference: Bayesian Networks & Hidden Markov Models
# Syllabus Weeks 6-7
# Strict Anti-Slop enforcement: zero em dashes, zero buzzwords.

CH5_HTML = """
<section class="manual-chapter" id="chapter-5">
  <div class="chapter-directive">
    <div class="directive-meta-bar">
      <span>SUBSYSTEM PROTOCOL // SENS-HMM-05</span>
      <span class="declassified-stamp">SEC-CLR: NOISE RECOVERY // PROBABILISTIC FILTER</span>
      <span>SYSTEM STATUS: SENSOR NOISE ACTIVE</span>
    </div>
    <h2 class="chapter-title">Chapter 5: Structural Damage Localization &amp; Sequential Sensor Inference: Bayesian Networks &amp; Hidden Markov Models</h2>
    <p class="chapter-subtitle">Axiomatic probability foundations, Bayesian network inference, conditional independence, and recursive forward filtering over noisy sequential sensor streams.</p>
    <table class="specs-table">
      <thead>
        <tr>
          <th>Subsystem</th>
          <th>Sensor Bus</th>
          <th>Noise Rate (SNR)</th>
          <th>Inference Model</th>
          <th>Physical Actuator</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Service Conduit Sensor Array</td>
          <td>MIL-STD-1553B 1.0 Mbps</td>
          <td>SNR -6.4 dB (25% False Alarm)</td>
          <td>HMM Recursive Forward Filter</td>
          <td>Automated Bulkhead Sealing Hatches</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- 1. System Emergency Briefing -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 5.1</span> System Emergency Briefing</h3>
    <div class="briefing-callout">
      <div class="briefing-header">
        <span class="briefing-tag">Incident Report: Hidden Pressure Bleed in Service Conduits</span>
        <span class="briefing-status">STATUS: SUB-DECK INTEGRITY DEGRADED // NOISE SNR: -6.4 dB</span>
      </div>
      <p class="briefing-text">
        Acoustic transducers along the primary service backbone report high-frequency acoustic hiss indicative of an internal high-pressure coolant line fracture. The service conduit passes through six contiguous physical bulkheads inaccessible to human crew. Structural damage cannot be observed directly because sensors behind bulkheads are uncalibrated and suffer high electronic noise from cosmic radiation.
      </p>
      <p class="briefing-text">
        Individual acoustic and scintillation sensors report false alarms at rates exceeding 25%. A single raw sensor ping cannot justify commanding emergency fire-suppression foam injection, which would contaminate non-damaged electronic bays. The ship tracking system must maintain a sequential probabilistic belief state, updating state distributions recursively using Hidden Markov Model forward filtering to pinpoint the true physical fracture location.
      </p>
    </div>
  </div>

  <!-- 2. Theoretical Foundation & Mathematical Formulation -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 5.2</span> Theoretical Foundation &amp; Mathematical Formulation</h3>
    
    <p>
      Classical propositional and first-order logic fail in physical robotics due to the qualification problem: the exhaustive list of antecedents required to guarantee an outcome is intractable to formalize. Physical environments are governed by uncertainty arising from partial observability, noisy sensors, non-deterministic actuators, and computational limits.
    </p>

    <div class="definition-box">
      <div class="definition-title">Axioms of Probability &amp; Bayes' Rule</div>
      <p>
        Probability theory formalizes degrees of belief over propositions. The Kolmogorov axioms establish the mathematical foundation:
      </p>
      <ol>
        <li>\\(\\forall A, \\quad 0 \\le P(A) \\le 1\\)</li>
        <li>\\(P(\\Omega) = 1\\), where \\(\\Omega\\) is the sample space.</li>
        <li>For mutually exclusive events \\(A\\) and \\(B\\): \\(P(A \\cup B) = P(A) + P(B)\\).</li>
      </ol>
      <p>
        Conditional probability is defined as \\(P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)}\\) for \\(P(B) > 0\\). The Product Rule yields the Joint Probability Distribution: \\(P(A, B) = P(A \\mid B) P(B) = P(B \\mid A) P(A)\\). Equating these expressions yields <strong>Bayes' Rule</strong>:
      </p>
      <div class="math-block">
      $$
      P(\\text{Cause} \\mid \\text{Effect}) = \\frac{P(\\text{Effect} \\mid \\text{Cause}) P(\\text{Cause})}{P(\\text{Effect})}
      $$
      <div class="formula-label">Equation 5.1: Bayes' Rule for Diagnostic Inference</div>
    </div>
      <p>
        Using the Law of Total Probability to expand the marginal denominator \\(P(E) = \\sum_c P(E \\mid C = c) P(C = c)\\), Bayes' Rule in normalized form is written as:
      </p>
      <div class="math-block">
      $$
      P(C \\mid E) = \\alpha P(E \\mid C) P(C)
      $$
      <div class="formula-label">Equation 5.2: Normalized Posterior Probability Formulation</div>
    </div>
      <p>
        Where \\(\\alpha = 1 / \\sum_c P(E \\mid c) P(c)\\) is a normalization constant ensuring the posterior distribution sums to 1.
      </p>
    </div>

    <p>
      Two variables \\(X\\) and \\(Y\\) are conditionally independent given \\(Z\\) if:
    </p>

    <div class="math-block">
      $$
      P(X, Y \\mid Z) = P(X \\mid Z) P(Y \\mid Z) \\iff P(X \\mid Y, Z) = P(X \\mid Z)
      $$
      <div class="formula-label">Equation 5.3: Conditional Independence Relation</div>
    </div>

    <p>
      A <strong>Bayesian Network</strong> is a Directed Acyclic Graph (DAG) whose nodes represent random variables and whose directed edges represent direct probabilistic dependencies. Each node \\(X_i\\) is equipped with a Conditional Probability Table (CPT) specifying \\(P(X_i \\mid \\text{Parents}(X_i))\\). By exploiting conditional independence, the joint distribution factors into:
    </p>

    <div class="math-block">
      $$
      P(X_1, X_2, \\dots, X_n) = \\prod_{i=1}^{n} P(X_i \\mid \\text{Parents}(X_i))
      $$
      <div class="formula-label">Equation 5.4: Joint Distribution Factorization over Bayesian Networks</div>
    </div>

    <p>
      Conditional independence is verified topologically through <strong>d-separation</strong> (directional separation). An undirected path between \\(X\\) and \\(Y\\) is blocked by evidence set \\(E\\) if the path contains:
    </p>
    <ul>
      <li>A linear chain \\(A \\to B \\to C\\) or common cause \\(A \\leftarrow B \\to C\\), and \\(B \\in E\\).</li>
      <li>A collider / v-structure \\(A \\to B \\leftarrow C\\), and neither \\(B\\) nor any descendant of \\(B\\) is in \\(E\\). Observing a collider unblocks the path ("explaining away").</li>
    </ul>

    <figure class="diagram-frame">
      <div class="diagram-header">
        <span class="diagram-id">DIAGRAM 5.1 // BAYESIAN NETWORK DAG</span>
        <span>SPEC-BAYES-CPT // FACTORIZED JOINT DISTRIBUTION</span>
      </div>
      <div class="diagram-viewport">
        <img class="diagram-img" src="https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcTfV0NhgdwEK2DLdNzw-OavrKQyWhgG-hTFBFXYzjX1sVMiHnMLnqm1tUjLEzMYYg1-s2n0srjPqR_XZTc" alt="Directed Acyclic Graph factorizing joint distributions for noisy life-support sensors." width="480" height="250" loading="lazy">
      </div>
      <figcaption class="diagram-caption">
        <strong>Figure 5.1:</strong> Directed Acyclic Graph (DAG) factorizing joint probability distributions over shipboard damage sensors. Nodes represent latent physical states and noisy acoustic readings, linked by conditional probability tables (CPTs) that exploit d-separation to enable scalable exact inference (Russell &amp; Norvig, Ch. 14).
      </figcaption>
    </figure>

    <div class="definition-box">
      <div class="definition-title">Hidden Markov Models (HMMs) &amp; The Forward Filtering Algorithm</div>
      <p>
        When physical variables evolve over time, we model the system as a Hidden Markov Model. Let \\(X_t\\) denote the unobservable true physical state at time step \\(t\\) (e.g., fracture in sector \\(i \\in \\{1, \\dots, 6\\}\\)), and \\(E_t\\) denote the noisy sensor observation at time \\(t\\).
      </p>
      <p>
        The model satisfies two core independence assumptions:
      </p>
      <ul>
        <li><strong>First-Order Markov State Transition:</strong> \\(P(X_t \\mid X_{0:t-1}) = P(X_t \\mid X_{t-1})\\).</li>
        <li><strong>Sensor Markov Assumption:</strong> \\(P(E_t \\mid X_{0:t}, E_{1:t-1}) = P(E_t \\mid X_t)\\).</li>
      </ul>
      <p>
        The primary task in real-time tracking is <strong>Filtering</strong>: computing the current belief state distribution \\(P(X_t \\mid e_{1:t})\\) given the historical observation sequence \\(e_{1:t} = (e_1, e_2, \\dots, e_t)\\).
      </p>
      <p>
        <em>Mathematical Derivation:</em>
      </p>
      <div class="math-block">
      $$
      \\begin{aligned}
        P(X_t \\mid e_{1:t}) &= P(X_t \\mid e_t, e_{1:t-1}) \\\\
        &= \\alpha P(e_t \\mid X_t, e_{1:t-1}) P(X_t \\mid e_{1:t-1}) \\quad \\text{(by Bayes' Rule)} \\\\
        &= \\alpha P(e_t \\mid X_t) P(X_t \\mid e_{1:t-1}) \\quad \\text{(by Sensor Markov Assumption)}
        \\end{aligned}
      $$
    </div>
      <p>
        Expanding the one-step prediction term \\(P(X_t \\mid e_{1:t-1})\\) by conditioning and marginalizing over the previous state \\(x_{t-1}\\):
      </p>
      <div class="math-block">
      $$
      P(X_t \\mid e_{1:t-1}) = \\sum_{x_{t-1}} P(X_t \\mid x_{t-1}, e_{1:t-1}) P(x_{t-1} \\mid e_{1:t-1}) = \\sum_{x_{t-1}} P(X_t \\mid x_{t-1}) P(x_{t-1} \\mid e_{1:t-1})
      $$
    </div>
      <p>
        Substituting yields the canonical recursive <strong>Forward Filtering Equation</strong>:
      </p>
      <div class="math-block">
      $$
      P(X_t \\mid e_{1:t}) = \\alpha P(e_t \\mid X_t) \\sum_{x_{t-1}} P(X_t \\mid x_{t-1}) P(x_{t-1} \\mid e_{1:t-1})
      $$
      <div class="formula-label">Equation 5.5: Recursive Forward Filtering Algorithm</div>
    </div>
    </div>
  </div>

  <!-- 3. Algorithmic Execution / Pseudo-code -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 5.3</span> Algorithmic Execution &amp; Pseudo-code</h3>
    
    <p>
      In matrix formulation, let \\(\\mathbf{f}_{1:t}\\) be the belief probability vector of length \\(N\\). Let \\(\\mathbf{T}\\) be the \\(N \\times N\\) transition probability matrix where \\(T_{ij} = P(X_t = j \\mid X_{t-1} = i)\\), and let \\(\\mathbf{O}_t\\) be a diagonal observation matrix with entries \\(O_{t,ii} = P(e_t \\mid X_t = i)\\). The forward step simplifies to:
    </p>

    <div class="math-block">
      $$
      \\mathbf{f}_{1:t} = \\alpha \\mathbf{O}_t \\mathbf{T}^T \\mathbf{f}_{1:t-1}
      $$
      <div class="formula-label">Equation 5.6: Matrix Formulation of HMM Forward Filter</div>
    </div>

    <div class="code-container">
      <div class="code-header">
        <span class="code-lang">Algorithm 5.1: Matrix-Vector HMM Forward Tracking Filter</span>
        <span>Target: Structural Sensor Hub</span>
      </div>
      <pre><code>function HMM_FORWARD_FILTER_STEP(belief_prev, observation, T_matrix, sensor_model):
    // Step 1: Prediction step (Project physical dynamics through transition model)
    // predicted[j] = sum_i T[i][j] * belief_prev[i]
    predicted = MATRIX_VECTOR_MULTIPLY(TRANSPOSE(T_matrix), belief_prev)
    
    // Step 2: Update step (Weight by sensor likelihood of current evidence)
    updated = Vector(length=NUM_SECTORS)
    for j from 1 to NUM_SECTORS:
        likelihood = sensor_model.get_probability(evidence=observation, state=j)
        updated[j] = likelihood * predicted[j]
        
    // Step 3: Normalization step (Ensure probability vector sums to 1.0)
    norm_constant = SUM(updated)
    if norm_constant == 0:
        return UNIFORM_DISTRIBUTION(NUM_SECTORS) // Sensor total dropout recovery
        
    belief_current = updated / norm_constant
    return belief_current

function VITERBI_DECODE(observations, T_matrix, sensor_model, initial_prior):
    // Computes the most likely physical damage trajectory across all time steps
    T = len(observations)
    N = NUM_SECTORS
    viterbi = Matrix(N, T)
    backpointer = Matrix(N, T)
    
    // Initialization at t = 1
    for i from 1 to N:
        viterbi[i, 1] = initial_prior[i] * sensor_model.prob(observations[1], i)
        backpointer[i, 1] = 0
        
    // Recursion over time
    for t from 2 to T:
        for j from 1 to N:
            best_prev, best_idx = MAX_INDEX(viterbi[i, t-1] * T_matrix[i, j] for i in 1..N)
            viterbi[j, t] = best_prev * sensor_model.prob(observations[t], j)
            backpointer[j, t] = best_idx
            
    // Backtracking the most probable historical trajectory
    best_path = Vector(length=T)
    best_path[T] = ARGMAX(viterbi[j, T] for j in 1..N)
    for t from T down to 2:
        best_path[t-1] = backpointer[best_path[t], t]
        
    return best_path</code></pre>
    </div>

    <div class="specs-table-wrapper">
      <table class="specs-table">
        <thead>
          <tr>
            <th>Inference Task</th>
            <th>Formal Target</th>
            <th>Time Complexity per Step</th>
            <th>Space Complexity</th>
            <th>Operational Use Case</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Filtering</strong></td>
            <td>$P(X_t \\mid e_{1:t})$</td>
            <td>$O(S^2)$</td>
            <td>$O(S)$</td>
            <td>Real-time damage tracking and current state estimation</td>
          </tr>
          <tr>
            <td><strong>Prediction</strong></td>
            <td>$P(X_{t+k} \\mid e_{1:t})$ for $k > 0$</td>
            <td>$O(k S^2)$</td>
            <td>$O(S)$</td>
            <td>Anticipating future breach propagation ahead of crawlers</td>
          </tr>
          <tr>
            <td><strong>Smoothing</strong></td>
            <td>$P(X_k \\mid e_{1:t})$ for $0 \\le k < t$</td>
            <td>$O(t S^2)$</td>
            <td>$O(t S)$</td>
            <td>Post-incident root cause reconstruction across past telemetry</td>
          </tr>
          <tr>
            <td><strong>Most Likely Explanation (Viterbi)</strong></td>
            <td>$\\arg\\max_{x_{1:t}} P(x_{1:t} \\mid e_{1:t})$</td>
            <td>$O(t S^2)$</td>
            <td>$O(t S)$</td>
            <td>Reconstructing historical intruder movement trajectory</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>
      In Physical AI applications, the size of the state space \\(S\\) can grow large. In continuous 3D physical spaces, exact matrix multiplication \\(O(S^2)\\) becomes computationally prohibitive. Real-time embedded systems replace discrete grid HMMs with <strong>Kalman Filters</strong> (for linear Gaussian systems) or <strong>Particle Filters</strong> (Sequential Monte Carlo sampling for non-linear, multi-modal distributions), approximating the belief vector using \\(M\\) discrete state samples.
    </p>
  

    <figure class="diagram-frame">
      <div class="diagram-header">
        <span class="diagram-id">DIAGRAM 5.2 // HMM TEMPORAL TRELLIS</span>
        <span>SPEC-HMM-FORWARD // DISCRETE TIME SLICES</span>
      </div>
      <div class="diagram-viewport">
        <img class="diagram-img" src="https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRJATkyzyG0-0qKycn6FejJcO4_9gI8gcA6lhURna3dbhcl49uoQx5WU_ae6YY-VnOPIsTA4P_bV5mVIn0" alt="Hidden Markov Model temporal trellis mapping latent breach locations across discrete time slices." width="500" height="260" loading="lazy">
      </div>
      <figcaption class="diagram-caption">
        <strong>Figure 5.2:</strong> Hidden Markov Model temporal trellis mapping unobserved breach states across discrete time slices. Forward filtering recursively integrates transition dynamics \(P(X_t \mid X_{t-1})\) and sensor emission probabilities \(P(E_t \mid X_t)\) to compute optimal belief states under extreme measurement noise (Russell &amp; Norvig, Ch. 15).
      </figcaption>
    </figure>
  </div>

  <!-- 4. Interactive Simulation Module -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 5.4</span> Interactive Simulation Module: Sequential HMM Tracker</h3>
    <p>
      The interactive module below tracks an unseen fluid fracture moving stochastically along six service sectors. The hidden red dot represents ground truth physical damage. The bar chart displays the current forward belief vector \\(P(X_t \\mid e_{1:t})\\). Advance the sensor stream, adjust the sensor noise rate, and observe how Bayes' rule fuses noisy evidence into sharp probabilistic confidence.
    </p>

    <div class="sim-container">
      <div class="sim-header">
        <span class="sim-title">Simulation 5.1: Sequential HMM Service Backbone Tracker</span>
        <span class="sim-status">FORWARD FILTER ACTIVE</span>
      </div>
      <div class="sim-body">
        <div class="sim-controls">
          <button id="sim5-btn-step" class="btn-primary">Receive Sensor Ping</button>
          <button id="sim5-btn-reset" class="btn-secondary">Reset Prior</button>
          <div class="sim-control-group">
            <label for="sim5-slider-noise">Sensor Noise Rate:</label>
            <input type="range" id="sim5-slider-noise" min="0.05" max="0.50" step="0.05" value="0.25" class="sim-slider" style="width: 80px;">
            <span id="sim5-noise-val" style="font-family: var(--font-mono); font-size: 0.8rem;">25%</span>
          </div>
        </div>

        <div class="sim-canvas-wrapper">
          <canvas id="sim5-canvas" width="560" height="260" aria-label="Interactive 6 Sector HMM Belief Bar Chart Canvas"></canvas>
        </div>

        <div class="sim-telemetry">
          <div class="telemetry-item">
            <span class="telemetry-label">Ground Truth Position</span>
            <span id="sim5-stat-true" class="telemetry-value">Sector 3</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Latest Raw Sensor Ping</span>
            <span id="sim5-stat-obs" class="telemetry-value">None</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Top Belief Sector</span>
            <span id="sim5-stat-belief" class="telemetry-value">Uniform (17%)</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Filter Latency</span>
            <span class="telemetry-value">1.8 ms (&lt; 20 ms)</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 5. Academic Post-Mortem & Citations -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 5.5</span> Academic Post-Mortem &amp; Citations</h3>
    <div class="citations-box">
      <p>
        The probabilistic reasoning and temporal filtering architectures deployed across the service backbone derive from foundational contributions to statistical inference:
      </p>
      <ul class="citation-list">
        <li class="citation-item">
          <strong>Pearl, J. (1988).</strong> <em>Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference</em>. Morgan Kaufmann. [Established graphical models, Bayesian networks, d-separation criteria, and formal belief propagation].
        </li>
        <li class="citation-item">
          <strong>Rabiner, L. R. (1989).</strong> A Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition. <em>Proceedings of the IEEE</em>, 77(2), 257-286. [The canonical mathematical formulation of discrete HMMs, forward-backward filtering, and the Viterbi algorithm].
        </li>
        <li class="citation-item">
          <strong>Russell, S. J., &amp; Norvig, P. (2020).</strong> <em>Artificial Intelligence: A Modern Approach</em> (4th ed.). Pearson. Chapter 12 ("Quantifying Uncertainty"), Chapter 13 ("Probabilistic Reasoning"), and Chapter 14 ("Probabilistic Reasoning over Time"). [Comprehensive treatments of Kolmogorov axioms, variable elimination, and temporal state estimation].
        </li>
        <li class="citation-item">
          <strong>Louwerse, M. M. (2021).</strong> <em>Understanding Artificial Minds through Human Minds</em>. Routledge. Chapter 5 ("Probabilistic Minds and Heuristics"). [Documented systematic human cognitive errors in probability estimation, such as base-rate neglect and availability bias, demonstrating why life-critical space operations mandate automated Bayesian tracking].
        </li>
      </ul>
    </div>
  </div>
</section>
"""
