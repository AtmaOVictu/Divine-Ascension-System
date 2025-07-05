"""Hidden moderators with latent activation logic."""

class HiddenModerator:
    """Represents a moderator that remains latent until tension or emotion
    exceeds a negation factor."""

    STATES = ("latent", "active", "revealed")

    def __init__(self, name: str, state: str = "latent", negation_factor: float = 0.5):
        self.name = name
        self.state = state
        self.negation_factor = negation_factor
        self.activation_triggered = False
        self.history = [state]

    def evaluate_state(self, tension: float, emotion: float) -> str:
        """Evaluate if the moderator should activate based on tension or emotion."""
        if not self.activation_triggered:
            if tension > self.negation_factor or emotion > self.negation_factor:
                self.activate_moderator()
        self.history.append(self.state)
        return self.state

    def activate_moderator(self) -> None:
        """Activate the moderator."""
        self.state = "active"
        self.activation_triggered = True

    def reveal_moderator(self) -> str:
        """Reveal the moderator if it has been activated."""
        if self.state == "active":
            self.state = "revealed"
        self.history.append(self.state)
        return self.state
