# Model Context Protocol servers (modelcontextprotocol/servers)

> Source: https://github.com/modelcontextprotocol/servers
> Collected: 2026-07-11
> Published: Unknown

A collection of reference implementations for MCP plus references to community-built servers and resources. For a full list of published MCP servers, the repo points to the official MCP Registry (registry.modelcontextprotocol.io); this repo holds only the small set of reference servers maintained by the MCP steering group. Warning: these are educational reference implementations, not production-ready solutions.

SDKs referenced (10 languages): C#, Go, Java, Kotlin, PHP, Python, Ruby, Rust, Swift, TypeScript.

Active reference servers (7): Everything (test server with prompts/resources/tools), Fetch (web content fetching/conversion), Filesystem (secure file operations with configurable access controls), Git (read/search/manipulate git repos), Memory (knowledge-graph-based persistent memory), Sequential Thinking (dynamic/reflective problem-solving via thought sequences), Time (time/timezone conversion).

Archived servers (moved to `servers-archived`): AWS KB Retrieval, Brave Search (replaced by an official server), EverArt, GitHub, GitLab, Google Drive, Google Maps, PostgreSQL, Puppeteer, Redis, Sentry, Slack (now maintained by Zencoder), SQLite.

Usage: TypeScript servers run via `npx` (e.g. `npx -y @modelcontextprotocol/server-memory`); Python servers via `uvx` or `pip` (e.g. `uvx mcp-server-git`). Includes example Claude Desktop client JSON configs for memory, filesystem, git, github, and postgres servers.

License: Apache License 2.0 for new contributions, existing code under MIT. Repo stats: TypeScript 70.7%, Python 18.0%, JavaScript 10.2%; 88.3k GitHub stars; 4,138 commits. Tagline: "Managed by Anthropic, but built together with the community."
