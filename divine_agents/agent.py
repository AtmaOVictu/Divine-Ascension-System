"""Ontological agent module."""

from __future__ import annotations

import math


def logistic(x: float, k: float = 10.0, c: float = 0.5) -> float:
    """Simple logistic function used to derive tension from emotion."""
    return 1.0 / (1.0 + math.exp(-k * (x - c)))


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and update tension via logistic mapping."""
        self.emotion = max(0.0, min(1.0, value))
        self.tension = logistic(self.emotion)

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
        if self.emotion < 0.3:
            mood = "mirno"
        elif self.emotion < 0.6:
            mood = "negotovo"
        else:
            mood = "strastno"

        if self.state == "Ego":
            return f"{mood} verjamem, da je resnica absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{mood} verjamem, da je resnica relativna, oblikovana z našimi odnosi."
        return f"{mood} verjamem, da so vse resnice eno, medsebojno povezane."
