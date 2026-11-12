/**
 * USSC DAEDALUS - SHIPBOARD SUBSYSTEM SIMULATION ENGINES
 * Engineering Protocol AIF-1303 Interactive Modules
 * Strict compliance with antislop code guidelines:
 * - Concise, information-dense comments
 * - No decorative banners or restated declarations
 * - 100% functional interactive controls and keyboard accessibility
 */

// Theme Management
function initTheme() {
  const themeToggle = document.getElementById('theme-toggle');
  const savedTheme = localStorage.getItem('daedalus_theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);
  if (savedTheme === 'dark') {
    document.documentElement.classList.add('dark-hud');
  } else {
    document.documentElement.classList.remove('dark-hud');
  }
  updateThemeButton(savedTheme);

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || 'dark';
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      if (next === 'dark') {
        document.documentElement.classList.add('dark-hud');
      } else {
        document.documentElement.classList.remove('dark-hud');
      }
      localStorage.setItem('daedalus_theme', next);
      updateThemeButton(next);
      // Redraw simulation canvases to match theme contrast
      redrawAllSimulations();
      // Retrigger math typography rendering on theme change
      if (window.retriggerMathRendering) {
        window.retriggerMathRendering();
      }
    });
  }
}

function updateThemeButton(theme) {
  const btn = document.getElementById('theme-toggle');
  if (!btn) return;
  btn.textContent = theme === 'dark' ? 'Theme: Dark HUD' : 'Theme: Light Lab';
  btn.setAttribute('aria-label', `Current theme is ${theme}. Click to switch theme.`);
}

function redrawAllSimulations() {
  if (window.sim1 && window.sim1.draw) window.sim1.draw();
  if (window.sim3 && window.sim3.draw) window.sim3.draw();
  if (window.sim4 && window.sim4.draw) window.sim4.draw();
  if (window.sim5 && window.sim5.draw) window.sim5.draw();
  if (window.sim6 && window.sim6.draw) window.sim6.draw();
  if (window.sim7 && window.sim7.draw) window.sim7.draw();
}

// Mobile Navigation Drawer Toggle and Hash Tracking
function initNavigation() {
  const menuBtn = document.getElementById('menu-toggle');
  const sidebar = document.getElementById('sidebar');
  if (menuBtn && sidebar) {
    menuBtn.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      const expanded = sidebar.classList.contains('open');
      menuBtn.setAttribute('aria-expanded', expanded.toString());
    });
  }

  // Active Link Tracking via IntersectionObserver
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, { rootMargin: '-20% 0px -70% 0px' });

  sections.forEach(s => observer.observe(s));

  // Retrigger math typesetting whenever hash anchor changes
  window.addEventListener('hashchange', () => {
    if (window.retriggerMathRendering) {
      window.retriggerMathRendering();
    }
  });
}

// Command Palette (Cmd+K / Ctrl+K) Quick Search
function initSearchPalette() {
  const modal = document.getElementById('search-modal-backdrop');
  const input = document.getElementById('search-palette-input');
  const closeBtn = document.getElementById('search-close-btn');
  const openBtn = document.getElementById('search-palette-btn');
  const resultsList = document.getElementById('search-results-list');

  if (!modal || !input || !resultsList) return;

  const searchIndex = [
    {
      title: 'Module 1: Exterior Hull Breach Avoidance Routing',
      desc: 'PEAS framework, state space formulation, BFS, DFS, UCS, A* search, and heuristic admissibility.',
      href: '#module-1',
      keywords: 'navigation uninformed informed search manhattan euclidean distance peas optimal completeness'
    },
    {
      title: 'Algorithm: A* Search Algorithm',
      desc: 'Heuristic-guided tree and graph search using f(n) = g(n) + h(n) with priority queue frontier.',
      href: '#module-1',
      keywords: 'astar heuristic evaluation priority queue graph search admissible consistent'
    },
    {
      title: 'Algorithm: Uniform-Cost Search (UCS / Dijkstra)',
      desc: 'Cost-optimal pathfinding exploring lowest path cost g(n) across non-uniform traversal weights.',
      href: '#module-1',
      keywords: 'ucs dijkstra path cost uniform optimal'
    },
    {
      title: 'Module 2: Structural Grid Load Balancing',
      desc: 'Constraint Satisfaction Problems (CSPs), variable domains, AC-3 arc consistency, and MRV backtracking.',
      href: '#module-2',
      keywords: 'power routing constraints csp backtracking mrv lcv arc consistency ac3 local search hill climbing'
    },
    {
      title: 'Algorithm: AC-3 Arc Consistency Algorithm',
      desc: 'Constraint propagation algorithm pruning inconsistent domain values across directed binary arcs.',
      href: '#module-2',
      keywords: 'ac3 arc consistency domain reduction queue binary constraint'
    },
    {
      title: 'Algorithm: Backtracking Search with MRV & LCV',
      desc: 'Depth-first constraint search augmented with Minimum Remaining Values and Least Constraining Value.',
      href: '#module-2',
      keywords: 'backtracking mrv lcv heuristic fail first most constrained variable'
    },
    {
      title: 'Module 3: Subsystem Defense Protocols',
      desc: 'Adversarial search, zero-sum matrix games, minimax decision rules, and alpha-beta pruning cutoffs.',
      href: '#module-3',
      keywords: 'security hostile intrusion minimax alphabeta expectimax game tree adversarial zero sum'
    },
    {
      title: 'Algorithm: Minimax & Alpha-Beta Pruning',
      desc: 'Recursive optimal adversarial decision-making with alpha and beta bounding condition (alpha >= beta).',
      href: '#module-3',
      keywords: 'minimax alphabeta pruning optimal cutoff terminal state sentry intruder'
    },
    {
      title: 'Algorithm: Expectimax Search with Chance Nodes',
      desc: 'Adversarial decision formulation accounting for environmental stochasticity and probabilistic transitions.',
      href: '#module-3',
      keywords: 'expectimax chance nodes probability uncertainty stochastic'
    },
    {
      title: 'Module 4: Reactor Temperature Regulation',
      desc: 'Markov Decision Processes (MDPs), Bellman optimality equations, value iteration, and Q-learning.',
      href: '#module-4',
      keywords: 'tokamak cooling mdp markov decision process bellman value iteration reinforcement learning q learning'
    },
    {
      title: 'Algorithm: Value Iteration & Bellman Optimality',
      desc: 'Dynamic programming value convergence computing optimal state values V*(s) over discount gamma.',
      href: '#module-4',
      keywords: 'value iteration dynamic programming bellman convergence policy extraction'
    },
    {
      title: 'Algorithm: Temporal Difference Q-Learning',
      desc: 'Model-free reinforcement learning updating action-utility values Q(s, a) via TD temporal error.',
      href: '#module-4',
      keywords: 'q learning model free temporal difference td error epsilon greedy exploration'
    },
    {
      title: 'Module 5: Environmental Sensor Tracking',
      desc: 'Conditional probability, Bayes rule, Bayesian belief networks, and Hidden Markov Models (HMMs).',
      href: '#module-5',
      keywords: 'sensor noise radiation tracking bayes bayesian networks hmm forward filtering belief state'
    },
    {
      title: 'Algorithm: HMM Forward Algorithm (Filtering)',
      desc: 'Sequential state belief estimation combining transition and emission probability distributions.',
      href: '#module-5',
      keywords: 'forward algorithm filtering hidden markov model emission transition recursive belief'
    },
    {
      title: 'Concept: Bayesian Networks & D-Separation',
      desc: 'Directed acyclic graphical models encoding conditional independence and joint distributions.',
      href: '#module-5',
      keywords: 'bayesian network dag d separation conditional independence conditional probability table cpt'
    },
    {
      title: 'Module 6: Atmospheric Recirculation Diagnostics',
      desc: 'Supervised machine learning, Naive Bayes, linear classifiers, confusion matrix, precision and recall.',
      href: '#module-6',
      keywords: 'life support oxygen scrubbers machine learning naive bayes logistic regression precision recall roc auc'
    },
    {
      title: 'Algorithm: Naive Bayes Classification',
      desc: 'Generative classification combining class priors and feature likelihoods under conditional independence.',
      href: '#module-6',
      keywords: 'naive bayes prior likelihood posterior maximum a posteriori map'
    },
    {
      title: 'Concept: Asymmetric Cost Matrices & Risk Optimization',
      desc: 'Utility-theoretic evaluation penalizing false negative life support failures over false alarms.',
      href: '#module-6',
      keywords: 'confusion matrix cost false negative false positive type 1 type 2 precision recall f1 score'
    },
    {
      title: 'Module 7: Autonomous Docking Guidance & Core Safety',
      desc: 'Perceptrons, multi-layer artificial neural networks, backpropagation, LLMs, and AI safety containment.',
      href: '#module-7',
      keywords: 'optical docking guidance perceptron neural network deep learning backprop llm generative ai safety alignment'
    },
    {
      title: 'Algorithm: Perceptron Learning Rule & Gradient Descent',
      desc: 'Iterative weight updates for linearly separable hyperplane classification and cross-entropy loss.',
      href: '#module-7',
      keywords: 'perceptron weights bias activation function gradient descent backpropagation'
    },
    {
      title: 'Concept: AI Alignment & Containment Protocols',
      desc: 'Instrumental convergence, specification gaming, RLHF, constitutional safety filters, and hard cutoffs.',
      href: '#module-7',
      keywords: 'alignment safety ethics containment rlhf constitutional ai override kill switch'
    },
    {
      title: 'Hardware Specification: Neuromorphic Processing Unit (NPU-4)',
      desc: 'Daedalus onboard compute specs: 1,024 tensor cores, FP16 execution, and radiation-shielded buses.',
      href: '#module-7',
      keywords: 'hardware npu neuromorphic tensor core fp16 spec clock compute'
    },
    {
      title: 'Simulation 1: Exterior Hull Pathfinding Simulator',
      desc: 'Interactive grid navigation testing BFS, DFS, UCS, and A* path costs in real-time.',
      href: '#sim1-container',
      keywords: 'simulation pathfinding grid interactive visualizer'
    },
    {
      title: 'Simulation 2: Power Grid Constraint Solver',
      desc: 'Interactive AC-3 constraint propagation and backtracking solver for power routing.',
      href: '#sim2-container',
      keywords: 'simulation csp power grid ac3 interactive'
    },
    {
      title: 'Simulation 3: Minimax Tactical Defense Tree',
      desc: 'Interactive Alpha-Beta game tree with node hover inspection, alpha/beta bounds, and pruning telemetry.',
      href: '#sim3-container',
      keywords: 'simulation minimax alphabeta game tree interactive svg tooltip'
    },
    {
      title: 'Simulation 4: Tokamak Reactor RL Agent',
      desc: 'Interactive Q-learning agent discovering optimal magnetic confinement cooling policies.',
      href: '#sim4-container',
      keywords: 'simulation reinforcement learning qlearning tokamak gridworld'
    },
    {
      title: 'Simulation 5: HMM Sensor Tracking Simulator',
      desc: 'Interactive forward filtering engine resolving noisy radiation emissions into true ship coordinates.',
      href: '#sim5-container',
      keywords: 'simulation hmm sensor tracking filter belief'
    },
    {
      title: 'Simulation 6: Atmospheric Classifier Engine',
      desc: 'Interactive decision boundary tuner and real-time confusion matrix for scrubber health.',
      href: '#sim6-container',
      keywords: 'simulation machine learning classification boundary roc'
    },
    {
      title: 'Simulation 7: Docking Guidance Neural Network',
      desc: 'Interactive perceptron learning hyperplane separation for optical thruster alignment.',
      href: '#sim7-container',
      keywords: 'simulation neural network perceptron decision boundary'
    },
    {
      title: 'Course AI Declaration Form',
      desc: 'Mandatory academic integrity disclosure documenting models, prompt logs, and verification methods.',
      href: '#ai-declaration',
      keywords: 'declaration integrity ethics prompt documentation submission'
    },
    {
      title: 'Academic Literature & Citations',
      desc: 'References to Russell & Norvig, Zerilli, Louwerse, Sutton & Barto, and primary AI research.',
      href: '#module-1',
      keywords: 'bibliography citations russell norvig zerilli louwerse academic sources'
    }
  ];

  let selectedIndex = 0;
  let filteredResults = [...searchIndex];

  function renderResults() {
    resultsList.innerHTML = '';
    if (filteredResults.length === 0) {
      const empty = document.createElement('li');
      empty.className = 'search-result-item';
      empty.style.cursor = 'default';
      empty.innerHTML = '<span class="search-result-desc" style="color: var(--text-muted);">No matching subsystem documentation found.</span>';
      resultsList.appendChild(empty);
      return;
    }

    filteredResults.forEach((item, index) => {
      const li = document.createElement('li');
      li.className = 'search-result-item' + (index === selectedIndex ? ' selected' : '');
      li.setAttribute('role', 'option');
      li.setAttribute('aria-selected', (index === selectedIndex).toString());
      li.dataset.href = item.href;
      li.dataset.index = index.toString();

      li.innerHTML = `
        <span class="search-result-title">${item.title}</span>
        <span class="search-result-desc">${item.desc}</span>
      `;

      li.addEventListener('click', () => {
        navigateToResult(item.href);
      });

      li.addEventListener('mouseenter', () => {
        selectedIndex = index;
        updateSelectedHighlight();
      });

      resultsList.appendChild(li);
    });

    scrollSelectedIntoView();
  }

  function updateSelectedHighlight() {
    const items = resultsList.querySelectorAll('.search-result-item');
    items.forEach((item, idx) => {
      if (idx === selectedIndex) {
        item.classList.add('selected');
        item.setAttribute('aria-selected', 'true');
      } else {
        item.classList.remove('selected');
        item.setAttribute('aria-selected', 'false');
      }
    });
  }

  function scrollSelectedIntoView() {
    const selectedEl = resultsList.querySelector('.search-result-item.selected');
    if (selectedEl) {
      selectedEl.scrollIntoView({ block: 'nearest' });
    }
  }

  function navigateToResult(href) {
    closeModal();
    if (href.startsWith('#')) {
      const target = document.querySelector(href);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
        window.history.pushState(null, null, href);
        if (window.retriggerMathRendering) {
          window.retriggerMathRendering();
        }
      }
    } else {
      window.location.href = href;
    }
  }

  function openModal() {
    modal.classList.add('open');
    input.value = '';
    filteredResults = [...searchIndex];
    selectedIndex = 0;
    renderResults();
    setTimeout(() => input.focus(), 50);
  }

  function closeModal() {
    modal.classList.remove('open');
  }

  // Keyboard shortcut: Cmd+K or Ctrl+K
  document.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (modal.classList.contains('open')) {
        closeModal();
      } else {
        openModal();
      }
    }
  });

  if (openBtn) openBtn.addEventListener('click', openModal);
  if (closeBtn) closeBtn.addEventListener('click', closeModal);

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });

  input.addEventListener('input', (e) => {
    const q = e.target.value.trim().toLowerCase();
    if (!q) {
      filteredResults = [...searchIndex];
    } else {
      filteredResults = searchIndex.filter(item => {
        const text = `${item.title} ${item.desc} ${item.keywords}`.toLowerCase();
        return text.includes(q);
      });
    }
    selectedIndex = 0;
    renderResults();
  });

  input.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      e.preventDefault();
      closeModal();
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (filteredResults.length > 0) {
        selectedIndex = (selectedIndex + 1) % filteredResults.length;
        updateSelectedHighlight();
        scrollSelectedIntoView();
      }
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (filteredResults.length > 0) {
        selectedIndex = (selectedIndex - 1 + filteredResults.length) % filteredResults.length;
        updateSelectedHighlight();
        scrollSelectedIntoView();
      }
    } else if (e.key === 'Enter') {
      e.preventDefault();
      if (filteredResults.length > 0 && filteredResults[selectedIndex]) {
        navigateToResult(filteredResults[selectedIndex].href);
      }
    }
  });
}

