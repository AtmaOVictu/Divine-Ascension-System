class AgentHistory:
    """Record transitions between agent states."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.transitions = []

    def record(self, state_from: str, state_to: str) -> None:
        """Store a transition event."""
        self.transitions.append({"from": state_from, "to": state_to})

    def last(self):
        return self.transitions[-1] if self.transitions else None
