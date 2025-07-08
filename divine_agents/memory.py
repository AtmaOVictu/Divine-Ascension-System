class Memory:
    """Simple in-memory storage for long-term and short-term data."""

    def __init__(self):
        self.long_term = []
        self.short_term = []

    def store_long_term(self, data):
        """Store data for persistent learning."""
        self.long_term.append(data)

    def store_short_term(self, data):
        """Store temporary data for immediate access."""
        self.short_term.append(data)

    def recall(self, source="long_term"):
        """Retrieve stored memories by source."""
        return getattr(self, source, [])
