"""Simple embedding-based retrieval without external dependencies."""
from typing import List, Tuple
import math


def simple_embedding(text: str) -> List[float]:
    """Create a naive letter-frequency embedding."""
    counts = [0] * 26
    for c in text.lower():
        if 'a' <= c <= 'z':
            counts[ord(c) - ord('a')] += 1
    norm = math.sqrt(sum(c * c for c in counts)) or 1.0
    return [c / norm for c in counts]


def build_index(texts: List[str]) -> List[Tuple[str, List[float]]]:
    """Build an index from texts and their embeddings."""
    return [(text, simple_embedding(text)) for text in texts]


def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    """Compute cosine similarity between two vectors."""
    return sum(a * b for a, b in zip(v1, v2))


def search(query: str, index: List[Tuple[str, List[float]]], top_k: int = 1) -> List[str]:
    """Return top_k texts from index most similar to the query."""
    q_emb = simple_embedding(query)
    scored = sorted(index, key=lambda item: cosine_similarity(q_emb, item[1]), reverse=True)
    return [text for text, _ in scored[:top_k]]
