# AnythingMCP (HelpCode-ai/anythingmcp)

> Source: https://github.com/HelpCode-ai/anythingmcp
> Collected: 2026-10-16
> Published: Unknown

## About

Open-source, self-hosted MCP gateway: turn any REST/OpenAPI, SOAP, GraphQL, OData or SQL API into MCP tools for Claude, ChatGPT & Copilot. 474 connectors incl. SAP S/4HANA & Business One, ERP, e-commerce.

- Repository: HelpCode-ai/anythingmcp
- License: AGPL-3.0-only
- Site: https://anythingmcp.com
- Stars: 751; Forks: 87; Watching: 5; Commits: 1,219
- Topics: ai-agents, chatgpt, claude, claude-connectors, ecommerce, erp, graphql-to-mcp, hacktoberfest, mcp, mcp-gateway, mcp-server, model-context-protocol, odata, openapi-to-mcp, rest-to-mcp, s4hana, sap, self-hosted, soap-to-mcp, sql-to-mcp

## README

**AnythingMCP is an open-source, self-hosted MCP gateway that turns any REST/OpenAPI, SOAP, GraphQL, OData or SQL system into MCP tools for Claude, ChatGPT and Copilot, without writing an MCP server.** It ships 474 ready connectors, among them SAP, Etsy, weclapp and Amazon Seller, and 20 of them need no API key.

Listed in the official Claude directory (claude.ai/directory/anythingmcp). Cloud trial available; self-hosted is the same AGPL code.

### Run it yourself

Requires Docker 24+ and `openssl`; on macOS start Docker Desktop first. No clone needed:

```sh
mkdir anythingmcp && cd anythingmcp
curl -fsSLo docker-compose.yml \
  https://raw.githubusercontent.com/HelpCode-ai/anythingmcp/main/docker-compose.quickstart.yml
printf 'JWT_SECRET=%s\nENCRYPTION_KEY=%s\n' "$(openssl rand -hex 32)" "$(openssl rand -hex 32)" > .env
docker compose up -d
```

Open http://localhost:3000 and register: the first account becomes admin. MCP endpoint is `http://localhost:4000/mcp`, API docs at `http://localhost:4000/api/docs`.

Keep the generated `.env` — `ENCRYPTION_KEY` decrypts stored credentials. On amd64 the image pulls in about 30 s and the API is healthy 24 s later. The image is amd64 only; the compose file pins the platform so it runs on Apple Silicon under emulation.

The quickstart binds to `127.0.0.1` on purpose. For an instance other people or a cloud AI client can reach, clone the repo and run `./setup.sh`: it asks for a domain, gets certificates through Caddy, generates the secrets and sets the MCP auth mode.

Other ways to run it: managed cloud (Frankfurt, Germany; 7-day free trial; DPA/AVV on request; SSO and SCIM self-hosted only), Railway, DigitalOcean.

### How it works

1. **Add a connector.** Install an adapter from the catalog (a ready JSON definition for SAP, Odoo, DHL and the rest), or point AnythingMCP at your own OpenAPI spec, WSDL, GraphQL endpoint, Postman collection or database. Once configured in your workspace it is a connector, and each of its operations is an MCP tool.
2. **Decide what the model sees.** Rename and describe the tools in the visual editor, drop the fields that must not leave your network, and choose which roles may call which tools.
3. **Hand one URL to your AI client.** An MCP server is the endpoint you add to Claude, ChatGPT, Copilot, Gemini or Cursor. It exposes the connectors you assign to it, and nothing else.

### Connect any API, SOAP service or database

Most companies have no MCP servers yet — they have a REST API, an ERP, a SOAP service from 2009 and a database. Each becomes a set of MCP tools:

- **OpenAPI / Swagger (REST)** — import a spec by URL or paste it; every operation becomes a tool with parameters, auth and endpoint mapping.
- **Postman collection, cURL** — folders, auth, body modes and `{{variables}}` carry over.
- **SOAP / WSDL** — each operation becomes a tool; envelopes, parameter order and WCF services handled.
- **GraphQL** — introspection turns queries and mutations into tools.
- **OData** (SAP Gateway included) — reads each service's `$metadata`; entity sets, keys and SAP business labels; V2 and V4.
- **SQL and MongoDB** — PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, SAP HANA, SQLite and MongoDB: schema, example and query tools, read-only by default.
- **Another MCP server** — discover its tools and serve them next to your own, behind the same auth and audit (MCP bridge).

