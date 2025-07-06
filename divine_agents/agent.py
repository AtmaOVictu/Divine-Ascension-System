"""Agent implementation for the ontological dialogue system."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion_level: float = 0.0
    emotion_type: str = "neutral"  # e.g. fear, joy, anger
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    RESPONSES = {
        "Ego": "Truth is absolute and independent of others.",
        "Jaz": "Truth is relative, shaped by our relationships.",
        "Enotnost": "All truths are one and interconnected.",
    }

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, level: float, kind: str | None = None) -> None:
        """Update emotion intensity and optionally its type."""
        self.emotion_level = level
        if kind:
            self.emotion_type = kind
        # emotions influence tension
        self.tension += level

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
        """Return a philosophical answer depending on current state and emotion."""
        base = self.RESPONSES.get(self.state, "")
        if self.emotion_type != "neutral":
            return f"I feel {self.emotion_type}. {base}"
        return base
