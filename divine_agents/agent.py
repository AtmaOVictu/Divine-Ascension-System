from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


EMOTION_PREFIX = {
    "fear": "Z zaskrbljenostjo",
    "joy": "Z veseljem",
    "anger": "Z jezo",
    "neutral": "",
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

    STATES = ("Ego", "Jaz", "Enotnost")
    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def feel(self, emotion_type: str, intensity: float) -> None:
        """Set the current emotion and adjust tension."""
        self.emotion_type = emotion_type
        self.emotion = intensity
        self.tension += intensity

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
        """Return a philosophical answer depending on the current state."""
        prefix = EMOTION_PREFIX.get(self.emotion_type, "")
        base = self.PHILOSOPHY.get(self.state, "")
        return f"{prefix} {base}".strip()
