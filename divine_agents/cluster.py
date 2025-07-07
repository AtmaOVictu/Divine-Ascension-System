from __future__ import annotations

import random
from typing import List

from .agent import Agent


class Cluster:
    """Group of agents that transition together."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def synchronize(self) -> List[str]:
        """Synchronize transitions across all agents."""
        reflections = []
        for agent in self.agents:
            agent.update_emotion(random.uniform(0, 1))
            agent.update_rationality(random.uniform(0, 1))
            agent.transition()
            reflections.append(agent.reflect_opposites())
        return reflections
