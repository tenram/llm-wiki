# Document Similarity Methods

> Sources: GeeksforGeeks, 2025-07-23
> Raw: [Document similarity methods](../../raw/machine-learning/2026-10-05-document-similarity-methods.md)

## Overview

Document similarity compares two documents for search, plagiarism detection, clustering, and related NLP tasks. The GeeksforGeeks article surveys vector, set, and character-edit approaches rather than presenting one universally best metric.

## Methods

**Cosine similarity** compares the angle between document vectors, commonly TF-IDF vectors. **Jaccard similarity** compares token sets using intersection divided by union. It emphasizes shared vocabulary and ignores repeated token counts.

**Euclidean distance** measures straight-line distance between word-count or TF-IDF vectors. **Manhattan distance** sums absolute coordinate differences and can be more robust in high-dimensional spaces. For both distance measures, lower distance indicates greater similarity.

**Levenshtein distance** counts the minimum character insertions, deletions, and substitutions needed to transform one sequence into another. It fits spelling and short-string comparisons better than semantic document comparison.

## Selection Guidance

Use cosine similarity for weighted lexical vectors, Jaccard for token-set overlap, Euclidean or Manhattan distance for numeric vector comparisons, and Levenshtein distance for character-level variation. These methods are sensitive to tokenization, normalization, vocabulary, document length, and representation choices. They do not by themselves establish semantic equivalence.

## See Also

- [HybridRAG System](../agent-memory-systems/hybridrag-system.md)
