from typing import List
import random
import math


class RetrievalIndex:
    """Simple in-memory vector store using deterministic pseudo-embeddings."""

    def __init__(self, dim: int = 5):
        self.dim = dim
        self.embeddings: List[List[float]] = []
        self.texts: List[str] = []

    def _embed(self, text: str) -> List[float]:
        seed = abs(hash(text)) % (2 ** 32)
        rng = random.Random(seed)
        return [rng.random() for _ in range(self.dim)]

    def add(self, text: str) -> None:
        self.embeddings.append(self._embed(text))
        self.texts.append(text)

    def _distance(self, a: List[float], b: List[float]) -> float:
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

    def search(self, query: str, k: int = 1) -> List[str]:
        if not self.texts:
            return []
        q_emb = self._embed(query)
        dists = [self._distance(q_emb, emb) for emb in self.embeddings]
        sorted_pairs = sorted(zip(dists, self.texts), key=lambda x: x[0])
        return [text for _, text in sorted_pairs[:k]]
