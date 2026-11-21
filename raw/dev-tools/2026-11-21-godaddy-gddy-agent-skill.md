# Agent skill for gddy

> Source: https://developer.godaddy.com/en/docs/api-users/cli/agent-skill
> Collected: 2026-11-21
> Published: Unknown

Title: Agent skill for gddy

URL Source: http://developer.godaddy.com/en/docs/api-users/cli/agent-skill

Final URL: https://developer.godaddy.com/en/docs/api-users/cli/agent-skill

Markdown Content:
[View as Markdown](https://developer.godaddy.com/llms.mdx/api-users/cli/agent-skill "View this page as plain markdown for LLM use")

Install the gddy agent skill so Claude Code or another AI coding agent can drive the GoDaddy CLI for you.

The `gddy` agent skill helps an AI coding agent install and use the [`gddy` CLI](https://developer.godaddy.com/docs/api-users/cli/set-up) on your behalf. Installing the skill is a one-time setup. After it's in place, describe what you want in plain language — find a domain, check pricing, register it, or update DNS records — and your agent runs the actual `gddy` commands using your own authenticated session.

After you install the skill, you can ask your agent things like:

*   "Set up `gddy` for me." (installs the CLI; you're prompted to log in automatically the first time a command needs it)
*   "Find available domains for a coffee subscription startup."
*   "Is `example.com` available, and what would it cost to register?"
*   "Add a CNAME record for `www` on `example.com` pointing to `example.github.io`."
*   "List the DNS records on `example.com`."

Your agent will run the equivalent `gddy` commands, parse the JSON output, and summarize the result. It also knows how to use the CLI's self-documentation to stay current as `gddy` evolves (`gddy --help`, `gddy search <keywords>`, `gddy tree`, and `gddy guide`).

The skill can purchase domains and modify DNS records if you ask it to. These guardrails apply when it does:

*   Domain purchase is real money and not reversible. The skill walks through the quote-then-purchase flow and confirms with you before finalizing a purchase.
*   `gddy dns set` and `gddy dns delete` are destructive — they replace or remove every matching record. The skill runs these with `--dry-run` first and shows you the change before applying it.
*   The skill acts with whatever credentials and environment your `gddy` CLI is authenticated against. Check with `gddy auth status` if you're unsure which account or environment your agent is operating on.

Skill vs. MCP server

This skill is not the same as the [GoDaddy MCP server](https://developer.godaddy.com/docs/api-users/mcp). The MCP server is a hosted, read-only service anyone can connect to for domain search and availability. The agent skill helps your coding agent install and run `gddy` itself, so it can do everything the CLI can do (including domain purchase and DNS management) using your own credentials. Go to [About the GoDaddy CLI](https://developer.godaddy.com/docs/api-users/cli#cli-agent-skill-mcp-server-and-rest-api) for a comparison of the CLI, the skill, and the MCP server.

The skill is compatible with [skills](https://github.com/vercel-labs/skills), a package-manager-style installer for agent skills. It supports Claude Code, Cursor, Codex, Windsurf, opencode, and many other compatible AI coding agents. The following procedure installs the `gddy` agent skill.

Agent & Automation Notes

Permissions Any account

Scopes`Depends on invoked command — the skill drives the gddy CLI, which inherits REST endpoint scopes`

Rate limit N/A (installation only) — see /docs/api-users/rate-limits for the CLI's underlying call limits.

Idempotent Yes

Destructive No

On failure Installation is safe to repeat. Re-run the install command to update or reinstall. Removing the skill does not affect the gddy CLI itself or its stored credentials.

Last updated on 11/16/2026

How is this guide?
