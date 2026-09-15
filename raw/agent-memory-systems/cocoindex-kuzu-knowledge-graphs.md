# Build Real-Time Knowledge Graphs from Documents Using CocoIndex + Kuzu

> Source: https://dev.to/cocoindex/build-real-time-knowledge-graphs-from-documents-using-cocoindex-kuzu-with-llms-live-updates-n1b
> Collected: 2026-07-31
> Published: Unknown

**CocoIndex** is a high-performance data transformation engine using a dataflow programming model, enabling incremental processing and live updates for knowledge graphs. **Kuzu** is an open-source, fast, lightweight graph database that runs locally or in production.

## Document-to-graph pipeline

1. **Ingestion** — documents enter the CocoIndex framework
2. **Transformation** — for each document: generate node summaries via LLM, extract relationships via LLM-powered structured extraction
3. **Export** — relationships stream into Kuzu as queryable graph data

## Key techniques

- **Dataflow programming**: developers define transformations rather than explicit create/update/delete operations; the framework manages data operations automatically
- **LLM extraction** captures two relationship types: concept-to-concept links (e.g., "CocoIndex supports Incremental Processing") and entity mentions in documents
- **Reusability**: switching from Neo4j to Kuzu retained intermediate transformation results, enabling instant export without reprocessing

The complete pipeline is reported at roughly 200 lines of Python code.
