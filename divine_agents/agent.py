"""Ontological agents capable of transitioning between states."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent able to move through states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        """Initialize the agent's history with the starting state."""
        if not self.history:
            self.history.append(self.state)

    def update_emotion(self, value: float) -> None:
        """Increment emotion intensity and increase tension accordingly."""
        self.emotion += value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Set the agent's tension to ``value``."""
        self.tension = value

    def transition(self) -> str:
        """Move to the next state when emotional thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Answer a question based on the agent's current ontological state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
