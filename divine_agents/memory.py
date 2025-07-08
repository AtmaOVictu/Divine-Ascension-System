class Memory:
    """Simple memory storage for agent reflections."""

    def __init__(self):
        self.short_term = []
        self.long_term = []

    def store_short_term(self, data):
        """Store data in short-term memory."""
        self.short_term.append(data)

    def store_long_term(self, data):
        """Store data in long-term memory."""
        self.long_term.append(data)

    def recall(self, which="history"):
        """Recall stored memories."""
        if which == "history":
            return self.long_term
        return self.short_term
