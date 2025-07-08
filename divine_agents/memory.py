class Memory:
    """Simple memory storage for agents."""

    def __init__(self):
        self.short_term = []
        self.long_term = []

    def store_short_term(self, data):
        """Store data in short-term memory."""
        self.short_term.append(data)

    def store_long_term(self, data):
        """Store data in long-term memory."""
        self.long_term.append(data)

    def recall(self, mode="short"):
        """Recall stored data from memory."""
        if mode == "long":
            return list(self.long_term)
        return list(self.short_term)
