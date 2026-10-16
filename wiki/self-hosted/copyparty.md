# copyparty

> Sources: 9001 (copyparty), Unknown date
> Raw: [copyparty (9001/copyparty)](../../raw/self-hosted/2026-10-16-copyparty.md)

## Overview

copyparty is a single-file, portable file server written in Python (MIT) that turns almost any device into a file server with resumable uploads and downloads from any web browser. Its stated philosophy is an "inverse unix philosophy — do all the things, and do an *okay* job": a quick drop-in service that covers a very broad feature set, with the explicit caveat that a more specialized alternative may fit a given need better. It is the most popular project in this wiki by star count (47.1k).

## Protocol Breadth

One server speaks many protocols simultaneously:

- HTTP(S) (the primary browser UI)
- WebDAV (read-write)
- SFTP
- FTP / FTPS
- TFTP (read/write)
- SMB/CIFS (unsafe, slow, not recommended for WAN)

It also supports IPv6 and unix sockets, UPnP/zeroconf/mDNS/SSDP announcement, and QR-code access.

## Uploads and Downloads

- **up2k** — JavaScript, resumable, multithreaded uploads with no filesize limit, even behind Cloudflare.
- **stash** — a simple PUT filedropper; plus a filename randomizer and write-only folders.
- **unpost** — undo/delete accidental uploads.
- **self-destruct** — uploads given a lifetime (server- or client-specified).
- **race the beam** — download files while they are still uploading.
- **dedup** — content-matching symlink/discard of duplicates.
- Folder downloads as zip/tar, and a read-only FUSE client.

## Browser Features

A file manager (cut/paste, delete, batch-rename), navpane directory tree, audio player with OS media controls and opus/mp3 transcoding, m3u8 playlists, image gallery with webm player and cbz manga/comics reader, a textfile browser with syntax highlighting and realtime streaming of growing files, thumbnails (images via Pillow/pyvips/FFmpeg, RAW via libraw/rawpy, video via FFmpeg, audio spectrograms) with cache eviction, a markdown viewer/editor with server-side variable expansion, and a multilingual UI.

## Indexing and Search

With `-e2dsa` copyparty indexes files (locate files by contents; search by name/path/date/size); `-e2ts` indexes audio metadata (ID3 tags). The index lives in `.hist/up2k.db` inside each volume by default and can be relocated with `--hist`, the `hist` volflag, or `--dbpath`.

## Accounts and Permissions

Access is per-folder, per-user. Accounts are added with `-a usr:pwd`; volumes with `-v src:dst:perm:...`. Permission letters: `r` read, `w` write, `m` move, `d` delete, `.` dotfiles, `g` get-only (download without listing), `G` upget, `h` html, `a` admin, `A` all. Password-protected resources can be linked with `?pw=` in the URL. Config files are recommended for complex setups and can be hot-reloaded.

## Extensibility

Event hooks and a script runner trigger programs on uploads/renames; handler plugins redefine behavior; identity providers (OAuth) and generic header auth replace built-in passwords; Prometheus metrics can be enabled; a version checker and self-destruct are built in.

## Deployment Footprint

The recommended distribution is a self-contained `copyparty-sfx.py` self-extractor; alternatives include PyPI, `copyparty.exe`/`.pyz`, Arch/Gentoo/Homebrew/Nix packages, Termux/a-Shell, Synology DSM, Docker, and chroot/bubblewrap wrappers (`prisonparty.sh`, `bubbleparty.sh`). Service scripts ship for systemd, Podman, OpenRC, FreeBSD rc, and NixOS.

## Limitations and Known Bugs

copyparty documents its own rough edges candidly: keep the index database off network shares; all volumes must exist at startup; Python 3.4 and older (including 2.7) have rare edge cases because Python did not yet handle EINTR; and a long "not my bugs" list covers upstream browser/OS issues (Chrome folder-symlink upload, Firefox ~4000-small-file crash, Windows max path length, Android/iOS media quirks). The testimonials page includes both praise ("certified good software", "wow this is better than nextcloud") and an unflattering Russian review, reproduced verbatim.

## See Also

- [Compass](compass.md) — service-catalog landing page, another self-hosted utility.
