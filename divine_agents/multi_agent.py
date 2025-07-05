from dataclasses import dataclass
import math
import random


def biological_transition(t: float, k_bio: float, c_bio: float) -> float:
    """Logistic function describing biological change."""
    return 1 / (1 + math.exp(-k_bio * (t - c_bio)))


def social_transition(t: float, k_soc: float, c_soc: float) -> float:
    """Logistic function describing social change."""
    return 1 / (1 + math.exp(-k_soc * (t - c_soc)))


@dataclass
class BioSocialAgent:
    """Agent with biological and social transition dynamics."""

    k_bio: float
    c_bio: float
    k_soc: float
    c_soc: float
    state_bio: float = 0.0
    state_soc: float = 0.0

    def evolve(self) -> None:
        """Update biological and social states."""
        self.state_bio = biological_transition(self.state_bio, self.k_bio, self.c_bio)
        self.state_soc = social_transition(self.state_soc, self.k_soc, self.c_soc)

    def get_state(self):
        return self.state_bio, self.state_soc


def create_random_agents(n: int) -> list[BioSocialAgent]:
    """Create ``n`` agents with random parameters for simulation."""
    agents = []
    for _ in range(n):
        agents.append(
            BioSocialAgent(
                k_bio=random.uniform(0.5, 1.5),
                c_bio=random.uniform(0.3, 0.7),
                k_soc=random.uniform(1.0, 2.0),
                c_soc=random.uniform(0.5, 0.8),
            )
        )
    return agents
