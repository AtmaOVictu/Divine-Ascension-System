class Memory:
    """Simple memory system storing short and long term records."""

    def __init__(self):
        self.short_term = []
        self.long_term = []

    def store_short_term(self, record):
        """Store a record in short term memory."""
        self.short_term.append(record)

    def store_long_term(self, record):
        """Store a record in long term memory."""
        self.long_term.append(record)

    def recall(self, source="long_term"):
        """Recall records from memory."""
        return self.long_term if source == "long_term" else self.short_term
