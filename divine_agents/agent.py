from __future__ import annotations

import random
from typing import Dict


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: Mapping of qualitative emotions to their intensity values.
    EMOTIONS: Dict[str, float] = {
        "fear": 0.7,
        "joy": 0.6,
        "anger": 0.8,
        "neutral": 0.0,
    }

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_value = self.EMOTIONS.get(emotion, 0.0)
        self.history = [state]

    def update_emotion(self, emotion: str) -> None:
        """Update emotion and adjust tension based on its intensity."""
        self.emotion = emotion
        self.emotion_value = self.EMOTIONS.get(emotion, 0.0)
        self.tension += self.emotion_value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_value > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer reflecting state and emotion."""
        prefix = f"With {self.emotion}: " if self.emotion != "neutral" else ""
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
