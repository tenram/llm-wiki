# Knowledge Base Index

## llm-workflows

Patterns and practices for using LLMs to build, maintain, and query personal or team knowledge bases.

| Article | Summary | Updated |
|---------|---------|---------|
| [LLM Wiki Pattern](wiki/llm-workflows/llm-wiki-pattern.md) | LLM-maintained persistent wiki as an alternative to query-time RAG, with raw/wiki/schema architecture and ingest/query/lint operations | 2026-07-11 |
| [Karpathy LLM Wiki](wiki/llm-workflows/karpathy-llm-wiki.md) | Repository implementation of the persistent wiki pattern with raw/wiki/index/log/schema workflow | 2026-08-18 |

## ai-agent-harnesses

Frameworks and essays on the scaffolding (tools, state control, orchestration) around AI coding agents.

| Article | Summary | Updated |
|---------|---------|---------|
| [Awesome Harness Engineering](wiki/ai-agent-harnesses/awesome-harness-engineering.md) | Curated resource list defining harness engineering as the primary lever for agent success | 2026-07-11 |
| [Harness Design Principles](wiki/ai-agent-harnesses/harness-design-principles.md) | Five-component harness model: rules, skills, hooks, MCP, memory | 2026-07-11 |
| [oh-my-claudecode](wiki/ai-agent-harnesses/oh-my-claudecode.md) | Zero-config Claude Code plugin adding 32 specialized agents and parallel execution modes | 2026-07-11 |
| [Superpowers](wiki/ai-agent-harnesses/superpowers.md) | Skills framework enforcing brainstorm-plan-TDD-review workflow before coding | 2026-07-11 |
| [Life-Harness](wiki/ai-agent-harnesses/life-harness.md) | Training-free runtime harness adaptation improving frozen-model agent performance | 2026-07-11 |
| [Statewright](wiki/ai-agent-harnesses/statewright.md) | State-machine tool restriction per workflow phase, enforced via Rust engine and MCP gateway | 2026-07-11 |
| [Firstmate](wiki/ai-agent-harnesses/firstmate.md) | Single-agent-to-many-crewmate orchestration in isolated git worktrees | 2026-07-11 |
| [Multica](wiki/ai-agent-harnesses/multica.md) | Managed agents platform treating AI coding agents as team members | 2026-07-11 |
| [ECC](wiki/ai-agent-harnesses/ecc.md) | Cross-harness "operating system" bundling skills, memory optimization, and security scanning | 2026-07-11 |
| [The Software Factory](wiki/ai-agent-harnesses/software-factory.md) | Playbook for rebuilding SaaS to feature parity via layered agent context, spec-driven builds, and the SPEAR workflow | 2026-07-21 |
| [OpenClaw](wiki/ai-agent-harnesses/openclaw.md) | Self-hosted multi-channel agent framework configured entirely through editable Markdown workspace files | 2026-07-31 |
| [GNHF](wiki/ai-agent-harnesses/gnhf.md) | Overnight autonomous agent orchestrator: committed iterations, usage-limit-aware retries, worktree concurrency | 2026-08-24 |
| [Munder Difflin](wiki/ai-agent-harnesses/munder-difflin.md) | Electron multi-agent office harness wrapping terminal CLIs as avatar agents coordinated by a GOD orchestrator over a file-based hive | 2026-08-24 |

## claude-code-ecosystem

Skills, plugins, and workflow integrations built on or around Claude Code.

