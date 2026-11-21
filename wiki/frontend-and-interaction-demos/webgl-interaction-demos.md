# WebGL Interaction Demos

> Sources: Houmahani Kane / Codrops, Unknown date; Guillermo Rauch, Unknown date; Codrops, Unknown date
> Raw: [Atmospheric Depth Gallery](../../raw/frontend-and-interaction-demos/2026-11-15-codrops-depth-gallery.md); [vinyl](../../raw/frontend-and-interaction-demos/2026-11-15-vinyl.md); [Gooey Sticky Menu](../../raw/frontend-and-interaction-demos/2026-11-15-gooey-sticky-menu.md)

## Overview

These three repositories are small, focused browser experiments that use the platform directly or with a narrow rendering stack: a Three.js depth gallery, a physical record-player simulation, and a WebGL2 gooey menu driven by scroll and shader geometry.

## Interaction patterns

The Atmospheric Depth Gallery maps scroll velocity and image-derived palettes to a mood-driven Three.js presentation. Vinyl cuts and presses audio into a simulated spiral groove, then reads it through a stylus model in an AudioWorklet. Gooey Sticky Menu keeps semantic HTML for layout and links while a canvas renders liquid strands, picture deformation, text, and material changes.

## Engineering lessons

The projects make expensive effects conditional: they cap pixels or visible objects, redraw only when state changes, isolate audio or shader work, and provide fallbacks or reduced-motion paths where applicable. They also document how layout, simulation state, and rendering coordinates stay synchronized.

## Practical takeaway

The examples are reference implementations for effect architecture, not drop-in components. Their strongest reusable idea is to keep the DOM or source data authoritative and derive the visual layer from it. The related [Physical and Deformable Web Experiments](physical-and-deformable-web-experiments.md) extends this pattern to page turning, physical media, and non-linear image-card transitions.
