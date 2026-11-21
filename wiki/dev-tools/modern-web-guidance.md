# Modern Web Guidance

> Sources: Google Chrome, Microsoft Edge, Mozilla Firefox, MDN, and the web community, Unknown date
> Raw: [Modern Web Guidance repository](../../raw/dev-tools/2026-11-15-modern-web-guidance.md)

## Overview

Modern Web Guidance is a set of agent skills that injects web-platform expertise, compatibility data, and best practices into coding-agent context. Its stated goal is to steer agents away from legacy patterns and toward native browser capabilities with performance, accessibility, and fallback considerations.

## Coverage and retrieval

The published catalog covers CSS and layout, HTML and DOM, JavaScript and browser APIs, user experience, forms, accessibility, performance, and built-in AI. The CLI can search for a relevant guide, retrieve a guide by ID, scan a codebase for legacy patterns, and install the skill collection through an interactive wizard.

## Safe adoption

Guidance is designed to be token-efficient and is evaluated so lower-value material can be pruned. It includes project configuration through `.mwgrc`, compatibility-aware adoption advice, and responsible fallback guidance rather than assuming every modern feature is available everywhere.

## Evaluation and privacy

The repository publishes an evaluation dashboard and describes benchmark-based checks for whether guidance improves agent output. It also documents telemetry and privacy behavior, available skill packs, update paths, and alternate installation methods. The captured source is a published repository; contribution work is directed to the separate `modern-web-guidance-src` repository.

## Practical takeaway

Modern Web Guidance is a domain-specific skill retrieval layer, not a frontend framework. Its useful boundary is between a coding agent and current platform knowledge: search or retrieve guidance before implementation, then validate browser support and the resulting behavior.

## See Also

- [Agent Skill Collections](../claude-code-ecosystem/agent-skill-collections.md)
- [Impeccable](../claude-code-ecosystem/impeccable.md)
- [WebGL Interaction Demos](../frontend-and-interaction-demos/webgl-interaction-demos.md)
