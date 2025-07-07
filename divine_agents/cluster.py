from __future__ import annotations

import random
from typing import List

from .agent import Agent


class Cluster:
    """Represents a cluster of agents sharing emotions and transitions."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents
        self.history: List[str] = []

    def synchronize(self) -> None:
        """Synchronize transitions across all agents in the cluster."""
        for agent in self.agents:
            agent.update_emotion(agent.mood, random.uniform(0, 1))
            agent.update_tension(random.uniform(0, 1))
            agent.transition()
            self.history.append(agent.state)
