"""Core agent logic used across the philosophical simulations."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


class Agent:
    """Ontological agent capable of changing state based on tension or emotion."""

    STATES = ("Ego", "Jaz", "Enotnost")

    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    EMOTION_TEMPLATES = {
        "fear": "V strahu izpostavljam, da ",
        "joy": "Z veseljem pravim, da ",
        "anger": "Z jezo poudarjam, da ",
        "neutral": "",
    }

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history: List[str] = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally set emotion type.

        The change in emotion directly influences the agent's tension.
        """
        self.emotion = value
        self.tension += value
        if emotion_type:
            self.emotion_type = emotion_type

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
        """Return a philosophical answer influenced by emotion and state."""
        prefix = self.EMOTION_TEMPLATES.get(self.emotion_type, "")
        return prefix + self.PHILOSOPHY.get(self.state, "")