| Article | Summary | Updated |
|---------|---------|---------|
| [Anthropic Agent Skills](wiki/claude-code-ecosystem/anthropics-skills.md) | Anthropic's reference spec and examples for dynamically-loaded Claude skills, plus the formal open agentskills.io format specification | 2026-07-21 |
| [Academic Research Skills](wiki/claude-code-ecosystem/academic-research-skills.md) | Multi-agent research-to-publication pipeline with non-bypassable human oversight gates | 2026-07-11 |
| [UI UX Pro Max Skill](wiki/claude-code-ecosystem/ui-ux-pro-max-skill.md) | BM25-ranked design intelligence skill covering styles, palettes, typography, and full design-system generation | 2026-07-11 |
| [article-writing-skills](wiki/claude-code-ecosystem/article-writing-skills.md) | System prompts emulating engineers' explanatory thinking patterns, not their prose style | 2026-07-11 |
| [Claude How To](wiki/claude-code-ecosystem/claude-howto.md) | Ten-module practical guide to Claude Code features and workflows | 2026-07-11 |
| [Claude Design](wiki/claude-code-ecosystem/claude-design.md) | Conversational design canvas integrated with org design systems and Claude Code | 2026-07-11 |
| [Claude Code GitHub CI Integration](wiki/claude-code-ecosystem/claude-code-github-ci-integration.md) | Two real-world setups wiring the Claude GitHub App into PR/issue workflows | 2026-07-11 |
| [Agent Skills Engineering Workflows](wiki/claude-code-ecosystem/agent-skills-engineering-workflows.md) | 24-skill collection encoding senior-engineer discipline (spec, plan, build, test, review, ship) as agent-loadable workflows | 2026-07-21 |
| [Awesome Claude Skills](wiki/claude-code-ecosystem/awesome-claude-skills.md) | 13-category curated list of third-party Claude Skills across dev, data, science, and media domains | 2026-07-21 |
| [Self-Improving AI Skills](wiki/claude-code-ecosystem/self-improving-ai-skills.md) | Pattern for compounding skill quality via a learnings.md feedback loop, without model fine-tuning | 2026-07-31 |
| [Claude Agent SDK: Subagents](wiki/claude-code-ecosystem/agent-sdk-subagents.md) | Python/TypeScript library exposing Claude Code's agent loop, tools, and subagent spawning outside the CLI | 2026-07-31 |

## antigravity-ecosystem

Agent-first skill catalogs and Antigravity-compatible installation surfaces.

| Article | Summary | Updated |
|---------|---------|---------|
| [Agentic Awesome Skills](wiki/antigravity-ecosystem/agentic-awesome-skills.md) | Large local skill catalog with AAS Core, exact stack validation, immutable plan preview, and Antigravity support | 2026-08-14 |

## agent-memory-systems

Persistent memory and retrieval architectures for AI agents.

| Article | Summary | Updated |
|---------|---------|---------|
| [RightMemory](wiki/agent-memory-systems/rightmemory.md) | Deterministic, file-based tree+graph memory for agent teams, explicitly non-embedding | 2026-07-11 |
| [Open Brain (OB1)](wiki/agent-memory-systems/ob1.md) | Self-hosted unified vector memory layer shared across AI tools via pgvector and MCP | 2026-07-11 |
| [Codebase Memory and Code Graphs](wiki/agent-memory-systems/codebase-memory-and-code-graphs.md) | Code-aware memory pattern turning repositories into persistent graph structure; compares codebase-memory-mcp (158-language Cypher-queryable graph MCP) and CodeGraph (Rust-kernel single-tool explore) | 2026-08-24 |
| [HybridRAG System](wiki/agent-memory-systems/hybridrag-system.md) | Combines vector similarity search with knowledge-graph retrieval in one RAG pipeline, across three implementations plus a store-comparison and a live-update construction pattern | 2026-07-31 |
| [Hermes Agent](wiki/agent-memory-systems/hermes-agent.md) | Nous Research's open-source multi-platform desktop agent with unified persistent memory and sandboxed subagents | 2026-07-21 |
| [Town](wiki/agent-memory-systems/town.md) | Commercial personal-assistant SaaS pairing users with a learning "Townie" for recurring work automation | 2026-07-21 |

## browser-and-mcp-tooling

Browser automation and the Model Context Protocol ecosystem.

