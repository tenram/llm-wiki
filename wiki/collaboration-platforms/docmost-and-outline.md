# Docmost and Outline

> Sources: Docmost README, 2026-10-19; Outline README, 2026-10-19
> Raw: [Docmost](../../raw/collaboration-platforms/2026-10-19-docmost.md); [Outline](../../raw/collaboration-platforms/2026-10-19-outline.md)

## Overview

Docmost and Outline are open-source collaborative knowledge-base products aimed at teams that need a wiki, documentation, and real-time editing. Both provide hosted options and self-hosting paths, but their repository descriptions emphasize different tradeoffs: Docmost highlights a broad documentation feature set and an AGPL core with separately licensed enterprise code, while Outline emphasizes a polished React/Node.js knowledge base, container deployment, contributor workflow, and a BSL 1.1 license.

## Product Scope

Docmost presents itself as an alternative to Confluence and Notion. Its README lists real-time collaboration, spaces, permissions, groups, comments, page history, search, attachments, embeds, diagrams, and translations. Diagrams include Draw.io, Excalidraw, and Mermaid.

Outline presents itself as a fast, collaborative team knowledge base built with React and Node.js. Its README focuses less on a feature inventory and more on the hosted product, self-hosting documentation, the source repository, and development practices.

## Deployment and Operations

Both projects point users to hosted offerings and documentation for self-hosting. Outline explicitly publishes release and nightly container images and directs production operators to its hosting guide. Docmost directs users to its documentation and cloud pricing page, while its repository structure includes Docker and application packages.

## Architecture and Development

Outline identifies React and Node.js as its primary application technologies and points contributors to a high-level architecture document. It uses categorized development logs, JSON production logs, Vitest tests, and Sequelize migrations. Its README says API endpoints and authentication should be thoroughly tested, without aiming for complete unit-test coverage.

Docmost's README is product-focused. It identifies documentation, development guidance, and the separation between core and enterprise code, but does not provide an equivalent architecture or testing overview in the captured source.

## Licensing

Docmost core is AGPL-3.0, while enterprise directories are covered by the project's enterprise license. Outline is BSL 1.1. These are materially different licensing models, so deployment and modification decisions require checking the current license text and the exact code paths used; the README summaries alone are not a substitute for legal review.

## Selection Notes

- Prefer Docmost when the priority is an open-source collaborative wiki with an explicitly listed documentation feature set, including diagrams, spaces, comments, attachments, embeds, and translations.
- Prefer Outline when the priority is its React/Node.js application model, documented container images, hosted service, and contributor-oriented development conventions.
- Compare the licenses before adopting either project. Docmost separates AGPL core from enterprise code; Outline uses BSL 1.1.

## See Also

- [Mattermost](mattermost.md) - open core self-hosted collaboration platform centered on chat, automation, calling, and AI.
