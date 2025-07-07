from __future__ import annotations

from enum import Enum
from typing import Dict


class Emotion(Enum):
    """Basic emotional states that influence tension."""

    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego"):
        self.name = name
        self.state = state
        self.emotions: Dict[Emotion, float] = {e: 0.0 for e in Emotion}
        self.tension: float = 0.0
        self.history = [state]

    def set_emotion(self, emotion: Emotion, intensity: float) -> None:
        """Set an emotion's intensity and recalculate tension."""
        intensity = max(0.0, min(1.0, intensity))
        self.emotions[emotion] = intensity
        self.tension = sum(self.emotions.values())

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def _highest_emotion(self) -> float:
        return max(self.emotions.values()) if self.emotions else 0.0

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self._highest_emotion() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
