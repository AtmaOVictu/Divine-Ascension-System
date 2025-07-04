"""Ouroboros agent that cycles endlessly through ontological states."""

from .agent import Agent

class OuroborosAgent(Agent):
    """Agent implementing an infinite cyclical state transition."""

    def transition(self) -> str:
        """Perform cyclical state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            else:
                self.state = "Ego"
        self.history.append(self.state)
        return self.state

    def cycle(self, steps: int = 3) -> str:
        """Execute a number of transitions and return the final state."""
        for _ in range(steps):
            self.transition()
        return self.state
