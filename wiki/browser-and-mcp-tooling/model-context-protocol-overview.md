# Model Context Protocol (MCP)

> Sources: Anthropic / MCP steering group, Unknown date; MCP docs, 2026-07-28; Anthropic support, Unknown date
> Raw: [What is the Model Context Protocol (MCP)?](../../raw/browser-and-mcp-tooling/model-context-protocol-overview.md); [MCP intro (2026-07-28 revision)](../../raw/browser-and-mcp-tooling/2026-07-31-mcp-getting-started-intro.md); [Local MCP Servers on Claude Desktop](../../raw/browser-and-mcp-tooling/local-mcp-servers-claude-desktop.md)

## Overview

An open standard for connecting AI applications to external systems: data sources, tools, and workflows, described with the analogy "MCP is like a USB-C port for AI applications." Aims to let developers "build once and integrate everywhere" instead of writing custom integrations per data source per AI app.

## Value Proposition

For developers: less integration work per external system. For AI applications/agents: access to a growing ecosystem of pre-built connectors. For end users: assistants that can actually reach their data and take action, not just talk about it. Supported clients cited include Claude, ChatGPT, VS Code, Cursor, and MCPJam.

Concrete reference servers and SDKs are catalogued in [MCP Reference Servers](mcp-reference-servers.md); browser automation over MCP is implemented by [Playwright MCP](playwright-mcp.md). Multi-model code review over MCP is implemented by [Deliberation](deliberation-mcp.md).

## Getting Started (2026-07-28 docs)

The current onboarding docs route builders to three concrete paths — build a server, build a client, or build an MCP App (an interactive app running inside an AI client) — plus a core-concepts/architecture page, replacing what had been a single introductory page.

## Local Setup on Claude Desktop

On Claude Desktop specifically, MCP servers install as single-click "desktop extensions" (`.mcpb` files) rather than manual JSON config: browse Anthropic-reviewed extensions under Settings > Extensions, or install a custom `.mcpb` via Advanced settings > Extension Developer. Claude Desktop ships a built-in Node.js runtime and supports Node.js, Python, and binary servers; sensitive config fields are encrypted via the OS credential store.

## See Also

- [MCP Reference Servers](mcp-reference-servers.md)
- [Playwright MCP](playwright-mcp.md)
- [Deliberation](deliberation-mcp.md)
