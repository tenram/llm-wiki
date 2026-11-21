# OpenCode + Cloudflare

> Sources: Cloudflare, 2026-10-14
> Raw: [OpenCode + Cloudflare](../../raw/ai-agent-harnesses/2026-11-21-cloudflare-opencode.md)

## Overview

Cloudflare’s OpenCode guide combines the OpenCode terminal agent with Cloudflare Skills, MCP servers, and Wrangler or the Cloudflare CLI. The recommended setup installs OpenCode, adds the Cloudflare skill bundle, configures the remote Cloudflare MCP server in `.opencode.jsonc`, and starts OpenCode from the project root.

## Tooling Layers

Skills provide durable platform guidance and route work across products. MCP supplies typed or code-mode access to Cloudflare APIs and focused services. Wrangler handles Workers development and deployment, while the beta `cf` CLI covers the broader public API and prints JSON. Agent-friendly docs expose `llms.txt` indexes and page-level Markdown for lower-context retrieval.

## Practical Takeaway

The guide illustrates a layered agent integration rather than a single plugin: persistent product knowledge, a bounded API surface, local development tooling, and documentation optimized for agents. OAuth and account permissions remain real trust boundaries; configure only the servers and scopes needed for the task.

## See Also

- [Harness Design Principles](harness-design-principles.md)
- [Agent Skills Platform](agent-skills-platform.md)
- [OpenCode Orchestration](../opencode-ecosystem/opencode-orchestration.md)
