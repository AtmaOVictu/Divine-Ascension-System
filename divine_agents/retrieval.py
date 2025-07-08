"""Simple semantic search utilities using deterministic embeddings."""

from __future__ import annotations

import hashlib
import math
from typing import List, Tuple


def get_embedding(text: str, dimension: int = 8) -> List[float]:
    """Return a deterministic pseudo-embedding for the given text."""
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    return [b / 255.0 for b in digest[:dimension]]


def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    """Compute cosine similarity between two vectors."""
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)


class VectorStore:
    """In-memory vector store for semantic search."""

    def __init__(self) -> None:
        self._data: List[Tuple[List[float], str]] = []

    def add(self, text: str) -> None:
        embedding = get_embedding(text)
        self._data.append((embedding, text))

    def search(self, query: str, top_k: int = 1) -> List[str]:
        query_emb = get_embedding(query)
        scored = [
            (cosine_similarity(query_emb, emb), text) for emb, text in self._data
        ]
        scored.sort(key=lambda x: x[0], reverse=True)
        return [text for _score, text in scored[:top_k]]
