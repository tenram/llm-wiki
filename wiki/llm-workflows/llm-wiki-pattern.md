# LLM Wiki Pattern

> Sources: Andrej Karpathy, 2026-04-04; `karpathy-llm-wiki`
> Raw: [LLM Wiki](../../raw/llm-workflows/2026-04-04-llm-wiki-pattern.md)

## Overview

Karpathy proposes replacing query-time RAG with an LLM that incrementally builds and maintains a persistent wiki: a structured, interlinked set of markdown files sitting between the user and raw sources. Rather than re-deriving synthesis on every question, the LLM compiles knowledge once, keeps it current as new sources arrive, and lets cross-references and contradictions accumulate over time.

The `karpathy-llm-wiki` repository is a direct implementation of this pattern.

## Core Idea

Standard RAG retrieves relevant chunks from raw documents at query time and generates an answer fresh each time; nothing is built up between queries. The wiki pattern instead has the LLM read each new source, extract key information, and integrate it into an existing wiki: updating entity pages, revising topic summaries, flagging contradictions with prior claims, and strengthening or challenging the evolving synthesis. The wiki is a persistent, compounding artifact rather than a retrieval index.

The human's role is sourcing, exploration, and asking good questions. The LLM's role is the bookkeeping: summarizing, cross-referencing, filing, maintaining consistency. Karpathy pairs an LLM agent with Obsidian for browsing; he frames it as "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

Applicable domains include personal tracking (goals, health, journaling), long-running research, book companion wikis (in the spirit of fan wikis like Tolkien Gateway), team/business knowledge bases fed by Slack or meeting transcripts, and any accumulating-knowledge task such as competitive analysis or trip planning.

## Architecture

Three layers:

1. **Raw sources** — immutable curated documents (articles, papers, images, data). The LLM reads but never modifies these; they are the source of truth.
2. **The wiki** — LLM-generated markdown files: summaries, entity pages, concept pages, comparisons, syntheses. The LLM owns this layer entirely, creating and updating pages and maintaining cross-references.
3. **The schema** — a configuration document (e.g. CLAUDE.md, AGENTS.md) defining wiki structure, conventions, and workflows for ingesting, querying, and maintaining. This is what turns the LLM into a disciplined maintainer rather than a generic chatbot, and it co-evolves with the user over time.

## Operations

**Ingest** — drop a new source into raw/, then have the LLM read it, discuss takeaways, write a summary page, update the index, update relevant entity/concept pages elsewhere in the wiki, and append a log entry. A single source might touch 10-15 pages. Karpathy prefers ingesting one source at a time and staying involved in reviewing updates, though batch ingestion with less supervision is also viable.

**Query** — ask questions against the wiki; the LLM searches for relevant pages, reads them, and synthesizes a cited answer. Output form can vary: markdown page, comparison table, slide deck (Marp), chart, canvas. Valuable answers can be filed back into the wiki as new pages so explorations compound alongside ingested sources.

**Lint** — periodic health check for contradictions between pages, stale claims superseded by newer sources, orphan pages with no inbound links, concepts mentioned but lacking a dedicated page, missing cross-references, and data gaps fillable via web search.

## Indexing and Logging

**index.md** is content-oriented: a catalog of every wiki page with a link, one-line summary, and optional metadata, organized by category. Updated on every ingest. The LLM reads it first when answering a query, then drills into specific pages. Karpathy notes this scales well without embedding-based RAG infrastructure up to roughly ~100 sources and hundreds of pages.

**log.md** is chronological: an append-only record of ingests, queries, and lint passes. A consistent entry prefix (e.g. `## [YYYY-MM-DD] ingest | Article Title`) keeps it parseable with tools like `grep "^## \[" log.md | tail -5`.

## Optional Tooling

- [qmd](https://github.com/tobi/qmd): a local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking, available as both CLI and MCP server. Useful once the wiki outgrows what the index file alone can support.
- Obsidian Web Clipper: browser extension for converting web articles to markdown for the raw collection.
- Obsidian attachment folder settings + a bound hotkey for downloading images locally, since LLMs cannot natively read markdown with inline images in one pass (the workaround is reading text first, then viewing referenced images separately).
- Obsidian graph view for visualizing wiki connectivity, hubs, and orphans.
- Marp for generating slide decks from wiki content.
- Dataview for querying page YAML frontmatter (tags, dates, source counts) if the LLM adds it.
- The wiki as a plain git repo, giving version history, branching, and collaboration for free.

## See Also

- [Karpathy LLM Wiki](karpathy-llm-wiki.md)

## Why This Works

The maintenance burden, not the reading or thinking, is what kills most personal wikis: updating cross-references, keeping summaries current, flagging contradictions, maintaining consistency across dozens of pages. LLMs don't get bored or forget updates, and can touch many files in one pass, so the cost of maintenance approaches zero.

Karpathy connects the idea to Vannevar Bush's Memex (1945): a personal, curated knowledge store with associative trails between documents, private and actively curated, where connections between documents are as valuable as the documents themselves. Bush's unsolved problem was who performs the maintenance; the LLM solves that.

The pattern is intentionally abstract: directory structure, schema conventions, page formats, and tooling are meant to be instantiated per-domain in collaboration with the LLM rather than copied rigidly.