Tools register at runtime, without a restart. Per-connector `{{VAR}}` values are interpolated on the server and never shown to the AI.

### Connector catalog

474 adapters, exposing 2,400+ tools. Every one has a setup guide on anythingmcp.com/guides, in seven languages.

- **ERP, accounting & invoicing:** SAP Business One, SAP S/4HANA, Odoo, weclapp, Xentral, Dynamics NAV, Lexware Office, sevDesk, Exact Online, bexio
- **E-commerce & marketplaces:** Amazon Seller, WooCommerce, Shopware 6, Magento, eBay, Etsy, Kaufland, OTTO, Oxomi
- **Logistics & shipping:** Deutsche Bahn, DHL, DPD, GLS, Shipcloud, Sendcloud
- **HR & field service:** Personio, HRWorks, Kenjo, MFR Mobile Field Report
- **Government & public data:** VIES VAT, Handelsregister, UK Companies House, DESTATIS, Bundesbank, OpenPLZ, NINA
- **Banking & payments:** Revolut Business, Wise, PAYONE, Razorpay, Paystack
- **Messaging:** WhatsApp, LINE, TeamViewer
- **Advertising & analytics:** Google Ads, Google Analytics 4, Google Search Console, Matomo
- **AI decision models:** Jev by TypeSafe — yes/no, classification and scoring with probabilities, in about 300 ms

**ERP connectors:** 18 systems with tools and markets. SAP Business One (24 tools, global), SAP S/4HANA Cloud (15), SAP S/4HANA via HANA SQL (10, read-only), SAP S/4HANA via OData (7), Odoo (11), Microsoft Dynamics NAV (6), ERPNext (11), Dolibarr (10), JTL-Wawi (10, DE), Xentral (30, DE), weclapp (11, DACH), Sage 100 (6, DE), Haufe X360 (7, DE), ScopeVisio (12, DE), AFAS Profit (6, NL), Zucchetti (6, IT), TeamSystem (6, IT), Axonaut (9, FR). Connectors marked with a dagger (†) were built from published API docs and not yet exercised against a live tenant.

**E-commerce & marketplace connectors:** 13 shops/marketplaces — Amazon Seller Central (15 tools), WooCommerce (49), Shopware 6 (6), Magento 2 / Adobe Commerce (13), BigCommerce (14), eBay Sell (10), Etsy (22), Ecwid (10), Kaufland (8), OTTO Market (8, DE), Zalando Direct Ship (5, EU), Billbee (8, DACH), Mercado Libre (4, LATAM).

**An adapter is a single JSON file.** That is why the catalog is this size, and why adding one is a reasonable first contribution.

### Security and governance

Everything runs on your infrastructure. OAuth2, RBAC, SSO and SCIM are in the self-hosted build, not held back for a paid tier.

- **Response mapping.** Each tool declares exactly which fields reach the model: drop a customer's IBAN or an employee's salary, or name the fields to keep. The editor shows the before/after on a real response; a shipped adapter goes from 12,172 B to 1,072 B (−91%). A broken mapping returns the raw response by default; set `"fallbackToRaw": false` on tools whose fields must never travel, and the call fails instead.
- **Read-only where it matters.** Every tool carries MCP annotations (`readOnlyHint`, `destructiveHint`), overridable per tool. Role-based tool whitelisting lets you publish a read-only MCP server. Database query tools run a single SELECT and block writes and stacked statements.
- **Every auth scheme you will meet.** OAuth2 (PKCE and Client Credentials), Bearer, API key, Basic, HMAC request signing, LOGIN_TOKEN and OAuth 1.0a. Credentials are encrypted at rest with AES-256-GCM.
- **Audit log.** Every tool call is recorded with input, output, duration and status in your own database, including the full upstream response the model never saw.
- **SSO and SCIM.** Entra ID, Google, Okta, Auth0 or any OIDC provider. Roles sync from directory groups on every sign-in; disabling someone in the directory also disables their workspace access and MCP API keys.

