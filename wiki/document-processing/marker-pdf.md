# marker-pdf

> Sources: Vik Paruchuri, 2026-01-31 (v1.10.2)
> Raw: [marker-pdf](../../raw/document-processing/marker-pdf.md)

## Overview

A Python library converting PDFs, images, PPTX, DOCX, XLSX, HTML, and EPUB into Markdown, JSON, chunks, or HTML, prioritizing speed and layout fidelity: tables, forms, LaTeX equations, inline math, references, and code blocks are preserved; headers/footers and page artifacts are stripped.

## Architecture and Performance

Modular pipeline of Providers, Builders, Processors, and Renderers exposed via task-specific converters (`PdfConverter`, `TableConverter`, `OCRConverter`, `ExtractionConverter`). A beta structured-extraction mode outputs to a JSON schema and can optionally call an LLM (Gemini by default, or Vertex, Ollama, Claude, OpenAI, Azure OpenAI) for accuracy. Requires Python 3.10+ and PyTorch; runs on GPU, CPU, or Apple MPS. Claimed throughput: 25 pages/second on an H100 in batch mode, benchmarked favorably against Llamaparse and Mathpix. GPL v3.0-or-later licensed.

## See Also

- [Docling](docling.md) — IBM Research's broader-format alternative (adds audio/video/email/financial docs), MIT-licensed.
