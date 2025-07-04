"""Ontological agent implementation.

Agents hold a current ontological ``state`` and transition between
``Ego`` -> ``Jaz`` -> ``Enotnost`` once their internal ``tension`` or
``emotion`` level exceeds configured thresholds.  Each agent also keeps
track of the type of emotion currently experienced which influences the
phrasing of responses during a dialogue.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str = "neutral"
    history: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float, kind: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            Intensity of the emotion in range ``0.0``-``1.0``.
        kind:
            Descriptive name of the emotion (e.g. ``fear`` or ``joy``).
        """
        self.emotion = value
        self.emotion_type = kind
        # Stronger emotions build tension and might trigger transitions
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
        """Return a philosophical answer influenced by current state and emotion."""

        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        if self.emotion_type != "neutral":
            return f"{base} (občuti {self.emotion_type})"
        return base