| Article | Summary | Updated |
|---------|---------|---------|
| [Playwright](wiki/browser-and-mcp-tooling/playwright.md) | Cross-browser automation library from Microsoft, increasingly used by AI agents | 2026-07-11 |
| [Playwright MCP](wiki/browser-and-mcp-tooling/playwright-mcp.md) | MCP server exposing Playwright via accessibility snapshots instead of screenshots | 2026-07-11 |
| [Stealth Browser Automation](wiki/browser-and-mcp-tooling/stealth-browser-automation.md) | Playwright and Puppeteer stealth layers for lower-fingerprint browser automation | 2026-08-18 |
| [Model Context Protocol Overview](wiki/browser-and-mcp-tooling/model-context-protocol-overview.md) | Open standard connecting AI apps to external data, tools, and workflows | 2026-07-31 |
| [Deliberation](wiki/browser-and-mcp-tooling/deliberation-mcp.md) | MCP server for consulting GPT/Gemini/Grok/OpenRouter models as reviewers, with a bias-guarded consensus loop | 2026-07-31 |
| [MCP Reference Servers](wiki/browser-and-mcp-tooling/mcp-reference-servers.md) | Steering-group-maintained reference MCP server implementations | 2026-07-11 |
| [LambdaTest Puppeteer Skill](wiki/browser-and-mcp-tooling/lambdatest-puppeteer-skill.md) | Agent skill teaching Puppeteer patterns for scraping, PDF/screenshot capture, and E2E testing | 2026-07-21 |
| [Firecrawl](wiki/browser-and-mcp-tooling/firecrawl.md) | Web context API for search, scrape, interact, crawl, map, and batch extraction with SDK and MCP support | 2026-08-28 |
| [Agent Reach](wiki/browser-and-mcp-tooling/agent-reach.md) | Capability layer that installs and routes web-access backends for agents across social, video, search, and GitHub channels | 2026-08-28 |

## collaboration-platforms

Open core and self-hosted collaboration suites.

| Article | Summary | Updated |
|---------|---------|---------|
| [Mattermost](wiki/collaboration-platforms/mattermost.md) | Open core collaboration platform with chat, automation, calling, screen sharing, and AI integration | 2026-08-28 |

## deepfake-detection

Facial-manipulation datasets, detection benchmarks, and related public research communication.

| Article | Summary | Updated |
|---------|---------|---------|
| [FaceForensics++](wiki/deepfake-detection/faceforensics-plusplus.md) | ICCV 2019 facial-manipulation detection benchmark with 1.8M+ manipulated images, incl. FaceShifter subset | 2026-07-11 |
| [Justus Thies: Tutorials & Demos](wiki/deepfake-detection/justus-thies-tutorials.md) | 2016-2023 catalog tracking the arc from reenactment demos to detection research to policy briefings | 2026-07-11 |

## osint-tools

Open-source investigation and archival tooling.

| Article | Summary | Updated |
|---------|---------|---------|
| [Bellingcat Tool Suite](wiki/osint-tools/bellingcat-tools.md) | Investigative collective's tools for verifiable web archiving, geolocation, and OSINT | 2026-07-11 |

## document-processing

Tools for converting documents into structured, LLM-usable formats.

| Article | Summary | Updated |
|---------|---------|---------|
| [marker-pdf](wiki/document-processing/marker-pdf.md) | Fast PDF/DOCX/PPTX-to-Markdown/JSON converter with optional LLM-boosted accuracy | 2026-07-31 |
| [Docling](wiki/document-processing/docling.md) | IBM Research's broad-format (incl. audio/video/email/financial docs) document-to-structured-data framework, MIT licensed | 2026-07-31 |
| [newspaper](wiki/document-processing/newspaper.md) | Python article extractor for page text, metadata, authors, and images | 2026-08-18 |

## research-and-training

Autonomous research systems and speculative/fringe LLM technique proposals.

