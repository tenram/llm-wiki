# PyMuPDF

> Sources: Artifex Software / PyMuPDF project, Unknown date
> Raw: [PyMuPDF](../../raw/document-processing/2026-09-30-pymupdf.md)

## Overview

PyMuPDF is a high-performance Python library built on the MuPDF C engine for extracting, rendering, converting, editing, and analyzing PDF and related documents. It offers low-level layout and metadata control without mandatory external dependencies and adds LLM-oriented extraction through PyMuPDF4LLM.

## Core capabilities

The library handles PDF derivatives, EPUB, CBZ, MOBI, FB2, SVG, text, Markdown, and images. PyMuPDF Pro adds Microsoft and Korean Office formats. APIs cover text and layout metadata, tables, images, rendering, OCR through Tesseract data, annotations, redaction, forms, encryption, links, bookmarks, metadata, page editing, merging, splitting, and PDF creation.

PyMuPDF4LLM exports Markdown, JSON, or text with multi-column reading order and page chunking, making it suitable for local RAG preprocessing. PyMuPDF runs locally and supports air-gapped workflows, but the project is AGPL-3.0 with separate commercial licensing from Artifex. PyMuPDF Pro is a separate commercial extension.

## Performance and concurrency

The project reports 10-50x extraction and 100x-or-more rendering improvements over pure-Python libraries in typical benchmarks, though these claims are workload-dependent. MuPDF is not safe for multithreaded use; multiprocessing with independent document handles is the recommended parallelization strategy. Reusing a `TextPage` can accelerate repeated extraction from one page.

## Comparison

PyMuPDF is a focused, fast PDF engine. [Docling](docling.md) provides a broader document-understanding pipeline with layout analysis, unified document representation, OCR, VLM support, and integrations across many document and media formats. [marker-pdf](marker-pdf.md) is another structured conversion alternative with a different license and pipeline emphasis.

## See Also

- [Docling](docling.md)
- [marker-pdf](marker-pdf.md)
