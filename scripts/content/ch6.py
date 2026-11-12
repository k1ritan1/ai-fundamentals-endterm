# Chapter 6: Atmospheric Decompression Classification & Rational Utility: Utility Theory, Classical Machine Learning, & Diagnostic Evaluation
# Syllabus Week 8
# Strict Anti-Slop enforcement: zero em dashes, zero buzzwords.

CH6_HTML = """
<section class="manual-chapter" id="chapter-6">
  <div class="chapter-directive">
    <div class="directive-meta-bar">
      <span>SUBSYSTEM PROTOCOL // ATM-ML-06</span>
      <span class="declassified-stamp">SEC-CLR: LIFE CRITICAL // ASYMMETRIC LOSS AUTH</span>
      <span>SYSTEM STATUS: CABIN DECOMPRESSION AUDIT</span>
    </div>
    <h2 class="chapter-title">Chapter 6: Atmospheric Decompression Classification &amp; Rational Utility: Utility Theory, Classical Machine Learning, &amp; Diagnostic Evaluation</h2>
    <p class="chapter-subtitle">Axiomatic utility under risk, supervised machine learning formulation, naive Bayes classification, and cost-sensitive confusion matrix optimization for life-critical diagnostics.</p>
    <table class="specs-table">
      <thead>
        <tr>
          <th>Subsystem</th>
          <th>Sensor Bus</th>
          <th>Cost Matrix Ratio</th>
          <th>Classifier Architecture</th>
          <th>Physical Actuator</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Environmental Scrubber Diagnostic</td>
          <td>RS-485 Optical Loop</td>
          <td>Cost(FN) = 50 * Cost(FP)</td>
          <td>Gaussian Naive Bayes MAP</td>
          <td>Hermetic Pressure Bulkhead Valves</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- 1. System Emergency Briefing -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 6.1</span> System Emergency Briefing</h3>
    <div class="briefing-callout">
      <div class="briefing-header">
        <span class="briefing-tag">Incident Report: Environmental Scrubber Array Sensor Telemetry</span>
        <span class="briefing-status">STATUS: CABIN MONITORING ACTIVE // HABITAT O2: 20.8 kPa</span>
      </div>
      <p class="briefing-text">
        Gas chromatography sensors in Crew Habitation Ring Alpha are reporting fluctuating partial pressures of oxygen, carbon dioxide ppm spikes, and acoustic micro-vibrations along duct lines. The life-support management software must determine whether these telemetry spikes represent a structural decompression breach or harmless transient turbulence from cycling air filtration scrubbers.
      </p>
      <p class="briefing-text">
        This diagnostic classification problem exhibits severe asymmetry in physical error costs. A False Positive classification triggers emergency explosive hermetic bulkhead isolation, trapping crew members in unpressurized corridors and venting nitrogen reserves. Conversely, a False Negative allows silent decompression to continue unchecked, leading to fatal hypoxia within 180 seconds. The classification threshold must be calibrated using formal utility theory and cost-sensitive machine learning.
      </p>
    </div>
  </div>

  <!-- 2. Theoretical Foundation & Mathematical Formulation -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 6.2</span> Theoretical Foundation &amp; Mathematical Formulation</h3>
    
    <p>
      Rational agents make decisions in uncertain environments by combining probabilistic beliefs with subjective preferences over states, formalized through <strong>Utility Theory</strong>.
    </p>

    <div class="definition-box">
      <div class="definition-title">Von Neumann-Morgenstern Utility Axioms &amp; The MEU Principle</div>
      <p>
        Let a lottery \\(L = [p_1, S_1; p_2, S_2; \\dots; p_n, S_n]\\) represent a probabilistic distribution over outcomes \\(S_i\\) with probabilities \\(p_i\\) such that \\(\\sum p_i = 1\\). Any rational preference relation \\(\\succ\\) satisfies the six von Neumann-Morgenstern axioms:
      </p>
      <ol>
        <li><strong>Orderability:</strong> Exactly one of \\(A \\succ B\\), \\(B \\succ A\\), or \\(A \\sim B\\) holds.</li>
        <li><strong>Transitivity:</strong> If \\(A \\succ B\\) and \\(B \\succ C\\), then \\(A \\succ C\\).</li>
        <li><strong>Continuity:</strong> If \\(A \\succ B \\succ C\\), then \\(\\exists p \\in [0, 1]\\) such that \\([p, A; (1-p), C] \\sim B\\).</li>
        <li><strong>Substitutability:</strong> If \\(A \\sim B\\), then for all \\(C\\) and \\(p\\), \\([p, A; (1-p), C] \\sim [p, B; (1-p), C]\\).</li>
        <li><strong>Monotonicity:</strong> If \\(A \\succ B\\), then \\(p > q \\iff [p, A; (1-p), B] \\succ [q, A; (1-q), B]\\).</li>
        <li><strong>Decomposability:</strong> Compound lotteries can be reduced to equivalent simple lotteries via probability calculus.</li>
      </ol>
      <p>
        When these axioms hold, there exists a real-valued utility function \\(U(s)\\) such that preferences are represented by expected utility. The <strong>Principle of Maximum Expected Utility (MEU)</strong> dictates that a rational agent chooses the action \\(a^*\\) maximizing expected utility:
      </p>
      <div class="math-block">
      $$
      a^* = \\arg\\max_{a \\in A} \\sum_{s'} P(s' \\mid s, a) U(s')
      $$
      <div class="formula-label">Equation 6.1: Principle of Maximum Expected Utility</div>
    </div>
      <p>
        The curvature of \\(U(s)\\) reflects operational risk posture:
      </p>
      <ul>
        <li><strong>Risk-Averse:</strong> Concave utility function (\\(U''(w) < 0\\)); \\(\\mathbb{E}[U(w)] < U(\\mathbb{E}[w])\\). The agent strictly prefers a guaranteed outcome over an uncertain lottery with equal expectation. Mandatory in life-support engineering.</li>
        <li><strong>Risk-Neutral:</strong> Linear utility function (\\(U''(w) = 0\\)); decisions depend solely on expected monetary or physical value.</li>
        <li><strong>Risk-Seeking:</strong> Convex utility function (\\(U''(w) > 0\\)); prefers the variance of lotteries.</li>
      </ul>
    </div>

    <div class="definition-box">
      <div class="definition-title">Supervised Machine Learning &amp; The Naive Bayes Classifier</div>
      <p>
        In supervised classification, the agent is given a training dataset \\(\\mathcal{D} = \\{(\\mathbf{x}_1, y_1), \\dots, (\\mathbf{x}_m, y_m)\\}\\), where \\(\\mathbf{x}_i \\in \\mathbb{R}^d\\) is a feature vector of sensor telemetry and \\(y_i \\in \\{0, 1\\}\\) is the binary ground-truth label (0 = Nominal Cabin, 1 = Decompression Breach).
      </p>
      <p>
        The <strong>Naive Bayes Classifier</strong> computes the posterior probability of class \\(y\\) using Bayes' rule, underpinned by the simplifying assumption that all feature dimensions \\(x_1, x_2, \\dots, x_d\\) are conditionally independent given the class label \\(y\\):
      </p>
      <div class="math-block">
      $$
      P(Y = c \\mid x_1, x_2, \\dots, x_d) = \\frac{P(Y = c) \\prod_{i=1}^{d} P(X_i = x_i \\mid Y = c)}{P(x_1, x_2, \\dots, x_d)}
      $$
      <div class="formula-label">Equation 6.2: Naive Bayes Posterior Probability Formulation</div>
    </div>
      <p>
        To prevent zero-frequency probability collapse when a novel sensor value is observed, we apply <strong>Laplace Smoothing</strong> (additive smoothing with pseudocount \\(k = 1\\)):
      </p>
      <div class="math-block">
      $$
      P(X_i = v \\mid Y = c) = \\frac{\\text{count}(X_i = v, Y = c) + 1}{\\text{count}(Y = c) + |V_i|}
      $$
      <div class="formula-label">Equation 6.3: Laplace Smoothing Parameter Estimation</div>
    </div>
      <p>
        For continuous features, linear classifiers compute a score function \\(z = \\mathbf{w}^T \\mathbf{x} + b\\) and map it to a probability using the logistic sigmoid function:
      </p>
      <div class="math-block">
      $$
      \\sigma(z) = \\frac{1}{1 + e^{-z}} = \\frac{1}{1 + \\exp(-(\\mathbf{w}^T \\mathbf{x} + b))}
      $$
      <div class="formula-label">Equation 6.4: Logistic Sigmoid Activation Function</div>
    </div>
    </div>

    <div class="definition-box">
      <div class="definition-title">Diagnostic Metrics &amp; Cost-Sensitive Asymmetry</div>
      <p>
        A binary classification model produces four distinct categorical outcomes:
      </p>
      <ul>
        <li><strong>True Positive (TP):</strong> Active breach correctly classified as breach (emergency bulkheads isolated).</li>
        <li><strong>False Positive (FP):</strong> Nominal cabin misclassified as breach (unnecessary lockdown; nitrogen loss).</li>
        <li><strong>True Negative (TN):</strong> Nominal cabin correctly classified as nominal.</li>
        <li><strong>False Negative (FN):</strong> Active breach misclassified as nominal (undetected decompression; crew hypoxia).</li>
      </ul>
      <p>
        Standard performance metrics are defined as:
      </p>
      <div class="math-block">
      $$
      \\begin{aligned}
        \\text{Precision} &= \\frac{\\text{TP}}{\\text{TP} + \\text{FP}} \\quad \\text{(Positive Predictive Value)} \\\\
        \\text{Recall (Sensitivity)} &= \\frac{\\text{TP}}{\\text{TP} + \\text{FN}} \\quad \\text{(True Positive Rate)} \\\\
        F_1\\text{-Score} &= 2 \\cdot \\frac{\\text{Precision} \\cdot \\text{Recall}}{\\text{Precision} + \\text{Recall}} = \\frac{2\\text{TP}}{2\\text{TP} + \\text{FP} + \\text{FN}}
        \\end{aligned}
      $$
      <div class="formula-label">Equation 6.5: Diagnostic Performance Metric Equations</div>
    </div>
      <p>
        <strong>Cost-Sensitive Decision Threshold:</strong> In life-critical space systems, accuracy is a misleading metric due to severe class imbalance. We formalize classification decisions through a cost matrix \\(C(\\hat{y}, y)\\). The expected risk of predicting class 1 given posterior probability \\(p = P(Y = 1 \\mid \\mathbf{x})\\) is:
      </p>
      <div class="math-block">
      $$
      \\mathcal{R}(\\text{predict } 1) = p \\cdot C(1, 1) + (1 - p) \\cdot C(1, 0) = (1 - p) \\cdot \\text{Cost}_{\\text{False Positive}}
      $$
    </div>
      <div class="math-block">
      $$
      \\mathcal{R}(\\text{predict } 0) = p \\cdot C(0, 1) + (1 - p) \\cdot C(0, 0) = p \\cdot \\text{Cost}_{\\text{False Negative}}
      $$
    </div>
      <p>
        Under this decision framework, the net expected value of taking action is \\(\\mathcal{V}(\\text{Predict } 1) = -\\mathcal{R}(\\text{predict } 1)\\). Predicting breach (\\(\\hat{y} = 1\\)) is optimal if and only if \\(\\mathcal{R}(\\text{predict } 1) < \\mathcal{R}(\\text{predict } 0)\\). Solving for the critical decision threshold \\(\\tau^*\\) yields:
      </p>
      <div class="math-block">
      $$
      \\tau^* = \\frac{\\text{Cost}_{\\text{False Positive}} - \\text{Cost}_{\\text{True Negative}}}{[\\text{Cost}_{\\text{False Positive}} - \\text{Cost}_{\\text{True Negative}}] + [\\text{Cost}_{\\text{False Negative}} - \\text{Cost}_{\\text{True Positive}}]} = \\frac{\\text{Cost}_{\\text{False Positive}}}{\\text{Cost}_{\\text{False Positive}} + \\text{Cost}_{\\text{False Negative}}}
      $$
      <div class="formula-label">Equation 6.6: Optimal Cost-Sensitive Bayesian Decision Threshold</div>
    </div>
      <p>
        Setting \\(\\text{Cost}_{\\text{False Negative}} = 100\\) (fatal hypoxia penalty) and \\(\\text{Cost}_{\\text{False Positive}} = 1\\) (false alarm cost) shifts the optimal operational threshold to \\(\\tau^* \\approx 0.0099\\). The system must favor high recall over precision to preserve crew life.
      </p>
    </div>
  </div>

  <!-- 3. Algorithmic Execution / Pseudo-code -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 6.3</span> Algorithmic Execution &amp; Pseudo-code</h3>
    
    <p>
      The atmospheric monitoring engine executes continuous classification over high-rate gas sensor telemetry, applying the cost-sensitive Bayesian threshold to trigger automated safety isolation protocols.
    </p>

    <div class="code-container">
      <div class="code-header">
        <span class="code-lang">Algorithm 6.1: Cost-Sensitive Atmospheric Fault Diagnostic Engine</span>
        <span>Target: Environmental Control Computer</span>
      </div>
      <pre><code>function CLASSIFY_ATMOSPHERIC_TELEMETRY(sensor_reading, model_weights, bias, cost_matrix):
    // sensor_reading: vector of [O2_loss_rate, CO2_ppm, acoustic_derivative]
    
    // Step 1: Compute linear score and posterior probability via sigmoid
    z = DOT_PRODUCT(model_weights, sensor_reading) + bias
    prob_breach = 1.0 / (1.0 + exp(-z))
    
    // Step 2: Compute optimal decision threshold from asymmetric cost matrix
    c_false_positive = cost_matrix.cost(predict=1, true=0) // Cost = 1
    c_false_negative = cost_matrix.cost(predict=0, true=1) // Cost = 100
    
    threshold = c_false_positive / (c_false_positive + c_false_negative)
    
    // Step 3: Issue classification and physical interlock command
    if prob_breach &gt;= threshold:
        action = COMMAND_SEAL_BULKHEADS
        status = ALARM_DECOMPRESSION
    else:
        action = MAINTAIN_CIRCULATION
        status = NOMINAL_CABIN
        
    return DiagnosticResult(prob=prob_breach, threshold=threshold, action=action, status=status)</code></pre>
    </div>

    <div class="specs-table-wrapper">
      <table class="specs-table">
        <thead>
          <tr>
            <th>Operational Threshold (\\(\\tau\\))</th>
            <th>Recall (Sensitivity)</th>
            <th>Precision</th>
            <th>False Negatives (Fatal Breaches)</th>
            <th>Physical AI Safety Evaluation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>\\(\\tau = 0.50\\) (Standard Balanced)</strong></td>
            <td>82.4%</td>
            <td>91.2%</td>
            <td>6 missed leaks</td>
            <td>Unacceptable: high crew fatality risk</td>
          </tr>
          <tr>
            <td><strong>\\(\\tau = 0.25\\) (Conservative)</strong></td>
            <td>94.1%</td>
            <td>78.0%</td>
            <td>2 missed leaks</td>
            <td>Marginal: potential hypoxia under slow decompression</td>
          </tr>
          <tr>
            <td><strong>\\(\\tau = 0.10\\) (Cost-Sensitive Optimal)</strong></td>
            <td>100.0%</td>
            <td>64.5%</td>
            <td>0 missed leaks</td>
            <td>Mission standard: zero human fatalities, manageable false alarms</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>
      In physical robotics deployments, gas chromatography sensors suffer from temperature drift and chemical absorption latency (2 to 5 seconds for gas diffusion across filter membranes). Feature engineering must incorporate temporal derivatives (\\(d[\\text{O}_2]/dt\\)) rather than raw instantaneous partial pressures, enabling rapid classification before cabin air volume drops below physiological safety margins.
    </p>
      <figure class="diagram-frame">
      <div class="diagram-header">
        <span class="diagram-id">DIAGRAM 6.1 // ROC &amp; PRECISION-RECALL CURVES</span>
        <span>SPEC-EVAL-ASYMMETRIC // CLASS IMBALANCE TRADE-OFF</span>
      </div>
      <div class="diagram-viewport">
        <img class="diagram-img" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7WI8ADISmOSYUm-H0R1zmoMcUJocIKgNSqIWqiGHaqSMId6kNjlzyAgND&s=10" alt="ROC vs Precision-Recall curves illustrating diagnostic trade-offs under extreme class imbalance." width="500" height="260" loading="lazy">
      </div>
      <figcaption class="diagram-caption">
        <strong>Figure 6.1:</strong> Receiver Operating Characteristic (ROC) vs Precision-Recall curves under severe class imbalance. In life-critical life support diagnostics where true breach events are rare (0.1%), the Precision-Recall curve reveals severe false alarm penalties masked by high area under the ROC curve (Russell &amp; Norvig, Ch. 19).
      </figcaption>
    </figure>
  </div>

  <!-- 4. Interactive Simulation Module -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 6.4</span> Interactive Simulation Module: Gas Classifier &amp; Confusion Matrix Sandbox</h3>
    <p>
      The interactive module below evaluates 120 sensor data points across Crew Habitation Ring Alpha. Red dots represent true hull breach incidents; green dots represent nominal cabin cycling. Adjust the decision threshold slider to observe the trade-off between Precision, Recall, and the total physical safety penalty cost.
    </p>

    <div class="sim-container">
      <div class="sim-header">
        <span class="sim-title">Simulation 6.1: Environmental Fault Classifier &amp; Confusion Matrix</span>
        <span class="sim-status">DIAGNOSTIC ENGINE ACTIVE</span>
      </div>
      <div class="sim-body">
        <div class="sim-controls">
          <div class="sim-control-group">
            <label for="sim6-slider-thresh">Decision Threshold (\\(\\tau\\)):</label>
            <input type="range" id="sim6-slider-thresh" min="0.05" max="0.95" step="0.05" value="0.50" class="sim-slider" style="width: 100px;">
            <span id="sim6-thresh-val" style="font-family: var(--font-mono); font-size: 0.8rem;">0.50</span>
          </div>
          <button id="sim6-btn-regen" class="btn-secondary">Resample Sensor Stream</button>
        </div>

        <div class="sim-canvas-wrapper" style="min-height: 200px;">
          <canvas id="sim6-canvas" width="600" height="200" aria-label="Interactive Sensor Scatter Plot and Decision Boundary Canvas"></canvas>
        </div>

        <!-- 2x2 Confusion Matrix Display -->
        <div style="margin-top: 1rem; display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
          <div style="background-color: var(--bg-surface-elevated); padding: 0.75rem; border: 1px solid var(--border-subtle); border-radius: 3px;">
            <div style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase;">Predicted: Breach (Positive)</div>
            <div style="display: flex; justify-content: space-between; margin-top: 0.4rem; font-family: var(--font-mono); font-size: 0.85rem;">
              <span>True Positive (TP): <strong id="sim6-cm-tp" style="color: #10b981;">0</strong></span>
              <span>False Positive (FP): <strong id="sim6-cm-fp" style="color: #f59e0b;">0</strong></span>
            </div>
          </div>
          <div style="background-color: var(--bg-surface-elevated); padding: 0.75rem; border: 1px solid var(--border-subtle); border-radius: 3px;">
            <div style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase;">Predicted: Nominal (Negative)</div>
            <div style="display: flex; justify-content: space-between; margin-top: 0.4rem; font-family: var(--font-mono); font-size: 0.85rem;">
              <span>False Negative (FN): <strong id="sim6-cm-fn" style="color: #ef4444;">0</strong></span>
              <span>True Negative (TN): <strong id="sim6-cm-tn" style="color: #10b981;">0</strong></span>
            </div>
          </div>
        </div>

        <div class="sim-telemetry">
          <div class="telemetry-item">
            <span class="telemetry-label">Precision</span>
            <span id="sim6-stat-prec" class="telemetry-value">--</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Recall (Sensitivity)</span>
            <span id="sim6-stat-rec" class="telemetry-value">--</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">F1-Score</span>
            <span id="sim6-stat-f1" class="telemetry-value">--</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Safety Penalty Cost</span>
            <span id="sim6-stat-cost" class="telemetry-value" style="color: #ef4444;">--</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 5. Academic Post-Mortem & Citations -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 6.5</span> Academic Post-Mortem &amp; Citations</h3>
    <div class="citations-box">
      <p>
        The decision-theoretic and statistical machine learning formulations underlying the atmospheric safety array originate from foundational contributions across economics and computer science:
      </p>
      <ul class="citation-list">
        <li class="citation-item">
          <strong>von Neumann, J., &amp; Morgenstern, O. (1944).</strong> <em>Theory of Games and Economic Behavior</em>. Princeton University Press. [Formulated the axiomatic foundations of expected utility theory under risk and subjective uncertainty].
        </li>
        <li class="citation-item">
          <strong>Fawcett, T. (2006).</strong> An Introduction to ROC Analysis. <em>Pattern Recognition Letters</em>, 27(8), 861-874. [The definitive treatment on receiver operating characteristic curves, cost-sensitive threshold selection, and diagnostic evaluation metrics].
        </li>
        <li class="citation-item">
          <strong>Russell, S. J., &amp; Norvig, P. (2020).</strong> <em>Artificial Intelligence: A Modern Approach</em> (4th ed.). Pearson. Chapter 16 ("Making Simple Decisions") and Chapter 19 ("Learning from Examples"). [Comprehensive coverage of lotteries, risk attitudes, Naive Bayes, Laplace smoothing, and linear classification].
        </li>
        <li class="citation-item">
          <strong>Zerilli, J. (2021).</strong> <em>A Citizen's Guide to Artificial Intelligence</em>. MIT Press. Chapter 3 ("Machine Learning, Predictions, and Fairness"). [Explored how algorithmic threshold calibration affects false negative distribution, establishing ethical standards for safety-critical medical and habitat automation].
        </li>
      </ul>
    </div>
  </div>
</section>
"""
