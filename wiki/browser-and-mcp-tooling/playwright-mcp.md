# Playwright MCP

> Sources: Microsoft, Unknown date; Playwright official docs, Unknown date
> Raw: [Playwright MCP](../../raw/browser-and-mcp-tooling/playwright-mcp.md); [Playwright MCP official docs (2026-10-13 snapshot)](../../raw/browser-and-mcp-tooling/2026-10-13-playwright-mcp-docs.md)

## Overview

An MCP server exposing [Playwright](playwright.md) browser automation to LLMs via structured accessibility snapshots rather than screenshots, so no vision model is required. Distinguished by Microsoft from a separate "Playwright CLI + SKILLS" offering: CLI+SKILLS is more token-efficient for high-throughput coding agents (skips loading large tool schemas), while MCP suits agentic loops needing persistent state and iterative introspection (exploratory automation, self-healing tests, long-running workflows).

## Key Features

- **Snapshot-based** — operates on the accessibility tree, not pixels; each element gets a unique ref (e.g., `e5`) for deterministic interaction. The LLM reads the snapshot and passes refs as the `target` of the next tool call — no screenshot or coordinate guessing.
- **LLM-friendly** — structured text output that LLMs parse naturally, cheaper than DOM dumps or screenshots.
- **Cross-browser** — Chrome, Firefox, WebKit, and Edge.
- **Full automation** — 70+ tools covering navigation, forms, network mocking, storage, tracing, video, and more.
- **Persistent sessions** — login state and cookies preserved between sessions by default.
- **Works everywhere** — VS Code, Cursor, Windsurf, Claude Code, Claude Desktop, and any MCP client. Browser opens in headed mode by default.

## Configuration

Runs via `npx @playwright/mcp@latest`; supports numerous browsers/engines, headless/headed modes, device emulation, persistent or isolated sessions, origin allow/block-listing, proxy configuration, and Docker deployment (headless Chromium only). Tool set is grouped by capability flags (`--caps`): core tools are always enabled; `network`, `storage`, `testing`, `devtools`, `pdf`, `vision`, and `config` groups add tools such as `browser_route` (network mocking), cookie/localStorage management, locator generation and visibility assertions, tracing/video recording, `browser_pdf_save`, coordinate-based mouse tools, and `browser_get_config`. The README explicitly states "Playwright MCP is not a security boundary."

## See Also

- [Playwright](playwright.md)
- [Puppeteer MCP Server (Python)](mcp-server-puppeteer-py.md) — community Playwright-based browser-automation MCP server, simpler and Python-native.
- [Model Context Protocol Overview](model-context-protocol-overview.md)
