"""Ontological agent capable of changing philosophical states."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Agent:
    """Represents an ontological agent with emotional context."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: Optional[str] = None
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, value: float, emotion_type: str) -> None:
        """Update emotional intensity and type, adjusting tension."""
        self.emotion = value
        self.emotion_type = emotion_type
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
        """Return a philosophical answer influenced by current state."""
        base_resp = {
            "Ego": "Truth is absolute and independent of others.",
            "Jaz": "Truth is relative and shaped by our relationships.",
            "Enotnost": "All truths are one, interconnected.",
        }
        reply = base_resp[self.state]
        if self.emotion_type:
            return f"{self.name} feels {self.emotion_type} and says: {reply}"
        return reply