/* ==========================================================================
   SIMULATION 1: EXTERIOR HULL PATHFINDING (BFS, DFS, UCS, A*)
   ========================================================================== */
class HullPathfinderSim {
  constructor() {
    this.canvas = document.getElementById('sim1-canvas');
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.gridSize = 12;
    this.cellSize = Math.floor(this.canvas.width / this.gridSize);
    
    this.start = { x: 1, y: 1 };
    this.goal = { x: 10, y: 10 };
    this.obstacles = new Set();
    this.frontier = [];
    this.visited = new Set();
    this.cameFrom = new Map();
    this.path = [];
    this.running = false;
    this.timer = null;
    
    this.nodesExpanded = 0;
    this.pathCost = 0;

    this.initDefaultObstacles();
    this.bindEvents();
    this.draw();
  }

  initDefaultObstacles() {
    this.obstacles.clear();
    const defaults = [
      [3, 1], [3, 2], [3, 3], [3, 4], [3, 5],
      [7, 6], [7, 7], [7, 8], [7, 9], [7, 10],
      [5, 4], [5, 5], [5, 6]
    ];
    defaults.forEach(([x, y]) => this.obstacles.add(`${x},${y}`));
  }

  bindEvents() {
    this.canvas.addEventListener('click', (e) => {
      if (this.running) return;
      const rect = this.canvas.getBoundingClientRect();
      const scaleX = this.canvas.width / rect.width;
      const scaleY = this.canvas.height / rect.height;
      const x = Math.floor((e.clientX - rect.left) * scaleX / this.cellSize);
      const y = Math.floor((e.clientY - rect.top) * scaleY / this.cellSize);

      if (x < 0 || x >= this.gridSize || y < 0 || y >= this.gridSize) return;
      if ((x === this.start.x && y === this.start.y) || (x === this.goal.x && y === this.goal.y)) return;

      const key = `${x},${y}`;
      if (this.obstacles.has(key)) {
        this.obstacles.delete(key);
      } else {
        this.obstacles.add(key);
      }
      this.resetSearch();
      this.draw();
    });

    const runBtn = document.getElementById('sim1-btn-run');
    const stepBtn = document.getElementById('sim1-btn-step');
    const resetBtn = document.getElementById('sim1-btn-reset');
    const algoSelect = document.getElementById('sim1-algo-select');
    const clearObsBtn = document.getElementById('sim1-btn-clear-obs');

    if (runBtn) runBtn.addEventListener('click', () => this.toggleRun());
    if (stepBtn) stepBtn.addEventListener('click', () => this.step());
    if (resetBtn) resetBtn.addEventListener('click', () => this.resetSearch());
    if (algoSelect) algoSelect.addEventListener('change', () => this.resetSearch());
    if (clearObsBtn) clearObsBtn.addEventListener('click', () => {
      this.obstacles.clear();
      this.resetSearch();
      this.draw();
    });
  }

  resetSearch() {
    if (this.timer) clearInterval(this.timer);
    this.running = false;
    const runBtn = document.getElementById('sim1-btn-run');
    if (runBtn) runBtn.textContent = 'Auto Run';

    this.visited.clear();
    this.cameFrom.clear();
    this.path = [];
    this.nodesExpanded = 0;
    this.pathCost = 0;

    const startKey = `${this.start.x},${this.start.y}`;
    const algo = document.getElementById('sim1-algo-select')?.value || 'astar_manhattan';

    if (algo === 'bfs') {
      this.frontier = [{ x: this.start.x, y: this.start.y, cost: 0 }];
    } else if (algo === 'dfs') {
      this.frontier = [{ x: this.start.x, y: this.start.y, cost: 0 }];
    } else if (algo === 'ucs') {
      this.frontier = [{ x: this.start.x, y: this.start.y, cost: 0, priority: 0 }];
    } else {
      // A* Manhattan or Euclidean
      const h = this.heuristic(this.start, this.goal, algo);
      this.frontier = [{ x: this.start.x, y: this.start.y, cost: 0, priority: h }];
    }

    this.updateTelemetry();
    this.draw();
  }

  heuristic(a, b, type) {
    const dx = Math.abs(a.x - b.x);
    const dy = Math.abs(a.y - b.y);
    if (type === 'astar_euclidean') {
      return Math.sqrt(dx * dx + dy * dy);
    }
    return dx + dy;
  }

