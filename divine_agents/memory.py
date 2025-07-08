class Memory:
    """Simple memory storage for short-term and long-term data."""

    def __init__(self) -> None:
        self.short_term = []
        self.long_term = []

    def store_short_term(self, item) -> None:
        """Store data in short-term memory."""
        self.short_term.append(item)

    def store_long_term(self, item) -> None:
        """Store data in long-term memory."""
        self.long_term.append(item)

    def recall(self, kind: str):
        """Recall data from memory based on type."""
        if kind == "short":
            return list(self.short_term)
        if kind == "long":
            return list(self.long_term)
        return []
