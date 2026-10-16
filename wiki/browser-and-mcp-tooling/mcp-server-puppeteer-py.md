# Puppeteer MCP Server (Python)

> Sources: Todd Wolven, Unknown date
> Raw: [Puppeteer MCP Server (Python) README](../../raw/browser-and-mcp-tooling/2026-10-13-mcp-server-puppeteer-py.md)

## Overview

A Python MCP server providing browser automation via [Playwright](playwright.md) (Python's equivalent to Puppeteer), enabling LLMs to navigate pages, take screenshots, click/fill forms, and execute JavaScript in a real browser. It is a Python-native alternative to the TypeScript Puppeteer MCP server, positioning itself as more stable with improved error handling and logging. Apache 2.0 licensed, by Todd Wolven.

## Tools

- `puppeteer_navigate` — navigate to a URL (timeout configurable, default 60s)
- `puppeteer_screenshot` — capture full-page or element screenshots (1280x720 default viewport; stored in memory as base64)
- `puppeteer_click` / `puppeteer_fill` — interact with elements by CSS selector
- `puppeteer_evaluate` — execute JavaScript in the browser console

Console logs are captured and stored; error handling covers navigation failures, missing elements, timeouts, and JS execution errors. Browser launches in non-headless mode for debugging.

## Setup

Requires Python 3.8+ and pip; install Playwright browsers via `playwright install`. Run `python puppeteer_server.py` or register it as an MCP server in Claude Desktop config (`python path/to/puppeteer.py`).

## See Also

- [Playwright MCP](playwright-mcp.md) — the official, far larger Microsoft Playwright MCP (70+ tools, accessibility-snapshot based).
- [Playwright](playwright.md) — the underlying automation library.
