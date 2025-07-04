"""Ontological agent capable of state transitions based on emotion and tension."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an agent with philosophical states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, value: float) -> None:
        """Update emotion level and increase tension."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Set tension level directly."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next philosophical state if thresholds are met."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical response based on current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
