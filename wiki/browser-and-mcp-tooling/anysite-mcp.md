# Anysite MCP

> Sources: Anysite, Unknown date
> Raw: [Anysite MCP Server README](../../raw/browser-and-mcp-tooling/2026-10-13-anysite-mcp-server.md)

## Overview

Anysite MCP is a hosted Model Context Protocol server ("the entire web is your database; your AI assistant is the query interface") letting any MCP client query structured data from LinkedIn, Instagram, Twitter/X, Reddit, YouTube, SEC EDGAR, Y Combinator, Crunchbase, and any URL — through five universal tools plus CRM write-back tools. It is a paid SaaS: hosted at `https://mcp.anysite.io/mcp`, MIT-licensed thin npm package, credit-based plans plus an MCP Unlimited option.

## Access Model

Clients that speak HTTP transport connect directly to the hosted server over Streamable HTTP with OAuth 2.0 or an `?api_key=` secret. For stdio-only clients, the `@anysiteio/mcp` npm package is a thin local proxy that forwards every request to the hosted server — no business logic lives in the package, so new endpoints and tools appear without a package update. Setup requires an `ANYSITE_ACCESS_TOKEN`; a degraded mode (empty tool list, reconnecting) applies if the remote is unreachable.

## The Five Universal Tools

- `discover(source, category)` — list endpoints with params and LLM hints; always called before `execute`.
- `execute(source, category, endpoint, params)` — fetch data; returns first 10 items plus a `cache_key`.
- `get_page(cache_key, offset, limit)` — paginate cached items without refetching (limit ≤ 50).
- `query_cache(cache_key, conditions?, sort_by?, aggregate?, group_by?)` — filter/sort/aggregate server-side.
- `export_data(cache_key, output_format, list_unpack?)` — dump the full dataset to `json`/`jsonl`/`csv` as a 24-hour download URL.

Plus 8 `crm_*` tools (HubSpot-style read/write: connections, schema, upsert, query, undo) visible when CRM integration is enabled.

## Data Model

Fetched data is cached server-side for 7 days: one paid `execute()` then unlimited `get_page`/`query_cache`/`export_data` without re-paying credits. Sources include LinkedIn, Instagram, X, Reddit, YouTube, SEC EDGAR, Y Combinator, Crunchbase, DuckDuckGo, a universal web parser, and AI parsers for GitHub, Amazon, Google Maps, G2, BuiltWith, Apify, GLEIF, and Newegg, with new endpoints appearing automatically.

## Workflow Skills

A separate Anysite Skills marketplace (17 workflows) packages the raw MCP access into named patterns — lead generation, competitor intelligence, person analyzer, market research, customer pain mining, brand reputation, positioning map — installed via the Claude Code plugin marketplace.

## See Also

- [Firecrawl](firecrawl.md) — comparable hosted web-data service with search/scrape/crawl/agent endpoints.
- [Model Context Protocol Overview](model-context-protocol-overview.md)
