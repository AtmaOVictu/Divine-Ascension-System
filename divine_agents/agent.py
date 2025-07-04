"""Core agent logic for the divine ascension system."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_name: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def feel(self, emotion_name: str, intensity: float) -> None:
        """Set current emotion and adjust tension."""
        self.emotion_name = emotion_name
        self.emotion = intensity
        self.tension += intensity

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity keeping the last emotion name."""
        self.feel(self.emotion_name, value)

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
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"[{self.emotion_name}] {base}"
