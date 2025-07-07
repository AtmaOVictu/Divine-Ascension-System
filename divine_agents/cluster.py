from __future__ import annotations
import random
from typing import List
from .agent import Agent


class Cluster:
    """Group of agents that synchronize their transitions."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def synchronize(self) -> List[str]:
        """Update agents' emotions and rationality and perform transitions."""
        lines: List[str] = []
        for agent in self.agents:
            agent.update_emotion(random.uniform(0, 1))
            agent.update_rationality(random.uniform(0, 1))
            new_state = agent.transition()
            lines.append(f"{agent.name} je zdaj v stanju {new_state}.")
        return lines
