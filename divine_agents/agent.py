"""Definition of the Agent class used throughout the dialogue system."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion_level: float = 0.0
    emotion_type: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Update emotion type and intensity and adjust tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion_level = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return f"({self.emotion_type}) Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"({self.emotion_type}) Resnica je relativna, oblikovana z našimi odnosi."
        return f"({self.emotion_type}) Vse resnice so eno, medsebojno povezane."
