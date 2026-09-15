# Bellingcat Tool Suite

> Sources: Bellingcat, Unknown date
> Raw: [Bellingcat: auto-archiver and tool suite](../../raw/osint-tools/bellingcat-tools.md)

## Overview

Bellingcat, an open-source investigative journalism collective, maintains a suite of Python/JS tools supporting digital investigations: verifiable web archiving, GitHub OSINT, phone-number-to-Telegram lookups, shadow-based geolocation, and Jupyter notebooks for command-line investigative techniques.

## auto-archiver

The most substantial tool: ingests URLs from CSV, Google Sheets, or CLI, and archives social media posts, videos, images, and webpages to local storage, S3, or Google Drive, generating CSV status reports and optionally writing results back to Google Sheets. Installable via Docker or pip; requires an orchestration config file. Designed for verifiable, auditable archival, a common OSINT/fact-checking requirement when source content may later be deleted or altered.

## Other Notable Tools

octosuite (GitHub data analysis), telegram-phone-number-checker, ShadowFinder (shadow-based geolocation), ukraine-timemap (civilian harm documentation), and open-source-research-notebooks (CLI-based investigation techniques for researchers/fact-checkers).

## See Also

- [auto-archiver](https://github.com/bellingcat/auto-archiver)
