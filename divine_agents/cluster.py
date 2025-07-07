from __future__ import annotations

import random
from typing import List

from .agent import Agent


class Cluster:
    """Group of agents interacting and evolving together."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def synchronize(self) -> List[str]:
        """Synchronize transitions across agents and collect reflections."""
        lines = []
        for agent in self.agents:
            agent.update_emotion(random.uniform(0, 1))
            state = agent.transition()
            lines.append(f"{agent.name} je v stanju: {state}")
            lines.append(agent.respond("Kaj je resnica?"))
        return lines
