# Data Privacy Stack (Presidio)

> Sources: Data Privacy Stack, Unknown date
> Raw: [Data Privacy Stack (GitHub organization)](../../raw/data-privacy/2026-10-16-data-privacy-stack.md)

## Overview

Data Privacy Stack is a GitHub organization ("Tools for AI native privacy preserving technologies," dataprivacystack.org) with four public repositories. Its flagship is **Presidio**, an open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) across text, images, and structured data. The organization has no public members listed.

## Repositories

- **presidio** — the flagship framework. Python, MIT, ~11.4k stars. Supports NLP, pattern matching, and customizable pipelines for PII detection and anonymization across text, images, and structured data.
- **presidio-research** — data-science tasks for developing new recognizers for Presidio, used to evaluate the whole system and individual PII recognizers/detection models. Jupyter Notebook, MIT, ~318 stars.
- **MVG** — CC-BY-4.0, minimal activity.
- **website** — Astro site, minimal activity.

## Why It Matters Here

Presidio is the de-identification layer that pairs naturally with the privacy-sensitive parts of agent and MCP workflows: before text, images, or structured records are sent to a model or third-party tool, a PII detection/redaction pass reduces what leaves the trust boundary. It is relevant to the redaction and field-mapping controls exposed by MCP gateways such as [AnythingMCP (HelpCode)](../browser-and-mcp-tooling/helpcode-anythingmcp.md), which lets an operator drop fields (e.g. IBAN, salary) before they reach the model.

## See Also

- [AnythingMCP (HelpCode)](../browser-and-mcp-tooling/helpcode-anythingmcp.md) — MCP gateway with per-tool response mapping for dropping sensitive fields.
- [Model Context Protocol Overview](../browser-and-mcp-tooling/model-context-protocol-overview.md) — the integration standard this data is passed through.
