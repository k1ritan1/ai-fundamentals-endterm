# Chapter 2: Auxiliary Power Distribution under Constraint: Local Search & Constraint Satisfaction Problems
# Syllabus Week 3
# Strict Anti-Slop enforcement: zero em dashes, zero buzzwords.

CH2_HTML = """
<section class="manual-chapter" id="chapter-2">
  <div class="chapter-directive">
    <div class="directive-meta-bar">
      <span>SUBSYSTEM PROTOCOL // PWR-CSP-02</span>
      <span class="declassified-stamp">SEC-CLR: RESTRICTED // AUX BUS CONTINGENCY</span>
      <span>SYSTEM STATUS: OVERLOAD WARNING</span>
    </div>
    <h2 class="chapter-title">Chapter 2: Auxiliary Power Distribution under Constraint: Local Search &amp; Constraint Satisfaction Problems</h2>
    <p class="chapter-subtitle">Local optimization landscapes, simulated annealing thermal schedules, and formal constraint satisfaction programming for resource-bounded electrical distribution.</p>
    <table class="specs-table">
      <thead>
        <tr>
          <th>Subsystem</th>
          <th>Compute Bus</th>
          <th>Memory Ceiling</th>
          <th>Propagation Constraint</th>
          <th>Actuator Interface</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Auxiliary Power Distribution Unit</td>
          <td>CAN-2 1.0 Mbps</td>
          <td>1.0 MB SRAM</td>
          <td>AC-3 Arc Consistency Queue</td>
          <td>High-Voltage Solid-State Relays</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- 1. System Emergency Briefing -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 2.1</span> System Emergency Briefing</h3>
    <div class="briefing-callout">
      <div class="briefing-header">
        <span class="briefing-tag">Incident Report: Auxiliary Power Bus Overload</span>
        <span class="briefing-status">STATUS: BUS THERMAL WARNING // CAPACITY: 8.0 kW CAP</span>
      </div>
      <p class="briefing-text">
        Primary tokamak fusion transmission conduits have suffered magnetic containment breakdown, dropping the ship main electrical distribution grid. All vessel operations are temporarily routed through the auxiliary emergency lithium-hydride fuel cell bank. Total instantaneous power capacity is capped at 8.0 kilowatts to prevent irreversible bus-bar thermal melting.
      </p>
      <p class="briefing-text">
        Six mission-critical subsystems compete for this restricted electrical budget: Life Support, Kinetic Shielding, Cryogenic Stasis Pods, Navigation Array, Thruster Feeds, and Communications. Uncoordinated allocation will induce inductive transformer spikes, triggering emergency circuit breakers and asphyxiating the dormant crew. Engineering personnel must execute formal constraint satisfaction protocols to find a viable, conflict-free power configuration within 90 seconds.
      </p>
    </div>
  </div>

  <!-- 2. Theoretical Foundation & Mathematical Formulation -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 2.2</span> Theoretical Foundation &amp; Mathematical Formulation</h3>
    
    <p>
      When the sequence of actions leading to a goal is irrelevant and only the final configuration matters, the planning challenge transitions from pathfinding to local search and optimization. In local search, the algorithm maintains one or more active states and moves iteratively toward neighboring configurations on an objective function surface \\(f(s)\\).
    </p>

    <p>
      Hill-Climbing search (greedy local search) continuously moves in the direction of increasing objective value \\(\\Delta f > 0\\). In state-space landscapes with complex topologies, standard hill climbing suffers from three classic structural failure modes:
    </p>
    <ul>
      <li><strong>Local Maxima:</strong> Peaks higher than neighboring states but lower than the global optimum, trapping the greedy search.</li>
      <li><strong>Plateaus:</strong> Flat regions where neighboring states have identical evaluation scores (\\(\\Delta f = 0\\)), causing the search to wander aimlessly without a directional gradient.</li>
      <li><strong>Ridges:</strong> Sequences of local maxima that slope gently upward, where individual orthogonal steps in any cardinal direction yield lower values, stalling progress.</li>
    </ul>

    <p>
      To escape local traps, Simulated Annealing borrows principles from statistical thermodynamics, modeling the controlled cooling of metallurgical crystal structures. At each iteration, a random neighbor state \\(s'\\) is generated. If \\(s'\\) improves the objective (\\(\\Delta E = f(s) - f(s') < 0\\) for cost minimization), the transition is accepted unconditionally. If the neighbor worsens the objective (\\(\\Delta E > 0\\)), the algorithm accepts the move probabilistically according to the Boltzmann-Gibbs distribution:
    </p>

    <div class="math-block">
      $$
      P(\\text{accept } s' \\mid s) = \\begin{cases} 
      1 & \\text{if } \\Delta E \\le 0 \\\\ 
      \\exp\\left(-\\frac{\\Delta E}{T}\\right) & \\text{if } \\Delta E > 0 
      \\end{cases}
      $$
      <div class="formula-label">Equation 2.1: Metropolis-Hastings Acceptance Criterion</div>
    </div>

    <p>
      Here, \\(T\\) is an artificial temperature parameter governed by a monotonic annealing cooling schedule \\(T(t)\\), such as geometric decay \\(T_{k+1} = \\alpha T_k\\) where \\(0.85 \\le \\alpha < 1.0\\). When \\(T\\) is high, the agent accepts suboptimal moves freely, exploring diverse energy basins. As \\(T \\to 0\\), the probability of accepting worse moves approaches zero, causing the algorithm to settle smoothly into the nearest deep optimum.
    </p>

    <div class="definition-box">
      <div class="definition-title">Formal Constraint Satisfaction Problem (CSP) Definition</div>
      <p>
        A Constraint Satisfaction Problem is formally defined as a 3-tuple \\(\\langle X, D, C \\rangle\\):
      </p>
      <ul>
        <li><strong>Variables \\(X\\):</strong> A finite set of variables \\(X = \\{X_1, X_2, \\dots, X_n\\}\\). For the power grid: \\(X = \\{\\text{LS}, \\text{KS}, \\text{CP}, \\text{NV}, \\text{TR}, \\text{CM}\\}\\).</li>
        <li><strong>Domains \\(D\\):</strong> A set of discrete domains \\(D = \\{D_1, D_2, \\dots, D_n\\}\\), where each \\(D_i\\) represents the allowable power levels for variable \\(X_i\\). For example, \\(D_{\\text{LS}} = \\{2, 3\\}\\), \\(D_{\\text{TR}} = \\{0, 1, 2, 3\\}\\).</li>
        <li><strong>Constraints \\(C\\):</strong> A set of constraints \\(C = \\{C_1, C_2, \\dots, C_m\\}\\). Each constraint \\(C_j = \\langle \\text{scope}, R \\rangle\\) specifies the subset of variables involved and the relation restricting their simultaneous assignments.</li>
      </ul>
    </div>

    <p>
      The Daedalus emergency power allocation is constrained by physical hardware limitations:
    </p>

    <div class="math-block">
      $$
      \\begin{aligned}
      &C_1: \\quad \\text{LS} + \\text{KS} + \\text{CP} + \\text{NV} + \\text{TR} + \\text{CM} \\le 8.0 \\quad \\text{(Total Bus Capacity Limit)} \\\\
      &C_2: \\quad \\text{KS} + \\text{TR} \\le 4.0 \\quad \\text{(Substation Alpha Overheating Threshold)} \\\\
      &C_3: \\quad \\text{LS} \\ge 2.0 \\quad \\text{(Life Support Atmospheric Scrubbing Minimum)} \\\\
      &C_4: \\quad \\text{CP} \\ge 1.0 \\quad \\text{(Cryogenic Stasis Cryo-Fluid Recirculation)}
      \\end{aligned}
      $$
      <div class="formula-label">Equation 2.2: Physical Hard Constraints on Vessel Electrical Buses</div>
    </div>

    <p>
      Solving CSPs through pure backtracking search (depth-first search with single-variable trial assignments) has a worst-case time complexity of \\(O(d^n)\\), where \\(d = \\max |D_i|\\) is domain size and \\(n\\) is the number of variables. To achieve tractability, the agent combines search with constraint propagation.
    </p>

    <div class="definition-box">
      <div class="definition-title">Inference: Arc Consistency (AC-3) &amp; Variable Ordering Heuristics</div>
      <p>
        A directed arc \\((X_i, X_j)\\) in the constraint graph is arc-consistent if for every value \\(x \\in D_i\\), there exists at least one value \\(y \\in D_j\\) satisfying the constraint between \\(X_i\\) and \\(X_j\\). The AC-3 algorithm enforces pairwise consistency across all arcs:
      </p>
      <div class="math-block">
      $$
      \\forall x \\in D_i, \\quad \\exists y \\in D_j \\quad \\text{such that} \\quad (x, y) \\in R_{ij}
      $$
    </div>
      <p>
        If no such \\(y\\) exists, \\(x\\) is pruned from \\(D_i\\). Whenever a domain is modified, all incoming arcs \\((X_k, X_i)\\) are re-added to the verification queue. The maximum time complexity of AC-3 is \\(O(cd^3)\\), where \\(c\\) is the number of binary constraints.
      </p>
      <p>
        Backtracking efficiency is enhanced by three standard heuristics:
      </p>
      <ul>
        <li><strong>Minimum Remaining Values (MRV / "Fail-First"):</strong> Choose the unassigned variable with the fewest remaining legal values in its domain. This prunes failing branches at the shallowest possible depth.</li>
        <li><strong>Degree Heuristic:</strong> Used as a tie-breaker for MRV; selects the variable involved in the largest number of constraints with other unassigned variables.</li>
        <li><strong>Least Constraining Value (LCV / "Fail-Last"):</strong> Given a chosen variable, select the domain value that eliminates the fewest choices for neighboring variables in the constraint graph.</li>
      </ul>
    </div>

    <figure class="diagram-frame">
      <div class="diagram-header">
        <span class="diagram-id">DIAGRAM 2.1 // CONSTRAINT TREE PRUNING</span>
        <span>SPEC-CSP-AC3 // POWER ROUTING DOMAINS</span>
      </div>
      <div class="diagram-viewport">
        <img class="diagram-img" src="https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcQLukEDG74V1ThYV4e-5InlrSgsIl5jjtBdAEw42p1DKsNJ5dg31Bnreuf-Cb-_IKklsDLiogRAeSlkXZs" alt="State-space tree pruning and backtracking search under power routing domain constraints (AC-3)." width="500" height="280" loading="lazy">
      </div>
      <figcaption class="diagram-caption">
        <strong>Figure 2.1:</strong> State-space tree pruning and backtracking search under power routing domain constraints. By maintaining arc consistency (AC-3) across binary transmission line pairs, inconsistent branch allocations are eliminated before recursive exploration, pruning factorial search spaces (Russell &amp; Norvig, Ch. 6).
      </figcaption>
    </figure>
  </div>

  <!-- 3. Algorithmic Execution / Pseudo-code -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 2.3</span> Algorithmic Execution &amp; Pseudo-code</h3>
    
    <p>
      The emergency electrical switching logic combines AC-3 arc consistency pruning with recursive backtracking search. In physical AI deployments, variables represent real inductive relays. Setting an invalid assignment can blow physical fuses, making forward checking mandatory before commanding physical solenoid switches.
    </p>

    <div class="code-container">
      <div class="code-header">
        <span class="code-lang">Algorithm 2.1: AC-3 Arc Consistency &amp; Backtracking CSP Solver</span>
        <span>Target: Auxiliary Power Router</span>
      </div>
      <pre><code>function SOLVE_POWER_GRID_CSP(variables, domains, constraints):
    // Enforce initial arc consistency before starting search
    if not AC3(variables, domains, constraints):
        return FAILURE // Inconsistent constraints: immediate bus trip
    return BACKTRACK(assignment={}, variables, domains, constraints)

function AC3(variables, domains, constraints):
    queue = Queue()
    for each binary constraint C(Xi, Xj) in constraints:
        queue.push((Xi, Xj))
        queue.push((Xj, Xi))
        
    while not queue.is_empty():
        (Xi, Xj) = queue.pop()
        if REVISE(Xi, Xj, domains, constraints):
            if len(domains[Xi]) == 0:
                return false // Domain wiped out, problem unsolvable
            for each Xk in NEIGHBORS(Xi) - {Xj}:
                queue.push((Xk, Xi))
    return true

function REVISE(Xi, Xj, domains, constraints):
    revised = false
    for each x in copy(domains[Xi]):
        // Check if there is any y in Dj satisfying constraint(x, y)
        if not any(constraints.satisfies(Xi=x, Xj=y) for y in domains[Xj]):
            domains[Xi].remove(x)
            revised = true
    return revised

function BACKTRACK(assignment, variables, domains, constraints):
    if len(assignment) == len(variables):
        return assignment // All power buses successfully scheduled
        
    // Apply MRV (Minimum Remaining Values) heuristic
    var = SELECT_UNASSIGNED_VARIABLE_MRV(assignment, variables, domains)
    
    // Apply LCV (Least Constraining Value) ordering
    for each value in ORDER_DOMAIN_VALUES_LCV(var, assignment, domains, constraints):
        if IS_CONSISTENT(var, value, assignment, constraints):
            assignment[var] = value
            
            // Forward checking: prune conflicting values from neighbor domains
            inferences = FORWARD_CHECK(var, value, assignment, domains, constraints)
            if inferences != FAILURE:
                result = BACKTRACK(assignment, variables, domains, constraints)
                if result != FAILURE:
                    return result
                    
            delete assignment[var]
            RESTORE_DOMAINS(inferences, domains)
            
    return FAILURE</code></pre>
    </div>

    <div class="specs-table-wrapper">
      <table class="specs-table">
        <thead>
          <tr>
            <th>Algorithm</th>
            <th>Search Type</th>
            <th>Completeness</th>
            <th>Optimality</th>
            <th>Physical AI Risk Profile</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Simple Hill Climbing</strong></td>
            <td>Local / Greedy</td>
            <td>No (trapped in local optima)</td>
            <td>No</td>
            <td>High: leaves vessel partially powered in local sub-peak</td>
          </tr>
          <tr>
            <td><strong>Simulated Annealing</strong></td>
            <td>Stochastic Local</td>
            <td>Asymptotically Complete</td>
            <td>Yes (with infinite cooling)</td>
            <td>Medium: requires careful thermal schedule tuning</td>
          </tr>
          <tr>
            <td><strong>Backtracking + AC-3 + MRV</strong></td>
            <td>Systematic Tree Search</td>
            <td>Yes (finite discrete domains)</td>
            <td>Yes (finds valid satisfying state)</td>
            <td>Low: guarantees hardware safety constraints are respected</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>
      Physical hardware safety imposes strict limits on the solver. The auxiliary bus controllers must evaluate allocations within 50 milliseconds to prevent undervoltage chatter in critical relays. If the CSP solver returns failure (indicating that total demand exceeds available energy even under optimal distribution), the supervisory controller triggers load-shedding protocols, dropping communications and thruster warming to preserve human life support.
    </p>
  </div>

  <!-- 4. Interactive Simulation Module -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 2.4</span> Interactive Simulation Module: Power Grid CSP Sandbox</h3>
    <p>
      The interactive control panel below models the auxiliary power distribution matrix of the Daedalus. Adjust subsystem voltage allocations manually, adjust the total capacity cap, or trigger the automated CSP solver to observe constraint resolution in real time.
    </p>

    <div class="sim-container" id="sim2-container">
      <div class="sim-header">
        <span class="sim-title">Simulation 2.1: Auxiliary Subsystem Power Allocation Matrix</span>
        <span class="sim-status">BUS TELEMETRY READY</span>
      </div>
      <div class="sim-body">
        <div class="sim-controls">
          <div class="sim-control-group">
            <label for="sim2-algo-select">Inference Engine:</label>
            <select id="sim2-algo-select" class="sim-select">
              <option value="backtracking">Backtracking CSP (AC-3 + MRV)</option>
              <option value="hill_climbing">Local Search (Hill Climbing)</option>
            </select>
          </div>
          <div class="sim-control-group">
            <label for="sim2-power-limit">Max Power Cap (kW):</label>
            <input type="number" id="sim2-power-limit" class="sim-input" value="8" min="4" max="14" style="width: 65px;">
          </div>
          <button id="sim2-btn-solve" class="btn-primary">Execute Solver</button>
          <button id="sim2-btn-step" class="btn-secondary">Step Search</button>
          <button id="sim2-btn-reset" class="btn-secondary">Reset Bus</button>
        </div>

        <div id="sim2-bus-list" style="background-color: var(--bg-primary); border: 1px solid var(--border-subtle); border-radius: 4px; margin-bottom: 1rem;">
          <!-- Dynamically populated by PowerGridCSPSim -->
        </div>

        <div class="sim-telemetry">
          <div class="telemetry-item">
            <span class="telemetry-label">Total Bus Draw</span>
            <span id="sim2-stat-total" class="telemetry-value">7 / 8 kW</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Active Conflicts</span>
            <span id="sim2-stat-conflicts" class="telemetry-value">0</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Constraint Status</span>
            <span id="sim2-stat-status" class="telemetry-value" style="color: #10b981;">CSP SATISFIED</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Bus Overheat Safety</span>
            <span class="telemetry-value">NOMINAL (&lt; 65°C)</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 5. Academic Post-Mortem & Citations -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 2.5</span> Academic Post-Mortem &amp; Citations</h3>
    <div class="citations-box">
      <p>
        The mathematical frameworks underlying the power routing engine derive from the foundational literature of constraint satisfaction and combinatorial optimization:
      </p>
      <ul class="citation-list">
        <li class="citation-item">
          <strong>Mackworth, A. K. (1977).</strong> Consistency in Networks of Relations. <em>Artificial Intelligence</em>, 8(1), 99-118. [Originated the arc consistency algorithms, specifically establishing AC-3 as the canonical standard for constraint propagation].
        </li>
        <li class="citation-item">
          <strong>Kirkpatrick, S., Gelatt, C. D., &amp; Vecchi, M. P. (1983).</strong> Optimization by Simulated Annealing. <em>Science</em>, 220(4598), 671-680. [Demonstrated how physical thermal annealing models solve NP-hard combinatorial optimization problems].
        </li>
        <li class="citation-item">
          <strong>Russell, S. J., &amp; Norvig, P. (2020).</strong> <em>Artificial Intelligence: A Modern Approach</em> (4th ed.). Pearson. Chapter 4 ("Search in Complex Environments") and Chapter 6 ("Constraint Satisfaction Problems"). [Detailed theoretical treatment of MRV heuristics, LCV value ordering, and formal constraint graphs].
        </li>
        <li class="citation-item">
          <strong>Louwerse, M. M. (2021).</strong> <em>Understanding Artificial Minds through Human Minds</em>. Routledge. Chapter 4 ("Problem Solving and Constraint Logic"). [Contrasted human heuristic reasoning under resource pressure with algorithmic constraint propagation, explaining why human operators succumb to tunnel vision during power grid crises].
        </li>
      </ul>
    </div>
  </div>
</section>
"""
