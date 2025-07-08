class Memory:
    """Simple in-memory storage for concepts and interactions."""

    def __init__(self):
        self.long_term = []
        self.short_term = []

    def store_long_term(self, data):
        self.long_term.append(data)

    def store_short_term(self, data):
        self.short_term.append(data)

    def recall(self, source="long"):
        return self.long_term if source == "long" else self.short_term

# shared memory instance
memory = Memory()
