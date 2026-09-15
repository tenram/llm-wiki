# Docling

> Source: https://www.docling.ai/ ; https://github.com/docling-project/docling
> Collected: 2026-07-31
> Published: Unknown

Docling is an open-source document processing framework, created by IBM Research Zurich, that converts messy documents into structured data for downstream AI and RAG processing.

## Features

- **Multi-format input**: PDF, DOCX, PPTX, XLSX, HTML, EPUB, audio (WAV, MP3), video (MP4, MOV, MKV, WebM), email (EML, MSG), images, LaTeX, plain text, ODF, plus specialized formats (XBRL financial reports, JATS articles, USPTO patents, Box Notes)
- **Intelligent extraction**: page layout analysis, reading-order detection, table structure recognition (including complex tables), formula handling (LaTeX conversion), code block detection, image classification
- **OCR** for scanned pages via customizable OCR engines
- **Unified format**: converts everything into a standardized `DoclingDocument` representation
- **Export formats**: Markdown, HTML, JSON, DocLang, DocTags
- **AI framework integration**: native support for LangChain, LlamaIndex, Crew AI, Haystack
- **Local/offline processing** for sensitive data
- **Visual language model support**: compatible with models like GraniteDocling
- Both CLI and programmatic (Python library) interfaces, plus a managed service

64k+ GitHub stars, hosted under the LF AI & Data Foundation, MIT licensed.
