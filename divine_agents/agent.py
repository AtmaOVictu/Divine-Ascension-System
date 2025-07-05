"""Ontological agents capable of philosophical state transitions."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


STATES = ("Ego", "Jaz", "Enotnost")


def _clamp(value: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    """Clamp a numeric value between ``minimum`` and ``maximum``."""
    return max(minimum, min(value, maximum))


@dataclass
class Agent:
    """Represents an agent with emotions and philosophical state."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str = "neutral"
    history: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.history.append(self.state)
        self.tension = _clamp(self.tension)
        self.emotion = _clamp(self.emotion)

    def update_emotion(self, value: float, emotion_type: Optional[str] = None) -> None:
        """Update the agent's emotional intensity and optional type."""
        self.emotion = _clamp(value)
        if emotion_type:
            self.emotion_type = emotion_type
        if self.emotion > 0.5:
            # heightened emotion slightly increases tension
            self.tension = _clamp(self.tension + 0.1)

    def update_tension(self, value: float) -> None:
        """Set the tension value directly."""
        self.tension = _clamp(value)

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
        """Return a philosophical statement influenced by current emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]
        if self.emotion > 0.5 and self.emotion_type:
            return f"{self.emotion_type.upper()}: {base}"
        return base
