"""Core ontological agent model used for philosophical simulations."""

from __future__ import annotations

import math


def logistic_function(x: float, k: float = 1.0, c: float = 0.5) -> float:
    """Smooth activation used for tension updates."""
    return 1 / (1 + math.exp(-k * (x - c)))


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0,
                 emotion: float = 0.0, k: float = 1.0, c: float = 0.5) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.k = k
        self.c = c
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += logistic_function(value, self.k, self.c)

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
        tone = " mirno." if self.emotion <= 0.5 else " strastno."
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return base + tone

    def set_parameters(self, *, k: float | None = None, c: float | None = None) -> None:
        """Dynamically adjust logistic parameters."""
        if k is not None:
            self.k = k
        if c is not None:
            self.c = c
