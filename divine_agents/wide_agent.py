from .agent import Agent


class WideAgent(Agent):
    """An agent capable of operating across multiple dimensions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.dimensions = {"space": 0, "time": 0, "emotion": emotion}

    def update_dimension(self, key: str, value: float) -> None:
        """Update one of the internal dimensions."""
        self.dimensions[key] = value

    def respond(self, question: str) -> str:
        base = super().respond(question)
        return f"{base}"  # extra context could be added here
