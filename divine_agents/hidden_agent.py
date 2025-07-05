from dataclasses import dataclass, field


@dataclass
class HiddenModerator:
    """Represents a latent moderator that activates based on tension or emotion."""

    name: str
    state: str = "latent"
    negation_factor: float = 0.5
    activation_triggered: bool = False
    history: list[str] = field(default_factory=lambda: ["latent"])

    def evaluate_state(self, tension: float, emotion: float) -> None:
        """Evaluate conditions to decide if activation is needed."""
        if not self.activation_triggered and (
            tension > self.negation_factor or emotion > self.negation_factor
        ):
            self.activate_moderator()

    def activate_moderator(self) -> None:
        """Activate the moderator when the conditions are met."""
        self.state = "active"
        self.activation_triggered = True
        self.history.append(self.state)

    def reveal_moderator(self) -> None:
        """Reveal the moderator once it is needed in the system."""
        if self.state == "active":
            self.state = "revealed"
            self.history.append(self.state)
