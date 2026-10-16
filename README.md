# Knowledge Base Index

## llm-workflows

Patterns and practices for using LLMs to build, maintain, and query personal or team knowledge bases.

| Article | Summary | Updated |
|---------|---------|---------|
| [LLM Wiki Pattern](wiki/llm-workflows/llm-wiki-pattern.md) | LLM-maintained persistent wiki as an alternative to query-time RAG, with raw/wiki/schema architecture and ingest/query/lint operations | 2026-07-11 |
| [Karpathy LLM Wiki](wiki/llm-workflows/karpathy-llm-wiki.md) | Repository implementation of the persistent wiki pattern with raw/wiki/index/log/schema workflow | 2026-08-18 |
| [OpenAI Decisions API: Bounded Model Decisions](wiki/llm-workflows/openai-decisions-api.md) | Decision-oriented model interface for bounded classification, routing, and agent control choices, with policy enforcement kept in code | 2026-10-05 |

## ai-agent-harnesses

Frameworks and essays on the scaffolding (tools, state control, orchestration) around AI coding agents.

| Article | Summary | Updated |
|---------|---------|---------|
| [Awesome Harness Engineering](wiki/ai-agent-harnesses/awesome-harness-engineering.md) | Curated resource list defining harness engineering as the primary lever for agent success | 2026-09-30 |
| [Harness Design Principles](wiki/ai-agent-harnesses/harness-design-principles.md) | Five-component harness model: rules, skills, hooks, MCP, memory | 2026-09-30 |
| [oh-my-claudecode](wiki/ai-agent-harnesses/oh-my-claudecode.md) | Zero-config Claude Code plugin adding 32 specialized agents and parallel execution modes | 2026-07-11 |
| [Superpowers](wiki/ai-agent-harnesses/superpowers.md) | Skills framework enforcing brainstorm-plan-TDD-review workflow before coding | 2026-07-11 |
| [Life-Harness](wiki/ai-agent-harnesses/life-harness.md) | Training-free runtime harness adaptation improving frozen-model agent performance | 2026-07-11 |
| [Statewright](wiki/ai-agent-harnesses/statewright.md) | State-machine tool restriction per workflow phase, enforced via Rust engine and MCP gateway | 2026-07-11 |
| [Firstmate](wiki/ai-agent-harnesses/firstmate.md) | Single-agent-to-many-crewmate orchestration in isolated git worktrees | 2026-07-11 |
| [Multica](wiki/ai-agent-harnesses/multica.md) | Managed agents platform treating AI coding agents as team members, driving 26 agent CLIs | 2026-09-17 |
| [ECC](wiki/ai-agent-harnesses/ecc.md) | Cross-harness "operating system" bundling skills, memory optimization, and security scanning | 2026-07-11 |
| [The Software Factory](wiki/ai-agent-harnesses/software-factory.md) | Playbook for rebuilding SaaS to feature parity via layered agent context, spec-driven builds, and the SPEAR workflow | 2026-07-21 |
| [Superset](wiki/ai-agent-harnesses/superset.md) | Desktop agentic IDE for parallel CLI-agent workspaces, review, browser previews, automation, remote access, CLI, SDK, and MCP | 2026-09-30 |
| [Caveman](wiki/ai-agent-harnesses/caveman.md) | Token-reduction skill, local proxy, and application middleware that compress agent prose and tool context with recovery | 2026-09-30 |
| [OpenClaw](wiki/ai-agent-harnesses/openclaw.md) | Self-hosted multi-channel agent framework configured entirely through editable Markdown workspace files | 2026-07-31 |
| [GNHF](wiki/ai-agent-harnesses/gnhf.md) | Overnight autonomous agent orchestrator: committed iterations, usage-limit-aware retries, worktree concurrency | 2026-08-24 |
| [Munder Difflin](wiki/ai-agent-harnesses/munder-difflin.md) | Electron multi-agent office harness wrapping terminal CLIs as avatar agents coordinated by a GOD orchestrator over a file-based hive | 2026-08-24 |
| [Ponytail](wiki/ai-agent-harnesses/ponytail.md) | Cross-harness skill enforcing a laziness ladder (stdlib/native/reuse before new code); benchmarked ~54% less code with 100% safety | 2026-09-17 |
| [DDC Skills for AI Agents in Construction](wiki/ai-agent-harnesses/ddc-construction-skills.md) | Cross-agent catalog of 238 construction-automation skills covering BIM, estimating, documents, reporting, analytics, and OpenConstructionERP | 2026-10-08 |
| [Hermes Skills Ecosystem](wiki/ai-agent-harnesses/hermes-skills-ecosystem.md) | Layered Hermes skill distribution: built-ins, official optional skills, and community skills with discovery and safety guidance | 2026-10-16 |
| [Agent Replicate](wiki/ai-agent-harnesses/agent-replicate.md) | OpenClaw skill for cloning an agent with explicit personality, memory, skill, registration, and communication choices | 2026-10-10 |
| [cmux](wiki/ai-agent-harnesses/cmux.md) | Native macOS Ghostty-based terminal workspace for AI agents with visible splits, notifications, embedded browser automation, SSH, hooks, and CLI/socket control | 2026-10-10 |
| [Agent Skills Platform](wiki/ai-agent-harnesses/agent-skills-platform.md) | Turns a workflow into a tested, installable agent skill and governs its lifecycle through a user-defined marketplace (evidence, discovery, rollback, quarantine, 17-platform distribution) | 2026-10-16 |
| [Hermes Incident Commander](wiki/ai-agent-harnesses/hermes-incident-commander.md) | Autonomous SRE agent that detects, diagnoses, and self-heals incidents via Hermes (memory, skill auto-creation, cron, gateway, subagents, RL), plus a safe standalone watchdog with an allow-listed remediation model | 2026-10-16 |

