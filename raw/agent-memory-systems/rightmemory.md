# RightMemory

> Source: https://github.com/RightL/RightMemory
> Collected: 2026-07-11
> Published: Unknown

"Tree + graph memory for teams of AI coding agents": a structured memory system persisting context across sessions, devices, and agent clients. Uses a hierarchical, markdown-based heading tree (#, ##, ###) for local context organization, plus graph-connected facts via typed edges (dep, cfg, ver, doc, todo, etc.) linking related information across sections.

Supports multi-device continuity (same memory follows agents across laptops/desktops/different clients, git-synced) and shared views for controlled collaboration through mirrored files (MF#) and provider questions (MQ#). Defines role-based operations: separate agent roles for retrieve, update, consolidation ("dreamer"), and reflection ("insight"), keeping main-agent work separate from memory-management operations.

Command-driven, vendor-neutral CLI interface compatible with Codex, Claude Code, and other command-capable agents. Two execution modes: Standalone (runs its own Pydantic AI agents locally) and CLI-Agent (delegates role execution to Codex CLI or Claude Code CLI); both share the same memory schema and command interface.

Notable claims: memory is file-based, inspectable, and deterministic (not opaque embeddings); explicit consolidation and reflection cycles are used to prevent memory drift.
