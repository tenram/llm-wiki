# Gotenberg

> Source: https://github.com/gotenberg/gotenberg
> Collected: 2026-10-13
> Published: Unknown

**Gotenberg** is a Docker-based API for converting documents to PDF. Trusted in production by thousands of companies. Also adopted by notable open-source projects.

Send your files via `multipart/form-data`, get a PDF back. No need to manage Chromium, LibreOffice, or fonts yourself.

## Quick Start

```bash
docker run --rm -p 3000:3000 gotenberg/gotenberg:8
```

Convert a URL to PDF:

```bash
curl \
  --request POST http://localhost:3000/forms/chromium/convert/url \
  --form url=https://sparksuite.github.io/simple-html-invoice-template/ \
  -o invoice.pdf
```

## Features

- **HTML, URL, Markdown to PDF** via Headless Chromium
- **Office documents to PDF** via LibreOffice (100+ formats)
- **Merge, split, rotate, flatten** PDFs
- **Watermark, stamp, encrypt** PDFs
- **PDF/A and PDF/UA** compliance
- **Screenshots** of URLs and HTML
- **Read/write metadata and bookmarks**

See the [full documentation](https://gotenberg.dev/docs/getting-started/introduction).

## Contributing

Questions and feedback: [GitHub Discussions](https://github.com/gotenberg/gotenberg/discussions).
Bug reports: [GitHub Issues](https://github.com/gotenberg/gotenberg/issues).

## Sponsors

If Gotenberg powers your workflow or your business, consider [becoming a sponsor](https://github.com/sponsors/gulien).

**Historic & GitHub Sponsors**

- TheCodingMachine
- pdfme
- PDFBolt
- FileToPDF.dev

**Powered By**

- Docker
- JetBrains