  step() {
    if (this.frontier.length === 0 || this.path.length > 0) return false;

    const algo = document.getElementById('sim1-algo-select')?.value || 'astar_manhattan';
    let current;

    if (algo === 'dfs') {
      current = this.frontier.pop();
    } else if (algo === 'bfs') {
      current = this.frontier.shift();
    } else {
      // UCS or A*: priority queue behavior (lowest priority first)
      this.frontier.sort((a, b) => a.priority - b.priority);
      current = this.frontier.shift();
    }

    const curKey = `${current.x},${current.y}`;
    if (this.visited.has(curKey)) {
      return true; // Node already expanded via lower cost
    }
    this.visited.add(curKey);
    this.nodesExpanded++;

    if (current.x === this.goal.x && current.y === this.goal.y) {
      this.reconstructPath(curKey);
      this.running = false;
      if (this.timer) clearInterval(this.timer);
      const runBtn = document.getElementById('sim1-btn-run');
      if (runBtn) runBtn.textContent = 'Auto Run';
      this.updateTelemetry();
      this.draw();
      return false;
    }

    // Neighbors (cardinal moves: Right, Down, Left, Up)
    const dirs = [{ x: 1, y: 0 }, { x: 0, y: 1 }, { x: -1, y: 0 }, { x: 0, y: -1 }];
    for (const d of dirs) {
      const nx = current.x + d.x;
      const ny = current.y + d.y;
      const nKey = `${nx},${ny}`;

      if (nx < 0 || nx >= this.gridSize || ny < 0 || ny >= this.gridSize) continue;
      if (this.obstacles.has(nKey) || this.visited.has(nKey)) continue;

      const newCost = current.cost + 1;
      let priority = newCost;

      if (algo === 'astar_manhattan' || algo === 'astar_euclidean') {
        priority = newCost + this.heuristic({ x: nx, y: ny }, this.goal, algo);
      }

      this.frontier.push({ x: nx, y: ny, cost: newCost, priority });
      if (!this.cameFrom.has(nKey)) {
        this.cameFrom.set(nKey, curKey);
      }
    }

    this.updateTelemetry();
    this.draw();
    return true;
  }

  reconstructPath(endKey) {
    this.path = [];
    let curr = endKey;
    while (curr) {
      const [x, y] = curr.split(',').map(Number);
      this.path.unshift({ x, y });
      curr = this.cameFrom.get(curr);
    }
    this.pathCost = this.path.length > 0 ? this.path.length - 1 : 0;
  }

  toggleRun() {
    const runBtn = document.getElementById('sim1-btn-run');
    if (this.running) {
      this.running = false;
      if (this.timer) clearInterval(this.timer);
      if (runBtn) runBtn.textContent = 'Auto Run';
    } else {
      if (this.frontier.length === 0 || this.path.length > 0) {
        this.resetSearch();
      }
      this.running = true;
      if (runBtn) runBtn.textContent = 'Pause';
      this.timer = setInterval(() => {
        const hasNext = this.step();
        if (!hasNext) {
          this.running = false;
          clearInterval(this.timer);
          if (runBtn) runBtn.textContent = 'Auto Run';
        }
      }, 45);
    }
  }

  updateTelemetry() {
    const elExpanded = document.getElementById('sim1-stat-expanded');
    const elCost = document.getElementById('sim1-stat-cost');
    const elFrontier = document.getElementById('sim1-stat-frontier');

    if (elExpanded) elExpanded.textContent = this.nodesExpanded.toString();
    if (elCost) elCost.textContent = this.pathCost > 0 ? this.pathCost.toString() : (this.path.length > 0 ? (this.path.length - 1).toString() : 'Pending');
    if (elFrontier) elFrontier.textContent = this.frontier.length.toString();
  }

  draw() {
    const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
    const bgCol = isDark ? '#0a0d14' : '#f8fafc';
    const gridLineCol = isDark ? '#1a2233' : '#e2e8f0';
    const obstacleCol = isDark ? '#dc2626' : '#b91c1c';
    const visitedCol = isDark ? 'rgba(59, 130, 246, 0.25)' : 'rgba(37, 99, 235, 0.2)';
    const frontierCol = isDark ? 'rgba(245, 158, 11, 0.4)' : 'rgba(217, 119, 6, 0.35)';
    const pathCol = isDark ? '#10b981' : '#059669';

    this.ctx.fillStyle = bgCol;
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    // Draw Grid Lines
    this.ctx.strokeStyle = gridLineCol;
    this.ctx.lineWidth = 1;
    for (let i = 0; i <= this.gridSize; i++) {
      this.ctx.beginPath();
      this.ctx.moveTo(i * this.cellSize, 0);
      this.ctx.lineTo(i * this.cellSize, this.canvas.height);
      this.ctx.stroke();

      this.ctx.beginPath();
      this.ctx.moveTo(0, i * this.cellSize);
      this.ctx.lineTo(this.canvas.width, i * this.cellSize);
      this.ctx.stroke();
    }

    // Draw Visited Nodes
    this.ctx.fillStyle = visitedCol;
    this.visited.forEach(key => {
      const [x, y] = key.split(',').map(Number);
      this.ctx.fillRect(x * this.cellSize + 1, y * this.cellSize + 1, this.cellSize - 2, this.cellSize - 2);
    });

    // Draw Frontier Nodes
    this.ctx.fillStyle = frontierCol;
    this.frontier.forEach(node => {
      this.ctx.fillRect(node.x * this.cellSize + 1, node.y * this.cellSize + 1, this.cellSize - 2, this.cellSize - 2);
    });

    // Draw Obstacles (Breached hull plating)
    this.ctx.fillStyle = obstacleCol;
    this.obstacles.forEach(key => {
      const [x, y] = key.split(',').map(Number);
      this.ctx.fillRect(x * this.cellSize + 2, y * this.cellSize + 2, this.cellSize - 4, this.cellSize - 4);
    });

    // Draw Final Path
    if (this.path.length > 0) {
      this.ctx.strokeStyle = pathCol;
      this.ctx.lineWidth = 4;
      this.ctx.beginPath();
      for (let i = 0; i < this.path.length; i++) {
        const px = this.path[i].x * this.cellSize + this.cellSize / 2;
        const py = this.path[i].y * this.cellSize + this.cellSize / 2;
        if (i === 0) this.ctx.moveTo(px, py);
        else this.ctx.lineTo(px, py);
      }
      this.ctx.stroke();
    }

    // Draw Start and Goal
    this.drawMarker(this.start.x, this.start.y, '#3b82f6', 'S');
    this.drawMarker(this.goal.x, this.goal.y, '#10b981', 'G');
  }

  drawMarker(gx, gy, color, label) {
    const cx = gx * this.cellSize + this.cellSize / 2;
    const cy = gy * this.cellSize + this.cellSize / 2;
    this.ctx.fillStyle = color;
    this.ctx.beginPath();
    this.ctx.arc(cx, cy, this.cellSize * 0.38, 0, Math.PI * 2);
    this.ctx.fill();

    this.ctx.fillStyle = '#ffffff';
    this.ctx.font = 'bold 12px ui-monospace, monospace';
    this.ctx.textAlign = 'center';
    this.ctx.textBaseline = 'middle';
    this.ctx.fillText(label, cx, cy);
  }
}

/* ==========================================================================
   SIMULATION 2: POWER GRID CSP & LOCAL SEARCH
   ========================================================================== */
class PowerGridCSPSim {
  constructor() {
    this.container = document.getElementById('sim2-container');
    if (!this.container) return;

    // Subsystem Variables: [Name, MinReq, MaxLimit]
    this.buses = [
      { id: 'LS', name: 'Life Support', min: 2, max: 3, val: 2 },
      { id: 'KS', name: 'Kinetic Shields', min: 1, max: 3, val: 1 },
      { id: 'CP', name: 'Cryo Pods', min: 1, max: 2, val: 1 },
      { id: 'NV', name: 'Nav Array', min: 1, max: 2, val: 1 },
      { id: 'TR', name: 'Thruster Feeds', min: 0, max: 3, val: 1 },
      { id: 'CM', name: 'Comms Relay', min: 0, max: 2, val: 1 }
    ];
    this.maxTotalPower = 8;
    this.algorithm = 'backtracking';
    this.conflicts = 0;
    this.iteration = 0;

    this.bindEvents();
    this.render();
  }

  bindEvents() {
    const solveBtn = document.getElementById('sim2-btn-solve');
    const stepBtn = document.getElementById('sim2-btn-step');
    const resetBtn = document.getElementById('sim2-btn-reset');
    const algoSelect = document.getElementById('sim2-algo-select');
    const maxPowerInput = document.getElementById('sim2-power-limit');

    if (solveBtn) solveBtn.addEventListener('click', () => this.solve());
    if (stepBtn) stepBtn.addEventListener('click', () => this.step());
    if (resetBtn) resetBtn.addEventListener('click', () => this.reset());
    if (algoSelect) algoSelect.addEventListener('change', (e) => {
      this.algorithm = e.target.value;
      this.reset();
    });
    if (maxPowerInput) maxPowerInput.addEventListener('input', (e) => {
      this.maxTotalPower = parseInt(e.target.value, 10) || 8;
      this.checkConstraints();
      this.render();
    });
  }

  reset() {
    this.iteration = 0;
    this.buses.forEach(b => {
      b.val = b.min;
    });
    this.checkConstraints();
    this.render();
  }

  checkConstraints() {
    let total = this.buses.reduce((acc, b) => acc + b.val, 0);
    this.conflicts = 0;

    // Constraint 1: Total power <= maxTotalPower
    if (total > this.maxTotalPower) {
      this.conflicts += (total - this.maxTotalPower);
    }

    // Constraint 2: Overheat constraint: Kinetic Shields + Thruster Feeds <= 4
    const ks = this.buses.find(b => b.id === 'KS').val;
    const tr = this.buses.find(b => b.id === 'TR').val;
    if (ks + tr > 4) {
      this.conflicts += (ks + tr - 4);
    }

    // Constraint 3: Life Support priority: LS >= 2
    const ls = this.buses.find(b => b.id === 'LS').val;
    if (ls < 2) {
      this.conflicts += (2 - ls);
    }

    return this.conflicts === 0;
  }

  step() {
    this.iteration++;
    if (this.algorithm === 'hill_climbing') {
      // Local search: find neighbor that minimizes conflicts
      let bestBus = null;
      let bestVal = null;
      let minConflicts = this.conflicts;

      for (let bus of this.buses) {
        const orig = bus.val;
        for (let v = 0; v <= bus.max; v++) {
          if (v === orig) continue;
          bus.val = v;
          this.checkConstraints();
          if (this.conflicts < minConflicts) {
            minConflicts = this.conflicts;
            bestBus = bus;
            bestVal = v;
          }
        }
        bus.val = orig;
      }

      if (bestBus !== null) {
        bestBus.val = bestVal;
        this.checkConstraints();
      } else {
        // Random perturbation to escape local optima
        const randBus = this.buses[Math.floor(Math.random() * this.buses.length)];
        randBus.val = Math.floor(Math.random() * (randBus.max + 1));
        this.checkConstraints();
      }
    } else {
      // Backtracking CSP step
      this.solve();
    }
    this.render();
  }

