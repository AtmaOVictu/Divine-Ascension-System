from __future__ import annotations
import random
from typing import List

from .agent import Agent

class Cluster:
    """Group of agents sharing interactions."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def synchronize(self) -> List[str]:
        """Update agents' emotions and tensions and perform transitions."""
        log: List[str] = []
        for agent in self.agents:
            agent.update_emotion(random.uniform(0, 1))
            agent.update_tension(random.uniform(0, 1))
            prev_state = agent.state
            agent.transition()
            if agent.state != prev_state:
                log.append(f"{agent.name} transitioned to {agent.state}")
        return log
