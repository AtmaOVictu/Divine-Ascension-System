from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion_level: float = 0.0
    emotion: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """Update emotion and intensity, adjusting tension accordingly."""
        self.emotion = emotion
        self.emotion_level = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def philosophical_principle(self) -> str:
        """Return the philosophical principle tied to the current state."""
        if self.state == "Ego":
            return "Truth is absolute and independent of others."
        if self.state == "Jaz":
            return "Truth is relative and shaped by our relationships."
        return "All truths are one, interconnected."

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
        principle = self.philosophical_principle()
        return f"In {self.state} with {self.emotion}, I believe: {principle}"
