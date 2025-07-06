class Memory:
    """Simple memory storage for agents."""

    def __init__(self):
        self.entries = []

    def record(self, text: str) -> None:
        """Store a memory entry."""
        self.entries.append(text)

    def recall(self, n: int = 1):
        """Recall the last n memory entries."""
        if n <= 0:
            return []
        return self.entries[-n:]
