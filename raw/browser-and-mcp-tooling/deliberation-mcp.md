# Deliberation (MCP server for multi-model consultation)

> Source: https://github.com/antonbabenko/deliberation
> Collected: 2026-07-31
> Published: Unknown

Deliberation is an MCP server that lets Claude Code and other AI development environments consult multiple AI models as domain experts during coding tasks, addressing the risk that a single model misses bugs or architectural issues a second model would catch.

## Architecture

- Seven specialized expert personas — Architect, Code Reviewer, Security Analyst, Debugger, Researcher, Plan Reviewer, Scope Analyst — auto-routed based on the request
- Consults GPT, Gemini, Grok, and 400+ OpenRouter models (Qwen, Kimi, DeepSeek, etc.)
- Models operate in advisory (read-only analysis) or implementation (workspace-write) mode
- Supported hosts: Claude Code (recommended), plus a standalone MCP server for Cursor, Codex CLI, Kiro, VS Code, and OpenCode

## Consensus Mode

The `/consensus` command runs a multi-round convergence loop with bias guards:
1. Claude commits a "blind verdict" before seeing external model opinions
2. External models review independently and vote
3. Claude arbitrates disagreements with required reasoning
4. Loop continues until consensus or max rounds

Session analytics track "which models earn their seat," helping teams identify their most reliable external reviewers. Setup is one-time via `/deliberation:setup`, with three installation paths: Claude Code plugin, standalone MCP server, or native host integrations.