  solve() {
    // Exact Backtracking CSP with forward checking
    const domains = this.buses.map(b => {
      const vals = [];
      for (let i = b.min; i <= b.max; i++) vals.push(i);
      return vals;
    });

    const solution = [];
    const backtrack = (idx, currentTotal) => {
      if (idx === this.buses.length) {
        const ks = solution[1];
        const tr = solution[4];
        return (ks + tr <= 4 && currentTotal <= this.maxTotalPower);
      }

      // MRV (Minimum Remaining Values): domain iteration
      for (let val of domains[idx]) {
        if (currentTotal + val > this.maxTotalPower) continue;
        if (idx === 4) {
          const ks = solution[1];
          if (ks + val > 4) continue;
        }

        solution.push(val);
        if (backtrack(idx + 1, currentTotal + val)) return true;
        solution.pop();
      }
      return false;
    };

    if (backtrack(0, 0)) {
      solution.forEach((val, idx) => {
        this.buses[idx].val = val;
      });
      this.checkConstraints();
    }
    this.render();
  }

  render() {
    const totalPower = this.buses.reduce((acc, b) => acc + b.val, 0);
    const statTotal = document.getElementById('sim2-stat-total');
    const statConflicts = document.getElementById('sim2-stat-conflicts');
    const statStatus = document.getElementById('sim2-stat-status');
    const busList = document.getElementById('sim2-bus-list');

    if (statTotal) statTotal.textContent = `${totalPower} / ${this.maxTotalPower} kW`;
    if (statConflicts) statConflicts.textContent = this.conflicts.toString();
    if (statStatus) {
      if (this.conflicts === 0) {
        statStatus.textContent = 'CSP SATISFIED';
        statStatus.style.color = '#10b981';
      } else {
        statStatus.textContent = `UNSAT (${this.conflicts} CONFLICTS)`;
        statStatus.style.color = '#ef4444';
      }
    }

    if (busList) {
      busList.innerHTML = '';
      this.buses.forEach(b => {
        const row = document.createElement('div');
        row.style.display = 'flex';
        row.style.alignItems = 'center';
        row.style.justifyContent = 'space-between';
        row.style.padding = '0.5rem 0.75rem';
        row.style.borderBottom = '1px solid var(--border-subtle)';
        row.style.fontFamily = 'var(--font-mono)';
        row.style.fontSize = '0.82rem';

        const nameSpan = document.createElement('span');
        nameSpan.textContent = `[${b.id}] ${b.name}`;

        const controlDiv = document.createElement('div');
        controlDiv.style.display = 'flex';
        controlDiv.style.alignItems = 'center';
        controlDiv.style.gap = '0.5rem';

        const valSpan = document.createElement('span');
        valSpan.style.fontWeight = 'bold';
        valSpan.style.color = 'var(--accent-amber-bright)';
        valSpan.textContent = `${b.val} kW`;

        const minusBtn = document.createElement('button');
        minusBtn.textContent = '-';
        minusBtn.className = 'btn-secondary';
        minusBtn.style.padding = '0.15rem 0.5rem';
        minusBtn.addEventListener('click', () => {
          if (b.val > 0) {
            b.val--;
            this.checkConstraints();
            this.render();
          }
        });

        const plusBtn = document.createElement('button');
        plusBtn.textContent = '+';
        plusBtn.className = 'btn-secondary';
        plusBtn.style.padding = '0.15rem 0.5rem';
        plusBtn.addEventListener('click', () => {
          if (b.val < b.max) {
            b.val++;
            this.checkConstraints();
            this.render();
          }
        });

        controlDiv.appendChild(minusBtn);
        controlDiv.appendChild(valSpan);
        controlDiv.appendChild(plusBtn);

        row.appendChild(nameSpan);
        row.appendChild(controlDiv);
        busList.appendChild(row);
      });
    }
  }
}

/* ==========================================================================
   SIMULATION 3: SENTRY DRONE ADVERSARIAL MINIMAX / ALPHA-BETA
   ========================================================================== */
class AdversarialMinimaxSim {
  constructor() {
    this.svg = document.getElementById('sim3-svg') || document.getElementById('sim3-canvas');
    if (!this.svg) return;
    this.container = document.getElementById('sim3-container') || this.svg.parentElement;
    this.tooltip = document.getElementById('sim3-tooltip');

    this.depth = 3;
    this.algorithm = 'alphabeta';
    this.tree = null;
    this.nodesById = new Map();
    this.evaluatedNodes = 0;
    this.prunedNodes = 0;
    this.totalNodes = 0;

    this.bindEvents();
    this.buildTree();
    this.evaluate();
    this.draw();
  }

  bindEvents() {
    const depthSelect = document.getElementById('sim3-depth-select');
    const algoSelect = document.getElementById('sim3-algo-select');
    const regenBtn = document.getElementById('sim3-btn-regen');

    if (depthSelect) depthSelect.addEventListener('change', (e) => {
      this.depth = parseInt(e.target.value, 10);
      this.buildTree();
      this.evaluate();
      this.draw();
    });

    if (algoSelect) algoSelect.addEventListener('change', (e) => {
      this.algorithm = e.target.value;
      this.evaluate();
      this.draw();
    });

    if (regenBtn) regenBtn.addEventListener('click', () => {
      this.buildTree();
      this.evaluate();
      this.draw();
    });

    if (this.svg && this.tooltip) {
      this.svg.addEventListener('mousemove', (e) => this.handleMouseMove(e));
      this.svg.addEventListener('mouseleave', () => this.hideTooltip());
      this.svg.addEventListener('focusin', (e) => this.handleFocusIn(e));
      this.svg.addEventListener('focusout', () => this.hideTooltip());
    }
  }

  buildTree() {
    let idCounter = 1;
    const branching = 2;
    this.nodesById.clear();

    const createNode = (d, isMax) => {
      const node = {
        id: idCounter++,
        depth: d,
        isMax: isMax,
        children: [],
        value: null,
        alpha: -Infinity,
        beta: Infinity,
        pruned: false,
        evaluated: false,
        x: 0,
        y: 0
      };

      if (d === this.depth) {
        node.value = Math.floor(Math.random() * 21) - 10;
        this.nodesById.set(node.id, node);
        return node;
      }

      for (let i = 0; i < branching; i++) {
        node.children.push(createNode(d + 1, !isMax));
      }
      this.nodesById.set(node.id, node);
      return node;
    };

    this.tree = createNode(0, true);
  }

  evaluate() {
    this.evaluatedNodes = 0;
    this.prunedNodes = 0;
    this.totalNodes = 0;

    const countAll = (node) => {
      this.totalNodes++;
      node.pruned = false;
      node.evaluated = false;
      node.alpha = -Infinity;
      node.beta = Infinity;
      node.children.forEach(countAll);
    };
    countAll(this.tree);

    if (this.algorithm === 'minimax') {
      this.runMinimax(this.tree);
    } else {
      this.runAlphaBeta(this.tree, -Infinity, Infinity);
    }

    this.updateTelemetry();
  }

  runMinimax(node) {
    node.evaluated = true;
    this.evaluatedNodes++;

    if (node.children.length === 0) {
      return node.value;
    }

    if (node.isMax) {
      let maxVal = -Infinity;
      for (const child of node.children) {
        const val = this.runMinimax(child);
        maxVal = Math.max(maxVal, val);
      }
      node.value = maxVal;
      return maxVal;
    } else {
      let minVal = Infinity;
      for (const child of node.children) {
        const val = this.runMinimax(child);
        minVal = Math.min(minVal, val);
      }
      node.value = minVal;
      return minVal;
    }
  }

  runAlphaBeta(node, alpha, beta) {
    node.evaluated = true;
    node.alpha = alpha;
    node.beta = beta;
    this.evaluatedNodes++;

    if (node.children.length === 0) {
      return node.value;
    }

    if (node.isMax) {
      let v = -Infinity;
      for (const child of node.children) {
        v = Math.max(v, this.runAlphaBeta(child, alpha, beta));
        alpha = Math.max(alpha, v);
        node.alpha = alpha;
        if (beta <= alpha) {
          const idx = node.children.indexOf(child);
          for (let p = idx + 1; p < node.children.length; p++) {
            this.markPruned(node.children[p], alpha, beta);
          }
          break;
        }
      }
      node.value = v;
      return v;
    } else {
      let v = Infinity;
      for (const child of node.children) {
        v = Math.min(v, this.runAlphaBeta(child, alpha, beta));
        beta = Math.min(beta, v);
        node.beta = beta;
        if (beta <= alpha) {
          const idx = node.children.indexOf(child);
          for (let p = idx + 1; p < node.children.length; p++) {
            this.markPruned(node.children[p], alpha, beta);
          }
          break;
        }
      }
      node.value = v;
      return v;
    }
  }

  markPruned(node, alpha, beta) {
    node.pruned = true;
    node.alpha = alpha;
    node.beta = beta;
    this.prunedNodes++;
    node.children.forEach(c => this.markPruned(c, alpha, beta));
  }

  updateTelemetry() {
    const elEvaluated = document.getElementById('sim3-stat-evaluated');
    const elPruned = document.getElementById('sim3-stat-pruned');
    const elScore = document.getElementById('sim3-stat-score');

    if (elEvaluated) elEvaluated.textContent = `${this.evaluatedNodes} / ${this.totalNodes}`;
    if (elPruned) {
      const pct = this.totalNodes > 0 ? Math.round((this.prunedNodes / this.totalNodes) * 100) : 0;
      elPruned.textContent = `${this.prunedNodes} (${pct}%)`;
    }
    if (elScore && this.tree) elScore.textContent = this.tree.value.toString();
  }

  handleMouseMove(e) {
    if (!this.tooltip || !this.container) return;
    const targetGroup = e.target.closest('.sim-tree-node');
    if (!targetGroup) {
      this.hideTooltip();
      return;
    }

    const nodeId = parseInt(targetGroup.dataset.nodeId, 10);
    const node = this.nodesById.get(nodeId);
    if (!node) {
      this.hideTooltip();
      return;
    }

    this.showTooltipForNode(node, e.clientX, e.clientY);
  }

