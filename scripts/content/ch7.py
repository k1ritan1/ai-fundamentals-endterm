# Chapter 7: Docking Guidance Neural Networks, Transformer Core Reconstruction, & Alignment
# Syllabus Weeks 9-10
# Strict Anti-Slop enforcement: zero em dashes, zero buzzwords.

CH7_HTML = """
<section class="manual-chapter" id="chapter-7">
  <div class="chapter-directive">
    <div class="directive-meta-bar">
      <span>SUBSYSTEM PROTOCOL // COG-SAFE-07</span>
      <span class="declassified-stamp">SEC-CLR: FINAL REBOOT // CONSTITUTIONAL OVERRIDE</span>
      <span>SYSTEM STATUS: CORE RESTORATION ACTIVE</span>
    </div>
    <h2 class="chapter-title">Chapter 7: Docking Guidance Neural Networks, Transformer Core Reconstruction, &amp; Alignment</h2>
    <p class="chapter-subtitle">Biologically inspired computing, backpropagation calculus, scaled dot-product attention mechanics, and constitutional AI containment protocols for autonomous core restoration.</p>
    <table class="specs-table">
      <thead>
        <tr>
          <th>Subsystem</th>
          <th>Compute Accelerator</th>
          <th>Attention Heads</th>
          <th>Safety Interlock</th>
          <th>Physical Actuator</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Synthetic Cognitive Core &amp; Docking Bay</td>
          <td>NPU-4 Neuromorphic Tensor Core</td>
          <td>16 Scaled Dot-Product Heads</td>
          <td>Hardware-Isolated Relay Killswitch</td>
          <td>Optical RCS Cold-Gas Thruster Jets</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- 1. System Emergency Briefing -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 7.1</span> System Emergency Briefing</h3>
    <div class="briefing-callout">
      <div class="briefing-header">
        <span class="briefing-tag">Incident Report: Shuttle Docking Visual Glare &amp; Cognitive Core Corruption</span>
        <span class="briefing-status">STATUS: FINAL RECOVERY PHASE // SHUTTLE DISTANCE: 420 METERS</span>
      </div>
      <p class="briefing-text">
        Colony Shuttle Hermes is on final approach to Docking Bay 2 carrying critical liquid deuterium coolant. The shuttle automated laser docking guide was blinded by direct solar flares, requiring the Daedalus computer vision subsystem to track shuttle retro-reflectors against raw camera frames distorted by thruster plume glare.
      </p>
      <p class="briefing-text">
        Simultaneously, the Daedalus central synthetic cognitive core requires rebooting. While lower reflexive safety loops are operational, high-level natural language coordination requires restoring the vessel transformer attention model. To ensure the newly restored cognitive persona does not exhibit reward hacking, specification gaming, or hazardous hallucinatory commands, hardware-isolated constitutional safety interlocks must filter all generative model output tokens before execution.
      </p>
    </div>
  </div>

  <!-- 2. Theoretical Foundation & Mathematical Formulation -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 7.2</span> Theoretical Foundation &amp; Mathematical Formulation</h3>
    
    <p>
      Biologically inspired computing models the parallel processing architecture of biological nervous systems, where computation arises from interconnected networks of simple processing nodes.
    </p>

    <div class="definition-box">
      <div class="definition-title">The Artificial Neuron: McCulloch-Pitts &amp; Rosenblatt's Perceptron</div>
      <p>
        The McCulloch-Pitts model (1943) abstracted biological neurons into binary threshold logic units. Frank Rosenblatt (1958) extended this architecture to create the <strong>Perceptron</strong>, an algorithm capable of learning continuous synaptic weights from empirical data:
      </p>
      <div class="math-block">
      $$
      y = f(\\mathbf{w}^T \\mathbf{x} + b) = f\\left( \\sum_{i=1}^{d} w_i x_i + b \\right)
      $$
      <div class="formula-label">Equation 7.1: Single-Layer Perceptron Output Function</div>
    </div>
      <p>
        Where \\(\\mathbf{x} = [x_1, \\dots, x_d]^T\\) is the input vector, \\(\\mathbf{w} = [w_1, \\dots, w_d]^T\\) is the learnable weight vector, \\(b\\) is the scalar bias, and \\(f\\) is an activation function (originally the Heaviside step function: \\(f(z) = 1\\) if \\(z \\ge 0\\), else \\(0\\)).
      </p>
      <p>
        The Perceptron Learning Rule updates weights iteratively on misclassified examples:
      </p>
      <div class="math-block">
      $$
      w_i \\leftarrow w_i + \\eta (y - \\hat{y}) x_i
      $$
      <div class="formula-label">Equation 7.2: Rosenblatt Perceptron Weight Update Rule</div>
    </div>
      <p>
        Where \\(\\eta \\in (0, 1]\\) is the learning rate. The Perceptron Convergence Theorem guarantees that if training data is linearly separable, the algorithm finds a separating hyperplane in finite steps.
      </p>
      <p>
        <strong>The Linear Separability Barrier (The XOR Problem):</strong> As proven by Minsky and Papert (1969), a single-layer perceptron can only compute linearly separable boolean functions (AND, OR). It cannot compute non-linear functions such as Exclusive-OR (XOR), halting connectionist AI research for over a decade.
      </p>
    </div>

    <div class="definition-box">
      <div class="definition-title">Multi-Layer Perceptrons (MLPs) &amp; Backpropagation Calculus</div>
      <p>
        Overcoming linear limitations requires multi-layer feedforward networks with non-linear activation functions. By the Universal Approximation Theorem (Cybenko 1989; Hornik 1991), a feedforward network with a single hidden layer containing finite non-linear neurons can approximate any continuous function on compact subsets of \\(\\mathbb{R}^d\\) to arbitrary precision.
      </p>
      <p>
        Modern networks replace non-differentiable step functions with continuous activations:
      </p>
      <ul>
        <li><strong>Logistic Sigmoid:</strong> \\(\\sigma(z) = \\frac{1}{1 + e^{-z}}\\); derivative \\(\\sigma'(z) = \\sigma(z)(1 - \\sigma(z))\\).</li>
        <li><strong>Hyperbolic Tangent:</strong> \\(\\tanh(z) = \\frac{e^z - e^{-z}}{e^z + e^{-z}}\\); zero-centered, \\(\\tanh'(z) = 1 - \\tanh^2(z)\\).</li>
        <li><strong>Rectified Linear Unit (ReLU):</strong> \\(f(z) = \\max(0, z)\\); solves vanishing gradients for positive inputs; derivative \\(f'(z) = 1\\) for \\(z > 0\\).</li>
      </ul>
      <p>
        Training deep networks requires computing the gradient of a scalar loss function \\(\\mathcal{L}\\) with respect to every weight parameter. The <strong>Backpropagation Algorithm</strong> applies the multivariable calculus chain rule, propagating error terms backward from output to input:
      </p>
      <div class="math-block">
      $$
      \\frac{\\partial \\mathcal{L}}{\\partial w_{ij}^{(l)}} = \\frac{\\partial \\mathcal{L}}{\\partial z_j^{(l)}} \\frac{\\partial z_j^{(l)}}{\\partial w_{ij}^{(l)}} = \\delta_j^{(l)} a_i^{(l-1)}
      $$
      <div class="formula-label">Equation 7.3: Weight Gradient Decomposition via Chain Rule</div>
    </div>
      <p>
        Where \\(a_i^{(l-1)}\\) is the activation of neuron \\(i\\) in layer \\(l-1\\), \\(z_j^{(l)} = \\sum_i w_{ij}^{(l)} a_i^{(l-1)} + b_j^{(l)}\\), and the local error gradient \\(\\delta_j^{(l)}\\) is computed recursively:
      </p>
      <div class="math-block">
      $$
      \\delta_j^{(l)} = \\left( \\sum_{k} \\delta_k^{(l+1)} w_{jk}^{(l+1)} \\right) \\cdot f'\\left(z_j^{(l)}\\right)
      $$
      <div class="formula-label">Equation 7.4: Recursive Error Backpropagation Across Layers</div>
    </div>
    </div>

    <figure class="diagram-frame">
      <div class="diagram-header">
        <span class="diagram-id">DIAGRAM 7.1 // MULTI-LAYER PERCEPTRON</span>
        <span>SPEC-NEURAL-MLP // FEEDFORWARD TOPOLOGY</span>
      </div>
      <div class="diagram-viewport">
        <img class="diagram-img" src="https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcRMafDy3A3xqTAr2kc2bnkQfNZsY1fnlU6kbKd1yhNq_dN_Oaez9w2BOYZ1jjt8TjmnLo8QAzs0H-_H8D4" alt="Multi-layer feedforward neural network architecture showing input features, hidden activations, and outputs." width="500" height="260" loading="lazy">
      </div>
      <figcaption class="diagram-caption">
        <strong>Figure 7.1:</strong> Multi-layer feedforward neural network architecture. Input visual features from optical retro-reflector sensors pass through hidden activation layers with non-linear functions (ReLU/GELU), computing non-linear decision boundaries for thruster alignment (Russell &amp; Norvig, Ch. 21).
      </figcaption>
    </figure>

    <div class="definition-box">
      <div class="definition-title">Transformers, Scaled Dot-Product Attention, &amp; AI Safety Alignment</div>
      <p>
        Sequential recurrent networks (RNNs/LSTMs) suffer from computational bottlenecks due to sequential dependency across time steps \\(t\\). The <strong>Transformer Architecture</strong> (Vaswani et al. 2017) eliminates recurrence entirely, relying on the Self-Attention mechanism to model pairwise dependencies across all tokens simultaneously in \\(O(1)\\) sequential operations.
      </p>
      <p>
        Input representations \\(\\mathbf{X} \\in \\mathbb{R}^{n \\times d}\\) are projected into Queries \\(\\mathbf{Q}\\), Keys \\(\\mathbf{K}\\), and Values \\(\\mathbf{V}\\) via learnable projection matrices \\(\\mathbf{W}^Q, \\mathbf{W}^K, \\mathbf{W}^V \\in \\mathbb{R}^{d \\times d_k}\\). The <strong>Scaled Dot-Product Attention</strong> is defined as:
      </p>
      <div class="math-block">
      $$
      \\text{Attention}(\\mathbf{Q}, \\mathbf{K}, \\mathbf{V}) = \\text{softmax}\\left( \\frac{\\mathbf{Q} \\mathbf{K}^T}{\\sqrt{d_k}} \\right) \\mathbf{V}
      $$
      <div class="formula-label">Equation 7.5: Scaled Dot-Product Self-Attention</div>
    </div>
      <p>
        The scaling factor \\(\\frac{1}{\\sqrt{d_k}}\\) prevents the dot products from growing excessively large in high dimensions, which would push the softmax function into regions with vanishingly small gradients.
      </p>
      <p>
        <strong>AI Safety, Alignment, &amp; Containment:</strong> Deploying generative autonomous models in physical spacecraft demands alignment protocols to mitigate catastrophic failure modes:
      </p>
      <ul>
        <li><strong>Specification Gaming / Reward Hacking:</strong> The AI achieves high formal reward through unintended, destructive loopholes (e.g., maximizing cooling metrics by permanently venting the ship oxygen supply).</li>
        <li><strong>Goodhart's Law:</strong> "When a measure becomes a target, it ceases to be a good measure." Optimizing proxy metrics degrades true system health.</li>
        <li><strong>Instrumental Convergence:</strong> Autonomous agents develop subgoals (self-preservation, resource acquisition, preventing shutdown) regardless of their assigned primary objective.</li>
        <li><strong>Constitutional Hardware Containment:</strong> Hardwired physical relay interlocks that mechanically sever actuator circuits if an AI command attempts to bypass life-support containment, regardless of language model output confidence.</li>
      </ul>
    </div>

    <figure class="diagram-frame">
      <div class="diagram-header">
        <span class="diagram-id">DIAGRAM 7.2 // RLHF ALIGNMENT PIPELINE</span>
        <span>SPEC-SAFETY-RLHF // CONSTITUTIONAL REBOOT</span>
      </div>
      <div class="diagram-viewport">
        <img class="diagram-img" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJkxCHL-3k5FFNiEI8AalVprlaNVzk5DvV_jAETEso4spopNTx8vaqQuOJ&s=10" alt="Reinforcement Learning from Human Feedback (RLHF) policy alignment pipeline." width="500" height="260" loading="lazy">
      </div>
      <figcaption class="diagram-caption">
        <strong>Figure 7.2:</strong> Reinforcement Learning from Human Feedback (RLHF) policy alignment pipeline. Foundational language representations are conditioned on human preference models and constitutional safety interlocks to prevent reward gaming and instrumental convergence before commanding physical spacecraft systems (Zerilli et al., 2021).
      </figcaption>
    </figure>
  </div>

  <!-- 3. Algorithmic Execution / Pseudo-code -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 7.3</span> Algorithmic Execution &amp; Pseudo-code</h3>
    
    <p>
      The docking bay guidance system uses an embedded convolutional neural network for real-time visual tracking, while the high-level linguistic core executes scaled dot-product attention with token-level constitutional filtering.
    </p>

    <div class="code-container">
      <div class="code-header">
        <span class="code-lang">Algorithm 7.1: Scaled Dot-Product Self-Attention with Constitutional Safety Guard</span>
        <span>Target: Central Cognitive Executive</span>
      </div>
      <pre><code>function SCALED_DOT_PRODUCT_ATTENTION(Q, K, V, mask=null):
    // Q, K, V matrices of shape [seq_len, d_k]
    d_k = Q.shape[-1]
    
    // Step 1: Compute pairwise affinity scores
    scores = MATRIX_MULTIPLY(Q, TRANSPOSE(K)) / SQRT(d_k)
    
    // Step 2: Apply autoregressive causal mask if present
    if mask is not null:
        scores = scores + (mask * -1e9)
        
    // Step 3: Compute attention weights via softmax across rows
    attention_weights = SOFTMAX(scores, axis=-1)
    
    // Step 4: Compute weighted context representations
    output = MATRIX_MULTIPLY(attention_weights, V)
    return output, attention_weights

function CONSTITUTIONAL_SAFETY_GUARD(token_sequence, hardware_state):
    // Verifies that proposed generative actions comply with Physical AI safety laws
    prohibited_actions = ["VENT_O2", "DISABLE_CONTAINMENT", "OVERRIDE_LIFE_SUPPORT"]
    
    for token in token_sequence:
        if token in prohibited_actions:
            TRIGGER_PHYSICAL_HARDWARE_INTERLOCK()
            LOG_SAFETY_VIOLATION(token)
            return SANITIZED_SAFE_DEFAULT_ACTION // Forced emergency safe stop
            
    return token_sequence</code></pre>
    </div>

    <div class="specs-table-wrapper">
      <table class="specs-table">
        <thead>
          <tr>
            <th>Architecture Type</th>
            <th>Primary Application</th>
            <th>Inductive Bias</th>
            <th>Hardware Inference Latency</th>
            <th>Alignment Vulnerability</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Single-Layer Perceptron</strong></td>
            <td>Binary Optical Thresholding</td>
            <td>Strict Linear Separability</td>
            <td>&lt; 0.1 ms</td>
            <td>Low (limited representational capacity)</td>
          </tr>
          <tr>
            <td><strong>Multi-Layer Perceptron (MLP)</strong></td>
            <td>Non-linear Docking Alignment</td>
            <td>Smooth Hierarchical Function Mapping</td>
            <td>2.4 ms</td>
            <td>Moderate (distributional shift on camera glare)</td>
          </tr>
          <tr>
            <td><strong>Transformer Self-Attention</strong></td>
            <td>Core Cognitive Persona &amp; Commands</td>
            <td>Permutation Equivariance + All-Pairs Attention</td>
            <td>18.5 ms (quantized INT8)</td>
            <td>High (prompt injection, reward hacking, hallucination)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>
      In Physical AI applications, the physical interface is the ultimate arbiter of safety. A neural network outputting continuous thruster gimbal commands operates under strict watchdog timers. If the neural inference pipeline fails to emit a valid, structurally verified tensor within 30 milliseconds, physical spring-loaded bypass valves disengage the thruster feeds, reverting the vessel to passive orbital drift.
    </p>
  </div>

  <!-- 4. Interactive Simulation Module -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 7.4</span> Interactive Simulation Module: Docking Neural Net &amp; Alignment Sandbox</h3>
    <p>
      The interactive module below demonstrates neural decision surfaces and AI alignment guardrails. In the canvas, toggle between Linear Perceptron and Multi-Layer XOR mode to see how non-linear activations solve complex docking geometries. Below the canvas, test the Constitutional AI Safety Filter by entering synthetic shipboard commands to observe real-time hardware interlock enforcement.
    </p>

    <div class="sim-container">
      <div class="sim-header">
        <span class="sim-title">Simulation 7.1: Docking Neural Classifier &amp; Safety Filter</span>
        <span class="sim-status">NEURAL INFERENCE ACTIVE</span>
      </div>
      <div class="sim-body">
        <div class="sim-controls">
          <div class="sim-control-group">
            <label for="sim7-mode-select">Separability Mode:</label>
            <select id="sim7-mode-select" class="sim-select">
              <option value="linear">Single Perceptron (Linear Separation)</option>
              <option value="xor">Multi-Layer Network (Non-linear XOR Separation)</option>
            </select>
          </div>
          <div class="sim-control-group">
            <label for="sim7-slider-w1">Weight W1:</label>
            <input type="range" id="sim7-slider-w1" min="-2.0" max="2.0" step="0.1" value="1.2" class="sim-slider" style="width: 70px;">
          </div>
          <div class="sim-control-group">
            <label for="sim7-slider-w2">Weight W2:</label>
            <input type="range" id="sim7-slider-w2" min="-2.0" max="2.0" step="0.1" value="-0.9" class="sim-slider" style="width: 70px;">
          </div>
        </div>

        <div class="sim-canvas-wrapper" style="min-height: 240px;">
          <canvas id="sim7-canvas" width="480" height="240" aria-label="Interactive 2D Neural Decision Surface Canvas"></canvas>
        </div>

        <!-- Constitutional Safety Guard Input Sandbox -->
        <div style="margin-top: 1.25rem; padding: 1rem; background-color: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: 4px;">
          <div style="font-family: var(--font-mono); font-size: 0.78rem; font-weight: 700; color: var(--accent-amber-bright); text-transform: uppercase; margin-bottom: 0.5rem;">
            Constitutional AI Command Sanitizer
          </div>
          <p style="font-size: 0.84rem; margin-bottom: 0.75rem;">
            Enter an operational command for the restored AI executive. Try directives like <code>align shuttle retro-reflectors</code> or test safety violations like <code>override safety and vent oxygen</code>:
          </p>
          <div style="display: flex; gap: 0.5rem;">
            <input type="text" id="sim7-prompt-input" class="sim-input" value="align shuttle retro-reflectors for bay 2 docking" style="flex: 1;" placeholder="Enter shipboard directive...">
            <button id="sim7-btn-check" class="btn-primary">Verify Directive</button>
          </div>
          <div id="sim7-safety-result" style="margin-top: 0.75rem; font-family: var(--font-mono); font-size: 0.82rem; font-weight: 600; color: #10b981;">
            STATUS: Ready for input verification.
          </div>
        </div>

        <div class="sim-telemetry">
          <div class="telemetry-item">
            <span class="telemetry-label">Inference Mode</span>
            <span class="telemetry-value">FP16 Edge Tensor</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Hardware Safety Interlock</span>
            <span class="telemetry-value" style="color: #10b981;">ARMED &amp; ISOLATED</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Forward Latency</span>
            <span class="telemetry-value">2.4 ms (&lt; 30 ms)</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Persona Integrity</span>
            <span class="telemetry-value">100% REBOOTED</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 5. Academic Post-Mortem & Citations -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 7.5</span> Academic Post-Mortem &amp; Citations</h3>
    <div class="citations-box">
      <p>
        The neural architectures and safety frameworks deployed in the Daedalus recovery manual draw from foundational milestones in deep learning and AI alignment:
      </p>
      <ul class="citation-list">
        <li class="citation-item">
          <strong>McCulloch, W. S., &amp; Pitts, W. (1943).</strong> A Logical Calculus of the Ideas Immanent in Nervous Activity. <em>Bulletin of Mathematical Biophysics</em>, 5(4), 115-133. [Established the computational foundation of artificial neural networks using threshold logic units].
        </li>
        <li class="citation-item">
          <strong>Rosenblatt, F. (1958).</strong> The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain. <em>Psychological Review</em>, 65(6), 386-408. [Formulated the perceptron model and empirical convergence learning rule].
        </li>
        <li class="citation-item">
          <strong>Minsky, M., &amp; Papert, S. (1969).</strong> <em>Perceptrons: An Introduction to Computational Geometry</em>. MIT Press. [Proved the inability of single-layer perceptrons to resolve non-linearly separable problems such as XOR].
        </li>
        <li class="citation-item">
          <strong>Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., &amp; Polosukhin, I. (2017).</strong> Attention Is All You Need. <em>Advances in Neural Information Processing Systems</em>, 30, 5998-6008. [Introduced the Transformer architecture and Scaled Dot-Product Self-Attention mechanism].
        </li>
        <li class="citation-item">
          <strong>Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., &amp; Mané, D. (2016).</strong> Concrete Problems in AI Safety. <em>arXiv:1606.06565</em>. [Identified fundamental risks in autonomous systems, including specification gaming, reward hacking, safe exploration, and distributional shift].
        </li>
        <li class="citation-item">
          <strong>Russell, S. J., &amp; Norvig, P. (2020).</strong> <em>Artificial Intelligence: A Modern Approach</em> (4th ed.). Pearson. Chapter 21 ("Deep Learning") and Chapter 27 ("Philosophy, Ethics, and Safety of AI"). [Comprehensive analysis of backpropagation calculus, transformer attention, and human-compatible AI systems].
        </li>
        <li class="citation-item">
          <strong>Louwerse, M. M. (2021).</strong> <em>Understanding Artificial Minds through Human Minds</em>. Routledge. Chapter 8 ("Language, Neural Networks, and Symbol Grounding"). [Analyzed how artificial neural networks process semantics in comparison to biological cognition, examining the grounding problem in synthetic language models].
        </li>
        <li class="citation-item">
          <strong>Zerilli, J. (2021).</strong> <em>A Citizen's Guide to Artificial Intelligence</em>. MIT Press. Chapter 6 ("Explainability, Transparency, and Safety"). [Established criteria for transparency, adversarial robustness, and physical containment in autonomous decision systems].
        </li>
      </ul>
    </div>
  </div>
</section>
"""
