from __future__ import annotations

import random
from typing import List, Optional

from .agent import Agent


class Cluster:
    """Group of agents that evolve together."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def synchronize(self, rng: Optional[random.Random] = None) -> None:
        """Update emotions and tensions of all agents and perform transitions."""
        rng = rng or random
        for agent in self.agents:
            agent.update_emotion(rng.uniform(0, 1))
            agent.update_tension(rng.uniform(0, 1))
            agent.transition()
