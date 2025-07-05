from __future__ import annotations

import math


def logistic_function(t: float, k: float = 1.0, c: float = 0.5) -> float:
    """Compute a logistic curve used for tension adjustments."""
    return 1 / (1 + math.exp(-k * (t - c)))


class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float, k: float = 1.0, c: float = 0.5) -> None:
        """Update emotion intensity and adjust tension using a logistic curve."""
        self.emotion = value
        # Tension follows a logistic growth based on emotion
        self.tension = logistic_function(value, k=k, c=c)

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
        """Return a philosophical answer depending on state and emotion."""
        emotional_prefix = ""
        if self.emotion > 0.5:
            emotional_prefix = "(z visokimi čustvi) "

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."

        return f"{emotional_prefix}{core}"