| Article | Summary | Updated |
|---------|---------|---------|
| [Autoresearch](wiki/research-and-training/autoresearch.md) | Overnight autonomous LLM-training experimentation on a single GPU with narrow agent write-access | 2026-07-11 |
| [The Guanyin Protocol: Semantic Anchoring](wiki/research-and-training/guanyin-protocol-semantic-anchoring.md) | [Quality-flagged] Self-published preprint proposing a coherence-improving prompt technique | 2026-07-11 |

## model-routing

Multi-model orchestration and routing services.

| Article | Summary | Updated |
|---------|---------|---------|
| [Model Fusion (OpenRouter)](wiki/model-routing/openrouter-fusion.md) | [Thin source] OpenRouter feature for running multiple models and fusing the best answer | 2026-07-31 |
| [opencode-model-router](wiki/model-routing/opencode-model-router.md) | OpenCode plugin routing tasks to the cheapest adequate model tier via an injected delegation protocol | 2026-07-31 |

## networking-tools

Networking and connectivity infrastructure products.

| Article | Summary | Updated |
|---------|---------|---------|
| [ZeroTier](wiki/networking-tools/zerotier.md) | Software-defined networking platform with five pricing tiers from free personal use to defense-grade Quantum | 2026-07-21 |

## opencode-ecosystem

Opencode terminal coding agent and its plugin/orchestration ecosystem.

| Article | Summary | Updated |
|---------|---------|---------|
| [Opencode Orchestration Layer](wiki/opencode-ecosystem/opencode-orchestration.md) | Maps awesome-opencode's plugin ecosystem and compares two competing multi-agent orchestration approaches (hierarchical vs. role-based) | 2026-07-31 |

## backend-infrastructure

Hosted backend platforms used as infrastructure by AI/agent tooling.

| Article | Summary | Updated |
|---------|---------|---------|
| [Supabase](wiki/backend-infrastructure/supabase.md) | Open-source Postgres development platform (auth, storage, realtime, vector tooling) built on managed PostgreSQL | 2026-07-31 |

## dev-tools

General-purpose developer utilities, not specific to LLM/agent workflows.

| Article | Summary | Updated |
|---------|---------|---------|
| [SQL Fiddle](wiki/dev-tools/sqlfiddle.md) | Web-based multi-dialect SQL playground for practicing and sharing queries | 2026-07-31 |

## web-standards

Web metadata and markup standards.

| Article | Summary | Updated |
|---------|---------|---------|
| [The Open Graph Protocol](wiki/web-standards/open-graph-protocol.md) | Metadata standard (og:title/type/image/url) for rich social-link previews | 2026-07-31 |
| [DOM Libraries: HyperHTML and Linkedom](wiki/web-standards/dom-libraries.md) | Lightweight DOM libraries for template updates and server-side DOM emulation | 2026-08-18 |

## server-monitoring

Self-hosted server monitoring dashboards.

| Article | Summary | Updated |
|---------|---------|---------|
| [Beszel](wiki/server-monitoring/beszel.md) | Lightweight hub+agent monitoring platform: Docker stats, SMART, GPU/temps, alerts, OAuth, historical data | 2026-08-24 |
| [Linux Dash](wiki/server-monitoring/linux-dash.md) | Minimal ~400KB real-time Linux dashboard; unmaintained since 2024, no auth — superseded by Beszel | 2026-08-24 |

## machine-learning

Gradient boosting library and applied classification patterns.

| Article | Summary | Updated |
|---------|---------|---------|
| [XGBoost](wiki/machine-learning/xgboost.md) | Optimized distributed gradient boosting library (GBDT) portable from laptop to Spark/Kubernetes scale | 2026-08-24 |
| [XGBoost Imbalanced Classification Pattern](wiki/machine-learning/xgboost-imbalanced-classification-pattern.md) | Bank-marketing worked pattern: class weighting and resampling reaching 0.84 recall on imbalanced positives | 2026-08-24 |
