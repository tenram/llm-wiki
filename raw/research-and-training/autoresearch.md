# Autoresearch (karpathy/autoresearch)

> Source: https://github.com/karpathy/autoresearch
> Collected: 2026-07-11
> Published: Unknown

An autonomous AI-agent system for LLM training research on single-GPU setups, framed around letting "an AI agent [use] a small but real LLM training setup... [to] experiment autonomously overnight." The agent modifies training code, runs 5-minute training runs, evaluates results, and iterates, producing a log of experiments and, ideally, an improved model by morning. All runs use a fixed 5-minute wall-clock time budget so experiments stay comparable regardless of architecture/hyperparameter changes.

Built on a single-GPU implementation of nanochat: GPT-style models, Muon + AdamW optimizers, validation measured in bits-per-byte (val_bpb). Core files: `prepare.py` (immutable, handles data prep/tokenizer training/eval utilities), `train.py` (the only file agents modify: model architecture, optimizer config, training loop), and `program.md` (human-edited markdown instructions guiding agent behavior).

Requirements: NVIDIA GPU, Python 3.10+, `uv` package manager. Quick start: install uv, `uv sync`, `uv run prepare.py` (one-time setup, ~2 min), then `uv run train.py` for a single experiment (~5 min).

Notable framing claim: the project imagines "autonomous swarms of AI agents running across compute cluster megastructures" doing frontier research, presented as satirical future fiction dated "March 2026." Currently NVIDIA-only; community forks exist for macOS (MLX/standard), Windows, and AMD.
