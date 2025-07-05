class HiddenModerator:
    """A moderator that remains latent until tension or emotion exceeds a threshold."""

    def __init__(self, name: str, state: str = "latent", negation_factor: float = 0.5):
        self.name = name
        self.state = state  # latent, active, revealed
        self.negation_factor = negation_factor
        self.activation_triggered = False

    def evaluate_state(self, tension: float, emotion: float) -> None:
        """Activate moderator if conditions exceed negation factor."""
        if not self.activation_triggered and (tension > self.negation_factor or emotion > self.negation_factor):
            self.activate_moderator()

    def activate_moderator(self) -> None:
        """Set the moderator to active state."""
        self.state = "active"
        self.activation_triggered = True

    def reveal_moderator(self) -> None:
        """Reveal the moderator when already active."""
        if self.state == "active":
            self.state = "revealed"

