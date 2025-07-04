"""Ontological agent implementation."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Agent:
    """Represents an agent transitioning through ontological states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion_level: float = 0.0
    emotion_label: str = "neutral"
    history: list[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, level: float, label: str | None = None) -> None:
        """Update emotion intensity and optional label, adjusting tension."""
        self.emotion_level = level
        if label is not None:
            self.emotion_label = label
        self.tension += level

    def update_tension(self, value: float) -> None:
        """Set tension level directly."""
        self.tension = value

    def _should_transition(self) -> bool:
        """Return True if thresholds for transition are met."""
        return self.tension > 0.7 or self.emotion_level > 0.5

    def transition(self) -> str:
        """Transition to the next state when thresholds are exceeded."""
        if self._should_transition():
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def _base_response(self) -> str:
        """Return a philosophical statement based on the ontological state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Respond to a question reflecting emotion and ontological state."""
        emotion_prefix = {
            "fear": "Plašno pravi:",
            "joy": "Veselo pravi:",
            "anger": "Jezno pravi:",
            "neutral": "Pove:",
        }.get(self.emotion_label, "Pove:")
        return f"{emotion_prefix} {self._base_response()}"
