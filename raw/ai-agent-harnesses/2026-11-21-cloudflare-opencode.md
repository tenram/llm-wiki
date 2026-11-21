# OpenCode + Cloudflare

> Source: https://developers.cloudflare.com/agent-setup/opencode/
> Collected: 2026-11-21
> Published: Unknown

Title: OpenCode + Cloudflare

URL Source: http://developers.cloudflare.com/agent-setup/opencode/

Final URL: https://developers.cloudflare.com/agent-setup/opencode/

Markdown Content:
[All agents](https://developers.cloudflare.com/agent-setup/)

![Image 1](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![Image 2](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)

Anomaly

Open-source terminal agent with a rich TUI that works with 75+ LLMs. Made by Anomaly.

Terminal Standalone Extension Open Source

1.   **Install OpenCode**

Install OpenCode. For npm, Homebrew, Bun, Scoop, or Windows options, see the [OpenCode install guide ↗︎](https://opencode.ai/docs/).

`curl -fsSL https://opencode.ai/install | bash`
2.   **Install Cloudflare Skills**

`npx skills add https://github.com/cloudflare/skills`
3.   **Add the Cloudflare MCP server**

Add the Cloudflare MCP server to `.opencode.jsonc`. For domain-specific MCP servers, refer to [mcp-server-cloudflare ↗︎](https://github.com/cloudflare/mcp-server-cloudflare). For the full Cloudflare API MCP server (Code Mode), refer to [cloudflare/mcp ↗︎](https://github.com/cloudflare/mcp).

```
{
  "mcp": {
    "cloudflare": { "type": "remote", "url": "https://mcp.cloudflare.com/mcp", "enabled": true }
  }
}
```
4.   **Launch OpenCode**

Start OpenCode from the root of your project, where `wrangler.jsonc` or `cloudflare.config.ts` lives (if either exists).

`opencode`
5.   **Try a prompt**

For example:

`Create a RAG pipeline using Vectorize and Workers AI to answer questions over my documentation.`

Expand any section to learn more.

Cloudflare Skills

Persistent platform context that teaches the agent how Cloudflare works.

Skills are instructions the agent loads on demand. The [cloudflare/skills](https://github.com/cloudflare/skills) bundle covers every layer of the platform — so the agent knows your conventions without you re-explaining them.

*   agents-sdk Build, debug, or review Cloudflare Agents SDK applications using the agents package.
*   basin Build and troubleshoot Cloudflare Basin analytics workflows with Basin Pipelines, Basin Catalog, and Basin SQL. Use for streaming data into R2 Iceberg tables, managing catalogs, or querying those tables; also use for requests using the former Data Platform, Pipelines, R2 Data Catalog, or R2 SQL names.
*   cf-cli Cloudflare's official cf CLI (beta) for the public Cloudflare API and Workers projects. Use for finding and running Cloudflare commands from the terminal — sign-in and profiles, cf cli search, cf schema, cf deploy/dev/build, resource commands for DNS, zones, D1, KV, and R2 — and for choosing between cf and Wrangler in a project.
*   cloudflare Discover and choose Cloudflare products for apps, APIs, AI agents, storage, networking, and security. Use for architecture and product selection, including when the user describes a need without naming a Cloudflare product; then find the relevant skill or documentation. Also use when a Cloudflare-proxied site shows a Cloudflare error page, a `52x` status, a 1xxx error code, or a Cloudflare `403`, to decide whether to fix Cloudflare configuration or the origin.
*   cloudflare-app-bootstrap Get a Cloudflare Workers app to a working local request by connecting its bindings, secrets, and initial data, then verifying real application behavior. Use for app setup or onboarding after the project exists; use frameworks-on-cloudflare or cf-cli to create or configure the project, and wrangler or cf-cli for isolated commands.
*   cloudflare-email-service Implement or troubleshoot Cloudflare Email Sending and Email Routing integrations and their delivery configuration.
*   cloudflare-one Design, configure, troubleshoot, or review Cloudflare One Zero Trust and SASE deployments. Use cloudflare-one-migrations for migration planning from other vendors. Also use when an agent, script, crawler, or other non-browser client needs to reach a webpage or API protected by Cloudflare Access.
*   cloudflare-one-migrations Assess and plan migrations from existing VPN, SWG, or SASE platforms to Cloudflare One, including policy mapping, parity gaps, and rollout.
*   durable-objects Build, debug, or review Cloudflare Durable Objects code for persistent state and coordination.
*   frameworks-on-cloudflare Build, migrate, and deploy web-framework applications on Cloudflare Workers. Use when a framework project such as Astro, SvelteKit, React Router, TanStack Start, Nuxt, Hono, or a React or Vue SPA targets Cloudflare, or when a framework repository contains Workers deployment configuration.
*   gateway-workers Build, debug, or review Cloudflare Workers invoked by the Forward action in Gateway HTTP policies, including the GatewayMiddleware entrypoint, Gateway types, context, and continuation.
*   k2 Build and troubleshoot Cloudflare K2 or K2 Streams durable logs. Use for stream setup, producing from Workers or HTTP, configuring retention and inputs, and consuming through subscriptions.
*   nextjs-on-cloudflare Build, migrate, and deploy Next.js apps on Cloudflare Workers with vinext. Use when starting a Next.js project on Cloudflare, moving an existing app to Workers, choosing between vinext and OpenNext, or setting up vinext for Workers. For setup, migration, or deployment, install vinext's upstream skills with `npx skills add cloudflare/vinext` if missing, then read and follow the applicable skill and docs.
*   sandbox-migrate-to-next Migrate Cloudflare Sandbox apps from stable @cloudflare/sandbox to @cloudflare/sandbox@next (SDK 1.0 preview). Use sandbox-next for apps already on the preview.
*   sandbox-next Build or maintain Cloudflare Sandbox apps on @cloudflare/sandbox@next (SDK 1.0 preview). Use sandbox-migrate-to-next when porting a stable app.
*   sandbox-stable Build or maintain Cloudflare Sandbox apps on the stable @cloudflare/sandbox package. Use sandbox-next for preview apps and sandbox-migrate-to-next for stable-to-preview migrations.
*   turnstile-spin Set up, repair, or migrate to Cloudflare Turnstile bot verification in an existing frontend and backend, including server-side Siteverify.
*   web-perf Audit, diagnose, or optimize website loading and interaction performance, Core Web Vitals, and Lighthouse performance scores.
*   workers-best-practices Cloudflare Workers best practices for production applications. Use when writing, reviewing, or configuring Workers.
*   workers-development Run, inspect, and debug Cloudflare Workers during local development with cf dev, wrangler dev, or the Cloudflare Vite plugin, using Local Explorer to read and seed binding data and query local traces and logs. Also routes production debugging to Workers observability. Use for debugging requests whether or not the project uses Wrangler.
*   workers-profiling Profile or debug CPU usage and memory allocation in deployed Cloudflare Workers and Durable Objects. Then use this information to optimize your code.
*   wrangler Run or troubleshoot Wrangler CLI commands in projects that have a wrangler.jsonc, wrangler.json, or wrangler.toml file, including local development, Previews, deployment, and resource management. For new projects and projects without a Wrangler configuration file, use the cf CLI instead.

MCP servers

Live access to the Cloudflare API, docs, and observability.

MCP servers provide typed tools to call into Cloudflare at runtime. There are two options: [Code Mode](https://blog.cloudflare.com/code-mode-mcp/) — a single server that covers the entire Cloudflare API (2,500+ endpoints in ~1,000 tokens) — or a set of focused, domain-specific servers hosted in the [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) repo. The full catalog is also in the [MCP servers for Cloudflare](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/) docs.

*   Cloudflare API MCP Server code mode Best when you want broad access across Cloudflare's APIs through code execution https://mcp.cloudflare.com/mcp
*   Code mode API code mode Broad access to the full Cloudflare API via code execution, with minimal token overhead https://mcp.cloudflare.com/mcp
*   Browser Run server Fetch web pages, convert them to markdown and take screenshots https://browser.mcp.cloudflare.com/mcp
*   Cloudflare Blog server Search and read posts from the Cloudflare Blog https://blog.mcp.cloudflare.com/mcp
*   Cloudflare One CASB server Quickly identify any security misconfigurations for SaaS applications to safeguard users & data https://casb.mcp.cloudflare.com/mcp
*   Container server Spin up a sandbox development environment https://containers.mcp.cloudflare.com/mcp
*   Demo Day server Demonstrate a minimal Cloudflare MCP server https://demo-day.mcp.cloudflare.com/mcp
*   Digital Experience Monitoring server Get quick insight on critical applications for your organization https://dex.mcp.cloudflare.com/mcp
*   Documentation server Get up-to-date reference information on Cloudflare https://docs.mcp.cloudflare.com/mcp

Wrangler CLI

Local dev, deploys, and Workers-specific commands.

Use [Wrangler](https://developers.cloudflare.com/workers/wrangler/) for local development, deploys, and product-specific commands like `wrangler d1 migrations apply` or `wrangler tail`. The bundled **wrangler** Skill teaches the agent when to reach for it.

Agent-friendly docs

Token-efficient references optimized for agents.

Append `/index.md` to any Cloudflare docs URL for a clean markdown version. Every top-level product section also has its own `llms.txt` — a page index sized for a single context window. A few useful ones:

For a full overview of how these docs are structured for agents, refer to the [Docs for Agents guide](https://developers.cloudflare.com/docs-for-agents/).

`Add bot protection and rate limiting to my login and checkout endpoints.``Set up a Waiting Room to handle flash sale traffic spikes without dropping requests.``Build an AI chat agent using the Cloudflare Agents SDK with persistent conversation history stored in D1.``Set up rate limiting and WAF rules to block abuse on my public API.``Add a D1 database to my Worker and create a users table with full CRUD endpoints.`

*   The Cloudflare API MCP server uses Code Mode — OpenCode writes JavaScript to reach any of 2,500+ endpoints in ~1,000 tokens.
*   OpenCode supports 75+ LLMs — you can use Cloudflare Workers AI as the model provider for a fully Cloudflare-native workflow.
*   Use OpenCode's plan agent (Tab key) to break down complex Workers projects before coding.

Should I use Skills, the MCP server, a CLI, or all of them?
All three. Skills provide persistent Cloudflare expertise so OpenCode knows when to reach for Durable Objects vs KV, how to structure a Workers project, and when to call CLI vs API. The Cloudflare API MCP server handles platform operations (DNS, WAF, Zero Trust, R2 buckets). Wrangler handles local dev, deploys, and Workers-specific commands. The bundled `wrangler` Skill teaches OpenCode which to use. For tasks across the whole Cloudflare API, OpenCode can also use the [Cloudflare CLI](https://developers.cloudflare.com/cf/), `cf`.

Can OpenCode use the Cloudflare CLI?
Yes. The [Cloudflare CLI](https://developers.cloudflare.com/cf/), `cf`, is in beta and covers the whole Cloudflare API and prints JSON output. Install it with `npm install -g cf`, sign in with `cf auth login`, and tell OpenCode to prefer it in `AGENTS.md`. Refer to [Use cf with AI agents](https://developers.cloudflare.com/cf/agents/).

How do I connect OpenCode to Cloudflare?
The first time OpenCode calls a Cloudflare tool, you will be redirected to authorize via OAuth and choose permissions.

Can I use Workers AI as the model provider in OpenCode?
Yes. OpenCode supports 75+ model providers, including Cloudflare Workers AI. Configure your model in `.opencode.jsonc`.

Is OpenCode open source?

Yes. OpenCode is fully open source and available at [github.com/anomalyco/opencode](https://github.com/anomalyco/opencode).

MCP server connection fails
Verify the MCP configuration in `.opencode.jsonc` uses `"type": "remote"` with the correct URL. Run `opencode mcp list` to check connected servers.

Getting outdated information about Cloudflare products
Point the agent directly at [developers.cloudflare.com/llms.txt](https://developers.cloudflare.com/llms.txt) for a directory of every product, or `developers.cloudflare.com/<product>/llms.txt` for a product-specific index.

Cloudflare is not just a deploy target for agents, it is a full stack for building your own.

[![Image 3](https://developers.cloudflare.com/icons/agents/claude/light.svg)![Image 4](https://developers.cloudflare.com/icons/agents/claude/dark.svg) Anthropic ### Claude Code Terminal-based coding agent that understands your codebase, runs commands, edits files, and manages git. Made by Anthropic. View guide](https://developers.cloudflare.com/agent-setup/claude-code/)[![Image 5](https://developers.cloudflare.com/icons/agents/codex/light.svg)![Image 6](https://developers.cloudflare.com/icons/agents/codex/dark.svg) OpenAI ### Codex OpenAI coding agent available as a terminal CLI and desktop app. It reads and writes files, runs commands, and browses the web in a sandbox. View guide](https://developers.cloudflare.com/agent-setup/codex/)[![Image 7](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![Image 8](https://developers.cloudflare.com/icons/agents/cursor/dark.svg) Cursor ### Cursor AI-first IDE built on VS Code with multi-file Composer edits and background agents. Made by Cursor. View guide](https://developers.cloudflare.com/agent-setup/cursor/)[![Image 9](https://developers.cloudflare.com/icons/agents/copilot/light.svg)![Image 10](https://developers.cloudflare.com/icons/agents/copilot/dark.svg) GitHub ### GitHub Copilot Editor extension and CLI with agent mode, workspace context, and native PR integration. Made by GitHub. View guide](https://developers.cloudflare.com/agent-setup/github-copilot/)[![Image 11](https://developers.cloudflare.com/icons/agents/pi/light.svg)![Image 12](https://developers.cloudflare.com/icons/agents/pi/dark.svg) Earendil ### Pi Minimal, extensible agent harness that you can make your own. Made by Earendil. View guide](https://developers.cloudflare.com/agent-setup/pi/)[![Image 13](https://developers.cloudflare.com/icons/agents/vibe/light.svg)![Image 14](https://developers.cloudflare.com/icons/agents/vibe/dark.svg) Mistral AI ### Vibe Coding agent for terminal, IDE, and cloud workflows that reads files, runs commands, writes code, and opens pull requests. Made by Mistral AI. View guide](https://developers.cloudflare.com/agent-setup/vibe/)[![Image 15](https://developers.cloudflare.com/icons/agents/devin/light.svg)![Image 16](https://developers.cloudflare.com/icons/agents/devin/dark.svg) Cognition ### Devin A full IDE with an agent manager built in — the command center for managing all your agents in one place. Made by Cognition. View guide](https://developers.cloudflare.com/agent-setup/devin/)[![Image 17](https://developers.cloudflare.com/icons/agents/visual-studio-code/light.svg)![Image 18](https://developers.cloudflare.com/icons/agents/visual-studio-code/dark.svg) Microsoft ### Visual Studio Code Free, open-source code editor with native Model Context Protocol (MCP) client support and Copilot Chat integration. Made by Microsoft. View guide](https://developers.cloudflare.com/agent-setup/visual-studio-code/)[![Image 19](https://developers.cloudflare.com/icons/agents/command-code/light.svg)![Image 20](https://developers.cloudflare.com/icons/agents/command-code/dark.svg) Command Code ### Command Code Command Code is one of the most used coding agents for open models. It automatically learns your coding taste and self-improves as you work. View guide](https://developers.cloudflare.com/agent-setup/command-code/)[![Image 21](https://developers.cloudflare.com/icons/agents/bionic/light.svg)![Image 22](https://developers.cloudflare.com/icons/agents/bionic/dark.svg) LM Studio ### Bionic Powerful agent for coding and work. Natively local, with open models in the cloud. By LM Studio. View guide](https://developers.cloudflare.com/agent-setup/bionic/)[![Image 23](https://developers.cloudflare.com/icons/agents/factory/light.svg)![Image 24](https://developers.cloudflare.com/icons/agents/factory/dark.svg) Factory ### Droid Model-agnostic coding agent that plans, edits files, runs commands, and automates CI, from the terminal, desktop app, or cloud. Made by Factory. View guide](https://developers.cloudflare.com/agent-setup/droid/)