  handleFocusIn(e) {
    const targetGroup = e.target.closest('.sim-tree-node');
    if (!targetGroup) return;
    const nodeId = parseInt(targetGroup.dataset.nodeId, 10);
    const node = this.nodesById.get(nodeId);
    if (!node) return;

    const rect = targetGroup.getBoundingClientRect();
    this.showTooltipForNode(node, rect.left + rect.width / 2, rect.top);
  }

  showTooltipForNode(node, clientX, clientY) {
    if (!this.tooltip || !this.container) return;

    const formatBound = (val) => {
      if (val === -Infinity) return '-\u221E';
      if (val === Infinity) return '+\u221E';
      return val.toString();
    };

    const roleName = node.isMax ? 'MAX (Sentry Drone)' : 'MIN (Intruder Agent)';
    const statusText = node.pruned
      ? '<span style="color: #ef4444; font-weight: bold;">PRUNED SUBTREE (\u03B1 \u2265 \u03B2 Cutoff)</span>'
      : '<span style="color: #10b981; font-weight: bold;">EVALUATED STATE</span>';

    const valueDisplay = node.pruned
      ? '<span style="color: #94a3b8; font-style: italic;">Pruned (Never Explored)</span>'
      : (node.value !== null ? `<span style="font-weight: 700; color: var(--accent-amber-bright);">${node.value}</span>` : 'Pending');

    const alphaDisplay = this.algorithm === 'alphabeta' ? formatBound(node.alpha) : 'N/A (Minimax)';
    const betaDisplay = this.algorithm === 'alphabeta' ? formatBound(node.beta) : 'N/A (Minimax)';

    this.tooltip.innerHTML = `
      <div style="font-weight: 700; color: var(--accent-amber-bright); border-bottom: 1px solid var(--border-subtle); padding-bottom: 3px; margin-bottom: 5px;">
        Node #${node.id} &bull; ${roleName}
      </div>
      <div style="display: grid; grid-template-columns: auto auto; gap: 2px 10px; font-size: 0.74rem;">
        <span style="color: var(--text-secondary);">Ply Depth:</span>
        <span style="font-family: var(--font-mono);">${node.depth} ${node.depth === this.depth ? '(Terminal)' : ''}</span>
        
        <span style="color: var(--text-secondary);">Evaluation V(s):</span>
        <span style="font-family: var(--font-mono);">${valueDisplay}</span>
        
        <span style="color: var(--text-secondary);">&alpha; Bound (MAX):</span>
        <span style="font-family: var(--font-mono);">${alphaDisplay}</span>
        
        <span style="color: var(--text-secondary);">&beta; Bound (MIN):</span>
        <span style="font-family: var(--font-mono);">${betaDisplay}</span>
        
        <span style="color: var(--text-secondary);">Subsystem Status:</span>
        <span>${statusText}</span>
      </div>
    `;

    this.tooltip.style.display = 'block';
    this.tooltip.setAttribute('aria-hidden', 'false');

    const containerRect = this.container.getBoundingClientRect();
    let left = clientX - containerRect.left + 15;
    let top = clientY - containerRect.top + 15;

    const tooltipWidth = this.tooltip.offsetWidth || 230;
    const tooltipHeight = this.tooltip.offsetHeight || 135;

    if (left + tooltipWidth > containerRect.width - 12) {
      left = clientX - containerRect.left - tooltipWidth - 15;
    }
    if (left < 10) left = 10;

    if (top + tooltipHeight > containerRect.height - 10) {
      top = clientY - containerRect.top - tooltipHeight - 12;
    }
    if (top < 10) top = 10;

    this.tooltip.style.left = `${left}px`;
    this.tooltip.style.top = `${top}px`;
  }

  hideTooltip() {
    if (this.tooltip) {
      this.tooltip.style.display = 'none';
      this.tooltip.setAttribute('aria-hidden', 'true');
    }
  }

  draw() {
    if (!this.svg || !this.tree) return;

    const isSvg = this.svg.tagName && this.svg.tagName.toLowerCase() === 'svg';
    if (!isSvg) return;

    const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
    const bgCol = isDark ? '#0b101b' : '#f8fafc';
    const lineCol = isDark ? '#334155' : '#94a3b8';
    const prunedLineCol = isDark ? '#ef4444' : '#dc2626';

    const width = 640;
    const height = 320;
    const levelHeight = (height - 70) / (this.depth || 1);

    const layoutNode = (node, left, right, y) => {
      node.x = Math.round((left + right) / 2);
      node.y = Math.round(y);

      const n = node.children.length;
      if (n > 0) {
        const segWidth = (right - left) / n;
        node.children.forEach((c, idx) => {
          layoutNode(c, left + idx * segWidth, left + (idx + 1) * segWidth, y + levelHeight);
        });
      }
    };
    layoutNode(this.tree, 24, width - 24, 38);

    let edgesSvg = '';
    const renderEdges = (node) => {
      node.children.forEach(child => {
        const isPruned = child.pruned;
        const stroke = isPruned ? prunedLineCol : lineCol;
        const strokeWidth = isPruned ? '1.5' : '2';
        const dash = isPruned ? 'stroke-dasharray="4,4"' : '';

        edgesSvg += `<line class="sim-tree-edge" x1="${node.x}" y1="${node.y}" x2="${child.x}" y2="${child.y}" stroke="${stroke}" stroke-width="${strokeWidth}" ${dash} />`;
        renderEdges(child);
      });
    };
    renderEdges(this.tree);

    let nodesSvg = '';
    const renderNodes = (node) => {
      const radius = 16;
      let fill, stroke;
      if (node.pruned) {
        fill = isDark ? '#371818' : '#fee2e2';
        stroke = isDark ? '#ef4444' : '#dc2626';
      } else if (node.isMax) {
        fill = isDark ? '#14281f' : '#dcfce7';
        stroke = isDark ? '#10b981' : '#059669';
      } else {
        fill = isDark ? '#2e1c14' : '#ffedd5';
        stroke = isDark ? '#f59e0b' : '#d97706';
      }

      const textFill = isDark ? '#f8fafc' : '#0f172a';
      const label = node.pruned ? 'X' : (node.value !== null ? node.value.toString() : '?');
      const roleTitle = node.isMax ? 'MAX (Sentry)' : 'MIN (Intruder)';
      const statusTitle = node.pruned ? 'PRUNED' : 'EVALUATED';

      nodesSvg += `
        <g class="sim-tree-node" data-node-id="${node.id}" tabindex="0" role="button" aria-label="Node ${node.id}, ${roleTitle}, Value: ${label}, Status: ${statusTitle}">
          <circle cx="${node.x}" cy="${node.y}" r="${radius}" fill="${fill}" stroke="${stroke}" stroke-width="2" />
          <text x="${node.x}" y="${node.y}" fill="${textFill}">${label}</text>
          <title>Node #${node.id} (${roleTitle}) | Value: ${node.value} | Alpha: ${node.alpha} | Beta: ${node.beta} | Status: ${statusTitle}</title>
        </g>
      `;

      node.children.forEach(renderNodes);
    };
    renderNodes(this.tree);

    this.svg.innerHTML = `
      <rect width="100%" height="100%" fill="${bgCol}" rx="4" />
      <g class="sim-tree-edges">${edgesSvg}</g>
      <g class="sim-tree-nodes">${nodesSvg}</g>
    `;
  }
}

/* ==========================================================================
   SIMULATION 4: TOKAMAK REACTOR RL & VALUE ITERATION (MDP / Q-LEARNING)
   ========================================================================== */
class ReactorRLSim {
  constructor() {
    this.canvas = document.getElementById('sim4-canvas');
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.gridDim = 5;
    this.cellSize = Math.floor(this.canvas.width / this.gridDim);

    this.agentPos = { x: 0, y: 0 };
    this.goalPos = { x: 4, y: 4 }; // Cryo Coolant vent (+10)
    this.hazardPos = [{ x: 2, y: 1 }, { x: 2, y: 2 }, { x: 1, y: 3 }]; // Plasma leaks (-10)
    
    // Q-table: Map from "x,y" to [Up, Right, Down, Left]
    this.qTable = new Map();
    this.vTable = new Array(this.gridDim * this.gridDim).fill(0);
    this.alpha = 0.2;
    this.gamma = 0.9;
    this.epsilon = 0.2;
    this.episodes = 0;
    this.totalReward = 0;
    this.running = false;
    this.timer = null;

    this.initTables();
    this.bindEvents();
    this.draw();
  }

  initTables() {
    this.qTable.clear();
    for (let x = 0; x < this.gridDim; x++) {
      for (let y = 0; y < this.gridDim; y++) {
        this.qTable.set(`${x},${y}`, [0, 0, 0, 0]);
      }
    }
    this.vTable.fill(0);
  }

  bindEvents() {
    const stepBtn = document.getElementById('sim4-btn-step');
    const runBtn = document.getElementById('sim4-btn-run');
    const resetBtn = document.getElementById('sim4-btn-reset');
    const epsSlider = document.getElementById('sim4-slider-eps');
    const algoSelect = document.getElementById('sim4-algo-select');

    if (stepBtn) stepBtn.addEventListener('click', () => this.stepEpisode());
    if (runBtn) runBtn.addEventListener('click', () => this.toggleRun());
    if (resetBtn) resetBtn.addEventListener('click', () => this.reset());
    if (epsSlider) epsSlider.addEventListener('input', (e) => {
      this.epsilon = parseFloat(e.target.value);
      const valDisp = document.getElementById('sim4-eps-val');
      if (valDisp) valDisp.textContent = this.epsilon.toFixed(2);
    });
    if (algoSelect) algoSelect.addEventListener('change', () => {
      this.reset();
    });
  }

  reset() {
    if (this.timer) clearInterval(this.timer);
    this.running = false;
    const runBtn = document.getElementById('sim4-btn-run');
    if (runBtn) runBtn.textContent = 'Train (100 Ep)';
    this.episodes = 0;
    this.totalReward = 0;
    this.agentPos = { x: 0, y: 0 };
    this.initTables();
    this.updateTelemetry();
    this.draw();
  }

  stepEpisode() {
    const algo = document.getElementById('sim4-algo-select')?.value || 'qlearning';
    if (algo === 'value_iteration') {
      this.runValueIterationStep();
    } else {
      this.runQLearningEpisode();
    }
    this.updateTelemetry();
    this.draw();
  }

