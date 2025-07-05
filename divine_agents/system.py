from dataclasses import dataclass
from typing import List
from .agent import Agent


@dataclass
class AgentSystem:
    """Manage a collection of agents and their interactions."""

    agents: List[Agent]
    factor: float = 0.3

    def density(self) -> int:
        """Return the number of agents, representing system density."""
        return len(self.agents)

    def propagate(self) -> None:
        """Increase emotion and tension based on density and apply transitions."""
        d = self.density()
        for agent in self.agents:
            agent.update_emotion(agent.emotion + self.factor * d)
            agent.update_tension(agent.tension + self.factor * d)
            agent.transition()
