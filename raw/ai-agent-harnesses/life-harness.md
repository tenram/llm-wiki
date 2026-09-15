# Life-Harness

> Source: https://github.com/Tianshi-Xu/Life-Harness
> Collected: 2026-07-11
> Published: Unknown

Official implementation of a research project on runtime adaptation for deterministic LLM agents. Central question: when a frozen LLM agent repeatedly fails in a deterministic environment, can the runtime harness around it be improved instead of retraining the model. Stated principle: "The model remains frozen; the benchmark environment remains intact; only the harness interface adapts."

Headline results: evaluated across 7 benchmarks and 18 model backbones, with 116 of 126 settings improved and an 88.5% average relative gain, entirely training-free.

Architecture: four runtime intervention layers — Action Realization (converts model decisions into executable environment actions), Environment Contract (explicitly defines task constraints at runtime), Trajectory Regulation (prevents repeated failure patterns across multi-step interactions), Procedural Skill (leverages successful recovery patterns). The method evolves a compact set of runtime layers by learning from observed failures, then applies those adaptations at evaluation time, preserving model determinism while improving performance through interface changes alone.

Supported environments: AgentBench-style (ALFWorld, DBBench, OS, WebShop) and Tau-bench-style (Airline, Retail, Telecom), reflected in the repo's `AgentBench/` and `TauBench/` directory split.
