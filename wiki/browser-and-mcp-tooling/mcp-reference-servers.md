# MCP Reference Servers

> Sources: Anthropic / MCP steering group, Unknown date
> Raw: [Model Context Protocol servers](../../raw/browser-and-mcp-tooling/mcp-reference-servers.md)

## Overview

The official `modelcontextprotocol/servers` repo holds a small, steering-group-maintained set of reference MCP server implementations, explicitly framed as educational, not production-ready. The full ecosystem of published servers instead lives in the separate MCP Registry (registry.modelcontextprotocol.io).

## Active Reference Servers

Everything (test server), Fetch (web content fetching/conversion), Filesystem (secure file ops with configurable access control), Git, Memory (knowledge-graph-based persistent memory), Sequential Thinking, and Time. Several previously-listed servers (GitHub, GitLab, Slack, PostgreSQL, Redis, Puppeteer, Google Drive/Maps, Sentry) have been archived, some superseded by official vendor-maintained servers.

SDKs exist for 10 languages (C#, Go, Java, Kotlin, PHP, Python, Ruby, Rust, Swift, TypeScript). License: Apache 2.0 for new contributions.

## See Also

- [Model Context Protocol Overview](model-context-protocol-overview.md)
- [Playwright MCP](playwright-mcp.md)
