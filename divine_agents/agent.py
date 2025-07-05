from __future__ import annotations

import math


def logistic_function(x: float, k: float = 1.0, c: float = 0.5) -> float:
    """Simple logistic curve used to evolve tension."""
    return 1.0 / (1.0 + math.exp(-k * (x - c)))


class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        k_bio: float = 1.0,
        c_bio: float = 0.5,
        k_soc: float = 1.0,
        c_soc: float = 0.5,
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

    def evolve(self) -> None:
        """Evolve internal tension using a logistic model."""
        bio = logistic_function(self.tension, self.k_bio, self.c_bio)
        soc = logistic_function(self.emotion, self.k_soc, self.c_soc)
        self.tension = min(1.0, bio + soc)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        self.evolve()
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
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            prefix = "Čustveno"
        elif self.emotion > 0.3:
            prefix = "Rahlo čustveno"
        else:
            prefix = "Mirno"

        return f"{prefix} odgovorim: {base}"
