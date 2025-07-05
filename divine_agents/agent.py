"""Ontological agent implementation."""

from dataclasses import dataclass
from enum import Enum
from typing import List


class EmotionType(Enum):
    """Supported emotion categories."""

    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"
    NEUTRAL = "neutral"


@dataclass
class Emotion:
    """Emotion with intensity and category."""

    kind: EmotionType
    intensity: float


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or Emotion(EmotionType.NEUTRAL, 0.0)
        self.history: List[str] = [state]

    def update_emotion(self, kind: EmotionType, intensity: float) -> None:
        """Update emotion and adjust tension accordingly."""
        self.emotion = Emotion(kind, intensity)
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion.intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = f"[{self.emotion.kind.value}:{self.emotion.intensity:.1f}] "
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
