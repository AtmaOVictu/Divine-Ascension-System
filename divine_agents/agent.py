"""Core agent logic for ontological state transitions and responses."""

from dataclasses import dataclass, field
from typing import List, Optional


EMOTION_PREFIX = {
    "anger": "z jezo pravi",
    "fear": "s strahom pravi",
    "joy": "z veseljem pravi",
    "neutral": "pravi",
}


PRINCIPLES = {
    "Ego": "Resnica je absolutna in neodvisna od drugih.",
    "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
    "Enotnost": "Vse resnice so eno, medsebojno povezane.",
}


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, value: float, emotion_type: Optional[str] = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if emotion_type:
            self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def _can_transition(self) -> bool:
        """Check whether thresholds for transition are met."""
        return self.tension > 0.7 or self.emotion > 0.5

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self._can_transition():
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        principle = PRINCIPLES.get(self.state, "")
        prefix = EMOTION_PREFIX.get(self.emotion_type, EMOTION_PREFIX["neutral"])
        return f"{prefix} '{principle}'"
