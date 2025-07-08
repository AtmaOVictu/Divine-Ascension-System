from typing import List

class VectorStore:
    """Naive in-memory vector store for semantic search without external deps."""

    def __init__(self) -> None:
        self.vocab: List[str] = []
        self.texts: List[str] = []
        self.embeddings: List[List[int]] = []

    def build_vocab(self, texts: List[str]) -> None:
        tokens = set()
        for text in texts:
            tokens.update(text.lower().translate(str.maketrans("","",".,!?")).split())
        self.vocab = sorted(tokens)

    def _get_embedding(self, text: str) -> List[int]:
        if not self.vocab:
            self.build_vocab([text])
        counts = {}
        for token in text.lower().translate(str.maketrans("","",".,!?")).split():
            counts[token] = counts.get(token, 0) + 1
        return [counts.get(token, 0) for token in self.vocab]

    def add_texts(self, texts: List[str]) -> None:
        if not self.vocab:
            self.build_vocab(texts)
        for text in texts:
            self.texts.append(text)
            self.embeddings.append(self._get_embedding(text))

    def _cosine_similarity(self, v1: List[int], v2: List[int]) -> float:
        dot = sum(a * b for a, b in zip(v1, v2))
        norm1 = sum(a * a for a in v1) ** 0.5
        norm2 = sum(b * b for b in v2) ** 0.5
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot / (norm1 * norm2)

    def search(self, query: str, top_k: int = 3) -> List[str]:
        if not self.texts:
            return []
        query_emb = self._get_embedding(query)
        sims = [self._cosine_similarity(query_emb, emb) for emb in self.embeddings]
        indices = sorted(range(len(sims)), key=lambda i: sims[i], reverse=True)[:top_k]
        return [self.texts[i] for i in indices]
