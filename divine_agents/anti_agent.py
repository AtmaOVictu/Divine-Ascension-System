from .agent import Agent

class AntiAgent(Agent):
    """Agent that transitions backwards through the ontological states."""

    def transition(self) -> str:
        """Move in reverse order when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Enotnost":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Ego"
        self.history.append(self.state)
        return self.state
