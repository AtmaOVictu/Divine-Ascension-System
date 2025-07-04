"""Ontological agent capable of emotional transitions and responses."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an agent that can transition through ontological states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion_level: float = 0.0
    emotion: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update emotion type and intensity, adjusting tension accordingly."""
        self.emotion = emotion
        self.emotion_level = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion and state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }

        emotion_prefix = {
            "fear": "S strahom odgovarjam: ",
            "joy": "Z veseljem delim: ",
            "anger": "Z jezo izjavljam: ",
            "neutral": "",
        }

        prefix = emotion_prefix.get(self.emotion, "")
        return prefix + base.get(self.state, "")
