from typing import List
from .agent import Agent


class AgentSystem:
    """Manage a collection of agents and their interactions."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def density(self) -> int:
        """Return the number of agents, representing system density."""
        return len(self.agents)

    def propagate(self) -> None:
        """Increase emotion and tension based on density and apply transitions."""
        d = self.density()
        for agent in self.agents:
            agent.update_emotion(agent.emotion + 0.3 * d)
            agent.update_tension(agent.tension + 0.3 * d)
            agent.transition()
