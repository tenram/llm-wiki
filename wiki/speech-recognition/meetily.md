# Meetily

> Sources: Zackriya Solutions, Unknown date
> Raw: [Meetily README](../../raw/speech-recognition/2026-11-21-meetily.md)

## Overview

Meetily is a privacy-first, open-source meeting assistant for Windows, macOS, and Linux. It captures audio, transcribes locally with Whisper or Parakeet, and generates summaries using a local model by default. Its stated boundary is that recordings and transcripts remain on the device unless a user deliberately sends transcript text to a cloud provider for summarization.

## Architecture And Features

The application uses a Tauri shell with a Rust backend and Next.js frontend. It supports real-time and imported audio, local transcription, speaker-related features in the commercial edition, multiple summary providers including Ollama and OpenAI-compatible endpoints, and a plain self-hosted workflow. Packaged support differs by operating system; Linux is documented primarily as a source-build or installer path.

## Privacy Boundary

The README distinguishes local transcription and storage from optional cloud summarization. That is a useful deployment distinction, but “local first” does not by itself prove that every build, dependency, update check, or optional integration is offline. Teams handling sensitive meetings should inspect the selected build and network behavior before adoption.

## See Also

- [Vexa](vexa.md)
- [ROCm Whisper API](rocm-whisper-api.md)
- [Faster Whisper on ROCm](faster-whisper-rocm-strix-halo.md)
