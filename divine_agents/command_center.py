from typing import List
from .agent import Agent

class CommandCenter:
    """Simple coordinator that manages multiple agents."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def synchronize(self) -> List[str]:
        """Apply transitions to all agents and return their states."""
        results = []
        for agent in self.agents:
            results.append(f"{agent.name} prehaja v stanje: {agent.transition()}")
        return results
