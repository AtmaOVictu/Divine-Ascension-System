"""Utilities for hidden moderators with latent activation."""

from dataclasses import dataclass


@dataclass
class HiddenModerator:
    """Represents a latent moderator that activates under tension or emotion."""

    name: str
    state: str = "latent"  # latent, active, revealed
    negation_factor: float = 0.5
    activation_triggered: bool = False

    def evaluate_state(self, tension: float, emotion: float) -> None:
        """Activate when conditions exceed the negation factor."""
        if not self.activation_triggered:
            if tension > self.negation_factor or emotion > self.negation_factor:
                self.activate_moderator()

    def activate_moderator(self) -> None:
        """Set state to active and mark activation."""
        self.state = "active"
        self.activation_triggered = True

    def reveal_moderator(self) -> None:
        """Reveal the moderator if already active."""
        if self.state == "active":
            self.state = "revealed"
