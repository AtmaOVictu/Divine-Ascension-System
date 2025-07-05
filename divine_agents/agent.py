"""Core logic for ontological agents."""

from __future__ import annotations

import math


def logistic_function(t: float, k: float = 1.0, c: float = 0.5) -> float:
    """Return logistic growth of ``t``.

    Parameters
    ----------
    t:
        Current value influencing the transition.
    k:
        Speed of transition.
    c:
        Critical point of the transition.
    """

    return 1 / (1 + math.exp(-k * (t - c)))


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        *,
        k_bio: float = 1.0,
        c_bio: float = 0.5,
        k_soc: float = 1.5,
        c_soc: float = 0.6,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.k_bio = k_bio
        self.c_bio = c_bio
        self.k_soc = k_soc
        self.c_soc = c_soc
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def evolve(self) -> None:
        """Update tension based on logistic transitions."""
        bio = logistic_function(self.tension, self.k_bio, self.c_bio)
        soc = logistic_function(self.tension, self.k_soc, self.c_soc)
        self.tension = bio + soc

    def get_state(self) -> tuple[float, float]:
        """Return current tension and emotion."""
        return self.tension, self.emotion

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
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
