# tmux for Local Development

> Sources: Ian Jones / Delicious Brains, 2022-05-25
> Raw: [How to Use tmux for Remote & Local Development](../../raw/dev-tools/2026-11-21-tmux-for-local-development.md)

## Overview

tmux multiplexes independent shells into sessions, windows, and panes. The source explains its familiar remote-server resilience and argues that the same structure is useful locally: a named development workspace can be restored and revisited without rebuilding terminal windows by hand.

## Core Model

A session contains windows, and each window contains panes. The prefix key invokes commands for creating, naming, switching, splitting, resizing, zooming, detaching, and reattaching. The article uses `Ctrl+a` as a remapped prefix, while tmux defaults to `Ctrl+b`; the configuration choice is personal and should be made explicit in a team setup.

## Local Workflow

A practical layout gives each project a window and related shells or monitoring commands their own panes. Detaching leaves processes running, so a terminal can be closed and reopened without losing the workspace. `tmux-resurrect` and `tmux-continuum` extend this by restoring sessions after a reboot. The author also uses keyboard navigation, pane zoom, and Vim-style copy-mode controls to reduce pointer dependence.

## Limits

The source is a workflow tutorial, not a security or collaboration model. Restored commands can have side effects, and shared configuration should document platform differences, prefix bindings, and plugin trust.

## See Also

- [Modern Web Guidance](modern-web-guidance.md)
- [Build Your Own X](build-your-own-x.md)