Example response mapping:

```json
{
  "transform": {
    "mode": "select",
    "fallbackToRaw": false,
    "exclude": ["customer.iban", "customer.taxId"],
    "select": { "order": "$.id", "total": "$.amounts.gross", "status": "$.state" }
  }
}
```

### Use it from Claude, ChatGPT, Copilot and Gemini

The same MCP server works in every client that speaks MCP, so you build a connector once. Claude (custom connector; OAuth 2.0 out of the box; one-click from the Claude Directory on Cloud), ChatGPT (Plugins → Add custom MCP server, or as the tool layer of an Apps SDK app), Meta Muse (Settings → Connectors → Add custom connector), Copilot, Gemini, Cursor and other MCP clients.

### Knowledge Graph and AI skills

Forwarding calls leaves the hard part to the agent: knowing which tool to call next, and what the business means by "open order". AnythingMCP learns both and hands them back as context, not as extra tool calls.

- **Knowledge Graph.** A per-workspace map of entities (customers, orders, products) and how they relate across connectors, built from tool definitions and real calls, and editable by hand. It stores field names and relationships, never values. Each server exposes it through a `kg_how_to_obtain` tool, so the agent can ask how to get from a Shopware order to a DHL tracking number.
- **AI skills.** Recurring usage turned into small rules ("today's revenue includes order statuses 2, 3 and 4") that you apply, edit or dismiss, and that are composed into the server's instructions.

The AI passes are off by default and use your own OpenAI, OpenRouter or Anthropic key; the graph, the editor and the MCP tool work without one.

### Where it fits

Most MCP gateways federate and secure MCP servers you already have. AnythingMCP starts one step earlier: it creates the MCP servers from the APIs, ERPs and databases you already run, then serves, scopes and audits them behind one endpoint. If your tools are already MCP servers and all you need is federation, a pure gateway may be enough.

### FAQ (selected)

- **What is an MCP gateway?** A single MCP endpoint in front of many tools, which handles authentication, access control and audit for all of them. AnythingMCP is a gateway that also generates the tools.
- **How do I connect my ERP to Claude or ChatGPT?** Install the ERP's adapter, enter API credentials, add the MCP server URL. Start with a role that can only read.
- **How do I turn an OpenAPI spec into an MCP server?** Create a REST connector and import the spec; every operation becomes an MCP tool on the `/mcp` endpoint, with no code.
- **Can I connect a SOAP/WSDL service to Claude?** Yes; AnythingMCP parses the WSDL and builds the SOAP envelope on every call, WCF included. Signed WS-Security messages are not supported yet.
- **Can Claude query my SQL Server, Oracle or PostgreSQL database safely?** Query tools are read-only by default; use a SELECT-only database user, prefer static queries, whitelist tools per role, use response mapping, and rely on the audit log.
- **How do I connect Shopware, WooCommerce or Amazon Seller Central to Claude?** Install the e-commerce adapter; WooCommerce ships 49 tools, Amazon Seller uses the official Selling Partner API, Shopware 6 reads the Store API.

### Community

In production at KOCH Freiburg GmbH (15+ internal systems: ERP, CRM, SOAP services and on-prem databases). helpcode.ai extracted it from that system and open-sourced it. AI-assisted development, human-reviewed.

### License

Open source under the GNU Affero General Public License v3 (AGPL-3.0-only). Commercial use inside your own company is included; the copyleft obligation only starts if you modify AnythingMCP and offer the modified version to others over a network. Cloud-operator code under `ee/` is separately licensed and not required for self-hosting.

## Repository layout (top-level)

`.github`, `.impeccable`, `content/guides`, `deploy`, `docs`, `packages`, `scripts`, plus `.env.example`, `AGENTS.md`, `CHANGELOG.md`, `CITATION.cff`, `CLA.md`, `CLAUDE.md`, `Dockerfile`, `LICENSE`, `LICENSING.md`, `README.md` (plus `.de`, `.ja`, `.zh-CN`), `docker-compose*.yml`, `glama.json`, `server.json`, `setup.sh`, `start.sh`.
