# Life-Harness

> Sources: Tianshi Xu et al., Unknown date
> Raw: [Life-Harness](../../raw/ai-agent-harnesses/life-harness.md)

## Overview

A research project testing whether a frozen LLM agent's repeated failures in deterministic environments can be fixed by adapting the runtime harness around it, rather than retraining the model. Principle: "the model remains frozen; the benchmark environment remains intact; only the harness interface adapts."

## Method

Four runtime intervention layers: Action Realization (converts decisions into executable actions), Environment Contract (explicit runtime task constraints), Trajectory Regulation (prevents repeated failure patterns across steps), and Procedural Skill (reuses successful recovery patterns). The harness layers are evolved by learning from observed failures and applied at evaluation time, training-free.

## Results

Evaluated across 7 benchmarks and 18 model backbones (AgentBench-style: ALFWorld, DBBench, OS, WebShop; Tau-bench-style: Airline, Retail, Telecom); improved 116 of 126 settings with an 88.5% average relative gain.

This is direct empirical support for the "harness over model" thesis argued qualitatively elsewhere in this topic.

## See Also

- [Harness Design Principles](harness-design-principles.md)
- [Statewright](statewright.md)
