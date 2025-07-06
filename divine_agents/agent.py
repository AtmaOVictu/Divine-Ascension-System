from __future__ import annotations

from dataclasses import dataclass


class Agent:
    """Represent an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Agent identifier.
    state:
        Ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Initial tension level.
    emotion:
        Initial emotion intensity between ``0`` and ``1``.
    emotion_label:
        Optional textual description of the current emotion.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0,
                 emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = max(0.0, min(1.0, value))
        # emotional intensity contributes directly to tension
        self.tension += self.emotion

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

    def set_emotion(self, label: str, intensity: float) -> None:
        """Assign an emotion label and update intensity."""
        self.emotion_label = label
        self.update_emotion(intensity)

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
        base: str
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        prefix = {
            "fear": "Z negotovostjo",
            "anger": "Z jezo",
            "joy": "Z veseljem",
        }.get(self.emotion_label, "")

        if prefix:
            return f"{prefix}, {base}"
        return base
