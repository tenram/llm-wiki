# The Open Graph Protocol

> Source: https://ogp.me/
> Collected: 2026-07-31
> Published: Unknown

The Open Graph protocol lets any web page become a rich object in a social graph; Facebook is the primary implementation/consumer.

## Purpose

Before Open Graph, no single standard provided comprehensive metadata for rich content representation across social platforms. Open Graph offers one unified system developers can implement instead of platform-specific formats.

## Core properties

Added to a page's HTML `<head>`:
- `og:title` — the object's name
- `og:type` — content category
- `og:image` — visual representation
- `og:url` — permanent identifier

Builds on existing technologies (RDFa, Dublin Core, microformats). Consistent metadata lets social platforms auto-extract and display titles, descriptions, images, and other context when content is shared.
