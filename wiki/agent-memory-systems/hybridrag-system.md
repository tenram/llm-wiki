# HybridRAG: Combining Knowledge Graphs and Vector Retrieval

> Sources: Abhishek Biswas, Unknown date; Hybrid_rag_simulation, Unknown date; washaqamons22d04 (Medium), Unknown date; CocoIndex, Unknown date; respan.ai, Unknown date; ArcadeDB, Unknown date; Neo4j, Unknown date
> Raw: [Building a HybridRAG System](../../raw/agent-memory-systems/hybridrag-system.md); [Hybrid RAG Neo4j Chatbot Guide](../../raw/agent-memory-systems/hybrid-rag-neo4j-chatbot-guide.md); [CocoIndex + Kuzu Knowledge Graphs](../../raw/agent-memory-systems/cocoindex-kuzu-knowledge-graphs.md); [Chroma vs Neo4j](../../raw/agent-memory-systems/chroma-vs-neo4j.md)

## Overview

A retrieval architecture combining VectorRAG (embedding similarity search) and GraphRAG (structured entity/relationship queries) into one pipeline, aiming to cover both fact-lookup (extractive) and synthesis-style (abstractive) queries better than either method alone.

## Pipeline

Documents are chunked, embedded, and stored in a vector index. In parallel, a two-stage prompting process extracts entities and relationships into a Neo4j graph or similar store such as ArcadeDB. At query time, results from both stores are merged into context passed to the final generator. LangChain orchestrates the pipeline; evaluation uses faithfulness and answer-relevance metrics.

This vector+graph combination is conceptually adjacent to memory systems like [OB1](ob1.md) (vector-centric) and [RightMemory](rightmemory.md) (graph/tree-centric); HybridRAG explicitly argues for combining both rather than choosing one.

## A Second Implementation: Vector + Cypher-Templated Graph

A separate client build applies the same two-store idea to a document-and-graph-rich domain: document embeddings live in a vector store, while an existing graph is queried through Cypher templates for relational facts documents cannot surface. The notable addition here is a **dual grounding gate** — answers must pass separate document-based and graph-based checks before being returned.

## Real-Time / Incremental Graph Construction

CocoIndex + Kuzu tackles the construction side rather than the retrieval side: a dataflow engine extracts summarized nodes and relationships from documents, then streams them into a lightweight graph database with live updates as documents change. This complements the HybridRAG variants above, which assume the graph already exists.

## Choosing a Vector/Graph Store

For teams picking backing stores rather than architecture, [Chroma vs Neo4j](../../raw/agent-memory-systems/chroma-vs-neo4j.md) frames it as prototyping-simplicity versus production graph maturity — i.e. the same VectorRAG-vs-GraphRAG tradeoff HybridRAG argues against choosing between, but from a pick-one-store buyer's perspective.

The `Hybrid_rag_simulation` repository reinforces the pattern as a working prototype rather than a paper-only idea.

## See Also

- [OB1](ob1.md)
- [RightMemory](rightmemory.md)
