"""Agent logic for ontological state transitions and responses."""


from __future__ import annotations

from dataclasses import dataclass, field
from math import exp, log


def logistic_function(t: float, k: float = 1.0, c: float = 0.0) -> float:
    """Return logistic growth for value ``t``."""
    return 1 / (1 + exp(-k * (t - c)))


def logarithmic_function(t: float, k: float = 1.0, c: float = 0.1) -> float:
    """Return logarithmic growth for value ``t``."""
    return k * log(t + c)


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_label: str = "neutral"
    history: list[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float, label: str = "neutral") -> None:
        """Update emotion intensity and adjust tension using logistic growth."""
        self.emotion = value
        self.emotion_label = label
        self.tension += logistic_function(value)

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
        """Return a philosophical answer influenced by the current emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} Občutim {self.emotion_label}."
