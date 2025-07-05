import math
from .agent import Agent


def biological_transition(t: float, k_bio: float, c_bio: float) -> float:
    """Logistic transition for biological phase."""
    return 1 / (1 + math.exp(-k_bio * (t - c_bio)))


def social_transition(t: float, k_soc: float, c_soc: float) -> float:
    """Logistic transition for social phase."""
    return 1 / (1 + math.exp(-k_soc * (t - c_soc)))


class DynamicAgent(Agent):
    """Agent with dynamic tension and social phases."""

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
        self.state_bio = tension
        self.state_soc = 0.0
        self.k_bio = k_bio
        self.c_bio = c_bio
        self.k_soc = k_soc
        self.c_soc = c_soc
        self.shadow = 0.0

    def update_emotion(self, value: float, shadow: float = 0.0) -> None:
        """Update emotion and tension, recording opposing shadow."""
        self.emotion = value
        self.shadow = shadow
        self.tension += value + shadow

    def evolve(self) -> None:
        """Evolve biological and social states, then attempt transition."""
        self.state_bio = biological_transition(self.state_bio, self.k_bio, self.c_bio)
        self.state_soc = social_transition(self.state_soc, self.k_soc, self.c_soc)
        self.transition()

    def get_state(self):
        """Return current biological and social phases with emotion info."""
        return self.state_bio, self.state_soc, self.emotion, self.shadow


class MultiAgentSystem:
    """Container managing multiple dynamic agents."""

    def __init__(self, num_agents: int = 5) -> None:
        self.agents = [DynamicAgent(name=f"A{i}") for i in range(num_agents)]

    def evolve_agents(self) -> None:
        for agent in self.agents:
            agent.evolve()

    def update_agents_emotion(self, emotions, shadows) -> None:
        for agent, em, sh in zip(self.agents, emotions, shadows):
            agent.update_emotion(em, sh)

    def get_agents_state(self):
        return [agent.get_state() for agent in self.agents]
