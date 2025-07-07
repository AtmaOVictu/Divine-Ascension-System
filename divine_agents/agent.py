"""Core logic for ontological agents and their state transitions."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class EmotionType(Enum):
    """Enumeration of basic emotions influencing tension."""

    NEUTRAL = "neutral"
    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_label: EmotionType = EmotionType.NEUTRAL
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, label: EmotionType, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""

        self.emotion_label = label
        self.emotion = value

        if label in (EmotionType.FEAR, EmotionType.ANGER):
            self.tension = min(1.0, self.tension + value)
        elif label is EmotionType.JOY:
            self.tension = max(0.0, self.tension - value / 2)
        # Neutral does not modify tension

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
        """Return a philosophical answer reflecting state and emotion."""

        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"({self.emotion_label.value}) {base}"
