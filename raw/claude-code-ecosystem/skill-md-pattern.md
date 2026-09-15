# The SKILL.md Pattern: How to Write AI Agent Skills That Actually Work

> Source: https://bibek-poudel.medium.com/the-skill-md-pattern-how-to-write-ai-agent-skills-that-actually-work-72a3169dd7ee
> Collected: 2026-07-31
> Published: Unknown

SKILL.md is described as an open standard for reusable, agent-loadable instruction packages that activate automatically on matching requests. Core claim: "If your skill does not trigger, it is almost never the instructions. It is the description."

## Progressive disclosure architecture

Three-level loading system to minimize context overhead:
1. **Metadata** — only `name`/`description` load at startup
2. **Instructions** — full `SKILL.md` body loads once the skill triggers
3. **Resources** — referenced files (`scripts/`, `references/`, `assets/`) load on demand during execution

## Description as trigger

The `description` field determines activation; it must state both what the skill does and specific trigger phrases users might use, not just general capabilities.

## Folder structure

Minimal skill needs only `SKILL.md`. Optional: `scripts/` (executable code), `references/` (supporting docs), `assets/` (templates).

## Examples covered

Four progressively complex skills: a README writer, a git commit generator, a code reviewer with separate reference files, and a Linear sprint planner using MCP integration.

## Cross-platform note

"A skill that works on Claude Code will very likely work on Codex, but runtime behaviors ... differ between platforms" — skills are portable, but platform-specific implementations still matter.
