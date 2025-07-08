"""Ontological agents capable of emotional state transitions and dialogue."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an agent with emotional context and philosophical state."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, value: float, kind: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            Intensity of the emotion in range ``0..1``.
        kind:
            Optional description of the emotion (e.g. ``"fear"`` or ``"joy"``).
        """
        self.emotion = value
        if kind is not None:
            self.emotion_type = kind
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

    def respond(self) -> str:
        """Return a philosophical answer influenced by emotion and state."""
        base = {
            "Ego": "Truth is absolute and independent of others.",
            "Jaz": "Truth is relative and shaped by our relationships.",
            "Enotnost": "All truths are one, interconnected.",
        }[self.state]

        if self.emotion_type in {"fear", "anger"}:
            prefix = "With trembling voice,"
        elif self.emotion_type == "joy":
            prefix = "Joyfully,"
        else:
            prefix = "Calmly,"

        return f"{prefix} {base}"
