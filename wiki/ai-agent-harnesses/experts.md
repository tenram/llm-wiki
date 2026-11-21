# Experts

> Sources: Ken Collins / metaskills, Unknown date
> Raw: [metaskills/experts](../../raw/ai-agent-harnesses/2026-11-15-experts.md)

## Overview

Experts is a JavaScript runtime for composing OpenAI Assistants and tools into parent/child assistant systems. The repository emphasizes lifecycle hooks, tool delegation, streaming or buffered output, and compatibility with both ES modules and CommonJS.

## Runtime shape

An assistant owns instructions, runs, threads, and tools. Assistants can be used as tools, while ordinary tools can be attached to a parent run. The project supports callbacks such as `beforeAsk` and `afterInit`, configurable run options, optional remote-resource updates, and a model default that can be overridden through `EXPERTS_DEFAULT_MODEL`.

## Operational lessons

Tool names must be unique across a parent assistant's complete tool set. Debug output can be enabled or reduced through environment variables, and recent changes avoid logging large instruction strings. The changelog also documents compatibility fixes and output buffering for bespoke interfaces.

## Limits

This source is a repository changelog and implementation snapshot, not an independent evaluation of reliability or current OpenAI API compatibility. Verify the package against the target Assistants API before production use.

## See Also

- [Omnigent](omnigent.md)
- [Ruvnet Agent Ecosystem](ruvnet-agent-ecosystem.md)
