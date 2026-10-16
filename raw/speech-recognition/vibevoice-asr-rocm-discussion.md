# VibeVoice-ASR ROCm and Docker Discussion

> Source: https://huggingface.co/microsoft/VibeVoice-ASR/discussions/3
> Collected: 2026-10-05
> Published: Unknown

The Hugging Face model page identifies `microsoft/VibeVoice-ASR` as an automatic-speech-recognition Transformers model licensed under MIT and supporting 51 languages.

In a community discussion, a user documents running it with ROCm and Docker. The post advises verifying the ROCm version, using a `rocm/pytorch:rocm7.1_ubuntu24.04_py3.12_pytorch_release_2.9.1` image, exposing `/dev/kfd` and `/dev/dri`, and adding the `video` group.

The post then installs AMD's flash-attention fork with `FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE"`, installs VibeVoice, and starts the Gradio ASR demo with the same environment variable. This is a user-contributed deployment note, not an official Microsoft installation guide.
