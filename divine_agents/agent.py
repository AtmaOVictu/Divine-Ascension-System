"""Ontological agents that shift states based on tension and emotion."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an agent capable of philosophical reasoning and state transitions."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_label: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, value: float, label: str) -> None:
        """Update emotion intensity, label and adjust tension accordingly."""
        self.emotion = value
        self.emotion_label = label
        self.tension += value

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
        """Return a philosophical answer depending on the current state and emotion."""
        if self.state == "Ego":
            base = "Truth is absolute and independent of others."
        elif self.state == "Jaz":
            base = "Truth is relative, shaped by our relationships."
        else:
            base = "All truths are one, interconnected."

        return f"{base} (feeling {self.emotion_label})"
