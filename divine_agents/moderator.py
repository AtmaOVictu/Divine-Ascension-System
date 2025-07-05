"""Hidden and latent agents used for dynamic moderation."""

from typing import Optional


class HiddenModerator:
    """Represents a moderator that activates only when needed."""

    def __init__(self, name: str, state: str = "latent", negation_factor: float = 0.5):
        self.name = name
        self.state = state  # latent -> active -> revealed
        self.negation_factor = negation_factor
        self.activation_triggered = False

    def evaluate_state(self, tension: float, emotion: float) -> None:
        """Activate if tension or emotion exceeds the negation factor."""
        if not self.activation_triggered:
            if tension > self.negation_factor or emotion > self.negation_factor:
                self.activate_moderator()

    def activate_moderator(self) -> None:
        """Move moderator into the active state."""
        self.state = "active"
        self.activation_triggered = True

    def reveal_moderator(self) -> None:
        """Reveal moderator when in active state."""
        if self.state == "active":
            self.state = "revealed"


class LatentAgent:
    """Agent that remains latent until tension crosses a threshold."""

    def __init__(self, name: str, state: str = "latent", threshold: float = 0.5, negation_factor: float = 0.3):
        self.name = name
        self.state = state  # latent -> active -> revealed
        self.threshold = threshold
        self.negation_factor = negation_factor

    def evaluate_state(self, tension: float) -> None:
        """Check if activation conditions are met."""
        if self.state == "latent" and tension > self.threshold - self.negation_factor:
            self.activate_agent()

    def activate_agent(self) -> None:
        """Activate the agent."""
        self.state = "active"

    def reveal_agent(self) -> None:
        """Reveal the agent when already active."""
        if self.state == "active":
            self.state = "revealed"