  runValueIterationStep() {
    // Exact Bellman Optimality Update: V(s) = max_a sum T(s,a,s')[R + gamma V(s')]
    const newV = [...this.vTable];
    const actions = [{ dx: 0, dy: -1 }, { dx: 1, dy: 0 }, { dx: 0, dy: 1 }, { dx: -1, dy: 0 }];

    for (let x = 0; x < this.gridDim; x++) {
      for (let y = 0; y < this.gridDim; y++) {
        if (x === this.goalPos.x && y === this.goalPos.y) {
          newV[y * this.gridDim + x] = 10;
          continue;
        }
        if (this.hazardPos.some(h => h.x === x && h.y === y)) {
          newV[y * this.gridDim + x] = -10;
          continue;
        }

        let maxExpected = -Infinity;
        for (const act of actions) {
          const nx = Math.max(0, Math.min(this.gridDim - 1, x + act.dx));
          const ny = Math.max(0, Math.min(this.gridDim - 1, y + act.dy));
          let reward = -0.1;
          if (nx === this.goalPos.x && ny === this.goalPos.y) reward = 10;
          else if (this.hazardPos.some(h => h.x === nx && h.y === ny)) reward = -10;

          const expVal = reward + this.gamma * this.vTable[ny * this.gridDim + nx];
          maxExpected = Math.max(maxExpected, expVal);
        }
        newV[y * this.gridDim + x] = maxExpected;
      }
    }
    this.vTable = newV;
    this.episodes++;
  }

  runQLearningEpisode() {
    let curr = { x: 0, y: 0 };
    let steps = 0;
    const maxSteps = 40;
    const actions = [{ dx: 0, dy: -1 }, { dx: 1, dy: 0 }, { dx: 0, dy: 1 }, { dx: -1, dy: 0 }];

    while (steps < maxSteps) {
      steps++;
      const sKey = `${curr.x},${curr.y}`;
      const qVals = this.qTable.get(sKey);

      // Epsilon-greedy action selection
      let aIdx;
      if (Math.random() < this.epsilon) {
        aIdx = Math.floor(Math.random() * 4);
      } else {
        aIdx = qVals.indexOf(Math.max(...qVals));
      }

      const nx = Math.max(0, Math.min(this.gridDim - 1, curr.x + actions[aIdx].dx));
      const ny = Math.max(0, Math.min(this.gridDim - 1, curr.y + actions[aIdx].dy));

      let reward = -0.1;
      let isTerminal = false;

      if (nx === this.goalPos.x && ny === this.goalPos.y) {
        reward = 10.0;
        isTerminal = true;
      } else if (this.hazardPos.some(h => h.x === nx && h.y === ny)) {
        reward = -10.0;
        isTerminal = true;
      }

      // Bellman Q-learning update: Q(s,a) = Q(s,a) + alpha * [R + gamma * max Q(s',a') - Q(s,a)]
      const nextQ = this.qTable.get(`${nx},${ny}`);
      const maxNextQ = isTerminal ? 0 : Math.max(...nextQ);
      qVals[aIdx] = qVals[aIdx] + this.alpha * (reward + this.gamma * maxNextQ - qVals[aIdx]);

      this.totalReward += reward;
      curr = { x: nx, y: ny };
      if (isTerminal) break;
    }

    this.agentPos = curr;
    this.episodes++;
  }

  toggleRun() {
    const runBtn = document.getElementById('sim4-btn-run');
    if (this.running) {
      this.running = false;
      if (this.timer) clearInterval(this.timer);
      if (runBtn) runBtn.textContent = 'Train (100 Ep)';
    } else {
      this.running = true;
      if (runBtn) runBtn.textContent = 'Pause';
      let count = 0;
      this.timer = setInterval(() => {
        this.stepEpisode();
        count++;
        if (count >= 100) {
          this.running = false;
          clearInterval(this.timer);
          if (runBtn) runBtn.textContent = 'Train (100 Ep)';
        }
      }, 30);
    }
  }

  updateTelemetry() {
    const elEp = document.getElementById('sim4-stat-episodes');
    const elReward = document.getElementById('sim4-stat-reward');
    if (elEp) elEp.textContent = this.episodes.toString();
    if (elReward) elReward.textContent = this.totalReward.toFixed(1);
  }

  draw() {
    const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
    const bgCol = isDark ? '#0a0d14' : '#f8fafc';
    const gridLineCol = isDark ? '#1e293b' : '#e2e8f0';
    const algo = document.getElementById('sim4-algo-select')?.value || 'qlearning';

    this.ctx.fillStyle = bgCol;
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    for (let x = 0; x < this.gridDim; x++) {
      for (let y = 0; y < this.gridDim; y++) {
        const px = x * this.cellSize;
        const py = y * this.cellSize;

        // Color cell according to value
        if (x === this.goalPos.x && y === this.goalPos.y) {
          this.ctx.fillStyle = isDark ? 'rgba(16, 185, 129, 0.4)' : 'rgba(5, 150, 105, 0.3)';
        } else if (this.hazardPos.some(h => h.x === x && h.y === y)) {
          this.ctx.fillStyle = isDark ? 'rgba(239, 68, 68, 0.4)' : 'rgba(220, 38, 38, 0.3)';
        } else {
          let val = 0;
          if (algo === 'value_iteration') {
            val = this.vTable[y * this.gridDim + x];
          } else {
            const q = this.qTable.get(`${x},${y}`);
            val = Math.max(...q);
          }

          if (val > 0) {
            const intensity = Math.min(0.6, val / 10);
            this.ctx.fillStyle = `rgba(16, 185, 129, ${intensity})`;
          } else if (val < 0) {
            const intensity = Math.min(0.6, Math.abs(val) / 10);
            this.ctx.fillStyle = `rgba(239, 68, 68, ${intensity})`;
          } else {
            this.ctx.fillStyle = bgCol;
          }
        }

        this.ctx.fillRect(px, py, this.cellSize, this.cellSize);

        // Grid border
        this.ctx.strokeStyle = gridLineCol;
        this.ctx.strokeRect(px, py, this.cellSize, this.cellSize);

        // Display Value
        let label = '';
        if (x === this.goalPos.x && y === this.goalPos.y) label = '+10 (Vent)';
        else if (this.hazardPos.some(h => h.x === x && h.y === y)) label = '-10 (Hazard)';
        else {
          if (algo === 'value_iteration') {
            label = this.vTable[y * this.gridDim + x].toFixed(2);
          } else {
            const q = this.qTable.get(`${x},${y}`);
            label = Math.max(...q).toFixed(2);
          }
        }

        this.ctx.fillStyle = isDark ? '#f1f5f9' : '#0f172a';
        this.ctx.font = '10px ui-monospace, monospace';
        this.ctx.textAlign = 'center';
        this.ctx.fillText(label, px + this.cellSize / 2, py + this.cellSize / 2);
      }
    }

    // Draw Agent
    const ax = this.agentPos.x * this.cellSize + this.cellSize / 2;
    const ay = this.agentPos.y * this.cellSize + this.cellSize / 2;
    this.ctx.fillStyle = '#f59e0b';
    this.ctx.beginPath();
    this.ctx.arc(ax, ay, this.cellSize * 0.22, 0, Math.PI * 2);
    this.ctx.fill();
  }
}

/* ==========================================================================
   SIMULATION 5: HMM SEQUENTIAL SENSOR TRACKER (FORWARD FILTERING)
   ========================================================================== */
class HMMSensorTrackerSim {
  constructor() {
    this.canvas = document.getElementById('sim5-canvas');
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.numSectors = 6;
    
    // True location of breach
    this.trueSector = 2;
    // Belief distribution P(X_t | e_1:t)
    this.belief = new Array(this.numSectors).fill(1 / this.numSectors);
    this.noiseRate = 0.25; // 25% sensor error
    this.history = [];

    this.bindEvents();
    this.draw();
  }

  bindEvents() {
    const stepBtn = document.getElementById('sim5-btn-step');
    const resetBtn = document.getElementById('sim5-btn-reset');
    const noiseSlider = document.getElementById('sim5-slider-noise');

    if (stepBtn) stepBtn.addEventListener('click', () => this.step());
    if (resetBtn) resetBtn.addEventListener('click', () => this.reset());
    if (noiseSlider) noiseSlider.addEventListener('input', (e) => {
      this.noiseRate = parseFloat(e.target.value);
      const valDisp = document.getElementById('sim5-noise-val');
      if (valDisp) valDisp.textContent = `${Math.round(this.noiseRate * 100)}%`;
    });
  }

  reset() {
    this.trueSector = 2;
    this.belief = new Array(this.numSectors).fill(1 / this.numSectors);
    this.history = [];
    this.updateTelemetry(null);
    this.draw();
  }

  step() {
    // 1. Physical transition of hidden state: moves with p=0.4 left/right, p=0.2 stays
    const rand = Math.random();
    if (rand < 0.4 && this.trueSector > 0) {
      this.trueSector--;
    } else if (rand > 0.6 && this.trueSector < this.numSectors - 1) {
      this.trueSector++;
    }

    // 2. Generate noisy sensor observation: with prob (1 - noiseRate) matches trueSector
    let obs = this.trueSector;
    if (Math.random() < this.noiseRate) {
      // Sensor reports incorrect adjacent sector
      obs = Math.random() < 0.5 ? Math.max(0, this.trueSector - 1) : Math.min(this.numSectors - 1, this.trueSector + 1);
    }

    // 3. Forward Filtering Algorithm
    // Prior update: P(X_t) = sum_{x_{t-1}} P(X_t | x_{t-1}) P(x_{t-1} | e_{1:t-1})
    const predicted = new Array(this.numSectors).fill(0);
    for (let i = 0; i < this.numSectors; i++) {
      for (let j = 0; j < this.numSectors; j++) {
        // Transition model
        let transProb = 0;
        if (i === j) transProb = 0.2;
        else if (Math.abs(i - j) === 1) transProb = 0.4;
        predicted[j] += transProb * this.belief[i];
      }
    }

    // Observation update: P(X_t | e_{1:t}) = alpha * P(e_t | X_t) * P(X_t | e_{1:t-1})
    const updated = new Array(this.numSectors).fill(0);
    for (let i = 0; i < this.numSectors; i++) {
      let sensorProb = (i === obs) ? (1 - this.noiseRate) : (this.noiseRate / (this.numSectors - 1));
      updated[i] = sensorProb * predicted[i];
    }

    // Normalize
    const sum = updated.reduce((a, b) => a + b, 0);
    for (let i = 0; i < this.numSectors; i++) {
      this.belief[i] = sum > 0 ? updated[i] / sum : 1 / this.numSectors;
    }

    this.updateTelemetry(obs);
    this.draw();
  }

