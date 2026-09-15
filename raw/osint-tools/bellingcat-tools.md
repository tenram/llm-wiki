# Bellingcat: auto-archiver and tool suite

> Source: https://github.com/bellingcat/auto-archiver ; https://github.com/bellingcat
> Collected: 2026-07-11
> Published: Unknown

## Org profile

Bellingcat is described on GitHub as "An independent investigative collective of researchers, investigators and citizen journalists brought together by a passion for open source research."

Pinned/featured repositories: ukraine-timemap (JavaScript, 295 stars) — a TimeMap instance documenting civilian harm in Ukraine; octosuite (Python, 1.9k stars) — a terminal toolkit for analyzing GitHub data; auto-archiver (Python, 1.1k stars, see below); telegram-phone-number-checker (Python, 1.7k stars) — identifies whether phone numbers are associated with Telegram accounts; ShadowFinder (Python, 590 stars) — locates potential shadow positions globally; open-source-research-notebooks (Jupyter Notebook, 314 stars) — notebooks enabling researchers and fact-checkers to use command-line tools for digital investigations.

## auto-archiver

A Python tool for automated, secure, and verifiable archival of web content. Ingests URLs from CSV files, Google Sheets, or the command line, and archives social media posts, videos, images, and webpages. Captured content can be enriched and stored locally or in remote destinations such as S3 buckets or Google Drive. Generates CSV reports tracking archival status and can write results back into Google Sheets.

Installation: Docker (`docker pull bellingcat/auto-archiver && docker run -it --rm -v secrets:/app/secrets bellingcat/auto-archiver --config secrets/orchestration.yaml`) or pip (`pip install auto-archiver && auto-archiver --help`). Requires an orchestration configuration file; supports batch processing with automated status reporting. 1.1k GitHub stars, 107 forks; active contribution guidelines.
