# Firecrawl (2026-10-13 README)

> Source: https://github.com/firecrawl/firecrawl
> Collected: 2026-10-13
> Published: Unknown

# Firecrawl

**Supercharge your AI agents with data from the web and beyond. Building the library for superintelligence.** Open source and available as a hosted service (firecrawl.dev).

## Why Firecrawl?

- **Industry-leading reliability**: Covers 96% of the web, including JS-heavy pages — no proxy headaches, just clean data
- **Blazingly fast**: P95 latency of 3.4s across millions of pages, built for real-time agents and dynamic apps
- **LLM-ready output**: Clean markdown, structured JSON, screenshots, and more — spend fewer tokens, build better AI apps
- **We handle the hard stuff**: Rotating proxies, orchestration, rate limits, JS-blocked content, and more — zero configuration
- **Agent ready**: Connect Firecrawl to any AI agent or MCP client with a single command
- **Media parsing**: Parse and extract content from web-hosted PDFs, DOCX, and more
- **Actions**: Click, scroll, write, wait, and press before extracting content
- **Open source**: Developed transparently and collaboratively

## Feature Overview

### Core Endpoints

| Feature | Description |
|---------|-------------|
| Search | Search the web and get full page content from results |
| Scrape | Convert any URL to markdown, HTML, screenshots, or structured JSON |
| Interact | Scrape a page, then interact with it using AI prompts or code |

### More

| Feature | Description |
|---------|-------------|
| Agent | Automated data gathering, just describe what you need |
| Crawl | Scrape all URLs of a website with a single request |
| Map | Discover all URLs on a website instantly |
| Batch Scrape | Scrape thousands of URLs asynchronously |

## Agent endpoint

**The easiest way to get data from the web.** Describe what you need, and the AI agent searches, navigates, and retrieves it. No URLs required. Agent is the evolution of the `/extract` endpoint: faster, more reliable, and doesn't require you to know the URLs upfront.

- Accepts a prompt (`https://api.firecrawl.dev/v2/agent`); returns a result plus cited sources.
- Structured output via a schema (e.g., Pydantic in Python).
- Optional URL focus: pass `urls` to focus the agent on specific pages.
- Effort selection: `low` (simple lookups on one site), `medium` (multi-step tasks on a few pages), `high` (deep research, complex navigation, critical data).
- Every effort level runs the `spark-2` model. Effort changes the reasoning budget, not the model. Deprecated `spark-1-pro` and `spark-1-mini` names still accepted, run `spark-2`.

## Crawl

Crawl an entire website (`POST https://api.firecrawl.dev/v2/crawl`), returns a job ID; poll `GET /v2/crawl/{id}` for status and per-page markdown. SDKs handle polling automatically.

## Map

Discover all URLs on a website instantly (`POST https://api.firecrawl.dev/v2/map`), returns URL+title+description. Map with search returns URLs ordered by relevance.

## SDKs

Python (`pip install firecrawl-py`), Node.js (`npm install firecrawl`), Go, Java, Elixir, Rust, Ruby, .NET, PHP.

## Power Your Agent

- **Skill**: `npx -y firecrawl-cli@latest init --all --browser`; works with Claude Code, Antigravity, OpenCode, and more.
- **MCP**: `firecrawl-mcp` (npx, with `FIRECRAWL_API_KEY` env).
- **Agent onboarding**: `curl https://firecrawl.dev/agent-onboarding/SKILL.md`.

## Integrations

- Agents & AI tools: Firecrawl Skills Catalog (github.com/firecrawl/skills), Firecrawl CLI, Firecrawl MCP (github.com/mendableai/firecrawl-mcp-server).
- Platforms: Lovable, Zapier, n8n.

## Open Source vs Cloud

Firecrawl is open source under AGPL-3.0. The cloud version adds additional features. To self-host, see the Self-Hosting Guide.

## License

Primarily AGPL-3.0. The SDKs and some UI components are licensed under MIT.

Note: it is the sole responsibility of end users to respect websites' policies when scraping. By default, Firecrawl respects robots.txt directives.
