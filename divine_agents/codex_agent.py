"""Advanced agent with logistic and logarithmic evolution."""

import math
from .agent import Agent


def logistic_function(t: float, k: float, c: float) -> float:
    """Basic logistic function."""
    return 1 / (1 + math.exp(-k * (t - c)))


def logarithmic_function(t: float, k: float, c: float) -> float:
    """Basic logarithmic growth."""
    return k * math.log(t + c)


class CodexAgent(Agent):
    """Agent that evolves tension using logistic and logarithmic functions."""

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

    def evolve(self) -> None:
        """Update tension using logistic and logarithmic functions."""
        bio = logistic_function(self.tension, self.k_bio, self.c_bio)
        soc = logarithmic_function(self.tension, self.k_soc, self.c_soc)
        self.tension = bio + soc

    def update_emotion(self, value: float) -> None:
        """Override to include evolution step."""
        self.emotion = value
        self.tension += value
        self.evolve()

    def respond(self, question: str) -> str:
        base = super().respond(question)
        if self.emotion > 0.5:
            return base + " (izraženo s strastjo)"
        if self.emotion < -0.5:
            return base + " (z dvomom)"
        return base
