import math
import random
from typing import List

from .agent import Agent


def logistic(value: float, k: float, c: float) -> float:
    """Calculate a logistic transition for a given value."""
    return 1.0 / (1.0 + math.exp(-k * (value - c)))


class DynamicAgent(Agent):
    """Agent with biological and social evolution using logistic functions."""

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        k_bio: float = 1.0,
        c_bio: float = 0.5,
        k_soc: float = 1.5,
        c_soc: float = 0.5,
    ) -> None:
        super().__init__(name, state, tension, emotion)
        self.k_bio = k_bio
        self.c_bio = c_bio
        self.k_soc = k_soc
        self.c_soc = c_soc
        self.social = 0.0

    def evolve(self) -> None:
        """Evolve tension and social state via logistic transitions."""
        self.tension = logistic(self.tension, self.k_bio, self.c_bio)
        self.social = logistic(self.social, self.k_soc, self.c_soc)

    def update_emotion(self, value: float, shadow: float = 0.0) -> None:
        """Update emotion and adjust tension considering a shadow value."""
        self.emotion = value
        self.tension += value + shadow


class MultiAgentSystem:
    """Simple container managing multiple DynamicAgents."""

    def __init__(self, num_agents: int = 2) -> None:
        self.agents = [DynamicAgent(f"A{i+1}") for i in range(num_agents)]

    def step(self) -> None:
        """Randomly update emotions and evolve all agents."""
        for agent in self.agents:
            emotion = random.uniform(0, 1)
            shadow = random.uniform(-0.5, 0.5)
            agent.update_emotion(emotion, shadow)
            agent.evolve()
            agent.transition()

    def dialogue(self) -> List[str]:
        """Return dialogue lines for all agents."""
        lines = []
        for agent in self.agents:
            lines.append(f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}")
        return lines
