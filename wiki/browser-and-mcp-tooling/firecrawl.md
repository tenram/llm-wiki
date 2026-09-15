# Firecrawl

> Sources: Firecrawl README, 2026-08-28
> Raw: [firecrawl.md](../../raw/browser-and-mcp-tooling/firecrawl.md)

## Overview

Firecrawl is a web context API for agents: it searches, scrapes, interacts with, crawls, and maps websites, then returns LLM-friendly Markdown, JSON, screenshots, or structured data. It ships with SDKs, CLI workflows, and an MCP surface for plugging web access into agent stacks.

## Core Capabilities

- **Search**: find pages and return full content from results
- **Scrape**: convert URLs into markdown, HTML, screenshots, or JSON
- **Interact**: click, scroll, write, wait, and navigate before extracting
- **Agent**: describe the task and let the service gather data
- **Crawl**: fetch a site across many URLs asynchronously
- **Map**: discover the URL surface of a site
- **Batch Scrape**: process many URLs at once

## Agent and Developer Integration

The repo emphasizes direct use from agents and developer tools:

- a Firecrawl CLI skill for agent onboarding
- an MCP server for web access inside MCP clients
- SDKs across Python, Node.js, Go, Java, Elixir, Rust, Ruby, .NET, and PHP

That makes it useful as a web-data layer for RAG pipelines, research agents, and browser-assisted workflows.

## Operating Model

Firecrawl splits into a hosted web API and an open-source self-hosted stack. The README positions the hosted service as the easiest path, while the repo includes the code and integration points for local use and contribution.

## See Also

- [Playwright](playwright.md)
- [Playwright MCP](playwright-mcp.md)
- [Model Context Protocol Overview](model-context-protocol-overview.md)
