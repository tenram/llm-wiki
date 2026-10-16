# faster-whisper on AMD Strix Halo

> Source: https://github.com/nabe2030/faster-whisper-rocm-strix-halo
> Collected: 2026-10-05
> Published: Unknown

Drop-in recipe for Ubuntu 26.04 + ROCm 7.2.2 + CTranslate2 v4.7.1 official wheel. No source build is required.

The repository reports testing on a GMKtec EVO-X2 with a Ryzen AI Max+ 395, Radeon 8060S (`gfx1151`), and 96 GB UMA VRAM. It reports Whisper large-v3 at about 11.5x realtime for an English 11-second clip and 6.56x realtime for a 30 minute 44 second Japanese recording.

The source states that CTranslate2 v4.7.1's ROCm wheel includes `gfx1151` kernels, while AMD's ROCm 7.2.2 packages provide runtime support. It recommends Ubuntu's inbox amdgpu driver and says `HSA_OVERRIDE_GFX_VERSION` is not needed for this setup.

For Japanese long-form transcription, the source reports that `vad_filter=False` and `condition_on_previous_text=False` improved throughput and reduced observed hallucinations and dropped segments in its test. The author says this has not been systematically tested outside English and Japanese.

Known limitations include no tests over one hour, no formal Japanese word-error-rate measurement, no speaker diarization, no testing of concurrent workloads, and testing on one Strix Halo platform only.
