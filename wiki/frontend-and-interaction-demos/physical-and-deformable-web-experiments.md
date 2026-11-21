# Physical and Deformable Web Experiments

> Sources: Codrops, Unknown date; dmtrbrl, Unknown date
> Raw: [Lookbook Hover Effects](../../raw/frontend-and-interaction-demos/2026-11-21-lookbook-hover-effects.md); [LeafThrough](../../raw/frontend-and-interaction-demos/2026-11-21-leafthrough.md); [Discography](../../raw/frontend-and-interaction-demos/2026-11-21-discography.md)

## Overview

These projects show three ways to make browser interfaces feel physical: WebGL and GSAP transitions for image cards, a reusable three.js magazine with bending pages, and a 3D CD browsing experience that combines cases, discs, booklets, and audio previews.

## Interaction Patterns

Lookbook Hover Effects provides eight non-linear card reveals, mostly using GSAP and WebGL, with a CSS `clip-path` variation and a simple static-server setup. LeafThrough packages a 3D page-turning magazine for vanilla JavaScript, React, Vue, Svelte, Web Components, and existing three.js scenes. It includes drag, click, keyboard, screen-reader descriptions, reduced-motion behavior, a plain fallback, page preloading, and unloading for large magazines. Discography uses three.js and Solid to turn album browsing into a physical object workflow: open a jewel case, read a booklet through LeafThrough, and play short previews.

## Engineering Lessons

The strongest shared pattern is to keep content and accessibility data authoritative outside the visual effect. LeafThrough retains page descriptions in the DOM and has a plain view; Discography keeps collection metadata and source provenance in JSON; Lookbook’s variations are small, inspectable demos. The effects are reference implementations, not drop-in components, and their performance, licensing, and browser support need project-specific verification.

## See Also

- [WebGL Interaction Demos](webgl-interaction-demos.md)
- [Modern Web Guidance](../dev-tools/modern-web-guidance.md)
- [AI for UI Skills](../claude-code-ecosystem/ai-for-ui-skills.md)
