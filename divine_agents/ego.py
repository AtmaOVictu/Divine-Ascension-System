class Ego:
    """Simple component representing an agent's ego."""

    def __init__(self):
        self.urgency_history = []

    def react_to_urgency(self, urgency: str) -> None:
        """Record a new urgency affecting the ego."""
        self.urgency_history.append(urgency)
