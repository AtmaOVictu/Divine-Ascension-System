class Memory:
    """Simple memory store for short- and long-term information."""

    def __init__(self) -> None:
        self.long_term = []
        self.short_term = []
        self.history = []

    def store_long_term(self, data) -> None:
        """Store data in long-term memory."""
        self.long_term.append(data)

    def store_short_term(self, data) -> None:
        """Store data in short-term memory."""
        self.short_term.append(data)

    def recall(self, key: str):
        """Retrieve stored information."""
        if key == "history":
            return self.history
        if key == "short":
            return self.short_term
        if key == "long":
            return self.long_term
        return []
