# Karpathy LLM Wiki

> Source: https://github.com/Astro-Han/karpathy-llm-wiki
> Collected: 2026-08-18
> Published: Unknown

This repository operationalizes the persistent wiki pattern for LLM workflows. It uses raw/, wiki/, index, log, and schema files to keep a compounding markdown knowledge base under git.

The repo is a concrete implementation of the idea Karpathy described: the LLM maintains the wiki, not a query-time RAG index. That makes the wiki itself the durable artifact, with ingest, query, and lint steps encoded as part of the workflow.
