"""Ontological agents capable of philosophical state transitions."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent.

    Attributes
    ----------
    name: str
        Agent identifier.
    state: str
        Current ontological state. One of ``Ego``, ``Jaz`` or ``Enotnost``.
    tension: float
        Accumulated tension level (0-1). Used to trigger state transitions.
    emotion: float
        Current emotional intensity (0-1).
    history: List[str]
        Log of previous states for debugging and analysis.
    """

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=lambda: ["Ego"])

    EMOTION_THRESHOLD: float = 0.5
    TENSION_THRESHOLD: float = 0.7

    def update_emotion(self, value: float) -> None:
        """Update emotion and adjust tension.

        Parameters
        ----------
        value: float
            New emotional intensity. This also increments tension
            by the same value to model emotional impact on stress.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.TENSION_THRESHOLD or self.emotion > self.EMOTION_THRESHOLD:
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
