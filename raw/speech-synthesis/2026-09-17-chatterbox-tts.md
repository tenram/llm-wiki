# Chatterbox TTS

> Source: https://github.com/resemble-ai/chatterbox
> Collected: 2026-09-17
> Published: Unknown

A family of state-of-the-art, open-source text-to-speech models by Resemble AI. 26.5k stars. SoTA open-source TTS.

## Model Zoo

| Model | Size | Languages | Key Features | Best For |
|-------|------|-----------|--------------|----------|
| Chatterbox-Turbo | 350M | English | Paralinguistic Tags (`[laugh]`), Lower Compute/VRAM | Zero-shot voice agents, Production |
| Chatterbox-Nano | 110M | English | Same architecture as Turbo, runs on CPU (3x realtime on 8 cores) | On-device / CPU inference |
| Chatterbox-Multilingual V3 | 500M | 23+ | Improved speaker similarity, reduced hallucinations, more natural multilingual speech | Global applications, localization, cross-language voice cloning |
| Single Language Pack | 500M each | 6 dedicated finetunes | Language/region-specific quality control | Priority languages, dialect-sensitive apps |
| Chatterbox | 500M | English | CFG & Exaggeration tuning | General zero-shot TTS with creative controls |

## Latest Release: Chatterbox Multilingual V3

The latest general-purpose multilingual TTS model. Keeps the same 0.5B model size while improving speaker similarity, reducing hallucinations, and producing more natural, conversational speech across languages. Alongside V3, the Single Language Pack provides dedicated finetunes for priority languages (Chinese, Latam Spanish, Brazilian Portuguese, Spain Spanish, Portugal Portuguese, Hindi).

## Chatterbox-Turbo

Built on a streamlined 350M parameter architecture for low-latency English voice agents. Distilled speech-token-to-mel decoder reduces generation from 10 steps to one while retaining high-fidelity audio. Paralinguistic tags (`[cough]`, `[laugh]`, `[chuckle]`) are native.

## Chatterbox-Nano

Shares Turbo's architecture in an even smaller 110M package for the most resource-constrained deployments. Targets on-device and CPU inference, running 3x faster than realtime on 8 CPU cores, with the same single-step decoder and paralinguistic tag support.

## Installation

```
pip install chatterbox-tts
```

Developed and tested on Python 3.11 on Debian 11; dependencies pinned in pyproject.toml.

## Usage

```python
from chatterbox.tts_turbo import ChatterboxTurboTTS
model = ChatterboxTurboTTS.from_pretrained(device="cuda")
wav = model.generate(text, audio_prompt_path="your_10s_ref_clip.wav")
```

Nano loads through the same `ChatterboxTurboTTS` class with `nano=True`. Multilingual via `ChatterboxMultilingualTTS.from_pretrained(device=device, t3_model="v3")` with `language_id` parameter.

## Supported Languages (Multilingual)

Arabic, Danish, German, Greek, English, Spanish, Finnish, French, Hebrew, Hindi, Italian, Japanese, Korean, Malay, Dutch, Norwegian, Polish, Portuguese, Russian, Swedish, Swahili, Turkish, Chinese.

## Tips

- Reference clip must match the specified language tag; otherwise outputs may inherit the accent of the reference clip's language. Set `cfg_weight` to `0` to mitigate.
- Defaults (`exaggeration=0.5`, `cfg_weight=0.5`) work well for most prompts.
- Expressive/dramatic speech: lower `cfg_weight` (~0.3), increase `exaggeration` (~0.7+).

## Built-in Perth Watermarking

Every audio file includes Resemble AI's Perth (Perceptual Threshold) Watermarker — imperceptible neural watermarks that survive MP3 compression, audio editing, and common manipulations while maintaining nearly 100% detection accuracy.

## Evaluation

Chatterbox Turbo evaluated against competitive TTS systems using Podonos' standardized suite: ElevenLabs Turbo v2.5, Cartesia Sonic 3, VibeVoice 7B. Evaluation reports publicly accessible.

## Acknowledgements

Podonos, Cosyvoice, Real-Time-Voice-Cloning, HiFT-GAN, Llama 3, S3Tokenizer.