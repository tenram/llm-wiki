# Statewright

> Source: https://github.com/statewright/statewright
> Collected: 2026-07-11
> Published: Unknown

A framework implementing state machine constraints to control which tools an AI agent can access during different phases of a workflow. Tagline: "Agents are suggestions, states are laws." Targets brittleness from giving agents 40+ tools and open-ended problems (re-reading files repeatedly, editing during review phases, deploying before tests pass) by constraining the problem space to focused, per-phase contexts rather than scaling the model.

Three-layer architecture: Engine (Rust, `crates/engine`), a pure state machine evaluator with no LLM dependencies; Agent Binary (`sw-agent`), a direct-to-Ollama executor with per-state model routing; Plugin Layer (MCP gateway plus plugins) integrating with Claude Code, Codex, Pi, opencode, Cursor.

Key features: per-state tool restriction, "bash discernment" blocking destructive commands (e.g. `rm -rf`, `sed -i`) even when Bash is allowed, edit guards limiting diff size/files per state, conditional transitions via guard logic, per-state model routing (cheap models for recon, frontier models for hard reasoning), approval gates/interrupts for human review, environment scoping to hide sensitive variables or substitute test credentials.

Install: `/plugin marketplace add statewright/statewright`, `/plugin install statewright`, activate via `/statewright start bugfix`. Reported results on a 5-task SWE-bench subset: models improved from 2/10 to 10/10 passing under the constrained state machine; rough capability threshold around 13GB model size. Enforcement is "hard" for Claude Code, Codex, Oh My Codex, Pi, opencode, and "advisory" (context injection only) for Cursor.

Licensing: engine/agent layers Apache 2.0; MCP gateway FSL-1.1-ALv2 converting to Apache 2.0 in 2029; includes a patent pledge. Commercial tiers at statewright.ai (Free, Pro $29/mo, Team $99/mo, Enterprise); self-hosting via Docker Compose with PocketBase backend and Ollama.
