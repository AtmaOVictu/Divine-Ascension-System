from typing import List
from .agent import Agent


class EnergyNetwork:
    """Model for energy and voltage interactions between agents."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def transfer(self, source: Agent, target: Agent, factor: float) -> None:
        """Transfer energy from source to target and update voltage."""
        delta = source.energy * factor
        source.update_energy(-delta)
        target.update_energy(delta)
        # Voltage change is proportional to energy transferred
        target.update_voltage(delta * 0.1)

    def step(self) -> None:
        """Apply a simple interaction among all agents in the network."""
        if len(self.agents) < 2:
            return
        for i, agent in enumerate(self.agents):
            next_agent = self.agents[(i + 1) % len(self.agents)]
            self.transfer(agent, next_agent, 0.1)
