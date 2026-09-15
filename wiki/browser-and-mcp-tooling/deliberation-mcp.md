# Deliberation (Multi-Model Consultation MCP Server)

> Sources: Anton Babenko, Unknown date
> Raw: [Deliberation](../../raw/browser-and-mcp-tooling/deliberation-mcp.md)

## Overview

An MCP server letting Claude Code (and other hosts) consult other AI models — GPT, Gemini, Grok, and 400+ OpenRouter models — as domain-specific reviewers during coding tasks, on the premise that a single model's blind spots are best caught by a second, independent model rather than more prompting of the same model.

## Architecture

Seven expert personas (Architect, Code Reviewer, Security Analyst, Debugger, Researcher, Plan Reviewer, Scope Analyst) are auto-routed based on the request. Consulted models can run in advisory (read-only) or implementation (workspace-write) mode.

## Consensus Mode

The standout mechanic is a bias-guarded convergence loop: Claude commits a "blind verdict" before seeing any external opinion, external models then review independently and vote, Claude arbitrates any disagreement with required reasoning, and the loop repeats until consensus or a round cap. Session analytics track which external models "earn their seat," turning ad hoc second-opinion requests into a measured, repeatable review process.

## See Also

- [Model Context Protocol Overview](model-context-protocol-overview.md)