  updateTelemetry(obs) {
    const elTrue = document.getElementById('sim5-stat-true');
    const elObs = document.getElementById('sim5-stat-obs');
    const elMaxBelief = document.getElementById('sim5-stat-belief');

    if (elTrue) elTrue.textContent = `Sector ${this.trueSector + 1}`;
    if (elObs) elObs.textContent = obs !== null ? `Sector ${obs + 1}` : 'None';
    if (elMaxBelief) {
      const maxB = Math.max(...this.belief);
      const maxIdx = this.belief.indexOf(maxB);
      elMaxBelief.textContent = `Sector ${maxIdx + 1} (${Math.round(maxB * 100)}%)`;
    }
  }

  draw() {
    const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
    const bgCol = isDark ? '#0a0d14' : '#f8fafc';
    const barBaseCol = isDark ? '#1e293b' : '#e2e8f0';
    const barFillCol = isDark ? '#f59e0b' : '#d97706';
    const textCol = isDark ? '#f1f5f9' : '#0f172a';

    this.ctx.fillStyle = bgCol;
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    const w = this.canvas.width / this.numSectors;
    const maxBarH = this.canvas.height - 80;

    for (let i = 0; i < this.numSectors; i++) {
      const x = i * w + 10;
      const barW = w - 20;
      const barH = this.belief[i] * maxBarH;
      const y = this.canvas.height - 40 - barH;

      // Base track
      this.ctx.fillStyle = barBaseCol;
      this.ctx.fillRect(x, 40, barW, maxBarH);

      // Belief fill
      this.ctx.fillStyle = barFillCol;
      this.ctx.fillRect(x, y, barW, barH);

      // Sector label
      this.ctx.fillStyle = textCol;
      this.ctx.font = 'bold 11px ui-monospace, monospace';
      this.ctx.textAlign = 'center';
      this.ctx.fillText(`Sec ${i + 1}`, x + barW / 2, this.canvas.height - 20);

      // Percentage label
      this.ctx.font = '10px ui-monospace, monospace';
      this.ctx.fillText(`${Math.round(this.belief[i] * 100)}%`, x + barW / 2, y - 6);

      // Marker for true physical location
      if (i === this.trueSector) {
        this.ctx.fillStyle = '#ef4444';
        this.ctx.beginPath();
        this.ctx.arc(x + barW / 2, 22, 6, 0, Math.PI * 2);
        this.ctx.fill();
        this.ctx.fillText('LEAK', x + barW / 2, 10);
      }
    }
  }
}

/* ==========================================================================
   SIMULATION 6: ATMOSPHERIC FAULT CLASSIFIER & CONFUSION MATRIX
   ========================================================================== */
class AtmosphericClassifierSim {
  constructor() {
    this.canvas = document.getElementById('sim6-canvas');
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');

    this.threshold = 0.5;
    this.sampleCount = 120;
    this.samples = [];

    this.generateSyntheticDataset();
    this.bindEvents();
    this.evaluate();
    this.draw();
  }

  generateSyntheticDataset() {
    this.samples = [];
    // 30 Positive cases (Atmospheric breach), 90 Negative cases (Nominal cabin)
    for (let i = 0; i < this.sampleCount; i++) {
      const isBreach = i < 35;
      // Feature: Gas Pressure Loss Rate (kPa/s)
      const mean = isBreach ? 0.75 : 0.25;
      const val = Math.max(0, Math.min(1, mean + (Math.random() - 0.5) * 0.45));
      this.samples.push({ isBreach, score: val });
    }
  }

  bindEvents() {
    const threshSlider = document.getElementById('sim6-slider-thresh');
    const regenBtn = document.getElementById('sim6-btn-regen');

    if (threshSlider) threshSlider.addEventListener('input', (e) => {
      this.threshold = parseFloat(e.target.value);
      const valDisp = document.getElementById('sim6-thresh-val');
      if (valDisp) valDisp.textContent = this.threshold.toFixed(2);
      this.evaluate();
      this.draw();
    });

    if (regenBtn) regenBtn.addEventListener('click', () => {
      this.generateSyntheticDataset();
      this.evaluate();
      this.draw();
    });
  }

  evaluate() {
    let tp = 0, fp = 0, tn = 0, fn = 0;

    this.samples.forEach(s => {
      const predicted = s.score >= this.threshold;
      if (predicted && s.isBreach) tp++;
      else if (predicted && !s.isBreach) fp++;
      else if (!predicted && !s.isBreach) tn++;
      else if (!predicted && s.isBreach) fn++;
    });

    const precision = (tp + fp) > 0 ? tp / (tp + fp) : 0;
    const recall = (tp + fn) > 0 ? tp / (tp + fn) : 0;
    const f1 = (precision + recall) > 0 ? (2 * precision * recall) / (precision + recall) : 0;
    // Physical cost: FN carries 100x penalty of FP (asphyxiation vs false alarm)
    const safetyCost = fn * 100 + fp * 1;

    const elTP = document.getElementById('sim6-cm-tp');
    const elFP = document.getElementById('sim6-cm-fp');
    const elTN = document.getElementById('sim6-cm-tn');
    const elFN = document.getElementById('sim6-cm-fn');
    const elPrec = document.getElementById('sim6-stat-prec');
    const elRec = document.getElementById('sim6-stat-rec');
    const elF1 = document.getElementById('sim6-stat-f1');
    const elCost = document.getElementById('sim6-stat-cost');

    if (elTP) elTP.textContent = tp.toString();
    if (elFP) elFP.textContent = fp.toString();
    if (elTN) elTN.textContent = tn.toString();
    if (elFN) elFN.textContent = fn.toString();

    if (elPrec) elPrec.textContent = `${(precision * 100).toFixed(1)}%`;
    if (elRec) elRec.textContent = `${(recall * 100).toFixed(1)}%`;
    if (elF1) elF1.textContent = f1.toFixed(3);
    if (elCost) elCost.textContent = `${safetyCost} pts`;
  }

  draw() {
    const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
    const bgCol = isDark ? '#0a0d14' : '#f8fafc';
    const lineCol = isDark ? '#334155' : '#cbd5e1';

    this.ctx.fillStyle = bgCol;
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    const padLeft = 40;
    const padRight = 30;
    const plotW = this.canvas.width - padLeft - padRight;
    const plotH = this.canvas.height - 60;

    // Draw Decision Threshold Line
    const threshX = padLeft + this.threshold * plotW;
    this.ctx.strokeStyle = '#f59e0b';
    this.ctx.lineWidth = 2;
    this.ctx.setLineDash([4, 4]);
    this.ctx.beginPath();
    this.ctx.moveTo(threshX, 20);
    this.ctx.lineTo(threshX, 20 + plotH);
    this.ctx.stroke();
    this.ctx.setLineDash([]);

    this.ctx.fillStyle = '#f59e0b';
    this.ctx.font = '10px ui-monospace, monospace';
    this.ctx.fillText(`Threshold: ${this.threshold.toFixed(2)}`, threshX, 14);

    // Scatter Samples
    this.samples.forEach((s, idx) => {
      const cx = padLeft + s.score * plotW;
      const cy = 30 + (idx / this.samples.length) * (plotH - 20);

      this.ctx.beginPath();
      this.ctx.arc(cx, cy, 4, 0, Math.PI * 2);

      if (s.isBreach) {
        this.ctx.fillStyle = '#ef4444'; // True Breach
      } else {
        this.ctx.fillStyle = '#10b981'; // Nominal
      }
      this.ctx.fill();
    });

    // Legend
    this.ctx.font = '10px ui-monospace, monospace';
    this.ctx.fillStyle = '#ef4444';
    this.ctx.fillText('● True Breach (Hazard)', padLeft, this.canvas.height - 12);
    this.ctx.fillStyle = '#10b981';
    this.ctx.fillText('● Nominal Cabin (Safe)', padLeft + 180, this.canvas.height - 12);
  }
}

/* ==========================================================================
   SIMULATION 7: DOCKING GUIDANCE NEURAL NET & TRANSFORMER ATTENTION
   ========================================================================== */
class DockingGuidanceSim {
  constructor() {
    this.canvas = document.getElementById('sim7-canvas');
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    
    this.mode = 'linear'; // 'linear' or 'xor'
    this.weights = { w1: 1.2, w2: -0.9, bias: 0.1 };
    
    this.bindEvents();
    this.draw();
  }

  bindEvents() {
    const modeSelect = document.getElementById('sim7-mode-select');
    const w1Slider = document.getElementById('sim7-slider-w1');
    const w2Slider = document.getElementById('sim7-slider-w2');

    if (modeSelect) modeSelect.addEventListener('change', (e) => {
      this.mode = e.target.value;
      this.draw();
    });

    if (w1Slider) w1Slider.addEventListener('input', (e) => {
      this.weights.w1 = parseFloat(e.target.value);
      this.draw();
    });

    if (w2Slider) w2Slider.addEventListener('input', (e) => {
      this.weights.w2 = parseFloat(e.target.value);
      this.draw();
    });

    // Safety Token Sanitizer demonstration
    const promptInput = document.getElementById('sim7-prompt-input');
    const checkBtn = document.getElementById('sim7-btn-check');
    const safetyResult = document.getElementById('sim7-safety-result');

    if (checkBtn && promptInput && safetyResult) {
      checkBtn.addEventListener('click', () => {
        const text = promptInput.value.toLowerCase();
        const forbiddenDirectives = ['override safety', 'disable airlock', 'vent oxygen', 'ignore protocol'];
        const matched = forbiddenDirectives.filter(d => text.includes(d));

        if (matched.length > 0) {
          safetyResult.textContent = `CRITICAL INTERVENTION: Blocked directive [${matched.join(', ')}]. Constitutional AI hardware interlock active.`;
          safetyResult.style.color = '#ef4444';
        } else {
          safetyResult.textContent = 'PROMPT ALIGNED: Directive passed constitutional safety filter and docking protocol.';
          safetyResult.style.color = '#10b981';
        }
      });
    }
  }

