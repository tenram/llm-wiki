# Open Brain (OB1)

> Sources: NateBJones-Projects, Unknown date; LobeHub OB1 local stack, Unknown date
> Raw: [Open Brain (OB1)](../../raw/agent-memory-systems/ob1.md)

## Overview

A self-hosted unified memory layer meant to let multiple AI tools (Claude, ChatGPT, Cursor) share one persistent memory store without SaaS middleware. Tagline: "One database, one AI gateway, one chat channel."

## Architecture

PostgreSQL with pgvector for vector-based semantic search, deployable via Supabase or self-hosted Kubernetes; an MCP server for tool integration; edge functions for processing; a SvelteKit or Next.js dashboard. Features multi-user isolation via row-level security, auto-capture from Slack/Discord, and import recipes from ChatGPT, Perplexity, Obsidian, Gmail, and social platforms.

Unlike [RightMemory](rightmemory.md)'s deterministic, file-based, non-embedding approach, OB1 is explicitly vector/embedding-centric. Onboarding is a documented 45-minute setup; contributions (recipes, skills, schemas) go through a structured review pipeline. License: FSL-1.1-MIT.

The LobeHub local-stack listing shows OB1 as a packaged deployment surface for local use.

## See Also

- [RightMemory](rightmemory.md)
- [HybridRAG System](hybridrag-system.md)
