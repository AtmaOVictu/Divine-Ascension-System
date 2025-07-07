"""Ontological agent implementation.

An :class:`Agent` can move between three philosophical states based on
its emotional intensity and tension.  The states reflect different
understandings of truth:

``Ego``
    Truth is absolute and independent of others.
``Jaz``
    Truth is relative and shaped by relationships.
``Enotnost``
    All truths are one and interconnected.
"""

from dataclasses import dataclass, field


EMOTION_THRESHOLD = 0.5
TENSION_THRESHOLD = 0.7


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: list[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # emotion contributes to overall tension
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > TENSION_THRESHOLD or self.emotion > EMOTION_THRESHOLD:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