## claude-code-ecosystem

Skills, plugins, and workflow integrations built on or around Claude Code.

| Article | Summary | Updated |
|---------|---------|---------|
| [Anthropic Agent Skills](wiki/claude-code-ecosystem/anthropics-skills.md) | Anthropic's reference spec and examples for dynamically-loaded Claude skills, plus the formal open agentskills.io format specification | 2026-10-16 |
| [Academic Research Skills](wiki/claude-code-ecosystem/academic-research-skills.md) | Multi-agent research-to-publication pipeline with non-bypassable human oversight gates | 2026-07-11 |
| [UI UX Pro Max Skill](wiki/claude-code-ecosystem/ui-ux-pro-max-skill.md) | BM25-ranked design intelligence skill covering styles, palettes, typography, and full design-system generation | 2026-07-11 |
| [article-writing-skills](wiki/claude-code-ecosystem/article-writing-skills.md) | System prompts emulating engineers' explanatory thinking patterns, not their prose style | 2026-07-11 |
| [Claude How To](wiki/claude-code-ecosystem/claude-howto.md) | Ten-module practical guide to Claude Code features and workflows | 2026-07-11 |
| [Claude Design](wiki/claude-code-ecosystem/claude-design.md) | Conversational design canvas integrated with org design systems and Claude Code | 2026-07-11 |
| [Claude Code GitHub CI Integration](wiki/claude-code-ecosystem/claude-code-github-ci-integration.md) | Two real-world setups wiring the Claude GitHub App into PR/issue workflows | 2026-07-11 |
| [Agent Skills Engineering Workflows](wiki/claude-code-ecosystem/agent-skills-engineering-workflows.md) | 24-skill collection encoding senior-engineer discipline (spec, plan, build, test, review, ship) as agent-loadable workflows | 2026-07-21 |
| [Awesome Claude Skills](wiki/claude-code-ecosystem/awesome-claude-skills.md) | 13-category curated list of third-party Claude Skills across dev, data, science, and media domains | 2026-10-16 |
| [Awesome Claude Code](wiki/claude-code-ecosystem/awesome-claude-code.md) | The most-starred Claude Code awesome list (55.8k stars) covering skills, agents, status lines, tooling, and plugins; README generated from a structured resource table | 2026-10-16 |
| [Self-Improving AI Skills](wiki/claude-code-ecosystem/self-improving-ai-skills.md) | Pattern for compounding skill quality via a learnings.md feedback loop, without model fine-tuning | 2026-07-31 |
| [Claude Agent SDK: Subagents](wiki/claude-code-ecosystem/agent-sdk-subagents.md) | Python/TypeScript library exposing Claude Code's agent loop, tools, and subagent spawning outside the CLI | 2026-07-31 |
| [i-have-adhd](wiki/claude-code-ecosystem/i-have-adhd.md) | Cross-agent output style skill that leads with actions, suppresses tangents, caps lists, and ends with one next step | 2026-09-30 |
| [ASD-STE100 Skill](wiki/claude-code-ecosystem/asd-ste100-skill.md) | Aerospace controlled-language rules repurposed for unambiguous agent-facing text | 2026-10-05 |

