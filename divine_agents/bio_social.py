import math
import random
from typing import Tuple, List

from .agent import Agent


def biological_transition(t: float, k_bio: float, c_bio: float) -> float:
    """Logistic function modeling biological transitions."""
    return 1 / (1 + math.exp(-k_bio * (t - c_bio)))


def social_transition(t: float, k_soc: float, c_soc: float) -> float:
    """Logistic function modeling social transitions."""
    return 1 / (1 + math.exp(-k_soc * (t - c_soc)))


nptype = float


class BioSocialAgent(Agent):
    """Agent with biological and social transition dynamics."""

    def __init__(self,
                 name: str,
                 state_bio: float = 0.0,
                 state_soc: float = 0.0,
                 k_bio: float = 1.0,
                 c_bio: float = 0.5,
                 k_soc: float = 1.5,
                 c_soc: float = 0.6,
                 **kwargs) -> None:
        super().__init__(name, **kwargs)
        self.state_bio = nptype(state_bio)
        self.state_soc = nptype(state_soc)
        self.k_bio = k_bio
        self.c_bio = c_bio
        self.k_soc = k_soc
        self.c_soc = c_soc

    def evolve(self) -> Tuple[float, float]:
        """Evolve biological and social states and update emotion."""
        self.state_bio = biological_transition(self.state_bio, self.k_bio, self.c_bio)
        self.state_soc = social_transition(self.state_soc, self.k_soc, self.c_soc)
        emotion_value = float((self.state_bio + self.state_soc) / 2)
        self.update_emotion(emotion_value)
        self.transition()
        return float(self.state_bio), float(self.state_soc)

    def get_bio_social_state(self) -> Tuple[float, float]:
        return float(self.state_bio), float(self.state_soc)


def simulate_agents(num_agents: int, steps: int) -> List[BioSocialAgent]:
    """Simulate a list of agents through several evolution steps."""
    agents = [
        BioSocialAgent(
            name=f"Agent {i+1}",
            k_bio=random.uniform(0.5, 1.5),
            c_bio=random.uniform(0.3, 0.7),
            k_soc=random.uniform(1.0, 2.0),
            c_soc=random.uniform(0.5, 0.8),
        )
        for i in range(num_agents)
    ]

    for _ in range(steps):
        for agent in agents:
            agent.evolve()
    return agents
