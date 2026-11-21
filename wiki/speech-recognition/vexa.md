# Vexa

> Sources: Vexa, Unknown date
> Raw: [Vexa README](../../raw/speech-recognition/2026-11-10-vexa.md)

## Overview

Vexa is an open-source meeting-bot and real-time transcription platform that can join Google Meet, Microsoft Teams, and Zoom, stream speaker-attributed transcripts, and optionally feed sandboxed agents that maintain a Markdown knowledge base. It supports hosted transcription and a self-hosted, air-gap-oriented deployment model.

## Two-Domain Architecture

Vexa separates meeting capture from agent work behind one gateway. The Meetings API sends bots, retrieves transcripts, manages status, and exposes recordings. The Agent API supports workspace chat, one-shot invocations, scheduled routines, event-triggered work, and workspace file access. Both bots and agents run as isolated, ephemeral workloads through a pluggable Docker, process, or Kubernetes runtime backend.

The workspace is a git-backed Markdown or Open Knowledge Format bundle. Agents can prepare meetings, process transcripts, answer questions over the workspace, and propose or commit updates. The README presents human approval as the boundary for irreversible actions and describes read-only or propose-only patterns for untrusted inputs.

## Deployment And Status

The project supports Docker Compose, a lighter all-in-one image, and Helm/Kubernetes deployment. Transcription can use a hosted token or a separate self-hosted GPU service. The README marks Meet, Teams, and Zoom capture, real-time transcription, speaker attribution, Docker runtime, agent chat, routines, events, and Kubernetes lifecycle support as available, while noting that some features remain incomplete or planned.

## Practical Takeaway

Vexa’s differentiator is upstream capture: it creates owned, structured meeting data before a document-RAG or knowledge system operates on it. It can also be used as a standalone transcription API, with the agent lane as an optional layer.

## See Also

- [Karpathy LLM Wiki](../llm-workflows/karpathy-llm-wiki.md)
- [ROCm Whisper API](rocm-whisper-api.md)
- [Meetily](meetily.md) — local-first meeting capture and summarization
- [HybridRAG: Combining Knowledge Graphs and Vector Retrieval](../agent-memory-systems/hybridrag-system.md)
