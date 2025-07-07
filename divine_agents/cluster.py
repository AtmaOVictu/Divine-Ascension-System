from __future__ import annotations

import random
from typing import List

from .agent import Agent


class Cluster:
    """Group of agents that can synchronize their transitions."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def synchronize(self) -> List[str]:
        """Update emotions randomly and perform transitions across agents."""
        lines = []
        for agent in self.agents:
            agent.update_emotion(random.uniform(0, 1))
            lines.append(f"{agent.name} prehaja v stanje: {agent.transition()}")
            lines.append(f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}")
        return lines
