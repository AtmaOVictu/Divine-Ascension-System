from __future__ import annotations

from typing import Optional


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent holds an ontological ``state`` (``Ego``, ``Jaz`` or ``Enotnost``),
    a ``tension`` level and an ``emotion`` intensity. ``emotion_label`` stores a
    textual description of the current emotion (e.g. ``"jeza"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: Optional[str] = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity without changing the label."""
        self.apply_emotion(None, value)

    def apply_emotion(self, label: Optional[str], intensity: float) -> None:
        """Set an emotion label and intensity and update tension."""
        if label is not None:
            self.emotion_label = label
        self.emotion = intensity
        self.tension += intensity

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
        prefix = f"({self.emotion_label}) " if self.emotion_label else ""
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
