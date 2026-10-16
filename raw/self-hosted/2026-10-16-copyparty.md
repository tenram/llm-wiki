# copyparty (9001/copyparty)

> Source: https://github.com/9001/copyparty
> Collected: 2026-10-16
> Published: Unknown

## About

Portable file server with accelerated resumable uploads, dedup, WebDAV, SFTP, FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file.

- Repository: 9001/copyparty
- License: MIT
- Language: Python
- Stars: 47.1k; Forks: 1.9k; Watching: 150; Commits: 4,840 (branch `hovudstraum`)
- Topics: copyparty, file-server, file-sharing, file-upload-server, ftp-server, nas-frontend, tftp-server, webdav-server
- Mirrors: https://copyparty.eu/ (official mirror). Read-only demo: https://a.ocv.me/pub/demo/

## README (top)

**copyparty** — turn almost any device into a file server with resumable uploads/downloads using *any* web browser.

- server only needs Python (2 or 3), all dependencies optional
- protocols: http(s) // webdav // sftp // ftp(s) // tftp // smb/cifs
- android app // iPhone shortcuts
- built in Norway with contributions from not-norway

### Quickstart

Just run **copyparty-sfx.py** — that's it. The sfx is a self-extractor which unpacks an embedded `tar.gz` into `$TEMP`; a zipapp alternative has slightly worse performance.

Other install paths: pypi (`python3 -m pip install --user -U copyparty`); `copyparty.exe` (win8+) or `copyparty32.exe` (win7+); Arch (`pacman -S copyparty`); Gentoo `::guru`; Homebrew (`brew install copyparty ffmpeg`); Nix (`nix profile install github:9001/copyparty`); NixOS module; Termux (Android); a-Shell (iOS); Synology DSM; `uv tool run copyparty`; a bootable flashdrive/CD-ROM "enterprise edition"; chroot via `bin/prisonparty.sh`; bubblewrap via `bin/bubbleparty.sh`; Docker (`scripts/docker`).

Enable thumbnails (images/audio/video), media indexing, and audio transcoding by installing recommended deps: Pillow and FFmpeg (per-OS commands given for Alpine/Debian/Fedora/FreeBSD/MacOS/Windows).

Running copyparty without arguments gives everyone read/write access to the current folder; use accounts and volumes.

Recommended options: `-e2dsa` general file indexing; `-e2ts` audio metadata indexing; `-v /mnt/music:/music:r:rw,foo -a foo:bar` shares a folder readable by anyone and read-write for user `foo`.

### Mirrors

Other download locations (non-GitHub): https://copyparty.eu/ (Hetzner, Finland, official mirror): `/py` = the sfx; `/en` = English-only sfx; `/pyz` = the zipapp; `/enz` = enterprise pyz; `/cli` = online cli helptext. Do not download from sourceforge.

### At home

Make it accessible over the internet with a Cloudflare quicktunnel (`cloudflared tunnel --url http://127.0.0.1:3923`); use `--xff-hdr cf-connecting-ip` to detect client IPs correctly. With a domain, set up a permanent Cloudflare tunnel.

### On servers

Service scripts: systemd (`contrib/systemd/copyparty.service`), chroot systemd (`prisonparty.service`), Podman systemd, OpenRC (Alpine/Gentoo), rc (FreeBSD), NixOS module, nginx reverse-proxy config. Env vars understood: `NOTIFY_SOCKET` (systemd type=notify), `S6_NOTIFY_FD` (dinit / s6).

Firewall example ports: 69 tftp, 1900 ssdp, 3921 ftp, 3922 sftp, 3923 http/https, 3945 smb, 3969 tftp, 3990 ftps, 5353 mdns, 12000 passive-ftp.

## Features

