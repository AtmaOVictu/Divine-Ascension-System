class VectorStore:
    """A minimal in-memory vector store using token overlap."""

    def __init__(self):
        self._documents = []
        self._embeddings = []

    def _embed(self, text: str) -> set:
        return set(text.lower().split())

    def add_document(self, text: str) -> None:
        self._documents.append(text)
        self._embeddings.append(self._embed(text))

    def search(self, query: str, top_k: int = 1) -> list:
        if not self._documents:
            return []
        q = self._embed(query)
        scores = []
        for emb in self._embeddings:
            inter = len(q & emb)
            union = len(q | emb)
            scores.append(inter / union if union else 0.0)
        ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        return [self._documents[i] for i in ranked[:top_k]]
