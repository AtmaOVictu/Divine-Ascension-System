from __future__ import annotations

import random
from typing import List

from .agent import Agent


class Cluster:
    """Cluster managing multiple agents and collective transitions."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents
        self.history: List[str] = []

    def synchronize(self) -> None:
        """Synchronize agents by updating emotions and triggering transitions."""
        for agent in self.agents:
            agent.update_emotion(agent.mood, random.uniform(0, 1))
            agent.update_tension(random.uniform(0, 1))
            new_state = agent.transition()
            self.history.append(f"{agent.name}:{new_state}")

    def dialogue(self, question: str) -> List[str]:
        """Generate dialogue lines for all agents."""
        lines = []
        for agent in self.agents:
            lines.append(f"{agent.name} ({agent.state}): {agent.respond(question)}")
        return lines