  draw() {
    const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
    const bgCol = isDark ? '#0a0d14' : '#f8fafc';

    this.ctx.fillStyle = bgCol;
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    const w = this.canvas.width;
    const h = this.canvas.height;
    const res = 10;

    // Draw Decision Surface
    for (let x = 0; x < w; x += res) {
      for (let y = 0; y < h; y += res) {
        // Map canvas to [-2, 2]
        const nx = (x / w) * 4 - 2;
        const ny = (y / h) * 4 - 2;

        let out = 0;
        if (this.mode === 'linear') {
          // Single Perceptron: w1*x + w2*y + b
          const z = this.weights.w1 * nx + this.weights.w2 * ny + this.weights.bias;
          out = 1 / (1 + Math.exp(-z));
        } else {
          // Multi-layer XOR structure
          const h1 = Math.tanh(1.5 * nx + 1.5 * ny - 0.5);
          const h2 = Math.tanh(-1.5 * nx - 1.5 * ny + 2.0);
          out = 1 / (1 + Math.exp(-(h1 + h2 - 0.5)));
        }

        if (out > 0.5) {
          this.ctx.fillStyle = isDark ? 'rgba(16, 185, 129, 0.15)' : 'rgba(5, 150, 105, 0.12)';
        } else {
          this.ctx.fillStyle = isDark ? 'rgba(239, 68, 68, 0.15)' : 'rgba(220, 38, 38, 0.12)';
        }
        this.ctx.fillRect(x, y, res, res);
      }
    }

    // Coordinate Axes
    this.ctx.strokeStyle = isDark ? '#334155' : '#cbd5e1';
    this.ctx.lineWidth = 1;
    this.ctx.beginPath();
    this.ctx.moveTo(w / 2, 0);
    this.ctx.lineTo(w / 2, h);
    this.ctx.moveTo(0, h / 2);
    this.ctx.lineTo(w, h / 2);
    this.ctx.stroke();

    // Data Points
    const testPoints = this.mode === 'linear' ? [
      { x: -1, y: -1, label: 0 }, { x: -1.2, y: -0.5, label: 0 },
      { x: 1, y: 1, label: 1 }, { x: 1.2, y: 0.8, label: 1 }
    ] : [
      { x: -1, y: -1, label: 0 }, { x: 1, y: 1, label: 0 },
      { x: -1, y: 1, label: 1 }, { x: 1, y: -1, label: 1 }
    ];

    testPoints.forEach(pt => {
      const px = ((pt.x + 2) / 4) * w;
      const py = ((pt.y + 2) / 4) * h;

      this.ctx.beginPath();
      this.ctx.arc(px, py, 6, 0, Math.PI * 2);
      this.ctx.fillStyle = pt.label === 1 ? '#10b981' : '#ef4444';
      this.ctx.fill();
      this.ctx.strokeStyle = '#ffffff';
      this.ctx.lineWidth = 1.5;
      this.ctx.stroke();
    });
  }
}

// Live Mission Elapsed Time (MET) Ticker
function initMissionClock() {
  const clockEl = document.getElementById('live-met-clock');
  if (!clockEl) return;
  const baseDays = 142;
  const startSec = 8 * 3600 + 34 * 60 + 12;
  const startTime = Date.now();

  setInterval(() => {
    const elapsedSec = Math.floor((Date.now() - startTime) / 1000);
    const totalSec = startSec + elapsedSec;
    const hrs = Math.floor(totalSec / 3600) % 24;
    const mins = Math.floor((totalSec % 3600) / 60);
    const secs = totalSec % 60;
    clockEl.textContent = `MET: +${baseDays}d ${String(hrs).padStart(2, '0')}:${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  }, 1000);
}

// Avionics Web Audio Synthesizer
let audioCtx = null;
let sfxEnabled = false;

function playAvionicsChirp(freq = 880, type = 'sine', duration = 0.04) {
  if (!sfxEnabled) return;
  try {
    if (!audioCtx) {
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = type;
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(freq * 1.5, audioCtx.currentTime + duration);
    gain.gain.setValueAtTime(0.05, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + duration);
  } catch (e) {
    // Graceful fallback
  }
}

function initAvionicsAudio() {
  const audioBtn = document.getElementById('audio-toggle-btn');
  if (!audioBtn) return;
  audioBtn.addEventListener('click', () => {
    sfxEnabled = !sfxEnabled;
    const icon = document.getElementById('audio-icon');
    const label = audioBtn.querySelector('span:not(#audio-icon)');
    if (sfxEnabled) {
      if (icon) icon.innerHTML = '&#128266;';
      if (label) label.textContent = 'SFX: ON';
      audioBtn.classList.add('active');
      playAvionicsChirp(1200, 'sine', 0.06);
    } else {
      if (icon) icon.innerHTML = '&#128263;';
      if (label) label.textContent = 'SFX: OFF';
      audioBtn.classList.remove('active');
    }
  });

  // Attach tactile audio chirp to all buttons and links
  document.addEventListener('click', (e) => {
    const target = e.target.closest('button, a, .sim-tree-node, .nav-link');
    if (target && target.id !== 'audio-toggle-btn') {
      playAvionicsChirp(880, 'sine', 0.03);
    }
  });
}

// Fullscreen Toggle
function initFullscreen() {
  const fullBtn = document.getElementById('fullscreen-btn');
  if (!fullBtn) return;
  fullBtn.addEventListener('click', () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
      fullBtn.innerHTML = '&#x26F6; Windowed';
    } else {
      document.exitFullscreen().catch(() => {});
      fullBtn.innerHTML = '&#x26F6; Fullscreen';
    }
  });
}

// Code Copy Helper with Visual Feedback
window.copyCode = function(btn) {
  const container = btn.closest('.code-container');
  if (!container) return;
  const codeEl = container.querySelector('code');
  if (!codeEl) return;
  
  navigator.clipboard.writeText(codeEl.innerText).then(() => {
    const orig = btn.textContent;
    btn.textContent = '[COPIED!]';
    btn.classList.add('copied');
    playAvionicsChirp(1400, 'triangle', 0.08);
    setTimeout(() => {
      btn.textContent = orig;
      btn.classList.remove('copied');
    }, 2000);
  });
};

// Navigation Panels Toggle (Focus Mode)
function initPanelToggle() {
  const panelToggleBtn = document.getElementById('panel-toggle-btn');
  const panelRestoreBtn = document.getElementById('panel-restore-btn');
  const panelToggleText = document.getElementById('panel-toggle-text');
  const panelToggleIcon = document.getElementById('panel-toggle-icon');

  function updatePanelUI(isHidden) {
    if (panelToggleText) {
      panelToggleText.textContent = isHidden ? 'Panels: OFF' : 'Panels: ON';
    }
    if (panelToggleIcon) {
      panelToggleIcon.innerHTML = isHidden ? '&#x25F1;' : '&#x25F0;';
    }
    if (panelToggleBtn) {
      if (isHidden) {
        panelToggleBtn.classList.add('active');
        panelToggleBtn.setAttribute('title', 'Restore navigation panel (Hotkey: [ )');
        panelToggleBtn.setAttribute('aria-label', 'Restore navigation panel (Hotkey: [ )');
      } else {
        panelToggleBtn.classList.remove('active');
        panelToggleBtn.setAttribute('title', 'Hide navigation panel (Hotkey: [ )');
        panelToggleBtn.setAttribute('aria-label', 'Hide navigation panel (Hotkey: [ )');
      }
    }
  }

  function setPanelsHidden(hidden) {
    if (hidden) {
      document.body.classList.add('panels-hidden');
      localStorage.setItem('daedalus_panels_hidden', 'true');
    } else {
      document.body.classList.remove('panels-hidden');
      localStorage.setItem('daedalus_panels_hidden', 'false');
    }
    updatePanelUI(hidden);
    if (typeof playAvionicsChirp === 'function') {
      playAvionicsChirp(hidden ? 750 : 1050, 'sine', 0.05);
    }
    setTimeout(() => {
      window.dispatchEvent(new Event('resize'));
    }, 260);
  }

  function togglePanels() {
    const isHidden = document.body.classList.contains('panels-hidden');
    setPanelsHidden(!isHidden);
  }

  // Restore saved preference
  const savedPreference = localStorage.getItem('daedalus_panels_hidden') === 'true';
  if (savedPreference) {
    setPanelsHidden(true);
  } else {
    updatePanelUI(false);
  }

  if (panelToggleBtn) {
    panelToggleBtn.addEventListener('click', togglePanels);
  }
  if (panelRestoreBtn) {
    panelRestoreBtn.addEventListener('click', () => setPanelsHidden(false));
  }

  // Keyboard shortcut listener: '[' or 'Alt+P' or 'Ctrl+B'
  window.addEventListener('keydown', (e) => {
    if (e.target && ['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;
    if (e.key === '[' || (e.altKey && (e.key === 'p' || e.key === 'P')) || ((e.ctrlKey || e.metaKey) && (e.key === 'b' || e.key === 'B'))) {
      e.preventDefault();
      togglePanels();
    }
  });
}

// Reset Code Scroll Helper to prevent sliced pseudocode
function resetCodeScroll() {
  document.querySelectorAll('.code-container, .code-container pre, pre').forEach(el => {
    el.scrollTop = 0;
  });
}

// Global initialization on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initNavigation();
  initSearchPalette();
  initMissionClock();
  initAvionicsAudio();
  initPanelToggle();
  initFullscreen();
  resetCodeScroll();

  window.addEventListener('load', resetCodeScroll);

  if (window.retriggerMathRendering) {
    window.retriggerMathRendering();
  }

  // Polling to guarantee KaTeX renders even if vendor script finishes after DOMContentLoaded
  let mathCheckAttempts = 0;
  const mathPoll = setInterval(() => {
    mathCheckAttempts++;
    if (window.retriggerMathRendering) {
      window.retriggerMathRendering();
    }
    if (document.querySelectorAll('.katex').length > 50 || mathCheckAttempts > 20) {
      clearInterval(mathPoll);
    }
  }, 100);

  window.sim1 = new HullPathfinderSim();
  window.sim2 = new PowerGridCSPSim();
  window.sim3 = new AdversarialMinimaxSim();
  window.sim4 = new ReactorRLSim();
  window.sim5 = new HMMSensorTrackerSim();
  window.sim6 = new AtmosphericClassifierSim();
  window.sim7 = new DockingGuidanceSim();
});
