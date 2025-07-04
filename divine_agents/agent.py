"""Ontological agent capable of transitioning between philosophical states."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


STATES = ("Ego", "Jaz", "Enotnost")


@dataclass
class Agent:
    """Represents an agent with emotional context and state history."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity, emotion type and adjust tension."""
        self.emotion = value
        self.emotion_type = emotion_type
        # Emotional intensity increases overall tension
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the state and emotion."""
        if self.emotion_type == "fear":
            prefix = "V strahu odgovarjam: "
        elif self.emotion_type == "joy":
            prefix = "Z veseljem povem: "
        elif self.emotion_type == "anger":
            prefix = "Z jezo trdim: "
        else:
            prefix = ""

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{prefix}{base}"
