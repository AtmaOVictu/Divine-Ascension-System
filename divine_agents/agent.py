"""Ontological agent capable of transitioning between philosophical states."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an agent with tension, emotion and ontological state."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str = "neutral"
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")
    PRINCIPLES = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float, kind: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            Intensity of the emotion in range ``0.0-1.0``.
        kind: str, optional
            Name of the emotion (e.g. ``"fear"`` or ``"joy"``).
        """

        self.emotion = value
        if kind is not None:
            self.emotion_type = kind
        # emotion intensifies tension
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
        """Return an answer depending on state and emotional tone."""
        base = self.PRINCIPLES.get(self.state, "")
        if self.emotion_type != "neutral":
            base += f" Čutim {self.emotion_type}."
        return base
