# Chapter 1: Sensory Array & Space Mapping: Agent Architectures & Breach Avoidance Pathfinding
# Syllabus Weeks 1-2
# Strict Anti-Slop enforcement: zero em dashes, zero buzzwords.

CH1_HTML = """
<section class="manual-chapter" id="chapter-1">
  <div class="chapter-directive">
    <div class="directive-meta-bar">
      <span>SUBSYSTEM PROTOCOL // NAV-PEAS-01</span>
      <span class="declassified-stamp">SEC-CLR: TOP SECRET // CREW REBOOT AUTH</span>
      <span>SYSTEM STATUS: COMPROMISED</span>
    </div>
    <h2 class="chapter-title">Chapter 1: Sensory Array &amp; Space Mapping: Agent Architectures &amp; Breach Avoidance Pathfinding</h2>
    <p class="chapter-subtitle">Autonomous agent formulation, environmental taxonomy, uninformed search strategies, and admissible heuristic pathfinding on damaged hull geometries.</p>
    <table class="specs-table">
      <thead>
        <tr>
          <th>Subsystem</th>
          <th>Compute Bus</th>
          <th>Memory Ceiling</th>
          <th>Cycle Deadline</th>
          <th>Physical Actuator</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>LIDAR &amp; Navigation Crawler Alpha-1</td>
          <td>SPI-4 100 MHz</td>
          <td>512 KB SRAM</td>
          <td>100 ms Hard RT</td>
          <td>Magnetic Crawler DC Motors</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- 1. System Emergency Briefing -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 1.1</span> System Emergency Briefing</h3>
    <div class="briefing-callout">
      <div class="briefing-header">
        <span class="briefing-tag">Incident Report: Hull Breach Sector 4-B</span>
        <span class="briefing-status">STATUS: DEPRESSURIZING // O2 LOSS: 14.2 kPa/min</span>
      </div>
      <p class="briefing-text">
        At 03:42 shipboard time, secondary micrometeorite fragments breached the exterior titanium-carbide plating of Sector 4-B, threatening primary cryogenic bay pressurization. The primary bridge navigation network is offline. Autonomous repair crawler unit Alpha-1 has been deployed from airlock staging bay 1 to reach and weld breach point Omega before life support reserve drops below the critical 15-minute margin. The exterior hull is pitted with impassable decompression craters, exposed high-voltage wiring, and radiation plumes.
      </p>
      <p class="briefing-text">
        Alpha-1 must plan an optimal, collision-free trajectory across the discretized hull grid. Every centimeter traversed drains precious reserve battery power. The crawler embedded microprocessor operates under a strict 100-millisecond real-time cycle deadline, requiring search algorithms that minimize node expansions while guaranteeing zero risk of crawler loss in the vacuum of space.
      </p>
    </div>
  </div>

  <!-- 2. Theoretical Foundation & Mathematical Formulation -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 1.2</span> Theoretical Foundation &amp; Mathematical Formulation</h3>
    
    <p>
      An intelligent agent is formally defined as an entity that perceives its environment through sensors and acts upon that environment through actuators. The agent behavior is governed by an internal agent function, denoted mathematically as:
    </p>

    <div class="math-block">
      $$
      f: \\mathcal{P}^* \\to \\mathcal{A}
      $$
      <div class="formula-label">Equation 1.1: Agent Function Mapping Percept Sequences to Actions</div>
    </div>

    <figure class="diagram-frame">
      <div class="diagram-header">
        <span class="diagram-id">DIAGRAM 1.1 // AGENT ARCHITECTURE</span>
        <span>SPEC-PEAS-AIF1303 // RECOVERY STAGE 1</span>
      </div>
      <div class="diagram-viewport">
        <img class="diagram-img" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDTWW1w669zb2l2OZgSKBRJH4QBIaZnAuqRm9JDHg_FcSpJKhozpuqiVlL&s=10" alt="Closed-loop agent-environment interface showing state transition feedback and actuator commands." width="480" height="240" loading="lazy">
      </div>
      <figcaption class="diagram-caption">
        <strong>Figure 1.1:</strong> Closed-loop agent-environment interface. Sensory percepts are acquired from the microgravity hull domain, processed via the agent program on ARM Cortex-M7 embedded SRAM, and dispatched to robotic magnetic actuators under strict real-time physical AI deadlines (Russell &amp; Norvig, Ch. 2).
      </figcaption>
    </figure>

    <p>
      Here, \\(\\mathcal{P}^*\\) represents the history of all percept sequences accumulated by the system up to time \\(t\\), and \\(\\mathcal{A}\\) denotes the set of executable physical actions. In physical robotics, the agent program implements this function on physical hardware architecture under finite compute, memory, and battery constraints.
    </p>

    <div class="definition-box">
      <div class="definition-title">PEAS Specification: Exterior Repair Crawler Alpha-1</div>
      <ul>
        <li><strong>Performance Measure:</strong> Minimize path traversal cost, seal all structural breaches before atmospheric depletion (penalty: -1000 for breach blowout), minimize electrical energy consumption per centimeter traveled, avoid hull fracture obstacles.</li>
        <li><strong>Environment:</strong> Microgravity exterior hull surface, localized decompression craters, radiation plumes, temperature differentials from -150°C to +120°C, high-frequency cosmic noise.</li>
        <li><strong>Actuators:</strong> Magnetic crawler tracks with dual brushless DC motors, cold-gas RCS stabilization thrusters, multi-axis robotic welding arm, inductive surface clamps.</li>
        <li><strong>Sensors:</strong> Stereoscopic LIDAR array (10 Hz point cloud), surface ultrasonic thickness transducer, 6-axis inertial measurement unit (IMU), battery shunt ammeter.</li>
      </ul>
    </div>

    <p>
      Understanding the mathematical nature of the operational environment dictates algorithm selection:
    </p>
    <ul>
      <li><strong>Observability:</strong> Partially observable if hull debris occludes remote sectors; fully observable once the orbital LIDAR satellite relays the elevation grid map.</li>
      <li><strong>Determinism:</strong> Stochastic in the presence of micro-meteoroid impacts and track slip, though modeled deterministically for initial path generation.</li>
      <li><strong>Episodic vs. Sequential:</strong> Sequential. Current steering decisions affect future crawler stability, power levels, and distance to the target breach.</li>
      <li><strong>Static vs. Dynamic:</strong> Dynamic. Breach expansion and debris trajectories alter traversability while the agent calculates its route.</li>
      <li><strong>Discrete vs. Continuous:</strong> Continuous physical motion, discretized into a navigation grid graph \\(G = (V, E)\\) for computational tractability.</li>
    </ul>

    <p>
      Formally, a search problem on the hull grid is defined by a 5-tuple:
    </p>

    <div class="math-block">
      $$
      \\langle S_0, \\text{Actions}(s), \\text{Result}(s, a), \\text{Goal-Test}(s), c(s, a, s') \\rangle
      $$
      <div class="formula-label">Equation 1.2: Formal Problem Formulation Tuple</div>
    </div>

    <p>
      Where \\(S_0\\) is the initial coordinate state, \\(\\text{Actions}(s)\\) returns the set of legal directional movements, \\(\\text{Result}(s, a)\\) yields the deterministic transition state \\(s'\\), \\(\\text{Goal-Test}(s)\\) verifies arrival at the target breach coordinate, and \\(c(s, a, s')\\) is the step cost representing energy consumption and surface traversal roughness.
    </p>

    <p>
      In uninformed search, the agent explores states without domain-specific knowledge beyond the step cost. Breadth-First Search (BFS) expands the shallowest unexpanded node using a FIFO queue, guaranteeing optimality when all step costs are equal (\\(c = 1\\)). Depth-First Search (DFS) expands the deepest node via a LIFO stack, which requires minimal space \\(O(bm)\\) but risks non-termination in cyclic graphs and fails to guarantee shortest paths. Uniform-Cost Search (UCS), equivalent to Dijkstra algorithm, expands nodes in order of cumulative path cost \\(g(n)\\) via a priority queue:
    </p>

    <div class="math-block">
      $$
      g(n) = \\sum_{i=1}^{k} c(s_{i-1}, a_i, s_i)
      $$
      <div class="formula-label">Equation 1.3: Cumulative Path Cost from Start to Node n</div>
    </div>

    <p>
      UCS is complete and cost-optimal for positive edge costs \\(c(s, a, s') \\ge \\epsilon > 0\\), but it explores uniformly in all directions, expanding unnecessary nodes opposite the target goal.
    </p>

    <p>
      Informed search introduces a heuristic function \\(h(n)\\), estimating the remaining cost to the goal from node \\(n\\). The \\(A^*\\) search algorithm combines the actual past cost \\(g(n)\\) with the estimated future cost \\(h(n)\\):
    </p>

    <div class="math-block">
      $$
      f(n) = g(n) + h(n)
      $$
      <div class="formula-label">Equation 1.4: A* Node Evaluation Function</div>
    </div>

    <p>
      For grid navigation with orthogonal 4-way movement, the Manhattan distance heuristic is calculated as:
    </p>

    <div class="math-block">
      $$
      h_{\\text{Manhattan}}(n) = |x_n - x_g| + |y_n - y_g|
      $$
      <div class="formula-label">Equation 1.5: Manhattan Distance Heuristic</div>
    </div>

    <p>
      When diagonal movement is permitted, the Euclidean distance provides a straight-line geometric lower bound:
    </p>

    <div class="math-block">
      $$
      h_{\\text{Euclidean}}(n) = \\sqrt{(x_n - x_g)^2 + (y_n - y_g)^2}
      $$
      <div class="formula-label">Equation 1.6: Euclidean Distance Heuristic</div>
    </div>

    <p>
      To guarantee that \\(A^*\\) finds the optimal path without suboptimal lock-in, the heuristic must satisfy two mathematical properties:
    </p>

    <div class="definition-box">
      <div class="definition-title">Mathematical Conditions for A* Optimality</div>
      <p>
        <strong>1. Admissibility (Tree Search Optimality):</strong> A heuristic \\(h(n)\\) is admissible if it never overestimates the true minimal cost \\(h^*(n)\\) to reach the goal:
      </p>
      <div class="math-block">
      $$
      \\forall n, \\quad 0 \\le h(n) \\le h^*(n)
      $$
    </div>
      <p>
        <em>Proof sketch:</em> Suppose a suboptimal goal \\(G_2\\) is selected from the frontier before the optimal goal \\(G\\). Because \\(G_2\\) is a goal node, \\(h(G_2) = 0\\), so \\(f(G_2) = g(G_2) > g(G)\\). For any ancestor node \\(n\\) of \\(G\\) on the frontier, \\(f(n) = g(n) + h(n) \\le g(n) + h^*(n) = g(G) < g(G_2) = f(G_2)\\). Hence, \\(A^*\\) will always expand \\(n\\) before \\(G_2\\), ensuring \\(G_2\\) cannot be returned first.
      </p>
      <p>
        <strong>2. Consistency / Monotonicity (Graph Search Optimality):</strong> In graph search with a closed set (explored table), a heuristic \\(h(n)\\) is consistent if for every node \\(n\\) and every successor \\(n'\\) generated by action \\(a\\), the estimated cost satisfies the triangle inequality:
      </p>
      <div class="math-block">
      $$
      h(n) \\le c(n, a, n') + h(n')
      $$
    </div>
      <p>
        Consistency guarantees that the sequence of \\(f(n)\\) values along any path is non-decreasing: \\(f(n') = g(n') + h(n') = g(n) + c(n, a, n') + h(n') \\ge g(n) + h(n) = f(n)\\). Consequently, the first time \\(A^*\\) expands a state, the path found to that state is guaranteed to be optimal, eliminating the need to reopen nodes in the closed set.
      </p>
      <p>
        <strong>Dominance:</strong> Given two admissible heuristics \\(h_1\\) and \\(h_2\\), if \\(h_2(n) \\ge h_1(n)\\) for all nodes \\(n\\), then \\(h_2\\) dominates \\(h_1\\). A dominating heuristic expands fewer or equal nodes than \\(h_1\\), directly conserving embedded CPU cycles.
      </p>
    </div>
  </div>

  <!-- 3. Algorithmic Execution / Pseudo-code -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 1.3</span> Algorithmic Execution &amp; Pseudo-code</h3>
    
    <p>
      Onboard Alpha-1, pathfinding executes on an ARM Cortex-M7 microcontroller with 512 KB of SRAM. To prevent memory exhaustion during graph search, we implement \\(A^*\\) using a binary min-heap for the priority queue and an open-addressing hash set for visited coordinates.
    </p>

    <div class="code-container">
      <div class="code-header">
        <span class="code-lang">Algorithm 1.1: Graph-Search A* with Consistent Heuristic</span>
        <span>Target: Embedded Path Planner</span>
      </div>
      <pre><code>function A_STAR_HULL_SEARCH(grid, start, goal, heuristic_fn):
    // Priority queue holds tuples (f_cost, node_coords)
    frontier = PriorityQueue()
    frontier.insert(item=start, priority=heuristic_fn(start, goal))
    
    // Tracking tables
    came_from = HashMap()          // Maps node -> predecessor node
    cost_so_far = HashMap()        // Maps node -> g_cost
    closed_set = HashSet()         // Explored nodes
    
    cost_so_far[start] = 0
    came_from[start] = null
    
    while not frontier.is_empty():
        current = frontier.extract_min()
        
        // Goal test upon expansion, not generation
        if current == goal:
            return RECONSTRUCT_PATH(came_from, current)
            
        if current in closed_set:
            continue
        closed_set.add(current)
        
        for next_node in grid.get_passable_neighbors(current):
            if next_node in closed_set:
                continue
                
            new_cost = cost_so_far[current] + grid.traversal_cost(current, next_node)
            
            if next_node not in cost_so_far or new_cost &lt; cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic_fn(next_node, goal)
                frontier.insert(item=next_node, priority=priority)
                came_from[next_node] = current
                
    return FAILURE // No passable path through hull breach debris</code></pre>
    </div>

    <div class="specs-table-wrapper">
      <table class="specs-table">
        <thead>
          <tr>
            <th>Search Strategy</th>
            <th>Frontier Structure</th>
            <th>Time Complexity</th>
            <th>Space Complexity</th>
            <th>Complete?</th>
            <th>Cost-Optimal?</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Breadth-First Search (BFS)</strong></td>
            <td>FIFO Queue</td>
            <td>$O(b^d)$</td>
            <td>$O(b^d)$</td>
            <td>Yes (if $b < \\infty$)</td>
            <td>Yes (if unit step costs)</td>
          </tr>
          <tr>
            <td><strong>Depth-First Search (DFS)</strong></td>
            <td>LIFO Stack</td>
            <td>$O(b^m)$</td>
            <td>$O(bm)$</td>
            <td>No (fails in infinite loops)</td>
            <td>No</td>
          </tr>
          <tr>
            <td><strong>Uniform-Cost Search (UCS)</strong></td>
            <td>Priority Queue by $g(n)$</td>
            <td>$O(b^{1 + \\lfloor C^* / \\epsilon \\rfloor})$</td>
            <td>$O(b^{1 + \\lfloor C^* / \\epsilon \\rfloor})$</td>
            <td>Yes (if $c \\ge \\epsilon > 0$)</td>
            <td>Yes</td>
          </tr>
          <tr>
            <td><strong>$A^*$ Search (Admissible $h$)</strong></td>
            <td>Priority Queue by $g(n) + h(n)$</td>
            <td>$O(b^{\\epsilon d})$ (heuristic quality dependent)</td>
            <td>$O(b^d)$ (retains all nodes in memory)</td>
            <td>Yes</td>
            <td>Yes</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
      <figure class="diagram-frame" style="margin: 0;">
        <div class="diagram-header">
          <span class="diagram-id">DIAGRAM 1.2 // A* PRIORITY QUEUE</span>
          <span>MEMORY FOOTPRINT: $O(b^d)$</span>
        </div>
        <div class="diagram-viewport">
          <img class="diagram-img" src="https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcSrkb6P5DRmgqrVpyprbkvIn4vmrYAf_YuueXXeJzEkuWYzKYdHmoN7Nt3xDoP797fE5H5SnJLOusuKWKo" alt="A* and UCS Priority Queue frontier node expansion visualization." width="380" height="220" loading="lazy">
        </div>
        <figcaption class="diagram-caption">
          <strong>Figure 1.2:</strong> Priority queue frontier expansion under evaluation function \(f(n) = g(n) + h(n)\).
        </figcaption>
      </figure>

      <figure class="diagram-frame" style="margin: 0;">
        <div class="diagram-header">
          <span class="diagram-id">DIAGRAM 1.3 // DFS CALL STACK</span>
          <span>MEMORY FOOTPRINT: $O(bm)$</span>
        </div>
        <div class="diagram-viewport">
          <img class="diagram-img" src="https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcSe2j5QCV9o_Lr5LRTH-NLl_COclfYTZv48x9isWeJujk8bDCYYbYUIGXrN02bla4GjbbxkIWY-a_x7NIY" alt="Depth-first search call-stack recursive depth traversal." width="380" height="220" loading="lazy">
        </div>
        <figcaption class="diagram-caption">
          <strong>Figure 1.3:</strong> LIFO call-stack memory depth during uninformed depth-first search traversal.
        </figcaption>
      </figure>
    </div>

    <p>
      In physical robotics applications, memory footprint is the primary bottleneck. Because \\(A^*\\) retains all generated nodes in memory, memory consumption on a dense 1000x1000 grid can exceed available SRAM before goal discovery. Under severe RAM limits, Memory-Bounded \\(A^*\\) (SMA*) or Iterative-Deepening \\(A^*\\) (IDA*) can be used, trading redundant re-expansions for an \\(O(bd)\\) linear memory footprint.
    </p>
  </div>

  <!-- 4. Interactive Simulation Module -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 1.4</span> Interactive Simulation Module: Exterior Hull Pathfinder</h3>
    <p>
      Test search strategies on the interactive exterior hull grid below. Click on any cell to place or remove structural breach obstacles (rendered in red). Select search algorithms from the control panel to observe how the frontier expands across the ship surface.
    </p>

    <div class="sim-container">
      <div class="sim-header">
        <span class="sim-title">Simulation 1.1: Hull Pathfinder Guidance Array</span>
        <span class="sim-status">SYSTEM ONLINE</span>
      </div>
      <div class="sim-body">
        <div class="sim-controls">
          <div class="sim-control-group">
            <label for="sim1-algo-select">Algorithm:</label>
            <select id="sim1-algo-select" class="sim-select">
              <option value="astar_manhattan">A* Search (Manhattan Heuristic)</option>
              <option value="astar_euclidean">A* Search (Euclidean Heuristic)</option>
              <option value="ucs">Uniform-Cost Search (UCS)</option>
              <option value="bfs">Breadth-First Search (BFS)</option>
              <option value="dfs">Depth-First Search (DFS)</option>
            </select>
          </div>
          <button id="sim1-btn-run" class="btn-primary">Auto Run</button>
          <button id="sim1-btn-step" class="btn-secondary">Single Step</button>
          <button id="sim1-btn-reset" class="btn-secondary">Reset Path</button>
          <button id="sim1-btn-clear-obs" class="btn-secondary">Clear Debris</button>
        </div>

        <div class="sim-canvas-wrapper">
          <canvas id="sim1-canvas" width="480" height="480" aria-label="Interactive 12 by 12 Hull Pathfinding Grid Canvas"></canvas>
        </div>

        <div class="sim-telemetry">
          <div class="telemetry-item">
            <span class="telemetry-label">Nodes Expanded</span>
            <span id="sim1-stat-expanded" class="telemetry-value">0</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Frontier Size</span>
            <span id="sim1-stat-frontier" class="telemetry-value">1</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Path Traversal Cost</span>
            <span id="sim1-stat-cost" class="telemetry-value">Pending</span>
          </div>
          <div class="telemetry-item">
            <span class="telemetry-label">Hardware Cycle Budget</span>
            <span class="telemetry-value">&lt; 100 ms</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 5. Academic Post-Mortem & Citations -->
  <div class="section-block">
    <h3 class="section-title"><span class="section-icon-pill">SEC 1.5</span> Academic Post-Mortem &amp; Citations</h3>
    <div class="citations-box">
      <p>
        The navigation procedures implemented in Alpha-1 originate from the seminal foundations of state-space search and heuristic pathfinding:
      </p>
      <ul class="citation-list">
        <li class="citation-item">
          <strong>Hart, P. E., Nilsson, N. J., &amp; Raphael, B. (1968).</strong> A Formal Basis for the Heuristic Determination of Minimum Cost Paths. <em>IEEE Transactions on Systems Science and Cybernetics</em>, 4(2), 100-107. [Formulated the \\(A^*\\) algorithm and proved cost-optimality under admissible heuristics].
        </li>
        <li class="citation-item">
          <strong>Russell, S. J., &amp; Norvig, P. (2020).</strong> <em>Artificial Intelligence: A Modern Approach</em> (4th ed.). Pearson. Chapter 2 ("Intelligent Agents") and Chapter 3 ("Solving Problems by Searching"). [Provided the PEAS framework, environmental taxonomy, and proofs for heuristic consistency and dominance].
        </li>
        <li class="citation-item">
          <strong>Louwerse, M. M. (2021).</strong> <em>Understanding Artificial Minds through Human Minds</em>. Routledge. Chapter 3 ("Spatial Reasoning and Navigation"). [Analyzed how machine pathfinding algorithms differ from human spatial mental models, demonstrating how systematic heuristic expansion prevents cognitive oversights during stress].
        </li>
        <li class="citation-item">
          <strong>Zerilli, J. (2021).</strong> <em>A Citizen's Guide to Artificial Intelligence</em>. MIT Press. Chapter 2 ("Algorithms and Autonomy"). [Explored the moral and operational accountability of delegating safety-critical navigation decisions to autonomous machines in hazardous environments].
        </li>
      </ul>
    </div>
  </div>
</section>
"""
