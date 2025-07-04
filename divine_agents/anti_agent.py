from .agent import Agent


class AntiAgent(Agent):
    """Represents an agent that transitions in reverse order."""

    def transition(self) -> str:
        """Reverse transition compared to Agent."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Enotnost":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Ego"
        self.history.append(self.state)
        return self.state
