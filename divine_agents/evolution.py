import math


def biological_transition(t: float, k_bio: float, c_bio: float) -> float:
    """Logistic function modeling biological transitions."""
    return 1 / (1 + math.exp(-k_bio * (t - c_bio)))


def social_transition(t: float, k_soc: float, c_soc: float) -> float:
    """Logistic function modeling social transitions."""
    return 1 / (1 + math.exp(-k_soc * (t - c_soc)))


class EvolvingAgent:
    """Agent with independent biological and social evolution."""

    def __init__(self, name: str, state_bio: float = 0.0, state_soc: float = 0.0,
                 k_bio: float = 1.0, c_bio: float = 0.5,
                 k_soc: float = 1.5, c_soc: float = 0.6):
        self.name = name
        self.state_bio = state_bio
        self.state_soc = state_soc
        self.k_bio = k_bio
        self.c_bio = c_bio
        self.k_soc = k_soc
        self.c_soc = c_soc

    def evolve(self) -> None:
        """Advance the agent through biological and social phases."""
        self.state_bio = biological_transition(self.state_bio, self.k_bio, self.c_bio)
        self.state_soc = social_transition(self.state_soc, self.k_soc, self.c_soc)

    def get_state(self) -> tuple:
        """Return the current biological and social states."""
        return self.state_bio, self.state_soc
