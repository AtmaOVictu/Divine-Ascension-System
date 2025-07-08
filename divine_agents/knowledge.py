from __future__ import annotations

import hashlib
import math
from typing import List, Tuple


def _embed(text: str, dim: int = 16) -> List[int]:
    """Deterministically embed text using SHA256 hashing."""
    digest = hashlib.sha256(text.encode()).digest()
    return [b for b in digest[:dim]]


def _cosine_sim(v1: List[int], v2: List[int]) -> float:
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    return dot / (norm1 * norm2)


class KnowledgeBase:
    """Simple in-memory store for documents and embeddings."""

    def __init__(self) -> None:
        self.documents: dict[str, str] = {}
        self.embeddings: dict[str, List[int]] = {}

    def add_document(self, doc_id: str, text: str) -> None:
        self.documents[doc_id] = text
        self.embeddings[doc_id] = _embed(text)

    def search(self, query: str, top_k: int = 1) -> List[Tuple[str, float]]:
        if not self.documents:
            return []
        query_vec = _embed(query)
        scored = []
        for doc_id, emb in self.embeddings.items():
            score = _cosine_sim(query_vec, emb)
            scored.append((self.documents[doc_id], score))
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]
