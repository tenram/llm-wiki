# AnythingLLM

> Sources: Mintplex Labs, Unknown date; Mintplex Labs, 2026-11-10
> Raw: [AnythingLLM README](../../raw/ai-agents/2026-10-19-anythingllm.md); [AnythingLLM README (2026-11-10 snapshot)](../../raw/ai-agents/2026-11-10-anythingllm.md)

## Overview

AnythingLLM is a local-first, self-hostable AI application for chatting with documents, running agents, and exposing a configurable multi-user workspace. Its README positions it as an all-in-one product: local or cloud model access, document ingestion, vector search, agents, MCP compatibility, scheduled tasks, model routing, memories, and deployment options are included rather than assembled from separate services.

## Product Shape

The application combines a React/Vite frontend, a Node.js Express server for model and vector-database interactions, a document collector service, Docker and cloud deployment assets, an embeddable chat widget, and a browser extension. The core workflow is document ingestion followed by chat with source citations, but the same workspace can run agents, no-code agent flows, custom skills, memories, scheduled prompts, dynamic model routing, and multimodal interactions.

The project supports local models through Lemonade and llama.cpp, hosted providers such as OpenAI, Anthropic, Bedrock, Gemini, and OpenRouter, and multiple vector stores including LanceDB, PGVector, Pinecone, Chroma, Weaviate, Qdrant, and Milvus. The README lists these as supported integrations; availability and behavior can vary by deployment. It also lists built-in browser and local speech capabilities, plus an API for custom integrations.

## Deployment And Governance

Desktop builds target macOS, Windows, and Linux. The Docker edition adds multi-user access controls, permissioning, embeddable chat, and production-oriented deployment paths for cloud providers. The README also documents a telemetry feature that sends anonymous installation, document-event, vector-database, model-provider, and chat-event metadata. It says users can disable telemetry with `DISABLE_TELEMETRY` or in the application; external model, embedding, vector, and model-CDN connections can still occur based on configuration.

## Practical Takeaway

AnythingLLM is a broad application surface for teams that want a ready-made private RAG and agent workspace rather than a narrow SDK. The tradeoff is architectural breadth: the monorepo includes UI, API, document processing, deployment, and integrations, so it is less minimal than a single-purpose retrieval component.

## See Also

- [Model Context Protocol (MCP)](../browser-and-mcp-tooling/model-context-protocol-overview.md)
- [HybridRAG: Combining Knowledge Graphs and Vector Retrieval](../agent-memory-systems/hybridrag-system.md)
- [Obot](obot.md)
