# Gotenberg

> Sources: Gotenberg project, Unknown date
> Raw: [Gotenberg README](../../raw/document-processing/2026-10-13-gotenberg.md)

## Overview

Gotenberg is a Docker-based HTTP API for converting documents to PDF. Files are sent via `multipart/form-data` and a PDF is returned, abstracting away Chromium, LibreOffice, and font management so clients do not have to run or configure those tools themselves. It is production-deployed by thousands of companies and adopted by notable open-source projects.

## Operation Model

Unlike library-based converters such as [marker-pdf](marker-pdf.md) or [Docling](docling.md), Gotenberg is a service: run `docker run -p 3000:3000 gotenberg/gotenberg:8`, then POST to endpoints under `/forms/...`. For example, a URL-to-PDF conversion is `POST /forms/chromium/convert/url` with a `url` form field, writing the response to a PDF file.

## Conversion Capabilities

- HTML, URL, and Markdown to PDF via headless Chromium.
- Office documents to PDF via LibreOffice, covering 100+ formats.
- PDF manipulation: merge, split, rotate, flatten.
- PDF decoration and protection: watermark, stamp, encrypt.
- PDF/A and PDF/UA compliance.
- Screenshots of URLs and HTML.
- Read/write PDF metadata and bookmarks.

## See Also

- [marker-pdf](marker-pdf.md) — library-based PDF/DOCX/PPTX-to-Markdown converter, complementary to Gotenberg's document-to-PDF service.
- [Docling](docling.md) — broader document-to-structured-data framework (MIT-licensed).
