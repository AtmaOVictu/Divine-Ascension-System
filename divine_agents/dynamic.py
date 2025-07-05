import math
from typing import List
from .agent import Agent


def biological_transition(t: float, k_bio: float, c_bio: float) -> float:
    """Logistic function modeling biological transitions."""
    return 1.0 / (1.0 + math.exp(-k_bio * (t - c_bio)))


def social_transition(t: float, k_soc: float, c_soc: float) -> float:
    """Logistic function modeling social transitions."""
    return 1.0 / (1.0 + math.exp(-k_soc * (t - c_soc)))


class DynamicAgent(Agent):
    """Agent with additional biological and social transition phases."""

    def __init__(
        self,
        id: int,
        initial_tension: float = 0.0,
        k_bio: float = 1.0,
        c_bio: float = 0.5,
        k_soc: float = 1.5,
        c_soc: float = 0.6,
        **kwargs,
    ) -> None:
        super().__init__(name=f"Agent{id}", state=kwargs.get("state", "Ego"), tension=initial_tension)
        self.state_bio = initial_tension
        self.state_soc = 0.0
        self.k_bio = k_bio
        self.c_bio = c_bio
        self.k_soc = k_soc
        self.c_soc = c_soc
        self.shadow = 0.0

    def update_emotion(self, emotion_value: float, shadow_value: float = 0.0) -> None:
        """Update emotion along with its opposite (shadow)."""
        super().update_emotion(emotion_value)
        self.shadow = shadow_value
        self.tension += shadow_value

    def evolve(self) -> None:
        """Evolve through biological and social phases and transition state."""
        self.state_bio = biological_transition(self.state_bio, self.k_bio, self.c_bio)
        self.state_soc = social_transition(self.state_soc, self.k_soc, self.c_soc)
        self.transition()

    def get_state(self) -> tuple:
        """Return current biological, social and ontological states."""
        return self.state_bio, self.state_soc, self.state


class MultiAgentSystem:
    """Simple system managing multiple DynamicAgents."""

    def __init__(self, num_agents: int = 2) -> None:
        self.agents: List[DynamicAgent] = [DynamicAgent(i) for i in range(num_agents)]

    def step(self, emotions: List[float], shadows: List[float]) -> None:
        """Update emotions and evolve all agents."""
        for agent, e_val, s_val in zip(self.agents, emotions, shadows):
            agent.update_emotion(e_val, s_val)
            agent.evolve()

    def states(self) -> List[tuple]:
        """Return states for all agents."""
        return [agent.get_state() for agent in self.agents]

