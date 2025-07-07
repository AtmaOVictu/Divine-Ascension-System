"""Ontological agents and their emotional state handling."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an agent that can transition between philosophical states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion_level: float = 0.0
    emotion: str = "neutral"
    history: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Initialize history with the starting state."""
        self.history.append(self.state)

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """Update current emotion and adjust tension based on intensity."""
        self.emotion = emotion
        self.emotion_level = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next state when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (čustvo: {self.emotion}, intenziteta: {self.emotion_level:.1f})"
