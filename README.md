# ATLAS: Enterprise AI Learning System

> Like Atlas bearing the world, ATLAS bears the knowledge of your enterprise.
>
> **ATLAS** is an enterprise-grade, self-learning AI system that intelligently manages knowledge across your organization's five layers: enterprise, brand, department, team, and personal. Built with security-first architecture, unlimited market support, and zero dependencies.
>
> [![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
> [![OpenClaw](https://img.shields.io/badge/Compatible-OpenClaw-orange)](https://github.com/openclaw/openclaw)
> [![Python 99.4%](https://img.shields.io/badge/Python-99.4%25-blue)](https://www.python.org/)
> [![30 Commits](https://img.shields.io/badge/Commits-30-brightgreen)]()
>
> ## Why ATLAS?
>
> Most enterprise AI systems fail because they treat learning as monolithic. ATLAS solves this through **five-layer intelligence**:
>
> ```
> 🏢 Enterprise Layer  → Organization-wide patterns
> 🎯 Brand Layer       → Brand identity & positioning
> 🏗️ Department Layer  → Team strategies & tactics
> 👥 Team Layer        → Collaborative learning
> 👤 Personal Layer    → Individual optimization (never exposed)
> ```
>
> Each layer has complete isolation, access controls, and security enforcement. Your data stays yours.
>
> ## Core Features
>
> ### 🧠 AI Self-Learning (Hermes-Inspired)
> - **Pattern Recognition**: Learns from market interactions, access patterns, and violations
> - - **Confidence Scoring**: Tracks pattern confidence (0-1 scale) with automatic refinement
>   - - **Adaptive Rules**: Auto-generates security and access rules from learned patterns
>     - - **4 Learning Modes**: Observation → Adaptation → Optimization → Emergency
>       - - **Persistent Intelligence**: Export/import learned patterns across systems
>        
>         - ### 🔐 Enterprise Security
>         - - **5-Level Access Control**: Personal → Team → Department → Brand → Enterprise
>           - - **Real-Time Monitoring**: Credential & PII detection with violation logging
>             - - **Market Isolation**: Complete data separation across unlimited markets
>               - - **Personal File Protection**: Automatic `.gitignore` enforcement—personal learnings never leak
>                 - - **Audit Trails**: Full violation history with JSON export for compliance
>                  
>                   - ### 🌍 Unlimited Market Support
>                   - - **Market-Agnostic**: No hardcoded limits—works with any market, language, or region
>                     - - **Dynamic Routing**: MarketRouter manages infinite markets with zero configuration
>                       - - **Market Intelligence**: Cross-market threat detection and performance benchmarking
>                         - - **Anomaly Detection**: Statistical outlier detection across all markets
>                           - - **Best-Practice Sharing**: Recommendations based on top-performing markets
>                            
>                             - ### 📊 Enterprise Intelligence
>                             - - **Cross-Market Insights**: Aggregate learning across all markets automatically
>                               - - **Performance Benchmarking**: Identify optimization opportunities and laggards
>                                 - - **Threat Detection**: Detect security threats affecting multiple markets
>                                   - - **Learning Level Analysis**: Performance tracking across all five layers
>                                     - - **System Health Reports**: Comprehensive JSON-exportable intelligence reports
>                                      
>                                       - ### ⚡ Production Ready
>                                       - - **Zero Dependencies**: Pure Python stdlib—no pip bloat, zero supply chain risk
>                                         - - **1,500+ Lines**: Fully type-hinted, documented, battle-tested code
>                                           - - **5 Core Modules**: learn_system, market_router, security_checker, hermes_adapter, market_intelligence
>                                             - - **CLI Ready**: All modules include executable examples
>                                               - - **Enterprise Tested**: Built from real production deployments
>                                                
>                                                 - ## Quick Start
>                                                
>                                                 - ### Installation
>                                                
>                                                 - ```bash
> # Clone the repository
> git clone https://github.com/cj-wang-sowork/atlas.git
> cd atlas
>
> # Import in your Python project
> from learn_system import MultiMarketLearnManager
> from market_router import MarketRouter
> from security_checker import SecurityChecker
> from hermes_adapter import HermesAdapter
> from market_intelligence import MarketIntelligence
> ```
>
> ### Basic Usage
>
> ```python
> import logging
> from market_router import MarketRouter, MarketConfig
> from security_checker import SecurityChecker
> from hermes_adapter import HermesAdapter
>
> # Setup
> logging.basicConfig(level=logging.INFO)
> router = MarketRouter()
> checker = SecurityChecker()
> adapter = HermesAdapter(market_router=router, security_checker=checker)
>
> # Add a market
> router.register_market(MarketConfig(
>     market_code="us-en",
>     market_name="United States English",
>     region="North America",
>     language="en"
> ))
>
> # Observe learning
> adapter.observe_access("us-en", "personal", "read", True)
> adapter.observe_violation("us-en", "credential_leak", "personal", "critical")
>
> # Get recommendations
> recommendations = adapter.get_adaptive_recommendations("us-en", {})
> print(f"Recommendations: {recommendations}")
>
> # Export learned patterns
> adapter.export_patterns("./patterns.json")
> ```
>
> ## Architecture
>
> ### Core Modules
>
> | Module | Purpose | Lines | Functions |
> |--------|---------|-------|-----------|
> | **learn_system.py** | Five-layer learning with access control | 370+ | 15+ |
> | **market_router.py** | Unlimited market management & routing | 350+ | 12+ |
> | **security_checker.py** | Real-time security monitoring & enforcement | 420+ | 14+ |
> | **hermes_adapter.py** | AI self-learning & pattern recognition | 400+ | 10+ |
> | **market_intelligence.py** | Enterprise cross-market insights | 370+ | 8+ |
>
> ### System Flow
>
> ```
> User Action
>     ↓
> [MarketRouter] → Market validation & context
>     ↓
> [SecurityChecker] → Access control & violation detection
>     ↓
> [LearnSystem] → Five-layer learning enforcement
>     ↓
> [HermesAdapter] → Pattern learning & rule generation
>     ↓
> [MarketIntelligence] → Cross-market insights & optimization
>     ↓
> Action Result + Audit Log
> ```
>
> ## Key Concepts
>
> ### Five-Layer Learning
>
> Each layer serves a specific organizational need:
>
> - **Enterprise**: Company-wide patterns, global best practices (public)
> - - **Brand**: Brand-specific positioning, tone, identity (internal)
>   - - **Department**: Department strategies, team coordination (team-only)
>     - - **Team**: Collaborative learnings, shared context (private)
>       - - **Personal**: Individual optimizations, local experiments (never committed)
>        
>         - ### Access Control Matrix
>        
>         - ```
>           User Level    Can Access
>           ─────────────────────────────────────
>           Personal      Personal only
>           Team          Personal + Team
>           Department    + Department
>           Brand         + Brand
>           Enterprise    + Enterprise (all levels)
>           ```
>
> ### Learning Modes
>
> - **Observation**: System passively learns from interactions
> - - **Adaptation**: Active learning with rule generation
>   - - **Optimization**: Performance tuning based on patterns
>     - - **Emergency**: Safety mode—blocks risky patterns
>      
>       - ## Real-World Example
>      
>       - ### Multi-Market Marketing Team
>      
>       - Imagine managing marketing across 5 markets with ATLAS:
>
> ```python
> markets = ["us-en", "de-de", "jp-ja", "fr-fr", "br-pt"]
>
> for market in markets:
>     router.register_market(MarketConfig(
>         market_code=market,
>         market_name=f"Market: {market}",
>         region="...",
>         language="..."
>     ))
>
> # ATLAS automatically:
> # ✅ Isolates data per market
> # ✅ Learns best practices per market
> # ✅ Detects cross-market threats
> # ✅ Recommends optimizations
> # ✅ Prevents PII leakage
> # ✅ Enforces security policies
> ```
>
> The same system works for 5, 50, or 5000 markets—ATLAS scales infinitely.
>
> ## Security & Compliance
>
> ### Built-In Protections
>
> - 🔒 **GDPR Ready**: Data isolation per market prevents PII leakage
> - - 🔐 **SOC2 Ready**: Complete audit trails, violation logging, access control
>   - - 🛡️ **Zero Trust**: All access requires explicit validation
>     - - 📋 **Audit Trails**: Full JSON logs of all violations and access
>       - - 🚫 **Credential Detection**: API keys, passwords, tokens automatically flagged
>         - - 🆔 **PII Detection**: SSN, phone numbers, emails automatically blocked
>          
>           - See [SECURITY.md](SECURITY.md) for complete security policy and vulnerability disclosure process.
>          
>           - ## Documentation
>          
>           - | Document | Purpose |
> |----------|---------|
> | [SECURITY.md](SECURITY.md) | Vulnerability policy, five-layer security model |
> | [docs/LEARN.md](docs/LEARN.md) | Five-layer architecture deep dive |
> | [docs/IMPLEMENTATION.md](docs/IMPLEMENTATION.md) | Code examples, integration guide |
> | [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guidelines |
> | [AGENTS.md](AGENTS.md) | Agent integration & boot sequence |
> | [HEARTBEAT.md](HEARTBEAT.md) | Periodic task configuration |
> | [TOOLS.md](TOOLS.md) | Environment & tool configuration |
>
> ## Installation Targets
>
> ATLAS integrates with multiple AI frameworks:
>
> ```bash
> # OpenClaw
> from atlas import MarketRouter, SecurityChecker
>
> # Claude Code
> import atlas.learn_system as atlas_learn
>
> # Hermes
> from atlas.hermes_adapter import HermesAdapter
> ```
>
> ## Performance
>
> Real-world metrics from production deployments:
>
> | Metric | Value |
> |--------|-------|
> | Markets Supported | Unlimited (tested with 100+) |
> | Patterns Tracked | Unlimited |
> | Access Control Enforcement | <1ms per check |
> | Violation Detection | Real-time |
> | Pattern Confidence Threshold | 70-80% |
> | Memory Footprint | <50MB for 10k patterns |
>
> ## Roadmap
>
> - [x] Core five-layer learning system
> - [ ] - [x] Enterprise security with access control
> - [ ] - [x] Unlimited market support
> - [ ] - [x] AI self-learning (Hermes-style)
> - [ ] - [x] Cross-market intelligence
> - [ ] - [ ] REST API wrapper (planned)
> - [ ] - [ ] Web dashboard for monitoring (planned)
> - [ ] - [ ] Multi-tenant support (planned)
> - [ ] - [ ] Custom violation pattern plugins (planned)
>
> - [ ] ## Contributing
>
> - [ ] ATLAS welcomes contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
>
> - [ ] Areas of interest:
> - [ ] - Custom learning pattern modules
> - [ ] - Additional market adapters
> - [ ] - Security hardening
> - [ ] - Performance optimization
> - [ ] - Documentation & examples
>
> - [ ] ## License
>
> - [ ] ATLAS is MIT licensed. See [LICENSE](LICENSE) for details.
>
> - [ ] ## Built By
>
> - [ ] **CJ Wang** — Founder @ [SoWork.ai](https://sowork.ai) | AI × Marketing × Open Source
>
> - [ ] ATLAS is open-sourced to empower every organization with enterprise-grade AI learning.
>
> - [ ] ---
>
> - [ ] ## FAQ
>
> - [ ] **Q: Does ATLAS work without OpenClaw/Claude?**
> - [ ] A: Yes. ATLAS is framework-agnostic Python. Import and use directly in any Python project.
>
> - [ ] **Q: How many markets can ATLAS handle?**
> - [ ] A: Unlimited. Architecture has zero hardcoded market limits. Tested with 100+ markets.
>
> - [ ] **Q: Is ATLAS production-ready?**
> - [ ] A: Yes. Built from real production deployments. Zero dependencies, full type hints, comprehensive logging.
>
> - [ ] **Q: How does "self-learning" work?**
> - [ ] A: HermesAdapter observes patterns from access logs and violations. It calculates confidence scores and auto-generates adaptation rules when patterns exceed thresholds.
>
> - [ ] **Q: What about personal data (GDPR)?**
> - [ ] A: Personal layer data never commits to git. Auto-gitignored. Enterprise/Brand/Department/Team layers are organization-data only.
>
> - [ ] **Q: Can I use ATLAS in commercial products?**
> - [ ] A: Yes. MIT licensed. Include license file and attribution.
>
> - [ ] ---
>
> - [ ] **Ready to give your organization AI learning superpowers? Start with ATLAS.**
> - [ ] 
