# Playwright MCP

> Source: https://github.com/microsoft/playwright-mcp
> Collected: 2026-07-11
> Published: Unknown

A Model Context Protocol server providing browser automation via Playwright, enabling LLMs to interact with web pages "through structured accessibility snapshots, bypassing the need for screenshots or visually-tuned models."

The README distinguishes Playwright MCP from a separate "Playwright CLI + SKILLS" offering: CLI+SKILLS is more token-efficient for high-throughput coding agents (avoids loading large tool schemas/accessibility trees), while MCP suits specialized agentic loops needing persistent state, rich introspection, and iterative reasoning (exploratory automation, self-healing tests, long-running autonomous workflows).

Key features: fast/lightweight (accessibility tree, not pixel input); LLM-friendly (no vision model required); deterministic tool application.

Requirements: Node.js 18+, any MCP client (VS Code, Cursor, Windsurf, Claude Desktop, Goose, Grok, Junie, etc.). Standard install via `npx @playwright/mcp@latest`, with setup snippets for Amp, Antigravity, Claude Code, Claude Desktop, Cline, Codex, Copilot, Cursor, and more.

Configuration: `--browser` (chrome/firefox/webkit/msedge), `--caps` (vision, pdf, devtools), `--cdp-endpoint`, `--device`/`--mobile` emulation, `--headless`, `--isolated`, `--storage-state`, `--extension` (connect to a running Chrome/Edge tab), `--allowed-hosts`/`--allowed-origins`/`--blocked-origins`, `--proxy-server`, `--init-page`/`--init-script`, `--output-dir`/`--output-mode`, `--port` (SSE transport), and a JSON config-file schema. Supports persistent user profiles or isolated in-memory sessions.

Docker support: `mcr.microsoft.com/playwright/mcp` image (headless Chromium only currently). Explicitly states "Playwright MCP is not a security boundary." Tools include `browser_click`, `browser_close`, `browser_console_messages`, `browser_drag`, `browser_drop`, `browser_evaluate`, `browser_file_upload`, `browser_fill_form`, and more, each with a read-only/mutating flag.
