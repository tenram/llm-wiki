# A Guide to Building a Hybrid RAG Neo4j Chatbot for Document-Rich Knowledge Systems

> Source: https://medium.com/@washaqamons22d04/a-guide-to-building-a-hybrid-rag-neo4j-chatbot-for-document-rich-knowledge-systems-400f9efa08dd
> Collected: 2026-07-31
> Published: Unknown

Describes a client system combining unstructured documents (PDFs, articles) with an existing Neo4j knowledge graph (hip-hop history domain) to produce document-grounded and relationally accurate answers.

## Architecture

1. **Vector database layer** — document embeddings (PDFs, URLs, articles) stored in Pinecone or Supabase for semantic search over long-form content
2. **Graph layer** — Neo4j queried via Cypher templates for relational patterns (artist connections, timelines, influences, shared appearances) that documents alone can't surface
3. **Orchestration layer** — an LLM determines query intent, retrieves from both sources, and synthesizes a response with automatic source attribution

## Key techniques

- **Content ingestion**: three sequential passes — text extraction, normalization (removing boilerplate), intelligent chunking to prevent embedding degradation
- **Hybrid retrieval workflow**: classify whether a query needs document knowledge, graph knowledge, or both; pull vector chunks and Cypher-templated graph context in parallel; combine into a cited answer
- **Quality gates**: requiring answers to pass separate document-based and graph-based grounding checkpoints, reported to meaningfully reduce hallucinations versus single-source RAG
