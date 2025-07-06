"""Ontological agents capable of philosophical state transitions."""
from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represent an agent with ontological states and emotional tension."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, value: float) -> None:
        """Set the emotion intensity and raise tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next ontological state when thresholds are met."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Respond based on the current ontological state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
