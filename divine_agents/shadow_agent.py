import math
from .agent import Agent

class AgentWithShadow(Agent):
    """Agent extended with shadow (opposite emotion) support."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, shadow: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.shadow = shadow

    def update_emotion(self, emotion_value: float, shadow_value: float) -> None:
        """Update emotion and shadow, influencing tension."""
        self.emotion = emotion_value
        self.shadow = shadow_value
        # Increase tension based on the combination of emotion and its shadow
        self.tension += (self.emotion + self.shadow)

    @staticmethod
    def logistic_emotion(t: float, shadow: float, k_emo: float = 1.0, c_emo: float = 0.0) -> float:
        """Return logistic emotion influenced by a shadow value."""
        base = 1 / (1 + math.exp(-k_emo * (t - c_emo)))
        return base * (1 + shadow)

    def get_tension(self) -> float:
        """Return current tension level."""
        return self.tension
