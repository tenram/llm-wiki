# FaceForensics++

> Sources: Rössler, Cozzolino, Verdoliva, Riess, Thies, Nießner, 2019
> Raw: [FaceForensics++](../../raw/deepfake-detection/faceforensics-plusplus.md)

## Overview

An ICCV 2019 benchmark for facial-manipulation detection, built on four forgery techniques (DeepFakes, Face2Face, FaceSwap, NeuralTextures) with over 1.8 million manipulated images, an order of magnitude larger than prior public forgery datasets at the time.

## Findings and Access

Central claim: incorporating domain-specific knowledge into detection models pushes accuracy to "unprecedented" levels, even under strong compression, exceeding human detection. Includes a separately donated Google/Jigsaw DeepFakes Detection Dataset and a hidden test set for standardized benchmarking via an online leaderboard. Full dataset access requires a request form.

## FaceShifter Subset

The FaceForensics repo also hosts a FaceShifter subset where the *original FaceShifter authors* produced and contributed the manipulated videos themselves, rather than FaceForensics generating them independently. It includes a reproduced accuracy table from the FaceShifter paper's appendix, letting FaceShifter-specific detection results be compared under the same benchmark conditions as the four core techniques. Manipulation-technique details live on the external FaceShifter project page, not in this repo.

## See Also

- [Justus Thies: Tutorials & Demos](justus-thies-tutorials.md)
