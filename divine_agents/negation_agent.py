"""Agent subclass emphasizing negation-based actions."""
from .agent import Agent


class NegationAgent(Agent):
    """An agent that applies negation when performing actions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, negation_factor: int = 1) -> None:
        super().__init__(name, state, tension, emotion)
        self.negation_factor = negation_factor

    def apply_negation(self, action: str) -> str:
        """Return an action string wrapped in negation symbols."""
        return f"¬({action})"

    def perform_action(self, action: str) -> str:
        """Perform an action with repeated negation based on the factor."""
        negated = action
        for _ in range(self.negation_factor):
            negated = self.apply_negation(negated)
        self.history.append(negated)
        return negated