## ai-agents

Platforms and patterns for building, running, and governing AI agents.

| Article | Summary | Updated |
|---------|---------|---------|
| [CrewAI](wiki/ai-agents/crewai.md) | Enterprise agent build-and-runtime platform positioned around unified development and centralized governance | 2026-10-05 |

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
| [HybridRAG System](wiki/agent-memory-systems/hybridrag-system.md) | Combines vector similarity search with knowledge-graph retrieval in one RAG pipeline, across three implementations plus a store-comparison and a live-update construction pattern | 2026-09-30 |
| [Hermes Agent](wiki/agent-memory-systems/hermes-agent.md) | Nous Research's open-source multi-platform desktop agent with unified persistent memory, sandboxed subagents, and layered built-in/optional skills | 2026-10-16 |
| [Town](wiki/agent-memory-systems/town.md) | Commercial personal-assistant SaaS pairing users with a learning "Townie" for recurring work automation | 2026-07-21 |
| [Graphify](wiki/agent-memory-systems/graphify.md) | Skill/CLI turning a whole project (code, docs, PDFs, images, video) into a local tree-sitter knowledge graph with explained EXTRACTED/INFERRED edges and MCP serving | 2026-09-17 |
| [RecallMax](wiki/agent-memory-systems/recallmax.md) | Local-first TypeScript library and CLI that compresses conversations and project history into structured agent memory without an LLM call | 2026-09-30 |

## browser-and-mcp-tooling

Browser automation and the Model Context Protocol ecosystem.

| Article | Summary | Updated |
|---------|---------|---------|
| [Playwright](wiki/browser-and-mcp-tooling/playwright.md) | Cross-browser automation library from Microsoft, increasingly used by AI agents | 2026-10-13 |
| [Playwright MCP](wiki/browser-and-mcp-tooling/playwright-mcp.md) | Official Microsoft MCP server exposing Playwright via accessibility snapshots; 70+ tools grouped by capability flags, snapshot-based and vision-free | 2026-10-13 |
| [Puppeteer MCP Server (Python)](wiki/browser-and-mcp-tooling/mcp-server-puppeteer-py.md) | Community Python MCP server on Playwright: navigate, screenshot, click/fill, and JS evaluation with configurable timeouts and logging | 2026-10-13 |
| [Anysite MCP](wiki/browser-and-mcp-tooling/anysite-mcp.md) | Hosted MCP server for structured web data (LinkedIn, Reddit, SEC, YC, Crunchbase, etc.) via five universal tools plus CRM write-back, with server-side caching | 2026-10-13 |
| [AnythingMCP (HelpCode)](wiki/browser-and-mcp-tooling/helpcode-anythingmcp.md) | Open-source, self-hosted MCP gateway turning any REST/OpenAPI/SOAP/GraphQL/OData/SQL API into MCP tools (474 connectors, 2,400+ tools) with response mapping, RBAC, audit, knowledge graph, and a family of ERP/SAP/e-commerce/SQL adapters | 2026-10-16 |
| [FastMCP](wiki/browser-and-mcp-tooling/fastmcp.md) | Prefect's Pythonic framework for building MCP servers, clients, and in-conversation apps; the standard application layer powering most MCP servers | 2026-10-16 |
| [Stealth Browser Automation](wiki/browser-and-mcp-tooling/stealth-browser-automation.md) | Playwright and Puppeteer stealth layers for lower-fingerprint browser automation | 2026-10-13 |
| [DevCDP](wiki/browser-and-mcp-tooling/devcdp.md) | MCP server giving assistants real Chrome DevTools access (console, network, DOM, source maps, debugger, discovery) for live debugging, with multi-session tab ownership | 2026-10-13 |
| [Model Context Protocol Overview](wiki/browser-and-mcp-tooling/model-context-protocol-overview.md) | Open standard connecting AI apps to external data, tools, and workflows | 2026-10-16 |
| [Deliberation](wiki/browser-and-mcp-tooling/deliberation-mcp.md) | MCP server for consulting GPT/Gemini/Grok/OpenRouter models as reviewers, with a bias-guarded consensus loop | 2026-07-31 |
| [MCP Reference Servers](wiki/browser-and-mcp-tooling/mcp-reference-servers.md) | Steering-group-maintained reference MCP server implementations | 2026-07-11 |
| [LambdaTest Puppeteer Skill](wiki/browser-and-mcp-tooling/lambdatest-puppeteer-skill.md) | Agent skill teaching Puppeteer patterns for scraping, PDF/screenshot capture, and E2E testing | 2026-07-21 |
| [Firecrawl](wiki/browser-and-mcp-tooling/firecrawl.md) | Web context API for search, scrape, interact, crawl, map, and batch extraction with an AI Agent endpoint (spark-2), SDK and MCP support | 2026-10-13 |
| [Agent Reach](wiki/browser-and-mcp-tooling/agent-reach.md) | Capability layer that installs and routes web-access backends for agents across social, video, search, and GitHub channels | 2026-08-28 |

