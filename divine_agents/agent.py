"""Core agent logic for philosophical state transitions."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(init=False)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history = [self.state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        previous = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        tone = "strastno" if self.emotion > 0.5 else "mirno"
        if self.state == "Ego":
            return f"{tone}: Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{tone}: Resnica je relativna, oblikovana z našimi odnosi."
        return f"{tone}: Vse resnice so eno, medsebojno povezane."
