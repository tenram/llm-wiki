# GoDaddy gddy Agent Skill

> Sources: GoDaddy, Unknown date
> Raw: [Agent skill for gddy](../../raw/dev-tools/2026-11-21-godaddy-gddy-agent-skill.md)

## Overview

GoDaddy’s `gddy` agent skill teaches compatible coding agents to install and operate the GoDaddy CLI through natural-language requests. The CLI can search domains, check pricing, register domains, and manage DNS using the user’s authenticated session.

## Safety Model

The source distinguishes installation from the actions the CLI can perform. Domain purchases require a quote-then-purchase flow and confirmation because they spend real money. DNS set and delete operations can replace or remove matching records, so the skill uses `--dry-run` before applying them. The agent should check `gddy auth status` when account or environment identity is uncertain.

## Practical Takeaway

This is a useful pattern for agent-operated infrastructure CLIs: keep authentication in the CLI, expose self-documentation, preview destructive mutations, and require confirmation for irreversible or paid actions. The skill itself does not make DNS or purchase actions safe without those gates being followed.

## See Also

- [Agent Skills Platform](../ai-agent-harnesses/agent-skills-platform.md)
- [OpenCode + Cloudflare](../ai-agent-harnesses/cloudflare-opencode.md)
