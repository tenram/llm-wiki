# Playwright MCP

> Sources: Microsoft, Unknown date
> Raw: [Playwright MCP](../../raw/browser-and-mcp-tooling/playwright-mcp.md)

## Overview

An MCP server exposing [Playwright](playwright.md) browser automation to LLMs via structured accessibility snapshots rather than screenshots, so no vision model is required. Distinguished by Microsoft from a separate "Playwright CLI + SKILLS" offering: CLI+SKILLS is more token-efficient for high-throughput coding agents (skips loading large tool schemas), while MCP suits agentic loops needing persistent state and iterative introspection (exploratory automation, self-healing tests, long-running workflows).

## Configuration

Runs via `npx @playwright/mcp@latest`; supports numerous browsers/engines, headless/headed modes, device emulation, persistent or isolated sessions, origin allow/block-listing, proxy configuration, and Docker deployment (headless Chromium only). Tool set includes `browser_click`, `browser_evaluate`, `browser_fill_form`, `browser_file_upload`, and more, each flagged read-only or mutating. The README explicitly states "Playwright MCP is not a security boundary."

## See Also

- [Playwright](playwright.md)
- [Model Context Protocol Overview](model-context-protocol-overview.md)
