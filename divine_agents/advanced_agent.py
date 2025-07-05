import math

from .agent import Agent


def logistic_function(t: float, k: float, c: float) -> float:
    """Return logistic progression for time t."""
    return 1 / (1 + math.exp(-k * (t - c)))


def logarithmic_function(t: float, k: float, c: float) -> float:
    """Return logarithmic progression for time t, safeguarded from negatives."""
    value = max(t + c, 1e-6)
    return k * math.log(value)


class AdvancedAgent(Agent):
    """Agent that evolves tension using logistic and logarithmic functions."""

    def __init__(self, name: str, emotion_type: str = "neutral", k_bio: float = 1.0,
                 c_bio: float = 0.5, k_soc: float = 1.5, c_soc: float = 0.6,
                 state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.emotion_type = emotion_type
        self.k_bio = k_bio
        self.c_bio = c_bio
        self.k_soc = k_soc
        self.c_soc = c_soc

    def update_emotion(self, value: float) -> None:
        """Update emotion and adjust tension based on emotion type."""
        self.emotion = value
        if self.emotion_type == "positive":
            self.tension += value
        elif self.emotion_type == "negative":
            self.tension -= value
        else:
            self.tension += value / 2

    def evolve(self) -> float:
        """Update tension using logistic and logarithmic transitions."""
        bio = logistic_function(self.tension, self.k_bio, self.c_bio)
        soc = logarithmic_function(abs(self.tension), self.k_soc, self.c_soc)
        self.tension = bio + soc
        self.transition()
        return self.tension
