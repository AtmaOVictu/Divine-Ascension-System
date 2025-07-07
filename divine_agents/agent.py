"""Ontological agents capable of emotional transitions and dialogue."""

from __future__ import annotations

from typing import List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTION_INTENSITY = {"fear": 0.8, "joy": 0.6, "anger": 0.9, "neutral": 0.0}

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = "neutral"
        self.history: List[str] = [state]

    def update_emotion(self, value: float | str) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            Either a numeric intensity in the range ``0-1`` or the name of an
            emotion defined in :data:`EMOTION_INTENSITY`.
        """
        if isinstance(value, str):
            self.emotion_label = value
            self.emotion = self.EMOTION_INTENSITY.get(value, 0.0)
        else:
            self.emotion_label = "custom"
            self.emotion = value
        self.tension += self.emotion

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

    # Additional convenience methods
    def describe_state(self) -> str:
        """Return the philosophical principle of the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = self.describe_state()
        if self.emotion > 0.5:
            return f"{base} Moja čustva ({self.emotion_label}) vplivajo na moje razmišljanje."
        return base
