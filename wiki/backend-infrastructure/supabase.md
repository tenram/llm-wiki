# Supabase

> Sources: Supabase, Unknown date
> Raw: [Supabase](../../raw/backend-infrastructure/supabase.md)

## Overview

Supabase is an open-source "Postgres development platform" providing Firebase-like developer ergonomics (auth, storage, realtime, auto-generated APIs) on top of a fully managed PostgreSQL database, rather than a proprietary backend.

## Architecture

Built from separately-maintained open-source components: PostgreSQL (core data), PostgREST (auto-generated REST/GraphQL APIs), GoTrue (JWT auth), a Realtime service (Elixir, WebSocket subscriptions), Kong (API gateway), and an S3-compatible storage layer with permissions enforced in Postgres itself. Ships an embeddings toolkit for AI/vector workloads. Official client libraries cover JavaScript, Python, Flutter, and Swift; community SDKs extend to Go, Rust, and C#.

## Relevance to This Wiki

Supabase appears in this wiki primarily as infrastructure other tools build on: [HybridRAG](../agent-memory-systems/hybridrag-system.md)'s Neo4j-chatbot variant uses it (interchangeably with Pinecone) as the vector-embedding store for document retrieval.

## See Also

- [HybridRAG System](../agent-memory-systems/hybridrag-system.md)
