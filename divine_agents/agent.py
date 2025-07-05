"""Ontological agents and utilities."""

import json
from typing import Tuple


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
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


def logistic_function(t: float, k: float, c: float) -> float:
    """Standard logistic function used for tension evolution."""
    return 1 / (1 + (2.718281828459045 ** (-k * (t - c))))


class DynamicAgent(Agent):
    """Agent with logistic tension evolution and state persistence."""

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        k_bio: float = 1.0,
        c_bio: float = 0.5,
        k_soc: float = 1.5,
        c_soc: float = 0.6,
    ) -> None:
        super().__init__(name, state, tension, emotion)
        self.k_bio = k_bio
        self.c_bio = c_bio
        self.k_soc = k_soc
        self.c_soc = c_soc

    def evolve(self) -> str:
        """Update tension using logistic growth and transition state."""
        bio = logistic_function(self.tension, self.k_bio, self.c_bio)
        soc = logistic_function(self.tension, self.k_soc, self.c_soc)
        self.tension = bio + soc
        return self.transition()

    def get_state(self) -> Tuple[float, float]:
        """Return current tension and emotion."""
        return self.tension, self.emotion

    def save(self, path: str) -> None:
        """Persist agent state to a JSON file."""
        data = {"state": self.state, "tension": self.tension, "emotion": self.emotion}
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh)

    def load(self, path: str) -> None:
        """Load agent state from a JSON file."""
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        self.state = data.get("state", self.state)
        self.tension = data.get("tension", self.tension)
        self.emotion = data.get("emotion", self.emotion)
        self.history.append(self.state)
