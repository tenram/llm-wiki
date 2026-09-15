# Agent Reach

> Sources: Agent Reach README, 2026-08-28
> Raw: [agent-reach.md](../../raw/browser-and-mcp-tooling/agent-reach.md)

## Overview

Agent Reach is a Python-based capability layer that gives AI agents internet access by selecting, installing, and routing the best available backend for each channel. It is designed for use by command-line agents and emphasizes diagnostics, fallback routing, and login-aware support for sites that resist simple API access.

## Channel Routing Model

The repo treats each platform as a channel with a ranked backend chain. Examples include:

- web → Jina Reader
- YouTube → yt-dlp
- GitHub → gh CLI
- RSS → feedparser
- search → Exa via mcporter
- Twitter/X, Reddit, Facebook, Instagram, LinkedIn, Xiaohongshu → login-aware or MCP-backed routes

The important idea is not a single scraper per site, but a changing best-path list that `agent-reach doctor` can inspect.

## Installation and Safety

The project is opinionated about safety:

- default installs are read-only checks
- `--dry-run` previews changes
- credentials stay local
- risky channels are explicit opt-ins

That makes it more of an agent ops layer than a crawler library.

## Why It Matters

Agent Reach packages the practical work of making an agent useful on the live web: choosing the right tool, handling login state, keeping routes current, and failing over when one backend stops working.

## See Also

- [Firecrawl](firecrawl.md)
- [Playwright MCP](playwright-mcp.md)
- [Model Context Protocol Overview](model-context-protocol-overview.md)
