# Open Brain (OB1)

> Sources: https://github.com/NateBJones-Projects/OB1; https://lobehub.com/pl/mcp/shawnsammartano-hub-ob1-local-stack
> Collected: 2026-08-18
> Published: Unknown

A self-hosted infrastructure project providing a unified memory layer for AI interactions, combining a database, AI gateway, and chat interface so multiple AI tools can share persistent memory without external middleware or SaaS dependencies. The shared theme is: one database, one gateway, one chat channel.

Architecture centers on PostgreSQL with pgvector for vector search; deployment can run through Supabase or self-hosted Kubernetes; an MCP server handles AI-tool integration; edge functions process workflows; frontend dashboard options include SvelteKit or Next.js.

Primary features include vector semantic search over stored thoughts and memories, multi-user isolation via row-level security, auto-capture integrations, data-import recipes, and an extensible skill system for common workflows.

The LobeHub local-stack source shows OB1 packaged as a runnable MCP-oriented stack, not just a standalone repo.
