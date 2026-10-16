# faster-whisper on AMD Strix Halo

> Sources: nabe2030, 2026-10-05
> Raw: [faster-whisper on AMD Strix Halo](../../raw/speech-recognition/faster-whisper-rocm-strix-halo.md)

## Overview

This repository documents a no-source-build recipe for faster-whisper on AMD Strix Halo hardware. It combines Ubuntu 26.04, ROCm 7.2.2, and the official CTranslate2 4.7.1 ROCm wheel.

## Installation Model

The recipe installs ROCm from AMD's package repository and CTranslate2 from its ROCm wheel archive. It targets `gfx1151` on a Ryzen AI Max+ 395 and says the wheel includes the required kernels, so `HSA_OVERRIDE_GFX_VERSION` is not needed in this configuration. The reported test platform was a GMKtec EVO-X2 with Radeon 8060S graphics and 96 GB of unified memory.

## Reported Results

The source reports about 11.5x realtime for an English 11-second clip and 6.56x realtime for a 30-minute Japanese recording. It also reports no memory fault during the long run. For Japanese long-form audio, `vad_filter=False` and `condition_on_previous_text=False` improved throughput and reduced hallucinations and dropped segments in the author's tests.

These are single-platform measurements. The source does not provide formal Japanese word-error-rate results, tests beyond one hour, concurrent workload tests, or validation across other Strix Halo systems.

## See Also

- [ROCm Whisper API](rocm-whisper-api.md)
- [VibeVoice-ASR with ROCm and Docker](vibevoice-asr.md)
