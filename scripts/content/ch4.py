# Chapter 4: Reactor Temperature Control & Drive Dynamics: Markov Decision Processes & Reinforcement Learning
# Syllabus Week 5
# Strict Anti-Slop enforcement: zero em dashes, zero buzzwords.

CH4_HTML = """
<section class="manual-chapter" id="chapter-4">
  <div class="chapter-directive">
    <div class="directive-meta-bar">
      <span>SUBSYSTEM PROTOCOL // RCT-RL-04</span>
      <span class="declassified-stamp">SEC-CLR: THERMAL EMERGENCY // COOLANT ENGAGE</span>
      <span>SYSTEM STATUS: CORE OSCILLATION</span>
    </div>
    <h2 class="chapter-title">Chapter 4: Reactor Temperature Control &amp; Drive Dynamics: Markov Decision Processes &amp; Reinforcement Learning</h2>
    <p class="chapter-subtitle">Sequential decision-making under uncertainty, Bellman optimality formulations, value iteration convergence, and model-free temporal difference Q-learning for thermal regulation.</p>
    <table class="specs-table">
      <thead>
        <tr>
          <th>Subsystem</th>
          <th>Control Protocol</th>
          <th>Convergence Tolerance</th>
          <th>Discount Factor</th>
          <th>Physical Actuator</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Tokamak Cryo-Cooling System</td>
          <td>Modbus-RTU 115.2 kbps</td>
          <td>epsilon = 0.001</td>
          <td>gamma = 0.95</td>
          <td>Cryo-Fluid Injector Valves &amp; Bypass Pumps</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- 1. System Emergency Briefing -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 4.1</span> System Emergency Briefing</h3>
    <div class="briefing-callout">
      <div class="briefing-header">
        <span class="briefing-tag">Incident Report: Tokamak Core Thermal Runaway</span>
        <span class="briefing-status">STATUS: MAGNETIC CONFINEMENT DRIFT // CORE TEMP: 1.28e8 K</span>
      </div>
      <p class="briefing-text">
        Magnetic confinement fields in the primary deuterium-tritium fusion tokamak have suffered harmonic instability following auxiliary power drops. Plasma temperature is oscillating unpredictably across five magnetic containment rings. Autonomous cryo-coolant injection valves must be manipulated continuously to steer core thermals back to the stable baseline without causing thermal quench shock.
      </p>
      <p class="briefing-text">
        Fluid coolant delivery exhibits physical thermal inertia: commanding a valve actuator produces delayed thermal changes 3 to 8 seconds later. Transition dynamics are stochastic due to turbulent plasma eddies. The engineering system must deploy Markov Decision Process formulations and Reinforcement Learning to discover optimal valve policies before core breach containment failure occurs.
      </p>
    </div>
  </div>

  <!-- 2. Theoretical Foundation & Mathematical Formulation -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 4.2</span> Theoretical Foundation &amp; Mathematical Formulation</h3>
    
    <p>
      When an agent acts in a stochastic environment where actions have uncertain outcomes and consequences play out over extended time horizons, decision-making is formalized through the mathematical framework of Markov Decision Processes.
    </p>

    <div class="definition-box">
      <div class="definition-title">Formal Markov Decision Process (MDP) Definition</div>
      <p>
        A discounted Markov Decision Process is defined as a 5-tuple \\(\\langle S, A, T, R, \\gamma \\rangle\\):
      </p>
      <ul>
        <li><strong>State Space \\(S\\):</strong> The set of all valid environmental states. For the tokamak reactor: discretized temperature-pressure vectors across grid sectors.</li>
        <li><strong>Action Space \\(A\\):</strong> The set of executable control actions, \\(A = \\{\\text{Inject Vent}, \\text{Increase Flow}, \\text{Decrease Flow}, \\text{Bypass Loop}\\}\\).</li>
        <li><strong>Transition Model \\(T(s, a, s') = P(s' \\mid s, a)\\):</strong> The conditional probability that executing action \\(a\\) in state \\(s\\) leads to state \\(s'\\). Satisfies \\(\\sum_{s' \\in S} T(s, a, s') = 1\\).</li>
        <li><strong>Reward Function \\(R(s, a, s')\\):</strong> The real-valued scalar feedback received upon transitioning. Stable thermal baseline yields \\(+10\\); plasma containment breach yields \\(-100\\); step energy cost is \\(-0.1\\).</li>
        <li><strong>Discount Factor \\(\\gamma \\in [0, 1)\\):</strong> Models the preference for immediate rewards over deferred rewards, ensuring mathematical convergence over infinite horizons:</li>
      </ul>
      <div class="math-block">
      $$
      G_t = \\sum_{k=0}^{\\infty} \\gamma^k R_{t+k+1}
      $$
      <div class="formula-label">Equation 4.1: Discounted Cumulative Return from Time t</div>
    </div>
    </div>

    <figure class="diagram-frame">
      <div class="diagram-header">
        <span class="diagram-id">DIAGRAM 4.1 // MDP STATE-ACTION TRANSITIONS</span>
        <span>SPEC-MDP-BELLMAN // PROBABILISTIC DYNAMICS</span>
      </div>
      <div class="diagram-viewport">
        <img class="diagram-img" src="https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcQk6HvxsXERwrIzbdrm2ZUxyg4a7fwOQYe0Xk65JF7UUIhoYgWsEAB0E21z42muC7zNdkkpZgYreQl_70I" alt="Markov Decision Process state-action transition automaton with transition probabilities and reward functions." width="500" height="270" loading="lazy">
      </div>
      <figcaption class="diagram-caption">
        <strong>Figure 4.1:</strong> Markov Decision Process state-action transition automaton. Control actions \(a \in A\) induce stochastic transitions across reactor states \(s \in S\) with probability \(P(s' \mid s, a)\) and immediate feedback \(R(s, a, s')\), governed by the Bellman optimality principle (Russell &amp; Norvig, Ch. 17).
      </figcaption>
    </figure>

    <p>
      The foundational assumption enabling tractable dynamic programming is the <strong>Markov Property</strong>: future states depend solely on the current state and action, independent of the historical percept trajectory:
    </p>

    <div class="math-block">
      $$
      P(S_{t+1} = s' \\mid S_t = s_t, A_t = a_t, S_{t-1} = s_{t-1}, \\dots, S_0 = s_0) = P(S_{t+1} = s' \\mid S_t = s_t, A_t = a_t)
      $$
      <div class="formula-label">Equation 4.2: The First-Order Markov Property</div>
    </div>

    <p>
      An agent behavior is specified by a policy \\(\\pi(a \\mid s)\\). The state-value function \\(V^\\pi(s)\\) quantifies expected return from state \\(s\\) under policy \\(\\pi\\), while the action-value function \\(Q^\\pi(s, a)\\) quantifies the expected return of taking action \\(a\\) in state \\(s\\) before following \\(\\pi\\).
    </p>

    <div class="definition-box">
      <div class="definition-title">Bellman Expectation &amp; Optimality Equations</div>
      <p>
        The Bellman Expectation Equation decomposes the value of a state recursively into immediate reward plus discounted expected future value:
      </p>
      <div class="math-block">
      $$
      V^\\pi(s) = \\sum_{a \\in A} \\pi(a \\mid s) \\sum_{s' \\in S} T(s, a, s') \\left[ R(s, a, s') + \\gamma V^\\pi(s') \\right]
      $$
    </div>
      <p>
        The optimal policy \\(\\pi^*\\) achieves the maximal value function across all states: \\(V^*(s) = \\max_\\pi V^\\pi(s)\\). The Bellman Optimality Equations express the non-linear relationship that must hold at equilibrium:
      </p>
      <div class="math-block">
      $$
      V^*(s) = \\max_{a \\in A} \\sum_{s' \\in S} T(s, a, s') \\left[ R(s, a, s') + \\gamma V^*(s') \\right]
      $$
    </div>
      <div class="math-block">
      $$
      Q^*(s, a) = \\sum_{s' \\in S} T(s, a, s') \\left[ R(s, a, s') + \\gamma \\max_{a' \\in A} Q^*(s', a') \\right]
      $$
    </div>
      <p>
        Once \\(Q^*(s, a)\\) is known, the optimal deterministic policy is extracted greedily: \\(\\pi^*(s) = \\arg\\max_a Q^*(s, a)\\).
      </p>
    </div>

    <p>
      When the environmental transition dynamics \\(T\\) and reward function \\(R\\) are known, <strong>Value Iteration</strong> solves for \\(V^*\\) through fixed-point iteration:
    </p>

    <div class="math-block">
      $$
      V_{k+1}(s) \\leftarrow \\max_{a \\in A} \\sum_{s' \\in S} T(s, a, s') \\left[ R(s, a, s') + \\gamma V_k(s') \\right]
      $$
      <div class="formula-label">Equation 4.3: Value Iteration Update Rule</div>
    </div>

    <p>
      By the Banach Fixed-Point Theorem, the Bellman backup operator is a \\(\\gamma\\)-contraction mapping in the \\(L_\\infty\\) norm: \\(\\|\\mathcal{T}V - \\mathcal{T}U\\|_\\infty \\le \\gamma \\|V - U\\|_\\infty\\). Because \\(\\gamma < 1\\), value iteration converges to a unique fixed point regardless of initialization:
    </p>

    <div class="math-block">
      $$
      \\|V_{k+1} - V^*\\|_\\infty \\le \\frac{2\\gamma}{1 - \\gamma} \\|V_k - V_{k-1}\\|_\\infty
      $$
      <div class="formula-label">Equation 4.4: Contraction Mapping Error Bound</div>
    </div>

    <div class="definition-box">
      <div class="definition-title">Model-Free Reinforcement Learning: Temporal Difference Q-Learning</div>
      <p>
        When plasma dynamics are too turbulent to model explicitly, the transition probabilities \\(T(s, a, s')\\) are unknown. The agent must learn directly from experiential transitions \\((s_t, a_t, r_{t+1}, s_{t+1})\\).
      </p>
      <p>
        Watkins Q-Learning is an <em>off-policy</em> Temporal Difference control algorithm. It updates the state-action value table by comparing the current estimate to a bootstrap target:
      </p>
      <div class="math-block">
      $$
      Q(S_t, A_t) \\leftarrow Q(S_t, A_t) + \\alpha \\left[ R_{t+1} + \\gamma \\max_{a'} Q(S_{t+1}, a') - Q(S_t, A_t) \\right]
      $$
    </div>
      <p>
        Where:
      </p>
      <ul>
        <li>\\(\\alpha \\in (0, 1]\\) is the learning rate parameter.</li>
        <li>\\(\\delta_t = R_{t+1} + \\gamma \\max_{a'} Q(S_{t+1}, a') - Q(S_t, A_t)\\) is the Temporal Difference (TD) error.</li>
        <li>\\(R_{t+1} + \\gamma \\max_{a'} Q(S_{t+1}, a')\\) is the target value.</li>
      </ul>
      <p>
        <strong>Exploration vs. Exploitation:</strong> To discover high-reward states while refining known policies, the agent uses an \\(\\epsilon\\)-greedy behavioral policy: with probability \\(1 - \\epsilon\\), it selects \\(\\arg\\max_a Q(s, a)\\); with probability \\(\\epsilon\\), it selects a random exploratory action.
      </p>
    </div>
  </div>

  <!-- 3. Algorithmic Execution / Pseudo-code -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 4.3</span> Algorithmic Execution &amp; Pseudo-code</h3>
    
    <p>
      The embedded reactor supervisory controller executes Tabular Q-Learning across the 5x5 discretized thermal manifold. A safety filter overrides exploratory actions if the predicted step violates immediate magnetic thermal tolerances.
    </p>

    <div class="code-container">
      <div class="code-header">
        <span class="code-lang">Algorithm 4.1: Tabular Q-Learning with Epsilon-Greedy Exploration</span>
        <span>Target: Tokamak Coolant Actuator</span>
      </div>
      <pre><code>function Q_LEARNING_REACTOR_CONTROLLER(env, alpha, gamma, epsilon_init, episodes):
    // Initialize Q-table to zero for all state-action pairs
    Q = HashMap(default=0.0)
    epsilon = epsilon_init
    
    for episode from 1 to episodes:
        state = env.reset()
        is_terminal = false
        
        while not is_terminal:
            // Epsilon-greedy action selection
            if RANDOM_UNIFORM(0, 1) &lt; epsilon:
                action = env.random_action() // Explore
            else:
                action = ARGMAX_ACTION(Q, state) // Exploit
                
            // Execute action on physical coolant valves
            next_state, reward, is_terminal = env.step(action)
            
            // Calculate Bellman optimality bootstrap target
            max_next_q = is_terminal ? 0.0 : MAX_Q_VALUE(Q, next_state)
            td_target = reward + gamma * max_next_q
            td_error = td_target - Q[state, action]
            
            // Q-table update
            Q[state, action] = Q[state, action] + alpha * td_error
            
            state = next_state
            
        // Decay exploration rate over training episodes
        epsilon = max(0.01, epsilon * 0.995)
        
    return EXTRACT_POLICY(Q)

function EXTRACT_POLICY(Q):
    policy = HashMap()
    for state in ALL_STATES:
        policy[state] = ARGMAX_ACTION(Q, state)
    return policy</code></pre>
    </div>

    <div class="specs-table-wrapper">
      <table class="specs-table">
        <thead>
          <tr>
            <th>Characteristic</th>
            <th>Value Iteration (Dynamic Programming)</th>
            <th>Q-Learning (Model-Free RL)</th>
            <th>SARSA (On-Policy TD)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Environment Knowledge</strong></td>
            <td>Requires explicit \\(T(s, a, s')\\) and \\(R\\)</td>
            <td>Model-free (samples from interaction)</td>
            <td>Model-free (samples from interaction)</td>
          </tr>
          <tr>
            <td><strong>Policy Category</strong></td>
            <td>Exact Dynamic Planning</td>
            <td>Off-policy (learns $Q^*$ regardless of behavior)</td>
            <td>On-policy (learns value of behavior policy $\\pi_\\epsilon$)</td>
          </tr>
          <tr>
            <td><strong>Convergence Requirement</strong></td>
            <td>Contraction mapping in $L_\\infty$ norm</td>
            <td>Robbins-Monro conditions $\\sum \\alpha_t = \\infty, \\sum \\alpha_t^2 < \\infty$</td>
            <td>All state-action pairs visited infinitely often</td>
          </tr>
          <tr>
            <td><strong>Physical AI Safety Risk</strong></td>
            <td>Zero risk in simulation, requires accurate model</td>
            <td>Risk of exploring catastrophic states (core meltdown)</td>
            <td>Safer exploration along margins, avoids high-variance edges</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>
      In Physical AI applications, pure random exploration (\\(\\epsilon\\)-greedy without guardrails) is hazardous: choosing an exploratory action that dumps cryo-coolant into a superheated vacuum vessel induces destructive mechanical stress. Safe RL architectures constrain the action space using control barrier functions (CBFs), ensuring the agent policy remains within safe operational envelopes.
    </p>
  </div>

  <!-- 4. Interactive Simulation Module -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 4.4</span> Interactive Simulation Module: Reactor Thermal Grid-World</h3>
    <p>
      The interactive simulation below displays the 5x5 thermal grid of the Daedalus fusion manifold. The green cell is the cryo-vent relief target (+10 reward); red cells represent catastrophic plasma hotspots (-10 penalty). Toggle between exact Value Iteration and live Q-Learning, adjust the exploration parameter \\(\\epsilon\\), and watch the learned state values converge.
    </p>

    <div class="sim-container">
      <div class="sim-header">
        <span class="sim-title">Simulation 4.1: Tokamak Coolant Manifold Grid-World RL</span>
        <span class="sim-status">THERMAL DYNAMICS ACTIVE</span>
      </div>
      <div class="sim-body">
        <div class="sim-controls">
          <div class="sim-control-group">
            <label for="sim4-algo-select">Algorithm:</label>
            <select id="sim4-algo-select" class="sim-select">
              <option value="qlearning">Q-Learning (Model-Free RL)</option>
              <option value="value_iteration">Value Iteration (Exact Bellman DP)</option>
            </select>
          </div>
          <div class="sim-control-group">
            <label for="sim4-slider-eps">Exploration (\\(\\epsilon\\)):</label>
            <input type="range" id="sim4-slider-eps" min="0.0" max="0.8" step="0.05" value="0.2" class="sim-slider" style="width: 80px;">
            <span id="sim4-eps-val" style="font-family: var(--font-mono); font-size: 0.8rem;">0.20</span>
          </div>
          <button id="sim4-btn-run" class="btn-primary">Train (100 Ep)</button>
          <button id="sim4-btn-step" class="btn-secondary">Step Episode</button>
          <button id="sim4-btn-reset" class="btn-secondary">Reset Q-Table</button>
        </div>

        <div class="sim-canvas-wrapper">
          <canvas id="sim4-canvas" width="440" height="440" aria-label="Interactive 5 by 5 Grid World RL Canvas"></canvas>
        </div>

        <div class="sim-telemetry">
          <div class="telemetry-item">
            <span class="telemetry-label">Training Episodes</span>
            <span id="sim4-stat-episodes" class="telemetry-value">0</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Cumulative Reward</span>
            <span id="sim4-stat-reward" class="telemetry-value">0.0</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Learning Rate (\\(\\alpha\\))</span>
            <span class="telemetry-value">0.20</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Discount (\\(\\gamma\\))</span>
            <span class="telemetry-value">0.90</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 5. Academic Post-Mortem & Citations -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 4.5</span> Academic Post-Mortem &amp; Citations</h3>
    <div class="citations-box">
      <p>
        The reinforcement learning and dynamic programming formulations employed in the thermal stabilization engine derive from foundational mathematical literature:
      </p>
      <ul class="citation-list">
        <li class="citation-item">
          <strong>Bellman, R. (1957).</strong> <em>Dynamic Programming</em>. Princeton University Press. [Established the principle of optimality and formulated functional equations for sequential multi-stage decision processes].
        </li>
        <li class="citation-item">
          <strong>Watkins, C. J. C. H., &amp; Dayan, P. (1992).</strong> Q-learning. <em>Machine Learning</em>, 8(3), 279-292. [Formulated the off-policy temporal difference Q-learning algorithm and provided rigorous mathematical proofs for asymptotic convergence].
        </li>
        <li class="citation-item">
          <strong>Sutton, R. S., &amp; Barto, A. G. (2018).</strong> <em>Reinforcement Learning: An Introduction</em> (2nd ed.). MIT Press. Chapter 3 ("Finite Markov Decision Processes") and Chapter 6 ("Temporal-Difference Learning"). [Definitive reference for value functions, Bellman equations, and SARSA versus Q-learning trade-offs].
        </li>
        <li class="citation-item">
          <strong>Louwerse, M. M. (2021).</strong> <em>Understanding Artificial Minds through Human Minds</em>. Routledge. Chapter 6 ("Learning from Consequences and Feedback"). [Explored parallels between reinforcement learning reward signals and biological dopamine pathways, contrasting human risk-aversion with algorithmic exploration].
        </li>
      </ul>
    </div>
  </div>
</section>
"""
