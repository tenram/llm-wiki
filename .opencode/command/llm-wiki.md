---
description: Ingest new content into the wiki (raw/ + wiki/). Usage: /llm-wiki <URL or pasted source>
---

use skill karpathy-llm-wiki

Run a full Ingest on the following source:

$ARGUMENTS

Follow the skill's Ingest workflow exactly:

1. **Fetch (raw/)** — Get the source (fetch the URL, or use pasted text). Pick or create the most relevant topic subdirectory. Save as `raw/<topic>/YYYY-MM-DD-descriptive-slug.md` with the metadata header from `.opencode/skills/karpathy-llm-wiki/references/raw-template.md`. Preserve the original text.
2. **Compile (wiki/)** — Determine placement: merge into an existing article with the same core thesis, or create a new article in the most relevant topic. Use `.opencode/skills/karpathy-llm-wiki/references/article-template.md`. Resolve factual conflicts with source attribution.
3. **Cascade updates** — Scan same-topic articles and `wiki/index.md` entries for affected content; refresh Updated dates on every materially affected article.
4. **Post-ingest** — Update `wiki/index.md` entries for every touched article, then append the ingest entry to `wiki/log.md` per the skill format.
5. **Sync READMEs** — Run `python3 scripts/sync-readmes.py` to regenerate the repo-root and wiki README mirrors from the index.

Do not skip steps. If the source is a URL, fetch it first; if pasted content, use it directly. If $ARGUMENTS is empty, ask what to ingest.