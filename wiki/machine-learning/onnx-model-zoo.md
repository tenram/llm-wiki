# ONNX Model Zoo

> Sources: ONNX (Apache-2.0), 2026-10-01
> Raw: [ONNX Model Zoo](../../raw/machine-learning/onnx-model-zoo.md)

## Overview

The ONNX Model Zoo was a curated collection of pre-trained models published in ONNX, the open interchange format that defines a common operator set and a common file format so a model trained in one framework runs on any ONNX-compatible runtime. Its durable contribution is not the model files — those moved to Hugging Face and Git LFS downloads ended July 1st, 2025 — but the pattern it demonstrated: ship a pre-trained model together with serialized test data and reference outputs, so every backend can verify it reproduces the expected numbers on first run.

## ONNX as an Interchange Format

ONNX is a standard format for representing machine learning models, supported by a broad community of partners. It pins down two things: a common set of operators and a common file format. That combination is what lets AI developers move models across frameworks, tools, runtimes, and compilers without reimplementing or re-validating them. The Model Zoo's premise was that "every ONNX backend should support running the models out of the box" — portability is a property of the format, so the burden shifts from the model author to the runtime.

## The Model Zoo Pattern

Models were sourced from prominent open-source repositories — `timm`, `torchvision`, `torch_hub`, and Hugging Face `transformers` — and exported to ONNX with the open-source [TurnkeyML](https://github.com/onnx/turnkeyml) toolchain. Contributions came from community members. The intent was to spread model usage to a wider audience of developers, researchers, and enthusiasts without requiring each of them to run the original training pipeline.

Three structural decisions carried the pattern:

- **Git LFS for weights.** Model files are large, so binaries were stored via [Git LFS](https://git-lfs.com/) rather than in the git object store. A plain clone fetches pointers only.
- **Validation as the publication gate.** Models land in a top-level category directory first and move into `validated/` only after accuracy checks pass. A "validated" listing is a stronger claim than a "listed" one.
- **Test data shipped with every model.** Each model directory contains `model.onnx` plus reference test data in one of two formats: serialized protobuf `TensorProto` files under `test_data_set_*` folders, or serialized NumPy archives as `test_data_*.npz`.

## Validation Contract

The shipped test data is the load-bearing part. A consumer loads the model, runs it against the bundled inputs, and compares the outputs to the stored reference tensors with `np.testing.assert_almost_equal`. Validation is thus a runnable assertion rather than a claims table — a backend that gets different numbers fails loudly on setup, before any application code is written.

The starter code is intentionally backend-agnostic. `onnx_backend` and `backend.run_model` are placeholders to be replaced with whatever framework's ONNX inference support the user has, so the same reference data validates across implementations.

## Coverage

The validated catalog was organized by task, spanning four expansion categories: Computer Vision, Natural Language Processing, Generative AI, and Graph Machine Learning. Validated task groupings:

- **Vision** — Image Classification; Object Detection & Image Segmentation; Body, Face & Gesture Analysis; Image Manipulation.
- **Language** — Machine Comprehension; Machine Translation; Language Modelling.
- **Other** — Visual Question Answering & Dialog; Speech & Audio Processing; Other interesting models.

Representative entries, chosen to show the era rather than the state of the art:

| Task | Models | Note from source |
|------|--------|------------------|
| Image classification | MobileNet, ResNet, SqueezeNet, VGG, AlexNet, GoogleNet, CaffeNet, RCNN_ILSVRC13, DenseNet-121, Inception V1/V2, ShuffleNet V1/V2, ZFNet-512, EfficientNet-Lite4 | Top-5 error from source: EfficientNet-Lite4 ~2.9%, ResNet ~3.6%, Inception V2 ~4.82%, AlexNet ~15% |
| Domain classification | MNIST-Handwritten Digit Recognition | CNTK CNN tutorial |
| Detection / segmentation | Tiny YOLOv2, SSD, SSD-MobileNetV1, Faster-RCNN, Mask-RCNN, RetinaNet, YOLO v2-coco, YOLO v3, Tiny YOLOv3, YOLOv4, DUC, FCN | YOLOv4 reported at mAP50 52.32 on COCO 2017, 41.7 FPS on a Tesla V100 |
| Body / face | ArcFace, UltraFace, Emotion FerPlus, Age and Gender Classification | ArcFace produces face embeddings; UltraFace targets edge devices |
| Image manipulation | CycleGAN (unpaired image-to-image), Super Resolution sub-pixel CNN, Fast Neural Style Transfer | Listed as papers without an ONNX link |
| Machine comprehension | BiDAF, BERT-Squad, RoBERTa, GPT-2, T5 | Transformer-era checkpoints |
| Speech & audio | Speech recognition RNN, Deep Voice, WaveNet | Papers only, no model links |
| Other | Text-to-image, time-series forecasting, DropoutNet, Neural Collaborative Filtering, hierarchical LSTM autoencoder | Papers only |

Many rows are literature references rather than downloadable checkpoints; the README marks these with a "contribute" link, inviting someone to supply the model.

## Quantization

INT8 models are not authored by hand — they are generated by [Intel Neural Compressor](https://github.com/intel/neural-compressor), an open-source Python library doing automatic accuracy-driven tuning. It implements both dynamic and static quantization for ONNX models and can express quantized models in either operator-oriented or tensor-oriented (QDQ) form. The zoo points to both a web-based UI service and code-based usage, with the UI intended to make quantization accessible without writing tuning scripts.

## Distribution Mechanics

Access was deliberately awkward at the file level and easy at the model level:

- **Git clone (not recommended).** A clone does not download models; only LFS pointers. `pip install git-lfs`, then `git lfs pull --include="[path to model].onnx" --exclude=""` for one model or `--include="*"` for all of them.
- **GitHub UI.** Navigate to the model page and click Download.
- **Model visualization.** Netron for a graphical view of each model's architecture.
- **Live demos.** A number of validated models had Hugging Face Spaces demos (`onnx/ResNet`, `onnx/VGG`, `onnx/EfficientNet-Lite4`, and others).

## Status: Deprecated, Moved to Hugging Face

The repository now carries a deprecation notice: model sharing largely transitioned to Hugging Face, which "maintains a vibrant and healthy state." The zoo is preserved for historical purposes, models are no longer available for LFS download as of July 1st, 2025, and the surviving model files are reachable at `https://huggingface.co/onnxmodelzoo`. At collection time the repo sat at 9.8k stars, 1.6k forks, 244 commits, 201 open issues.

The trajectory is the notable part. A format-plus-registry approach was superseded by a platform-plus-hub approach: the interchange format remains, but distribution, versioning, and discovery consolidated onto a single host that also runs inference demos and community fine-tunes. What survives of the zoo's contribution is the per-model validation contract, which is the one thing a hub does not standardize for you.

## See Also

- [XGBoost](xgboost.md)
- [XGBoost Imbalanced Classification Pattern](xgboost-imbalanced-classification-pattern.md)