- backend: IPv6 + unix-sockets; multiprocessing; volumes; accounts; ftp/tftp/webdav/smb servers; qr-code; upnp/zeroconf/mdns/ssdp; event hooks / script runner; reverse-proxy support; cross-platform (Windows, Linux, Macos, Android, iOS, FreeBSD, arm32/arm64, ppc64le, s390x, risc-v/riscv64, SGI IRIX).
- upload: plain multipart (ie6 support); up2k (js, resumable, multithreaded) — no filesize limit, even on Cloudflare; stash (simple PUT filedropper); filename randomizer; write-only folders; unpost (undo/delete accidental uploads); self-destruct; race the beam (download while uploading); symlink/discard duplicates (content-matching).
- download: single files; folders as zip/tar; FUSE client (read-only).
- browser: navpane; file manager (cut/paste, delete, batch-rename); audio player (OS media controls, opus/mp3 transcoding, m3u8 playlists); image gallery with webm player and cbz manga/comics reader; textfile browser with syntax highlighting and realtime streaming of growing files; thumbnails (images via Pillow/pyvips/FFmpeg, RAW via libraw-dcraw_emu/rawpy, videos via FFmpeg, audio spectrograms via FFmpeg) with cache eviction; multilingual UI; SPA (browse while uploading).
- server indexing: locate files by contents; search by name/path/date/size; search by ID3-tags etc.
- client support: folder sync (one-way only; full sync will never be supported); curl-friendly; opengraph (discord embeds).
- markdown: viewer; editor; variables.

## Testimonials

`good enough`, `surprisingly correct`, `certified good software`, `just works`, `why`, `wow this is better than nextcloud`.

## Motivations

- inverse unix philosophy — do all the things, and do an *okay* job. Quick drop-in service to get a lot of features in a pinch.
- run anywhere, support everything. As many web-browsers and python versions as possible; minimal dependencies (optional deps add bonus features); everything plaintext so it can be proofread for malicious code; no setup — just run the sfx.
- adaptable, malleable, hackable. No build steps; modify the js/python without node.js.
- "becoming rich is specifically *not* a motivation."

## Notes / bugs / breaking changes (selected)

- Bugs: `--th-ff-jpg` may fix video thumbnails on some FFmpeg versions; `--th-ff-swr` may fix audio thumbnails; keep `up2k.db` off network shares (`--hist` / `hist` volflag / `--dbpath`); all volumes must exist on startup. Python 3.4 and older (incl. 2.7) have rare edge cases because Python didn't handle EINTR yet.
- "not my bugs": Chrome/Firefox/Windows/Android/iOS issues documented with links (e.g. Chrome folder-upload symlink issue, Firefox ~4000-small-files crash, Windows max path length).
- Breaking changes: `1.9.16` (2023-11-04) `--stats`/prometheus `cpp_bans` → `cpp_active_bans`; `1.6.0` (2023-01-29) http-api delete/move now POST; `1.5.0` (2022-12-03) new chunksize formula for files larger than 128 GiB.

## FAQ (selected)

- Name is one word: copyparty (all-lowercase) or Copyparty.
- **volflag** = per-volume configuration; **volume** = a mapping from a URL (`/music/`) to a folder on the server's filesystem.
- Block read-access unless the exact URL is known: use the `g` permission, or `chmod 111 music`.
- Link to a password-protected volume/file by adding `?pw=hunter2` (or `?pw=username:password` with `--usernames`).
- `.hist` folders hold the filesystem index, thumbnails, audio transcodes, and markdown history; move with `--hist` or the `hist` volflag.
- Can download a file to the server from a URL using hooks (`bin/hooks/wget.py`).
- "thank you for playing" = banned for malicious traffic (fix real-ip behind reverse proxies).

## Accounts and volumes

Per-folder, per-user permissions. Config files are recommended for complex setups and can be reloaded at runtime (`systemctl reload copyparty` or the `[reload cfg]` control-panel button if the user has admin in any volume).

Arguments: `-a usr:pwd` adds an account; `-v src:dst:perm:perm:...` mounts a volume. Granting the same permissions to multiple accounts: `-v .::r,usr1,usr2:rw,usr3,usr4`.

Permissions: `r` (read), `w` (write), `m` (move), `d` (delete), `.` (dots), `g` (get: download only), `G` (upget), `h` (html), `a` (admin), `A` (all = `rwmda.`).

## Packages

Arch (`pacman -S copyparty`), Gentoo `::guru`, Homebrew, Nix, NixOS module. Fedora package does not exist yet.

## Other

- Browser support: "TLDR: yes".
- Performance: "defaults are usually fine - expect `8 GiB/s` download, `1 GiB/s` upload".
- Security: discord server for announcements; CSP nonce; CORS; filekeys (prevent filename bruteforcing); dirkeys; password hashing; HTTPS.
- SFX: copyparty.exe (win8+), copyparty32.exe (win7+), copyparty.pyz zipapp.
- Dependencies: mandatory = Python; optional enable bonus features.
- HTTP API documented in `docs/devnotes.md#http-api`.
