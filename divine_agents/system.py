from __future__ import annotations

from typing import List

from .agent import Agent


class AgentSystem:
    """Container for multiple agents managing density and interactions."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def density(self) -> int:
        """Return the number of agents in the system."""
        return len(self.agents)

    def apply_density_influence(self) -> None:
        """Increase tension for all agents based on system density."""
        dens = self.density()
        for agent in self.agents:
            agent.update_tension(agent.tension + 0.1 * dens)
