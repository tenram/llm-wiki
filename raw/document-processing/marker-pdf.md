# marker-pdf

> Source: https://pypi.org/project/marker-pdf/
> Collected: 2026-07-11
> Published: 2026-01-31 (v1.10.2)

Current version 1.10.2 (released January 31, 2026). Maintainer: Vik Paruchuri. License: GNU GPL v3.0-or-later.

A Python package that converts documents to Markdown, JSON, chunks, or HTML, emphasizing speed and accuracy. Supported input types: PDF, images, PPTX, DOCX, XLSX, HTML, EPUB, in all languages. Formats tables, forms, equations (LaTeX), inline math, links, references, and code blocks; extracts and saves images; removes headers, footers, and other page artifacts. Has a beta structured-extraction mode outputting to a JSON schema, and can optionally call an LLM to boost accuracy.

Architecture: a modular pipeline of Providers, Builders, Processors, and Renderers, exposed through configurable converters such as `PdfConverter`, `TableConverter`, `OCRConverter`, and `ExtractionConverter`.

Requirements: Python 3.10+, PyTorch; GPU, CPU, or Apple MPS supported; a `[full]` extras install adds support for non-PDF formats. Optional LLM backends: Gemini (default), Google Vertex, Ollama, Claude, OpenAI, Azure OpenAI.

Performance claim: benchmarks favorably against cloud services like Llamaparse and Mathpix, with a projected throughput of 25 pages/second on an H100 during batch processing.
