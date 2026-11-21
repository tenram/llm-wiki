# CrewAI

> Sources: CrewAI, 2026-10-05; CrewAI, 2026-11-10
> Raw: [CrewAI home](../../raw/ai-agents/crewai.md); [CrewAI README (2026-11-10 snapshot)](../../raw/ai-agents/2026-11-10-crewai.md)

## Overview

CrewAI is an open-source Python framework for production-ready multi-agent workflows. Its current README centers on two complementary primitives: autonomous, role-based Crews and precise, event-driven Flows. The commercial AMP Suite adds a control plane for deployment, observability, governance, security, and enterprise support.

## Platform Positioning

Crews optimize for agent autonomy, delegation, specialized roles, and collaborative problem solving. Flows provide event triggers, state, branching, routing, deterministic Python logic, and checkpoints. The framework is intended to combine both: use autonomous collaboration where useful, then wrap it in explicit workflow control where production behavior needs to be predictable.

The README also describes JSON-first project scaffolding, Python-native customization, tools, memory, knowledge, structured outputs, human input, MCP/A2A support, and optional official CrewAI skills for coding agents. AMP adds centralized tracing, a unified control plane, integrations, security controls, analytics, and cloud or on-premise deployment. Adoption and certification counts in the README are vendor claims.

## Practical Takeaway

CrewAI is relevant when an application needs more than one prompt or chatbot: multiple specialized agents, tools, structured outputs, human review, or workflows that combine autonomous reasoning with business logic. The README does not establish independent evidence for its performance claims, pricing, or technical limits.

## See Also

- [Harness Design Principles](../ai-agent-harnesses/harness-design-principles.md)
- [Sim](../ai-agent-harnesses/sim.md)
