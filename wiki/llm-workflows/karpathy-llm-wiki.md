# Karpathy LLM Wiki

> Sources: Andrej Karpathy, `karpathy-llm-wiki`
> Raw: [Karpathy LLM Wiki](../../raw/llm-workflows/karpathy-llm-wiki.md)

## Overview

This repository operationalizes the persistent wiki pattern for LLM workflows.

## Pattern

It uses raw/, wiki/, index, log, and schema files to keep a compounding markdown knowledge base under git.

The repo is a concrete implementation of the idea Karpathy described: the LLM maintains the wiki, not a query-time RAG index.

## See Also

- [LLM Wiki Pattern](llm-wiki-pattern.md)
