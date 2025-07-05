import math
from typing import List
from .agent import Agent


def logistic(t: float, k: float = 1.0, c: float = 0.5) -> float:
    """Compute logistic function value for time *t*."""
    return 1 / (1 + math.exp(-k * (t - c)))


class MultiAgentSystem:
    """Manage multiple agents and evolve them over time."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def evolve(self, t: float, k_emotion: float = 1.0, c_emotion: float = 0.5) -> None:
        """Evolve all agents by updating emotion via logistic curve and triggering transitions."""
        for agent in self.agents:
            new_emotion = logistic(t, k_emotion, c_emotion)
            agent.update_emotion(new_emotion)
            agent.transition()

    def get_states(self) -> List[str]:
        """Return the current states of all agents."""
        return [agent.state for agent in self.agents]