## collaboration-platforms

Open core and self-hosted collaboration suites.

| Article | Summary | Updated |
|---------|---------|---------|
| [Mattermost](wiki/collaboration-platforms/mattermost.md) | Open core collaboration platform with chat, automation, calling, screen sharing, and AI integration | 2026-08-28 |

## messaging-apis

Self-hosted REST APIs for messaging platforms, primarily WhatsApp messaging and session management.

| Article | Summary | Updated |
|---------|---------|---------|
| [Evolution API](wiki/messaging-apis/evolution-api.md) | Production-ready WhatsApp REST API supporting both Baileys-based WhatsApp Web and Meta's official Cloud API, with chatbot/CRM/event/storage integrations | 2026-10-13 |
| [WAHA — WhatsApp HTTP API](wiki/messaging-apis/waha.md) | Docker-first self-hosted WhatsApp REST API with Swagger UI, named sessions, QR login, and multiple engines (WEBJS/NOWEB/GOWS/WPP) | 2026-10-13 |

## hr-management

Open-source human-resource and payroll management systems.

| Article | Summary | Updated |
|---------|---------|---------|
| [Frappe HR](wiki/hr-management/frappe-hrms.md) | Open-source HRMS built on the Frappe framework: employee lifecycle, leave/attendance, expenses, performance, payroll and taxation, plus a mobile app; split from ERPNext at v14 | 2026-10-13 |

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

## reverse-engineering

Tools for analyzing binaries, applications, and runtime behavior — often agent-driven — to understand internals without source code.

| Article | Summary | Updated |
|---------|---------|---------|
| [REA: Reverse Engineer Anything](wiki/reverse-engineering/rea.md) | MCP server + CLI connecting agents to reverse-engineering tools (Hopper/Ghidra/IDA, JS/Electron, .NET, Android, firmware, packets) for evidence-backed inspection of apps without source | 2026-10-13 |
| [JS Reverse MCP](wiki/reverse-engineering/js-reverse-mcp.md) | AI-native JavaScript reverse-engineering MCP: 24 tools for scripts, breakpoints, network/WebSocket, and state replay, with protocol-layer (Patchright fork) and source-layer (CloakBrowser) anti-detection | 2026-10-13 |

## document-processing

Tools for converting documents into structured, LLM-usable formats.

