# oh-my-claudecode (OMC)

> Sources: Yeachan-Heo, Unknown date
> Raw: [oh-my-claudecode](../../raw/ai-agent-harnesses/oh-my-claudecode.md)

## Overview

A zero-configuration Claude Code plugin that layers a coordinated team of 32 specialized agents and 40+ skills on top of Claude Code, targeting the inefficiency of solo, sequential Claude Code use.

## Architecture

Agents are grouped by category (Analysis, Execution, Research, Frontend/UX, Testing, six specialized Code Review roles, Planning) and run on Haiku, Sonnet, or Opus depending on task difficulty for cost control. Four execution modes: Autopilot (sequential default), Ultrawork (max parallelism), Team (N coordinated agents), and Ralph mode (persistent verification loops with gates). Coordination uses a shared task list ("teams-first architecture") and natural-language orchestration rather than special syntax.

## Claims

Marketed benefits: 3-5x faster feature shipping, 30-50% lower token costs via model routing, and zero-configuration setup (`/omc-setup`). Stated adoption figures (36,000+ stars, 35,984 reviews at 4.8/5) are self-reported on the project's own marketing site and were not independently verified.

## See Also

- [Multica](multica.md)
- [Firstmate](firstmate.md)
- [ECC](ecc.md)
