# Autoresearch

> Sources: Andrej Karpathy, Unknown date
> Raw: [Autoresearch](../../raw/research-and-training/autoresearch.md)

## Overview

A single-GPU system letting an AI agent autonomously run LLM-training experiments overnight: it edits `train.py`, runs a fixed 5-minute training run, evaluates against a bits-per-byte validation metric, and iterates, aiming to produce an improved model (or at least a useful experiment log) by morning.

## Design Constraints

Built on a single-GPU nanochat implementation (GPT-style model, Muon+AdamW optimizers). Deliberately narrow agent write-access: only `train.py` is editable by the agent; `prepare.py` (data prep, tokenizer, eval utilities) is immutable, and `program.md` carries human-written behavioral instructions. The fixed 5-minute wall-clock budget per run keeps experiments comparable across architecture/hyperparameter changes, a constraint-based approach conceptually similar to [Statewright](../ai-agent-harnesses/statewright.md)'s per-phase tool restriction, though applied to compute time rather than tool access.

Framed partly as satire: the README imagines "autonomous swarms of AI agents running across compute cluster megastructures" doing frontier research, dated as future fiction. This stands in notable contrast to [Academic Research Skills](../claude-code-ecosystem/academic-research-skills.md)'s explicit human-in-the-loop philosophy for AI-assisted research.

Requires an NVIDIA GPU; community forks extend to macOS, Windows, and AMD.

## See Also

- [Statewright](../ai-agent-harnesses/statewright.md)
- [Academic Research Skills](../claude-code-ecosystem/academic-research-skills.md)
