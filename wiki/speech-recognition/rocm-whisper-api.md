# ROCm Whisper API

> Sources: jjajjara, 2026-10-05
> Raw: [ROCm-Whisper-API](../../raw/speech-recognition/rocm-whisper-api.md)

## Overview

ROCm-Whisper-API is a Dockerized HTTP service for OpenAI Whisper on AMD GPUs. It packages a ROCm-enabled PyTorch image, configurable Whisper model selection, and an upload endpoint for transcription.

## Deployment Pattern

The repository uses `rocm/pytorch:rocm6.3.4_ubuntu24.04_py3.12_pytorch_release_2.4.0`. Docker Compose passes `/dev/kfd` and `/dev/dri` into the container and exposes port 8080. The example endpoint is `POST /transcribe` with a multipart audio file.

`HSA_OVERRIDE_GFX_VERSION` is supplied for hardware that needs a ROCm compatibility override. The example uses `11.0.0` for Radeon 780M. `WHISPER_MODEL` selects models such as `base`, `small`, `medium`, or `large`.

## Limitations

The source is a deployment recipe, not a benchmark or a security guide. GPU compatibility, model memory use, authentication, and production request limits require separate validation.

## See Also

- [faster-whisper on AMD Strix Halo](faster-whisper-rocm-strix-halo.md)
- [VibeVoice-ASR with ROCm and Docker](vibevoice-asr.md)
