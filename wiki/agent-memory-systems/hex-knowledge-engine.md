# Hex Knowledge Engine

> Sources: Katherine Harrison / Hex, 2026-11-19
> Raw: [Introducing the Knowledge Engine](../../raw/agent-memory-systems/2026-11-21-hex-knowledge-engine.md)

## Overview

Hex describes a beta Knowledge Engine for Hex 4.0: a graph-based, self-learning context layer that reuses findings from analytics-agent conversations alongside governed workspace assets. Its goal is to reduce repeated discovery, improve consistency, lower cost and latency, and expose disagreements for human review.

## Lifecycle

A nightly Curator Agent converts guides, semantic models, published projects, and agent discoveries into knowledge units. The system reconciles duplicates, updates units when source context changes, and assigns trust statuses such as Verified or Debunked. When workspace guidance conflicts, it records contested knowledge instead of silently selecting one version. Agents search the graph first and return to raw context or the warehouse when they need new discovery or validation.

## Governance And Limits

Hex presents usage signals, contested knowledge, and source links as observability and steerability surfaces. The company reports a 22% response-time reduction and 25% cost reduction in its own workspace; these are vendor-reported results. The initial beta is limited to sources accessible to everyone in a workspace, and the article warns that self-learning can propagate wrong beliefs, so source governance and human correction remain necessary.

## See Also

- [HybridRAG: Combining Knowledge Graphs and Vector Retrieval](hybridrag-system.md)
- [Hindsight: Agent Memory That Learns](hindsight.md)
- [GBrain](gbrain.md)
