class HiddenModerator:
    """A latent moderator activated only when tension or emotion exceeds the
    negation factor. Initially in a latent state, it becomes active and can
    later be revealed."""

    def __init__(self, name: str, state: str = "latent", negation_factor: float = 0.5):
        self.name = name
        self.state = state  # latent, active, revealed
        self.negation_factor = negation_factor
        self.activation_triggered = False

    def evaluate_state(self, tension: float, emotion: float) -> None:
        """Trigger activation when conditions surpass the negation factor."""
        if not self.activation_triggered and (tension > self.negation_factor or emotion > self.negation_factor):
            self.activate_moderator()

    def activate_moderator(self) -> None:
        """Switch the moderator into an active state."""
        self.state = "active"
        self.activation_triggered = True

    def reveal_moderator(self) -> None:
        """Reveal the moderator to the system when active."""
        if self.state == "active":
            self.state = "revealed"
