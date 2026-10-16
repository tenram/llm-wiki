# ROCm-Whisper-API

> Source: https://github.com/jjajjara/rocm-whisper-api
> Collected: 2026-10-05
> Published: Unknown

A Dockerized API server for OpenAI's Whisper, optimized for AMD GPUs (ROCm). This project simplifies the deployment and utilization of the Whisper model for speech-to-text transcription on AMD's accelerated hardware.

The container uses `rocm/pytorch:rocm6.3.4_ubuntu24.04_py3.12_pytorch_release_2.4.0`.

`HSA_OVERRIDE_GFX_VERSION` must be specified when an AMD GPU requires it for ROCm compatibility. The repository gives `11.0.0` for AMD Radeon 780M. `WHISPER_MODEL` selects the loaded model; development used `base`, while `small`, `medium`, and `large` are alternatives.

The Docker Compose example exposes port 8080 and passes `/dev/kfd` and `/dev/dri` to the container. It accepts transcription uploads at:

```text
curl -X POST -F "file=@test.m4a" http://localhost:8080/transcribe
```
