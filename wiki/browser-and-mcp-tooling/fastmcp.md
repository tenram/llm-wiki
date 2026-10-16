# FastMCP

> Sources: Prefect, Unknown date
> Raw: [FastMCP (PrefectHQ)](../../raw/browser-and-mcp-tooling/2026-10-16-fastmcp.md)

## Overview

FastMCP (Apache-2.0, ~28.1k stars) is Prefect's Python framework for building MCP servers and clients. It bills itself as "the fast, Pythonic way to build MCP servers and clients," and claims a large installed base: FastMCP 1.0 was incorporated into the official MCP Python SDK in 2024, the standalone project is downloaded about a million times a day, and "some version of FastMCP powers 70% of MCP servers across all languages." It is the standard application-layer framework for the protocol catalogued in [Model Context Protocol Overview](model-context-protocol-overview.md).

## Three Pillars

- **Servers** — wrap ordinary Python functions into MCP-compliant tools, resources, and prompts. Schema, validation, and documentation are generated from type hints and docstrings.
- **Clients** — connect to any MCP server (local or remote, programmatic or CLI) with transport negotiation, authentication, and protocol lifecycle handled by the framework.
- **Apps** — give tools interactive UIs rendered directly in the conversation.

A server is a few lines:

```python
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

A TypeScript counterpart (github.com/PrefectHQ/fastmcp-ts) is maintained by the same team (`npm install @prefecthq/fastmcp-ts`).

## Enterprise Gateway: Prefect Horizon

FastMCP handles the MCP application layer; **Prefect Horizon** is Prefect's enterprise MCP gateway for scaling servers and tools across teams with centralized governance — deploying FastMCP servers from GitHub with branch previews and instant rollback, a private registry of a company's MCPs, SSO and tool-level RBAC, audit logs and observability, and remixing approved tools into purpose-built endpoints. This is the same "gateway layer above the protocol" pattern that [AnythingMCP (HelpCode)](helpcode-anythingmcp.md) implements by generating MCP servers from existing APIs.

## Installation and Upgrades

Recommended via `uv add fastmcp`. Documentation lives at gofastmcp.com and is also published in llms.txt format (`llms.txt` sitemap, `llms-full.txt` full text). The project ships explicit upgrade guides from FastMCP 3 and 2, from MCP SDK v1/v2, and from the low-level SDK v1/v2 — a sign of how much the underlying protocol SDKs have churned.

## Repository Notes

The repo splits into `fastmcp_remote`, `fastmcp_slim`, and `fastmcp_tasks` packages, and ships agent-facing skills under `.agents/skills` and `skills/fastmcp-client-cli` — the framework is itself packaged for coding agents to consume.

## See Also

- [Model Context Protocol Overview](model-context-protocol-overview.md) — the protocol this framework implements.
- [AnythingMCP (HelpCode)](helpcode-anythingmcp.md) — a self-hosted MCP gateway that generates servers from existing APIs/databases.
- [MCP Reference Servers](mcp-reference-servers.md) — steering-group-maintained reference server implementations.
