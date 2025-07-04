"""Core agent model used throughout the project."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Display name of the agent.
    state:
        Ontological state (``"Ego"``, ``"Jaz"``, or ``"Enotnost"``).
    tension:
        Accumulated tension level.
    emotion:
        Intensity of the current emotion in the range ``0..1``.
    emotion_type:
        The type of the current emotion (e.g. ``"fear"``, ``"joy"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str | None = None
    history: List[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion type and intensity and adjust tension.

        Parameters
        ----------
        emotion_type:
            Type of emotion (e.g. ``"fear"``, ``"joy"`` or ``"anger"``).
        value:
            Intensity in range ``0..1``.
        """

        self.emotion_type = emotion_type
        self.emotion = value

        # Fear and anger heighten tension, joy may ease it slightly.
        if emotion_type in {"fear", "anger"}:
            self.tension += value
        elif emotion_type == "joy":
            self.tension = max(0.0, self.tension - value / 2)
        else:
            self.tension += value / 2

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
        """Return a philosophical answer depending on the current state."""

        prefix = "" if not self.emotion_type else f"({self.emotion_type}) "

        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
