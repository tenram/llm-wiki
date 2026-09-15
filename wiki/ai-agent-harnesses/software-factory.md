# The Software Factory (Ryan Waliany)

> Sources: Ryan Waliany, Unknown date
> Raw: [The Software Factory: AI Build Playbook Summary](../../raw/ai-agent-harnesses/2026-07-21-software-factory.md)

## Overview

Ryan Waliany's "Software Factory" playbook argues that with the right architecture, AI agents can rebuild SaaS products to feature parity in 30 days, because the assembly layer of software (writing and wiring code) is now commoditized. Value has shifted entirely to the endpoints: deciding what to build and for whom. His company, Ambiguous AI, claims to have rebuilt 15 SaaS products to feature parity, generating 4 million lines of code in 30 days using the methodology below.

## Core Principles

- **Layered agent context**: agents perform best with context inherited top-down — company mission/values, domain-specific craft, product goals, then interface specifications — keeping 100+ agents consistent.
- **Structured thinking borrowed from consulting**: the pyramid principle (lead with the answer), MECE (mutually exclusive, collectively exhaustive), and a "seven circumstances" checklist, all used to strip ambiguity before an agent starts executing.
- **Three levels of specification**: computational goals (L1), algorithmic approach (L2), and volatile implementation details (L3). Humans own why and how; agents own the code.
- **The Spec**: a deterministic build brief covering product behavior, design, architecture, algorithm, and verification, written so the agent never has to exercise judgment on missing information.
- **System design as contracts**: composable, modular components with explicit typed inputs/outputs, enabling isolated testing and incremental trust as pieces are proven independently.
- **SPEAR workflow**: Scope (human) → Plan–Execute–Assess loop (agent, iterative) → Resolve (human). Human review gates bracket the mechanical middle.
- **Process and checklist pairing**: durable SOPs paired with atomic, restart-safe checklists. "Done" means every proof surface (tests, logs, diffs) agrees.
- **Testing at endpoints**: black-box assertions at system boundaries, measuring real outcomes rather than proxy metrics an agent could game.
- **The flywheel**: every production defect becomes a permanent automated guardrail, so safety compounds over time instead of resetting with each incident.
- **The harness**: the unifying system — architecture + SPEAR + runtime — that accepts a goal and produces a tested pull request.

## Key Insight

The bottleneck to agent-built software isn't model capability, it's specification clarity: well-specified problems (competitive programming being the canonical example) already get correct solutions from current models. The playbook's real function is forcing humans to externalize intent completely into artifacts, moving judgment off the agent and onto the spec.

## See Also

- [Awesome Harness Engineering](awesome-harness-engineering.md) — broader harness-engineering resource list this playbook's ideas sit within.
- [Harness Design Principles](harness-design-principles.md) — a complementary five-component model (rules, skills, hooks, MCP, memory) for harness construction.
