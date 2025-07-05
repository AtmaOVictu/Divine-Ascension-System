"""Simple simulation utilities for ontological agents."""

from math import exp, sin
from typing import Tuple, List
from .agent import Agent


def logistic_function(t: float, k: float, c: float) -> float:
    """Standard logistic function used for transitions."""
    return 1 / (1 + exp(-k * (t - c)))


class OntologicalAgent(Agent):
    """Extended Agent with evolve capability using logistic transitions."""

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
        """Update tension based on logistic bio and social transitions."""
        bio = logistic_function(self.tension, self.k_bio, self.c_bio)
        soc = logistic_function(self.tension, self.k_soc, self.c_soc)
        self.tension = bio + soc


def simulate(agent: OntologicalAgent, steps: int = 100) -> Tuple[List[float], List[float]]:
    """Run a simple simulation updating agent emotion over time."""
    step_size = 10 / max(1, steps - 1)
    tensions: List[float] = []
    emotions: List[float] = []
    t = 0.0
    for _ in range(steps):
        emotion_value = sin(t) * 5
        agent.update_emotion(emotion_value)
        agent.evolve()
        agent.transition()
        tensions.append(agent.tension)
        emotions.append(agent.emotion)
        t += step_size
    return tensions, emotions
