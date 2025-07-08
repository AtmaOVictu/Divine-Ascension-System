class Memory:
    """Simple memory system for storing agent states and emotions."""

    def __init__(self):
        self.short_term = []
        self.long_term = []
        self.history = []

    def store_short_term(self, item):
        self.short_term.append(item)
        if len(self.short_term) > 10:
            self.short_term.pop(0)

    def store_long_term(self, item):
        self.long_term.append(item)

    def store_history(self, item):
        self.history.append(item)

    def recall(self, category="short_term"):
        if category == "short_term":
            return self.short_term[-1] if self.short_term else None
        if category == "long_term":
            return self.long_term[-1] if self.long_term else None
        if category == "history":
            return list(self.history)
        return None

    def get_history_summary(self):
        return f"Total history records: {len(self.history)}"
