import math
from typing import Tuple

from .agent import Agent


def logistic_function(t: float, k: float, c: float) -> float:
    """Basic logistic growth function."""
    return 1.0 / (1.0 + math.exp(-k * (t - c)))


def logarithmic_function(t: float, k: float, c: float) -> float:
    """Basic logarithmic growth with offset to avoid negative domain."""
    if t + c <= 0:
        return 0.0
    return k * math.log(t + c)


class AdvancedAgent(Agent):
    """Agent with logistic and logarithmic tension evolution."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 k_bio: float = 1.0, c_bio: float = 0.5, k_soc: float = 1.5, c_soc: float = 0.6) -> None:
        super().__init__(name, state, tension, emotion)
        self.k_bio = k_bio
        self.c_bio = c_bio
        self.k_soc = k_soc
        self.c_soc = c_soc

    def evolve(self) -> str:
        """Update tension using logistic and logarithmic transitions then change state."""
        bio = logistic_function(self.tension, self.k_bio, self.c_bio)
        soc = logarithmic_function(self.tension, self.k_soc, self.c_soc)
        self.tension = bio + soc
        return self.transition()

    def get_state(self) -> Tuple[float, float]:
        """Return current tension and emotion."""
        return self.tension, self.emotion

    def respond(self, question: str) -> str:
        base = super().respond(question)
        if self.emotion > 0.5:
            mood = "čustveno"
        elif self.emotion < -0.5:
            mood = "umirjeno"
        else:
            mood = "nevtralno"
        return f"{base} (odgovorjeno {mood})"
