"""Agent logic for ontological transitions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


from .math_utils import logistic_function, logarithmic_function


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    k_bio: float = 1.0
    c_bio: float = 0.5
    k_soc: float = 1.5
    c_soc: float = 0.6
    history: List[str] = field(default_factory=lambda: ["Ego"])

    def __post_init__(self) -> None:
        self.history = [self.state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def evolve(self) -> None:
        """Update tension based on logistic and logarithmic transitions."""
        bio = logistic_function(self.tension, self.k_bio, self.c_bio)
        soc = logarithmic_function(self.tension, self.k_soc, self.c_soc)
        self.tension = bio + soc

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def get_state(self) -> tuple[float, float]:
        """Return current tension and emotion."""
        return self.tension, self.emotion

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


class AdvancedAgent(Agent):
    """Agent with emotion type influencing tension updates."""

    def __init__(self, name: str, emotion_type: str = "neutral", **kwargs: float) -> None:
        super().__init__(name, **kwargs)
        self.emotion_type = emotion_type

    def update_emotion(self, value: float) -> None:
        """Update emotion and tension depending on emotion type."""
        self.emotion = value
        if self.emotion_type == "positive":
            self.tension += value
        elif self.emotion_type == "negative":
            self.tension -= value
        else:
            self.tension += value / 2
