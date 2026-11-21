# VibeVoice-ASR with ROCm and Docker

> Sources: cool9203, 2026-10-05
> Raw: [VibeVoice-ASR ROCm and Docker discussion](../../raw/speech-recognition/vibevoice-asr-rocm-discussion.md)

## Overview

This Hugging Face discussion records a community deployment path for Microsoft's `VibeVoice-ASR` model on AMD ROCm using Docker. The model page identifies the model as MIT-licensed ASR software supporting 51 languages.

## Deployment Steps

The discussion recommends checking the installed ROCm version, starting from `rocm/pytorch:rocm7.1_ubuntu24.04_py3.12_pytorch_release_2.9.1`, and exposing `/dev/kfd` and `/dev/dri` to the container. It also adds the `video` group, uses host networking, and allocates shared memory for the container.

Inside the container, the author installs the ROCm fork of Flash Attention with `FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE"`, installs VibeVoice, and starts the Gradio ASR demo with the same environment variable.

## Source Status

This is a user-contributed discussion, not an official Microsoft installation guide. Treat the image tag, package compatibility, and command sequence as a starting point to verify against current ROCm and VibeVoice releases.

## See Also

- [Vexa](vexa.md)
