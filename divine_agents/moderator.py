class HiddenModerator:
    """Represents a hidden moderator with latent activation logic."""

    STATES = ("latent", "active", "revealed")

    def __init__(self, name: str, state: str = "latent", negation_factor: float = 0.5):
        self.name = name
        self.state = state
        self.negation_factor = negation_factor
        self.activation_triggered = False

    def evaluate_state(self, tension: float, emotion: float) -> None:
        """Check if conditions trigger activation."""
        if not self.activation_triggered and (tension > self.negation_factor or emotion > self.negation_factor):
            self.activate_moderator()

    def activate_moderator(self) -> None:
        """Activate moderator when conditions are met."""
        self.state = "active"
        self.activation_triggered = True

    def reveal_moderator(self) -> None:
        """Reveal moderator if already active."""
        if self.state == "active":
            self.state = "revealed"
