"""Core primitives for ontological agents."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def adjust_emotion(self, delta: float) -> None:
        """Increment emotion by ``delta`` and adjust tension."""
        self.emotion += delta
        self.tension += delta

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotion_note = f"(čustva: {self.emotion:.2f})"
        if self.state == "Ego":
            return f"Resnica je absolutna in neodvisna od drugih. {emotion_note}"
        if self.state == "Jaz":
            return f"Resnica je relativna, oblikovana z našimi odnosi. {emotion_note}"
        return f"Vse resnice so eno, medsebojno povezane. {emotion_note}"
