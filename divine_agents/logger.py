class CodeLogger:
    """Keeps track of important events for later inspection."""

    def __init__(self):
        self.history = []

    def log_event(self, event: str) -> None:
        """Record an event description."""
        self.history.append(event)

    def analyze_history(self):
        """Simple analysis looking for errors in the log."""
        suggestions = []
        for event in self.history:
            if "error" in event:
                suggestions.append(f"Napaka: {event}. Predlagam izboljšanje.")
        return suggestions
