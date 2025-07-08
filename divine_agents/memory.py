class Memory:
    """Simple container for short- and long-term memories."""

    def __init__(self):
        self.short_term = []
        self.long_term = []

    def store_short_term(self, data):
        self.short_term.append(data)

    def store_long_term(self, data):
        self.long_term.append(data)

    def recall(self, which="short"):
        return list(self.short_term if which == "short" else self.long_term)
