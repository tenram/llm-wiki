# Different methods to find Document Similarity

> Source: https://www.geeksforgeeks.org/nlp/different-methods-to-find-document-similarity/
> Collected: 2026-10-05
> Published: 2025-07-23

In natural language processing (NLP), document similarity is a crucial concept that helps in various applications such as search engines, plagiarism detection, and document clustering.

This article explores various methods used to determine how similar two documents are, discussing techniques ranging from simple statistical approaches to complex neural network models.

## Cosine Similarity

Cosine Similarity measures the cosine of the angle between two non-zero vectors in a multi-dimensional space. In terms of text documents, these vectors often represent term frequency-inverse document frequency (TF-IDF) scores.

Implementation:

- Convert text data into TF-IDF vectors.
- Compute the cosine of the angle between these vectors.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = ['Document one text here', 'Document two text goes here']
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
print(similarity)
```

The example output is `[[1. 0.51014902]]`. A value of 1 indicates perfect self-similarity; the second value indicates moderate similarity between the two documents.

## Jaccard Similarity

Jaccard Similarity compares the sets of tokens in two documents. It is the size of the intersection divided by the size of the union.

Implementation:

- Tokenize documents into sets of unique words.
- Calculate the intersection-to-union ratio.

```python
def jaccard_similarity(doc1, doc2):
    words_doc1 = set(doc1.lower().split())
    words_doc2 = set(doc2.lower().split())
    intersection = words_doc1.intersection(words_doc2)
    union = words_doc1.union(words_doc2)
    return float(len(intersection)) / len(union)
```

## Euclidean Distance

Euclidean distance, or L2 distance, measures the shortest path between points in a vector space. Convert documents into word-count or TF-IDF vectors, then calculate the distance. Lower values indicate greater similarity.

## Manhattan Distance

Manhattan distance, or L1 distance, sums absolute differences across vector dimensions. It can be more robust in high-dimensional spaces than Euclidean distance. Lower values represent greater similarity.

## Levenshtein Distance

Levenshtein distance measures the minimum number of single-character insertions, deletions, and substitutions needed to change one sequence into another. It is commonly used for spelling correction and related string comparisons.

## Conclusion

Document similarity methods have different strengths and are suitable for different requirements. Vector metrics work on numerical document representations, set metrics emphasize token overlap, and edit distance measures character-level changes.
