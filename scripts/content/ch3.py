# Chapter 3: Subsystem Defense Protocols: Adversarial Search, Game Trees, & Alpha-Beta Pruning
# Syllabus Week 4
# Strict Anti-Slop enforcement: zero em dashes, zero buzzwords.

CH3_HTML = r"""
<section class="manual-chapter" id="chapter-3">
  <div class="chapter-directive">
    <div class="directive-meta-bar">
      <span>SUBSYSTEM PROTOCOL // SEC-MMX-03</span>
      <span class="declassified-stamp">SEC-CLR: COMBAT ACTIVE // ENGAGEMENT AUTH</span>
      <span>SYSTEM STATUS: THREAT ENGAGED</span>
    </div>
    <h2 class="chapter-title">Chapter 3: Subsystem Defense Protocols: Adversarial Search, Game Trees, &amp; Alpha-Beta Pruning</h2>
    <p class="chapter-subtitle">Zero-sum competitive multi-agent game formulations, recursive minimax mechanics, alpha-beta pruning proofs, and expectimax decision-making under stochastic hazards.</p>
    <table class="specs-table">
      <thead>
        <tr>
          <th>Subsystem</th>
          <th>Compute Bus</th>
          <th>Search Ply Ceiling</th>
          <th>Pruning Guarantee</th>
          <th>Physical Actuator</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Sentry Fire-Control System</td>
          <td>PCIe Gen3 x4</td>
          <td>4 Ply Real-Time</td>
          <td>Alpha-Beta ($\alpha \ge \beta$)</td>
          <td>Kinetic Defense Turrets &amp; Gimbal Servos</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- 1. System Emergency Briefing -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 3.1</span> System Emergency Briefing</h3>
    <div class="briefing-callout">
      <div class="briefing-header">
        <span class="briefing-tag">Incident Report: Cargo Bay 3 Breach &amp; Intruder Detection</span>
        <span class="briefing-status">STATUS: COMBAT ACTIVE // DEFENSE ZONE COMPROMISED</span>
      </div>
      <p class="briefing-text">
        At 04:12 shipboard time, following hull decompression, an autonomous scavenging drone penetrated Cargo Bay 3 via the breached pressure seal. The intruder active objective is to sever auxiliary cryogenic coolant manifolds to scavenge rare copper-palladium conduits. Automated defense sentry turrets have engaged internal security protocols.
      </p>
      <p class="briefing-text">
        This engagement is a deterministic, zero-sum adversarial contest: every tactical advantage achieved by the intruder directly degrades Daedalus survival margins. The sentry turret fire-control computer must anticipate hostile evasion, manage limited kinetic ammunition, respect motorized gimbal slew rates, and choose optimal firing solutions before the scavenger reaches the cryogenic manifold.
      </p>
    </div>
  </div>

  <!-- 2. Theoretical Foundation & Mathematical Formulation -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 3.2</span> Theoretical Foundation &amp; Mathematical Formulation</h3>
    
    <p>
      In single-agent search (such as \(A^*\)), the environment is passive: the agent plans a trajectory through a static or stochastic world that does not actively attempt to frustrate its objectives. In adversarial environments, multiple agents possess conflicting utility functions.
    </p>

    <div class="definition-box">
      <div class="definition-title">Formal Zero-Sum Game Definition</div>
      <p>
        A two-player, perfect-information, turn-taking zero-sum game is defined by a 6-tuple:
      </p>
      <div class="math-block">
      $$
      \langle S_0, \text{Player}(s), \text{Actions}(s), \text{Result}(s, a), \text{Terminal-Test}(s), \text{Utility}(s, p) \rangle
      $$
    </div>
      <ul>
        <li><strong>Initial State \(S_0\):</strong> The starting physical layout of sentry turrets and intruder drones in Cargo Bay 3.</li>
        <li><strong>Player Function \(\text{Player}(s)\):</strong> Defines whose turn it is to act (\(\text{MAX}\) representing ship sentry defense; \(\text{MIN}\) representing the hostile scavenger).</li>
        <li><strong>Actions \(\text{Actions}(s)\):</strong> The set of legal maneuvers or firing solutions available to the active player in state \(s\).</li>
        <li><strong>Transition Model \(\text{Result}(s, a)\):</strong> Returns the resulting state after executing action \(a\).</li>
        <li><strong>Terminal Test \(\text{Terminal-Test}(s)\):</strong> True if the engagement is resolved (e.g., intruder destroyed or cryogenic line severed); false otherwise.</li>
        <li><strong>Utility Function \(\text{Utility}(s, p)\):</strong> A numeric payoff function for player \(p\) at terminal state \(s\). In zero-sum games: \(\text{Utility}_{\text{MAX}}(s) + \text{Utility}_{\text{MIN}}(s) = 0\).</li>
      </ul>
    </div>

    <p>
      The Minimax algorithm computes the optimal strategy for \(\text{MAX}\) under the fundamental assumption that \(\text{MIN}\) plays with perfect rationality to minimize \(\text{MAX}\) payoff. The recursive minimax value \(V(s)\) is expressed as:
    </p>

    <div class="math-block">
      $$
      V(s) = \begin{cases} 
      \text{Utility}(s) & \text{if } \text{Terminal-Test}(s) \\
      \max_{a \in \text{Actions}(s)} V(\text{Result}(s, a)) & \text{if } \text{Player}(s) = \text{MAX} \\
      \min_{a \in \text{Actions}(s)} V(\text{Result}(s, a)) & \text{if } \text{Player}(s) = \text{MIN}
      \end{cases}
      $$
      <div class="formula-label">Equation 3.1: The Minimax Value Function</div>
    </div>

    <p>
      A full minimax traversal over a game tree with branching factor \(b\) and maximum depth \(m\) requires \(O(b^m)\) time and \(O(bm)\) memory. In physical combat with a 40-millisecond cycle deadline, searching to terminal depth is impossible. The engine must truncate search at a fixed cutoff depth \(d\) and apply a linear weighted evaluation function \(V_{\text{eval}}(s) = f(\mathbf{w})\):
    </p>

    <div class="math-block">
      $$
      V_{\text{eval}}(s) = f(\mathbf{w}) = \mathbf{w}^T \mathbf{f}(s) = \sum_{i=1}^{k} w_i f_i(s) = w_1 (\text{Intruder Distance}) + w_2 (\text{Turret Line-of-Sight}) + w_3 (\text{Ammunition Reserve})
      $$
      <div class="formula-label">Equation 3.2: Linear Weighted Evaluation Function for Real-Time Cutoff</div>
    </div>

    <div class="definition-box">
      <div class="definition-title">Mathematical Formulation of Alpha-Beta Pruning</div>
      <p>
        Alpha-Beta pruning computes the exact minimax decision while pruning subtrees that cannot influence the final root value. The algorithm tracks two parameters along the search path:
      </p>
      <ul>
        <li><strong>\(\alpha\):</strong> The value of the best (highest-value) choice found so far along the path for \(\text{MAX}\). Initialized to \(-\infty\).</li>
        <li><strong>\(\beta\):</strong> The value of the best (lowest-value) choice found so far along the path for \(\text{MIN}\). Initialized to \(+\infty\).</li>
      </ul>
      <p>
        <strong>Pruning Condition:</strong> At any point during tree traversal, whenever:
      </p>
      <div class="math-block">
      $$
      \alpha \ge \beta
      $$
    </div>
      <p>
        the remaining child branches of the current node are pruned immediately.
      </p>
      <p>
        <em>Proof:</em> Consider a \(\text{MIN}\) node \(n\) where \(v \le \alpha\). The parent \(\text{MAX}\) ancestor already has an alternative path guaranteeing a payoff of at least \(\alpha\). Because \(n\) is controlled by \(\text{MIN}\), its value can only decrease further as remaining children are evaluated. Therefore, \(\text{MAX}\) will never choose the branch leading to \(n\). Exploring further children of \(n\) cannot alter the decision at the parent, proving the pruning is strictly conservative and sound.
      </p>
      <p>
        <strong>Pruning Efficiency:</strong> With arbitrary move ordering, alpha-beta examines \(O(b^{3m/4})\) nodes. Under <em>perfect move ordering</em> (where the best move is always evaluated first), time complexity drops to:
      </p>
      <div class="math-block">
      $$
      O(b^{m/2})
      $$
    </div>
      <p>
        This doubles the effective search depth achievable within the same compute time budget.
      </p>
    </div>

    <p>
      When the environment includes stochastic elements (such as debris deflection, turret jamming, or venting atmospheric gas), the Expectimax algorithm replaces deterministic \(\text{MIN}\) nodes with chance nodes:
    </p>

    <div class="math-block">
      $$
      V_{\text{Expectimax}}(s) = \sum_{s'} P(s' \mid s, a) V_{\text{Expectimax}}(s')
      $$
      <div class="formula-label">Equation 3.3: Expectimax Formulation over Chance Nodes</div>
    </div>

    <p>
      Unlike Minimax, which is invariant to positive monotonic transformations of the evaluation function, Expectimax values depend strictly on positive affine transformations: \(U'(s) = c_1 U(s) + c_2\) where \(c_1 > 0\). Non-linear scaling distorts expected values, altering the resulting physical actions.
    </p>
  </div>

  <!-- 3. Algorithmic Execution / Pseudo-code -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 3.3</span> Algorithmic Execution &amp; Pseudo-code</h3>
    
    <p>
      The sentry fire-control system executes depth-limited alpha-beta pruning. It prioritizes actions using move ordering heuristics, ordering target tracking solutions by angular displacement from the turret central bore axis.
    </p>

    <div class="code-container">
      <div class="code-header">
        <span class="code-lang">Algorithm 3.1: Alpha-Beta Pruning with Depth Cutoff</span>
        <span>Target: Sentry Fire-Control System</span>
      </div>
      <pre><code>function ALPHA_BETA_SEARCH(state, max_depth):
    alpha = -INFINITY
    beta = +INFINITY
    best_action = null
    best_val = -INFINITY
    
    // Order moves to maximize pruning efficiency
    actions = ORDER_ACTIONS(state, state.get_actions(player=MAX))
    
    for each action in actions:
        next_state = state.result(action)
        val = MIN_VALUE(next_state, alpha, beta, depth=1, max_depth)
        if val &gt; best_val:
            best_val = val
            best_action = action
        alpha = max(alpha, best_val)
        
    return best_action

function MAX_VALUE(state, alpha, beta, depth, max_depth):
    if state.is_terminal() or depth &gt;= max_depth:
        return EVALUATION_FUNCTION(state)
        
    v = -INFINITY
    actions = ORDER_ACTIONS(state, state.get_actions(player=MAX))
    
    for each action in actions:
        next_state = state.result(action)
        v = max(v, MIN_VALUE(next_state, alpha, beta, depth + 1, max_depth))
        if v &gt;= beta:
            return v // Beta cutoff: MIN will avoid this branch
        alpha = max(alpha, v)
    return v

function MIN_VALUE(state, alpha, beta, depth, max_depth):
    if state.is_terminal() or depth &gt;= max_depth:
        return EVALUATION_FUNCTION(state)
        
    v = +INFINITY
    actions = ORDER_ACTIONS(state, state.get_actions(player=MIN))
    
    for each action in actions:
        next_state = state.result(action)
        v = min(v, MAX_VALUE(next_state, alpha, beta, depth + 1, max_depth))
        if v &lt;= alpha:
            return v // Alpha cutoff: MAX will avoid this branch
        beta = min(beta, v)
    return v</code></pre>
    </div>

    <div class="specs-table-wrapper">
      <table class="specs-table">
        <thead>
          <tr>
            <th>Search Algorithm</th>
            <th>Search Depth Achievable (40 ms budget)</th>
            <th>Node Expansions at \(b=4, d=4\)</th>
            <th>Pruning Savings</th>
            <th>Optimality Guarantee</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Standard Minimax</strong></td>
            <td>Depth 2 to 3</td>
            <td>341 nodes</td>
            <td>0%</td>
            <td>Optimal against optimal adversary</td>
          </tr>
          <tr>
            <td><strong>Alpha-Beta (Random Ordering)</strong></td>
            <td>Depth 3 to 4</td>
            <td>~140 nodes</td>
            <td>~58% reduction</td>
            <td>Exact match with Minimax</td>
          </tr>
          <tr>
            <td><strong>Alpha-Beta (Optimal Move Ordering)</strong></td>
            <td>Depth 4 to 6</td>
            <td>~31 nodes</td>
            <td>~91% reduction</td>
            <td>Exact match with Minimax</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>
      In physical robotics deployments, the fire-control loop must incorporate physical actuator dynamics. Turret drive motors operate at a maximum slew rate of 180 degrees per second. If the algorithm selects a tactical aim point requiring 90 degrees of travel, the transition latency is 500 ms. Move generation must therefore penalize high-angle motor travel to avoid ballistic latency lag during combat.
    </p>
      <figure class="diagram-frame">
      <div class="diagram-header">
        <span class="diagram-id">DIAGRAM 3.1 // ALPHA-BETA GAME TREE</span>
        <span>SPEC-MINIMAX-CUTOFF // BOUND: $\alpha \ge \beta$</span>
      </div>
      <div class="diagram-viewport">
        <img class="diagram-img" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKW4txBdzaxOnJaFpZoe7tSzxYgt-5PMAO246dS2vLTVl6_v2gm47_RW33&s=10" alt="Minimax game tree with active alpha-beta pruning bounds and cutoff evaluations." width="520" height="260" loading="lazy">
      </div>
      <figcaption class="diagram-caption">
        <strong>Figure 3.1:</strong> Minimax adversarial game tree with active alpha-beta pruning cutoffs. Branches where the current node value violates the parent bound ($\alpha \ge \beta$) are discarded immediately without evaluating child subtrees, reducing effective branching factor from $O(b^m)$ to $O(b^{m/2})$ under optimal move ordering (Russell &amp; Norvig, Ch. 5).
      </figcaption>
    </figure>
  </div>

  <!-- 4. Interactive Simulation Module -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 3.4</span> Interactive Simulation Module: Adversarial Defense Tree Visualizer</h3>
    <p>
      The interactive visualizer below renders the adversarial game tree for Cargo Bay 3 defense. Green nodes represent sentry \(\text{MAX}\) decisions; amber nodes represent intruder \(\text{MIN}\) decisions. Toggle between Standard Minimax and Alpha-Beta Pruning to observe how branch pruning slashes node evaluations while preserving optimal tactical outcomes.
    </p>

    <div class="sim-container">
      <div class="sim-header">
        <span class="sim-title">Simulation 3.1: Sentry Turret Adversarial Game Tree</span>
        <span class="sim-status">TACTICAL TRACKING ACTIVE</span>
      </div>
      <div class="sim-body">
        <div class="sim-controls">
          <div class="sim-control-group">
            <label for="sim3-algo-select">Pruning Mode:</label>
            <select id="sim3-algo-select" class="sim-select">
              <option value="alphabeta">Alpha-Beta Pruning (Optimal Cutoffs)</option>
              <option value="minimax">Standard Minimax (Exhaustive)</option>
            </select>
          </div>
          <div class="sim-control-group">
            <label for="sim3-depth-select">Search Depth:</label>
            <select id="sim3-depth-select" class="sim-select">
              <option value="2">2 Ply (Shallow)</option>
              <option value="3" selected>3 Ply (Nominal)</option>
              <option value="4">4 Ply (Deep)</option>
            </select>
          </div>
          <button id="sim3-btn-regen" class="btn-primary">Regenerate Tree</button>
        </div>

        <div class="sim-canvas-wrapper" id="sim3-container" style="position: relative; overflow: visible;">
          <svg id="sim3-svg" viewBox="0 0 640 320" preserveAspectRatio="xMidYMid meet" class="sim-tree-svg" aria-label="Interactive Adversarial Game Tree SVG"></svg>
          <canvas id="sim3-canvas" width="640" height="320" style="display: none;" aria-hidden="true"></canvas>
          <div id="sim3-tooltip" class="sim-tree-tooltip" role="tooltip" aria-hidden="true"></div>
        </div>

        <div class="sim-telemetry">
          <div class="telemetry-item">
            <span class="telemetry-label">Evaluated Nodes</span>
            <span id="sim3-stat-evaluated" class="telemetry-value">--</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Pruned Nodes (Savings)</span>
            <span id="sim3-stat-pruned" class="telemetry-value">--</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Root Minimax Value</span>
            <span id="sim3-stat-score" class="telemetry-value">--</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Cycle Time Margin</span>
            <span class="telemetry-value">38.4 ms (&lt; 40 ms)</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 5. Academic Post-Mortem & Citations -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 3.5</span> Academic Post-Mortem &amp; Citations</h3>
    <div class="citations-box">
      <p>
        The game-theoretic principles governing sentry engagement derive from foundational research in adversarial algorithms and computational ethics:
      </p>
      <ul class="citation-list">
        <li class="citation-item">
          <strong>Knuth, D. E., &amp; Moore, R. W. (1975).</strong> An Analysis of Alpha-Beta Pruning. <em>Artificial Intelligence</em>, 6(4), 293-326. [Proved mathematical correctness and asymptotic optimality bounds for alpha-beta cutoffs under optimal move ordering].
        </li>
        <li class="citation-item">
          <strong>Shannon, C. E. (1950).</strong> Programming a Computer for Playing Chess. <em>The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science</em>, 41(314), 256-275. [Established minimax game trees, position evaluation functions, and the horizon effect in computational game theory].
        </li>
        <li class="citation-item">
          <strong>Russell, S. J., &amp; Norvig, P. (2020).</strong> <em>Artificial Intelligence: A Modern Approach</em> (4th ed.). Pearson. Chapter 5 ("Adversarial Search and Games"). [Comprehensive derivations of alpha-beta bounds, transposition tables, and expectimax chance formulations].
        </li>
        <li class="citation-item">
          <strong>Zerilli, J. (2021).</strong> <em>A Citizen's Guide to Artificial Intelligence</em>. MIT Press. Chapter 4 ("Military AI and Lethal Autonomous Weapons Systems"). [Examined ethical boundaries and verification mandates when delegating lethal kinetic authority to real-time algorithmic search systems].
        </li>
      </ul>
    </div>
  </div>
</section>
"""
