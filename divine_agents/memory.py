class Memory:
    """Simple memory storage for agents."""

    def __init__(self):
        self.long_term = []
        self.short_term = []

    def store_long_term(self, data):
        self.long_term.append(data)

    def store_short_term(self, data):
        self.short_term.append(data)

    def recall(self, key):
        if key == "history":
            return self.long_term
        return []

# Singleton instance used across the system
memory = Memory()
