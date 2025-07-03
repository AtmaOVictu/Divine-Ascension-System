from .agent import Agent

class NegationAgent(Agent):
    """Agent variant that emphasizes negation in its actions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, negation_factor: int = 1):
        super().__init__(name, state, tension, emotion)
        self.negation_factor = negation_factor

    def apply_negation(self, action: str) -> str:
        """Negate an action expression."""
        return f"\u00AC({action})"

    def perform_action(self, action: str) -> str:
        """Perform an action under the influence of negation."""
        result = action
        for _ in range(self.negation_factor):
            result = self.apply_negation(result)
        self.history.append(result)
        return result

    def evolve(self) -> str:
        """Advance the agent's state while amplifying negation."""
        state = self.transition()
        if state == "Jaz":
            self.negation_factor += 1
        elif state == "Enotnost":
            self.negation_factor += 2
        return state
