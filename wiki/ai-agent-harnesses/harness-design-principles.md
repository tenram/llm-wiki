# Harness Design Principles

> Sources: MindStudio, Unknown date
> Raw: [AI Agent Harness: Architecture Over Model Selection](../../raw/ai-agent-harnesses/harness-design-principles-mindstudio.md)

## Overview

Argues that harness architecture, not model choice, determines production reliability for AI agents, and breaks the harness down into five components.

## The Five Components

**Rules (system prompt):** specific behavioral constraints on scope, output format, and decision priorities outperform vague instructions.

**Skills (tools):** a curated capability set mapped to real tasks, each with precise naming, clear descriptions, and defined error behavior.

**Hooks:** intercept points for observability and control, pre-action hooks validate/authorize, post-action hooks filter outputs and catch errors, providing safety beyond prompt-only guardrails.

**MCP:** an open protocol that reduces custom integration work for external systems, databases, and APIs.

**Memory:** layered across in-context memory (current task), external storage (key-value for facts, vector for semantic retrieval, for cross-session persistence), and working memory (multi-step state tracking).

Cited failure modes: scope creep from imprecise rules, inconsistency from missing memory/context, and tool misuse from poor descriptions.

## See Also

- [Awesome Harness Engineering](awesome-harness-engineering.md)
- [Statewright](statewright.md)
- [RightMemory](../agent-memory-systems/rightmemory.md)
