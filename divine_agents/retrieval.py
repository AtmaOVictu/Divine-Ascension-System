"""Simple vector store for semantic retrieval."""

from __future__ import annotations

from typing import List, Optional

try:
    from openai import OpenAI
except Exception:  # pragma: no cover - openai might not be installed
    OpenAI = None


class SimpleVectorStore:
    """Lightweight vector store using embeddings if OpenAI is available."""

    def __init__(self, texts: Optional[List[str]] = None) -> None:
        self.texts: List[str] = []
        self.embeddings: List[List[float]] = []
        if texts:
            for text in texts:
                self.add_text(text)

    def _embed(self, text: str) -> List[float]:
        if OpenAI:
            client = OpenAI()
            response = client.embeddings.create(
                input=text,
                model="text-embedding-3-small",
            )
            return response.data[0].embedding
        # Fallback to naive character code embedding
        return [float(ord(c)) for c in text[:32]]

    def add_text(self, text: str) -> None:
        self.texts.append(text)
        self.embeddings.append(self._embed(text))

    def search(self, query: str) -> List[str]:
        if not self.texts:
            return []
        q_emb = self._embed(query)
        sims = []
        for emb in self.embeddings:
            # Cosine similarity
            dot = sum(a * b for a, b in zip(q_emb, emb))
            norm_q = sum(a * a for a in q_emb) ** 0.5
            norm_e = sum(a * a for a in emb) ** 0.5
            sims.append(dot / (norm_q * norm_e) if norm_q and norm_e else 0.0)
        best = self.texts[sims.index(max(sims))]
        return [best]
