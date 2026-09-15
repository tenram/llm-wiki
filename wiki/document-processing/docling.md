# Docling

> Sources: IBM Research Zurich / Docling project, Unknown date
> Raw: [Docling](../../raw/document-processing/docling.md)

## Overview

An open-source document processing framework converting messy, mixed-format documents into structured data for downstream AI/RAG pipelines. Compared to [marker-pdf](marker-pdf.md), Docling covers a much broader format surface (including audio, video, email, and financial/patent formats) and is backed by IBM Research rather than a single maintainer.

## Capabilities

Layout analysis, reading-order detection, table structure recognition, formula-to-LaTeX conversion, code block detection, and image classification feed a unified `DoclingDocument` representation, exportable to Markdown, HTML, JSON, DocLang, or DocTags. OCR handles scanned pages. Native integrations exist for LangChain, LlamaIndex, Crew AI, and Haystack, and it supports fully local/offline processing plus visual-language-model-assisted parsing (e.g. GraniteDocling).

## Format Coverage vs. marker-pdf

| | Docling | marker-pdf |
|---|---|---|
| Core formats | PDF, DOCX, PPTX, XLSX, HTML, EPUB | PDF, DOCX, PPTX, XLSX, HTML, EPUB (same core set) |
| Extended formats | Audio, video, email, LaTeX, ODF, XBRL, JATS, patents | — |
| LLM-boosted accuracy | Via VLM support (GraniteDocling) | Optional LLM call (Gemini, Vertex, Claude, OpenAI, etc.) |
| License | MIT | GPL v3.0-or-later |
| Backer | IBM Research / LF AI & Data Foundation | Vik Paruchuri |

Both target the same problem — getting documents into an AI-consumable structured form — but Docling trades marker-pdf's narrower, benchmarked-for-speed focus for broader format support and enterprise document types.

## See Also

- [marker-pdf](marker-pdf.md)
