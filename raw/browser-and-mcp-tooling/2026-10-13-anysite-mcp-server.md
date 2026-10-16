# Anysite MCP Server

> Source: https://github.com/anysiteio/anysite-mcp-server
> Collected: 2026-10-13
> Published: Unknown

# Anysite MCP Server

**The entire web is your database. Your AI assistant is the query interface.**

A Model Context Protocol server that lets Claude, Cursor, ChatGPT, and any MCP client query structured data from LinkedIn, Instagram, Twitter/X, Reddit, YouTube, SEC EDGAR, Y Combinator, Crunchbase, and any URL on the web — through five universal tools, plus CRM write-back tools.

## Quick start

Connect directly to the hosted server at `https://mcp.anysite.io/mcp`. It speaks MCP over Streamable HTTP with OAuth 2.0, and works with Claude Desktop, Claude Code, Cursor, Cline, Windsurf, ChatGPT, and any MCP-compliant client.

If your client supports HTTP transport, you do not need the npm package. The package exists as a stdio bridge for clients that only speak stdio.

#### Step 1: Sign up

Create an account at anysite.io. The `MCP30` promo covers your first month of MCP Unlimited ($30/month, 6 req/min fair-use, no credit counting). Credit-based plans (Starter $49 / Growth $200 / Scale $300 / Pro $549 / Enterprise from $1,199) also include MCP access.

#### Step 2: Connect your client

- **Claude Desktop** — OAuth: Settings → Connectors → Add Custom Connector, URL `https://mcp.anysite.io/mcp`, authorize in browser. Required: Settings → Capabilities → Tool access → "Tools already loaded" (the "Load tools when needed" mode uses name-based matching that fails on generic names like `discover` and `execute`).
- **Claude Code** — `claude mcp add --transport http anysite "https://mcp.anysite.io/mcp?api_key=YOUR_KEY"`. The URL carries your API key — treat it as a secret.
- **Cursor** — edit `~/.cursor/mcp.json` or project `.cursor/mcp.json` with the `url` + `transport: "http"`.
- **Cline, Windsurf, ChatGPT, any MCP client** — point at `https://mcp.anysite.io/mcp`, authenticate via OAuth or `?api_key=YOUR_KEY`.

#### Step 3: Verify

Ask the assistant to list tools. It should list: `discover`, `execute`, `get_page`, `query_cache`, `export_data` — plus eight `crm_*` tools if the CRM integration is enabled.

#### Step 4: Run a query

The assistant runs `discover` on LinkedIn, picks the right search endpoint, calls `execute`, then narrows server-side with `query_cache`.

## stdio bridge (npm package)

`@anysiteio/mcp` is a thin local proxy: it runs on stdio and forwards every request to `https://mcp.anysite.io/mcp` over Streamable HTTP with your token. No business logic lives in the package — tools, instructions, caching and exports all come from the server, so new endpoints and tools appear without a package update.

Use it when your client cannot speak HTTP transport: stdio-only IDE plugins, older Cline/Continue builds, custom stdio runners, or environments where outbound HTTP must go through a managed local process.

Install: `npm install -g @anysiteio/mcp` or run on demand with `npx -y @anysiteio/mcp`.

Configure your client:

```json
{
  "mcpServers": {
    "anysite": {
      "command": "npx",
      "args": ["-y", "@anysiteio/mcp"],
      "env": {
        "ANYSITE_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

Only `ANYSITE_ACCESS_TOKEN` is required — create one at app.anysite.io. The token can also live in `~/.anysite-mcp.env`.

## The tools

| Tool | Purpose |
|---|---|
| `discover(source, category)` | List endpoints in a category with their params and LLM hints. Always call before `execute`. |
| `execute(source, category, endpoint, params)` | Fetch data. Returns first 10 items + `cache_key`. |
| `get_page(cache_key, offset, limit)` | Paginate cached items without re-fetching (limit ≤ 50). |
| `query_cache(cache_key, conditions?, sort_by?, aggregate?, group_by?)` | Filter / sort / aggregate cached items server-side. |
| `export_data(cache_key, output_format, list_unpack?)` | Dump the full dataset to `json` / `jsonl` / `csv`. Returns a download URL. |
| `crm_*` (8 tools) | HubSpot-and-friends read/write: connections, schema, upsert contacts/companies, query, undo. Visible only when CRM is enabled. |

Sources surfaced through `discover`: LinkedIn, Instagram, Twitter/X, Reddit, YouTube, SEC EDGAR, Y Combinator, Crunchbase, DuckDuckGo, the universal web parser, plus AI parsers for GitHub, Amazon, Google Maps, G2, BuiltWith, Apify, GLEIF, Newegg and more.

Data fetched by `execute` is cached server-side for 7 days: one `execute()` call, then unlimited `get_page` / `query_cache` / `export_data` calls without re-paying API credits. Export files live for 24 hours (regenerated on demand while the cache entry is alive).

## Usage pattern

```
discover("linkedin", "search")
  → endpoints: ["users", "companies", "posts", ...] with params

execute("linkedin", "search", "users", { keywords: "CTO AI" })
  → { items: [...first 10], total: 50, cache_key: "abc...", next_offset: 10 }

get_page("abc...", offset=10)            # next page, free
query_cache("abc...", { conditions: [...] })
export_data("abc...", "csv")             # full dataset as a CSV download URL
```

## Migrating from 2.x

v3 is a breaking change: the package no longer reimplements the server locally — it proxies the hosted MCP server. Changes: `export_data` returns a download URL instead of a local file path; parameter renamed to `output_format`; `get_page` caps `limit` at 50; cache is server-side now (7-day TTL, survives restarts); CRM tools appear when enabled; env vars `ANYSITE_API_URL`/`ANYSITE_OPENAPI_URL` removed, `ANYSITE_MCP_URL` points at a different MCP server; `bin` aliases removed — command is `anysite-mcp`; two LinkedIn endpoints (`sn_search/users`, `company/employees`) excluded by server policy.

## Skills — ready-made workflows

Anysite Skills packages MCP access into named workflows: lead generation, competitor intelligence, person analyzer, market research, customer pain mining, brand reputation, positioning map. Full catalog of 17 skills (incl. VC analyst, influencer discovery, audience analysis, content analytics, trend analysis): github.com/anysiteio/agent-skills. Install in Claude Code:

```bash
/plugin marketplace add https://github.com/anysiteio/agent-skills
/plugin install anysite-lead-generation@anysite-skills
```

## Configuration

| Env var | Required | Default | Notes |
|---|---|---|---|
| `ANYSITE_ACCESS_TOKEN` | yes | — | Create one at app.anysite.io |
| `ANYSITE_MCP_URL` | no | `https://mcp.anysite.io/mcp` | Override the remote MCP server URL |

Variables can also live in `./.env` or `~/.anysite-mcp.env` (real environment variables and `./.env` take precedence over `~/.anysite-mcp.env`).

If the remote server is unreachable at startup, the bridge still starts in a degraded mode (empty tool list, descriptive errors on calls), keeps reconnecting in the background, and announces the tool list via `tools/list_changed` once the server is reachable again.

## License

MIT.
