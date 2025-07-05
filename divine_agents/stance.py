class Stance:
    """Represents a philosophical stance guiding an agent."""

    def __init__(self, name: str, principle: str) -> None:
        self.name = name
        self.principle = principle

    def apply(self, agent) -> str:
        """Return how the stance influences the agent."""
        return f"{agent.name} deluje po principu: {self.principle}"
