"""Core agent logic used throughout the project."""

from dataclasses import dataclass, field
from typing import List


EMOTION_THRESHOLD = 0.5
TENSION_THRESHOLD = 0.7


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > TENSION_THRESHOLD or self.emotion > EMOTION_THRESHOLD:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = "!" if self.emotion > EMOTION_THRESHOLD else ":"
        if self.state == "Ego":
            return f"Resnica je absolutna in neodvisna od drugih{prefix}"
        if self.state == "Jaz":
            return f"Resnica je relativna, oblikovana z nasimi odnosi{prefix}"
        return f"Vse resnice so eno, medsebojno povezane{prefix}"
