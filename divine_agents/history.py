class History:
    """Simple history tracker for agent events."""

    def __init__(self) -> None:
        self.events = []

    def record(self, agent_name: str, event: str) -> None:
        """Record an event related to a specific agent."""
        self.events.append((agent_name, event))

    def last(self):
        """Return the last recorded event or None."""
        return self.events[-1] if self.events else None
