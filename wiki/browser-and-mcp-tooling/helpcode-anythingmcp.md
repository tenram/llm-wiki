# AnythingMCP (HelpCode)

> Sources: HelpCode (helpcode.ai), Unknown date
> Raw: [HelpCode-ai GitHub organization (2026-10-13 snapshot)](../../raw/browser-and-mcp-tooling/2026-10-13-helpcode-ai.md); [AnythingMCP repository (2026-10-16 README snapshot)](../../raw/browser-and-mcp-tooling/2026-10-16-anythingmcp.md)

## Overview

AnythingMCP is an open-source (AGPL-3.0-only), self-hosted MCP gateway from HelpCode (helpcode.ai, Freiburg, Germany) that turns any REST/OpenAPI, SOAP, GraphQL, OData, or SQL system into MCP tools for Claude, ChatGPT, Copilot, Gemini, and Cursor — without writing an MCP server. It ships **474 connectors** (up from the 331 reported in the earlier org snapshot) exposing 2,400+ tools, with 20 connectors needing no API key. It is listed in the official Claude directory. The project was extracted from production use at KOCH Freiburg GmbH, where it connects AI assistants to 15+ internal systems.

## The AnythingMCP Family

HelpCode maintains a set of connectors sharing the same goal — reading/writing enterprise data through MCP with no code:

- **sql-to-mcp** — connect PostgreSQL, MySQL, SQL Server, Oracle, SAP HANA, MongoDB; read-only and audited.
- **openapi-to-mcp** / **odata-to-mcp** — turn any OpenAPI/Swagger/REST or OData (V2/V4, incl. SAP Gateway) service into MCP tools by reading the schema ($metadata); no code.
- **sap-mcp-server**, **sap-hana-mcp-server**, **sap-business-one-mcp-server** — SAP S/4HANA (OData or HANA SQL, guided by SAP's data dictionary and CDS views), Business One (read + create sales orders), and Concur.
- **erp-mcp-server** — 18 ERPs (SAP, Odoo, JTL-Wawi, Xentral, weclapp, ERPNext, …), self-hosted or cloud.
- **ecommerce-mcp-server** — Amazon, eBay, WooCommerce, Shopware, Kaufland, OTTO, and more.
- **anythingmcp-plugin** — Cursor/agent-client plugin exposing those systems as MCP tools, with cross-system briefing skills.
- **codebound-kit** — test kit for CODEBOUND, a "Safe Script Sandbox for AI Agents" inside AnythingMCP (Black Forest Hackathon 2026).

## How It Works

Three steps: (1) add a connector — install a catalog adapter (a single JSON file) or point AnythingMCP at your own OpenAPI spec, WSDL, GraphQL endpoint, Postman collection, or database; (2) decide what the model sees — rename/describe tools in a visual editor, drop fields that must not leave the network, and choose which roles may call which tools; (3) hand one URL to your AI client. Tools register at runtime without a restart, and per-connector `{{VAR}}` values are interpolated server-side and never shown to the AI.

Connector categories span ERP/accounting, e-commerce/marketplaces, logistics/shipping, HR/field service, government/public data, banking/payments, messaging, advertising/analytics, and AI decision models. The largest are WooCommerce (49 tools), Xentral (30), SAP Business One (24), Etsy (22), and Amazon Seller Central (15). Adapters marked as built only from published API docs (not yet exercised against a live tenant) are flagged honestly.

## Security and Governance

Everything runs on the operator's infrastructure, and OAuth2, RBAC, SSO, and SCIM are in the self-hosted build rather than held back for a paid tier:

- **Response mapping** — each tool declares exactly which fields reach the model. A shipped adapter goes from 12,172 B to 1,072 B (−91%) after dropping fields, which also reduces context cost. `"fallbackToRaw": false` makes a call fail rather than leak the raw response when a mapping breaks.
- **Read-only where it matters** — every tool carries MCP annotations (`readOnlyHint`, `destructiveHint`), and role-based tool whitelisting can publish a read-only server. Database query tools run a single SELECT and block writes and stacked statements.
- **Auth** — OAuth2 (PKCE and Client Credentials), Bearer, API key, Basic, HMAC request signing, LOGIN_TOKEN, and OAuth 1.0a. Credentials are encrypted at rest with AES-256-GCM.
- **Audit log** — every tool call recorded with input, output, duration, and status, including the full upstream response the model never saw.
- **SSO/SCIM** — Entra ID, Google, Okta, Auth0, or any OIDC provider; roles sync from directory groups on every sign-in.

These controls overlap with the purpose of a dedicated de-identification framework such as [Data Privacy Stack / Presidio](../data-privacy/data-privacy-stack.md): both aim to keep sensitive fields from leaving the trust boundary.

## Knowledge Graph and AI Skills

Beyond forwarding calls, AnythingMCP builds a per-workspace **Knowledge Graph** of entities (customers, orders, products) and their cross-connector relationships, storing field names and relationships but never values, exposed via a `kg_how_to_obtain` tool. **AI skills** turn recurring usage into small rules ("today's revenue includes order statuses 2, 3 and 4") composed into the server's instructions. The AI passes are off by default and use the operator's own OpenAI/OpenRouter/Anthropic key; the graph, editor, and MCP tool work without one.

## Where It Fits

Most MCP gateways federate and secure MCP servers you already have. AnythingMCP starts one step earlier: it generates the MCP servers from existing APIs, ERPs, and databases, then serves, scopes, and audits them behind one endpoint. For teams whose tools are already MCP servers, a pure federation gateway may suffice; [FastMCP](fastmcp.md) provides the application-layer framework and Prefect Horizon the enterprise gateway in that scenario.

## Deployment

Self-hosting needs Docker 24+ and `openssl`; the quickstart compose file binds to `127.0.0.1` and the first registered account becomes admin. A `./setup.sh` path adds a domain, Caddy certificates, generated secrets, and an MCP auth mode for internet-reachable instances. Managed cloud (Frankfurt, 7-day trial) runs the same AGPL code; SSO and SCIM are self-hosted only.

## See Also

- [Model Context Protocol Overview](model-context-protocol-overview.md)
- [FastMCP](fastmcp.md)
- [Data Privacy Stack (Presidio)](../data-privacy/data-privacy-stack.md)
