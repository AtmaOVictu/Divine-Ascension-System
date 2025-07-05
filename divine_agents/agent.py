"""Agent models and utilities for ontological simulations."""

from typing import Tuple
import math


def logistic_function(t: float, k: float = 1.0, c: float = 0.5) -> float:
    """Return a logistic transition value."""
    return 1 / (1 + math.exp(-k * (t - c)))


def logarithmic_function(t: float, k: float = 1.0, c: float = 1.0) -> float:
    """Return a logarithmic growth value."""
    return k * math.log(t + c)


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


class AdvancedAgent(Agent):
    """Agent with emotion type and logistic/logarithmic evolution."""

    def __init__(self, name: str, emotion_type: str = "neutral", **kwargs) -> None:
        super().__init__(name, **kwargs)
        self.emotion_type = emotion_type

    def update_emotion(self, value: float) -> None:
        """Override to adjust tension based on emotion type."""
        if self.emotion_type == "positive":
            self.tension += logarithmic_function(value)
        elif self.emotion_type == "negative":
            self.tension -= logarithmic_function(value)
        else:
            self.tension += logarithmic_function(value) / 2
        self.emotion = value

    def evolve(self) -> Tuple[float, float]:
        """Update tension using logistic growth."""
        bio = logistic_function(self.tension)
        soc = logarithmic_function(self.emotion)
        self.tension = bio + soc
        self.transition()
        return self.tension, self.emotion
