"""Core agent logic for philosophical state transitions."""

from dataclasses import dataclass, field
from typing import List


TENSION_THRESHOLD = 0.7
EMOTION_THRESHOLD = 0.5


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, value: float, kind: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if kind:
            self.emotion_type = kind
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

    def philosophy(self) -> str:
        """Return philosophical principle of the current state."""
        return {
            "Ego": "Truth is absolute and independent of others.",
            "Jaz": "Truth is relative and shaped by relationships.",
            "Enotnost": "All truths are one and interconnected.",
        }[self.state]

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        if self.emotion > EMOTION_THRESHOLD:
            return f"{base} (čustvo: {self.emotion_type})"
        return base