| Article | Summary | Updated |
|---------|---------|---------|
| [marker-pdf](wiki/document-processing/marker-pdf.md) | Fast PDF/DOCX/PPTX-to-Markdown/JSON converter with optional LLM-boosted accuracy | 2026-10-13 |
| [Docling](wiki/document-processing/docling.md) | IBM Research's broad-format (incl. audio/video/email/financial docs) document-to-structured-data framework, MIT licensed | 2026-10-13 |
| [PyMuPDF](wiki/document-processing/pymupdf.md) | Fast MuPDF-backed Python engine for PDF extraction, rendering, editing, OCR, and local LLM-ready Markdown/JSON output | 2026-09-30 |
| [newspaper](wiki/document-processing/newspaper.md) | Python article extractor for page text, metadata, authors, and images | 2026-08-18 |
| [LlamaIndex (run-llama)](wiki/document-processing/llamaindex.md) | Document processing platform for AI: cloud LlamaParse OCR/extract plus open-source LiteParse (Rust), LlamaAgents, and SDKs | 2026-09-17 |
| [Gotenberg](wiki/document-processing/gotenberg.md) | Docker-based HTTP API converting HTML/URL/Markdown/Office documents to PDF via Chromium and LibreOffice, plus PDF merge/split/watermark/encrypt and PDF/A, PDF/UA | 2026-10-13 |

## research-and-training

Autonomous research systems and speculative/fringe LLM technique proposals.

| Article | Summary | Updated |
|---------|---------|---------|
| [Autoresearch](wiki/research-and-training/autoresearch.md) | Overnight autonomous LLM-training experimentation on a single GPU with narrow agent write-access | 2026-07-11 |
| [The Guanyin Protocol: Semantic Anchoring](wiki/research-and-training/guanyin-protocol-semantic-anchoring.md) | [Quality-flagged] Self-published preprint proposing a coherence-improving prompt technique | 2026-07-11 |

## personal-finance

Self-hosted tools and catalogs for budgeting, bookkeeping, and personal money management.

| Article | Summary | Updated |
|---------|---------|---------|
| [Self-Hosted Budgeting and Personal Finance Apps](wiki/personal-finance/self-hosted-budgeting-apps.md) | Comparison of Budget Board, ezBookkeeping, Actual Budget, and the Awesome Selfhosted money-management catalog | 2026-10-10 |

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
| [ZeroTier](wiki/networking-tools/zerotier.md) | Software-defined networking platform with five pricing tiers from free personal use to defense-grade Quantum | 2026-10-13 |
| [pfSense](wiki/networking-tools/pfsense.md) | FreeBSD-based free network firewall distribution with a full web interface, package system, and commercial-firewall feature parity | 2026-10-13 |

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

General-purpose developer utilities and browser-based tools.

| Article | Summary | Updated |
|---------|---------|---------|
| [SQL Fiddle](wiki/dev-tools/sqlfiddle.md) | Web-based multi-dialect SQL playground for practicing and sharing queries | 2026-07-31 |
| [Mermaid Live Editor](wiki/dev-tools/mermaid-live-editor.md) | Online flowchart and diagram editor; fetched page exposed only the client-rendered title | 2026-10-05 |

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

Machine learning libraries, model formats, and applied classification patterns.

| Article | Summary | Updated |
|---------|---------|---------|
| [XGBoost](wiki/machine-learning/xgboost.md) | Optimized distributed gradient boosting library (GBDT) portable from laptop to Spark/Kubernetes scale | 2026-10-05 |
| [ONNX Model Zoo](wiki/machine-learning/onnx-model-zoo.md) | Deprecated curated ONNX model zoo whose durable contribution is the per-model validation contract (shipped test data + reference outputs), superseded for distribution by Hugging Face | 2026-10-01 |
| [XGBoost Imbalanced Classification Pattern](wiki/machine-learning/xgboost-imbalanced-classification-pattern.md) | Bank-marketing worked pattern: class weighting and resampling reaching 0.84 recall on imbalanced positives | 2026-08-24 |
| [Microsoft GUIDE Cybersecurity Incident Classification](wiki/machine-learning/cybersecurity-incident-classification.md) | XGBoost-centered pipeline classifying cybersecurity incidents with preprocessing, imbalance handling, tuning, and SHAP | 2026-10-05 |
| [Document Similarity Methods](wiki/machine-learning/document-similarity-methods.md) | Survey of cosine, Jaccard, Euclidean, Manhattan, and Levenshtein approaches for comparing documents | 2026-10-05 |
| [XGBoosting Dataset Catalog](wiki/machine-learning/xgboost-datasets.md) | Index of worked XGBoost examples using common academic, benchmark, and Kaggle datasets | 2026-10-05 |

