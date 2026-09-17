# Chatterbox TTS

> Sources: Resemble AI, 2025
> Raw: [Chatterbox TTS](../../raw/speech-synthesis/2026-09-17-chatterbox-tts.md)

## Overview

A family of state-of-the-art open-source text-to-speech models by Resemble AI, spanning a 110M CPU-runnable nano model to a 500M multilingual model supporting 23+ languages. All support zero-shot voice cloning from a reference clip and include built-in imperceptible watermarking.

## Model family

| Model | Size | Languages | Key Features |
|-------|------|-----------|--------------|
| Turbo | 350M | English | Single-step decoder (10→1 steps), native paralinguistic tags (`[laugh]`, `[chuckle]`) |
| Nano | 110M | English | Turbo architecture; 3x realtime on 8 CPU cores; on-device inference |
| Multilingual V3 | 500M | 23+ | Improved speaker similarity, reduced hallucinations, more natural cross-language speech |
| Single Language Pack | 500M each | 6 dedicated finetunes | Chinese, Latam/Spain Spanish, BR/PT Portuguese, Hindi |

## Notable engineering

- **Single-step decoder:** Turbo distilled the speech-token-to-mel decoder from 10 steps to 1, cutting compute/VRAM while retaining high-fidelity output.
- **Paralinguistic tags** are native to Turbo/Nano — `[cough]`, `[laugh]`, `[chuckle]` — for realism in voice agents and creative workflows.
- **Perth watermarking:** every generated file carries Resemble's Perceptual Threshold watermark, surviving MP3 compression and editing with ~100% detection accuracy.

## Usage notes

Reference clip language must match the `language_id` tag or outputs inherit the accent of the reference. Defaults (`exaggeration=0.5`, `cfg_weight=0.5`) work across languages; expressive speech wants lower `cfg_weight` (~0.3) and higher `exaggeration` (~0.7).

## Evaluation

Chatterbox Turbo was evaluated against ElevenLabs Turbo v2.5, Cartesia Sonic 3, and VibeVoice 7B using Podonos' reproducible subjective evaluation suite.