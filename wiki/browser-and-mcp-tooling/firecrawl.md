# Firecrawl

> Sources: Firecrawl README, 2026-08-28; Firecrawl README, 2026-10-13
> Raw: [firecrawl.md](../../raw/browser-and-mcp-tooling/firecrawl.md); [Firecrawl README (2026-10-13 snapshot)](../../raw/browser-and-mcp-tooling/2026-10-13-firecrawl.md)

## Overview

Firecrawl is a web context API for agents: it searches, scrapes, interacts with, crawls, and maps websites, then returns LLM-friendly Markdown, JSON, screenshots, or structured data. It ships with SDKs, CLI workflows, and an MCP surface for plugging web access into agent stacks. Reliability claims: covers 96% of the web (incl. JS-heavy pages) with P95 latency of 3.4s across millions of pages.

## Core Capabilities

- **Search**: find pages and return full content from results
- **Scrape**: convert URLs into markdown, HTML, screenshots, or JSON
- **Interact**: click, scroll, write, wait, and navigate before extracting
- **Agent**: describe the task and let the service gather data
- **Crawl**: fetch a site across many URLs asynchronously (job-based, SDKs poll automatically)
- **Map**: discover the URL surface of a site, optionally ordered by search relevance
- **Batch Scrape**: process many URLs at once

## Agent Endpoint

The `Agent` endpoint (the evolution of `/extract`) takes a prompt with no URLs required, and returns a result with cited sources. Supports structured output via a schema, optional URL focus, and effort selection (`low`/`medium`/`high`) that changes the reasoning budget — every effort level runs the `spark-2` model (deprecated `spark-1-*` names still accepted).

## Agent and Developer Integration

The repo emphasizes direct use from agents and developer tools:

- a Firecrawl CLI skill for agent onboarding (`npx -y firecrawl-cli@latest init --all --browser`; works with Claude Code, Antigravity, OpenCode)
- an MCP server (`firecrawl-mcp`) for web access inside MCP clients
- SDKs across Python, Node.js, Go, Java, Elixir, Rust, Ruby, .NET, and PHP
- platform integrations with Lovable, Zapier, and n8n

That makes it useful as a web-data layer for RAG pipelines, research agents, and browser-assisted workflows.

## Operating Model

Firecrawl splits into a hosted web API and an open-source self-hosted stack (AGPL-3.0; SDKs and some UI under MIT). The README positions the hosted service as the easiest path, while the repo includes the code and integration points for local use and contribution.

## See Also

- [Anysite MCP](anysite-mcp.md) — hosted MCP server for structured web data (LinkedIn, Reddit, etc.), a comparable web-data-as-a-service surface.
- [Playwright](playwright.md)
- [Playwright MCP](playwright-mcp.md)
- [Model Context Protocol Overview](model-context-protocol-overview.md)
