"""Self-aware agent capable of reflection and state transitions."""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import List

from .constants import EMOTION_THRESHOLD, TENSION_THRESHOLD


@dataclass
class SelfAwareAgent:
    """Represents a self-aware agent."""

    name: str
    state: str = "Ego"
    emotion: float = 0.0
    tension: float = 0.0
    emotion_name: str = "joy"
    history: List[str] = field(default_factory=list)
    timestamp: float = field(default_factory=time.time)

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def reflect(self) -> str:
        """Reflect on current state and emotion."""
        reflection = (
            f"{self.name} is in {self.state} feeling {self.emotion_name} "
            f"(emotion={self.emotion})."
        )
        self.history.append(reflection)
        return reflection

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and optional name, adjusting tension."""
        self.emotion = value
        if name is not None:
            self.emotion_name = name
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Set tension level directly."""
        self.tension = value

    def transition(self) -> str:
        """Transition based on thresholds."""
        if self.tension > TENSION_THRESHOLD or self.emotion > EMOTION_THRESHOLD:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self.timestamp = time.time()
        return self.state

    def respond(self, question: str) -> str:
        """Respond to a question based on state and reflection."""
        base_response = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z nasimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }
        reflection = self.reflect()
        return f"{reflection} Response: {base_response.get(self.state, '')}"