## speech-recognition

Open-source speech-to-text models and AMD ROCm deployment recipes.

| Article | Summary | Updated |
|---------|---------|---------|
| [ROCm Whisper API](wiki/speech-recognition/rocm-whisper-api.md) | Dockerized Whisper HTTP service for AMD GPUs with ROCm device passthrough and configurable models | 2026-10-05 |
| [faster-whisper on AMD Strix Halo](wiki/speech-recognition/faster-whisper-rocm-strix-halo.md) | No-source-build ROCm recipe for faster-whisper on gfx1151 with reported English and Japanese benchmarks | 2026-10-05 |
| [VibeVoice-ASR with ROCm and Docker](wiki/speech-recognition/vibevoice-asr.md) | Community Docker deployment note for Microsoft VibeVoice-ASR on ROCm with AMD Flash Attention | 2026-10-05 |

## fact-checking

Evidence-led workflows and agent systems for evaluating claims and misinformation.

| Article | Summary | Updated |
|---------|---------|---------|
| [Fake News Detection Multi-Agent System](wiki/fact-checking/fake-news-detector-agent.md) | Orchestrator, search, and scoring agents combining Google Search MCP and Gemini for news authenticity estimates | 2026-10-05 |
| [Fact Check Skill](wiki/fact-checking/fact-check-skill.md) | Claude and Codex skill with source evaluation, risk scoring, structured schemas, validation, and HTML cards | 2026-10-05 |
| [Fact Checker Skill Listing](wiki/fact-checking/fact-checker-app-pattern.md) | Claim verification workflow with six ratings, source hierarchy, context checks, and manipulation-pattern detection | 2026-10-05 |

## speech-synthesis

Open-source text-to-speech models and voice synthesis tooling.

| Article | Summary | Updated |
|---------|---------|---------|
| [Chatterbox TTS](wiki/speech-synthesis/chatterbox-tts.md) | Resemble AI's open-source TTS family (110M Nano to 500M Multilingual V3), single-step decoder, paralinguistic tags, Perth watermarking | 2026-09-17 |

## self-hosted

Self-hosted file servers, dashboards, and service-catalog tools.

| Article | Summary | Updated |
|---------|---------|---------|
| [Compass](wiki/self-hosted/compass.md) | Apache-2.0 service-catalog landing page that auto-discovers services, dashboards, and documents from Docker, Kubernetes, Tailscale, Headscale, static config, and a JSON API | 2026-10-16 |
| [copyparty](wiki/self-hosted/copyparty.md) | Single-file portable Python file server (47.1k stars) speaking HTTP/WebDAV/SFTP/FTP/TFTP/SMB, with resumable uploads, dedup, media indexing, thumbnails, and a browser file manager | 2026-10-16 |

## people

Profiles of individual developers and maintainers whose projects appear elsewhere in the wiki.

| Article | Summary | Updated |
|---------|---------|---------|
| [Felix Rieseberg](wiki/people/felix-rieseberg.md) | Engineer on Claude at Anthropic, Electron co-maintainer; author of windows95, macintosh.js, Clippy, Electron Fiddle, and claude-coach | 2026-10-16 |

## data-privacy

Privacy-preserving and de-identification tooling for AI and data workflows.

| Article | Summary | Updated |
|---------|---------|---------|
| [Data Privacy Stack (Presidio)](wiki/data-privacy/data-privacy-stack.md) | GitHub org for AI-native privacy tooling; flagship Presidio is an MIT Python framework for detecting, redacting, and anonymizing PII across text, images, and structured data | 2026-10-16 |
