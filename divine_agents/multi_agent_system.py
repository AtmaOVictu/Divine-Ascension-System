from __future__ import annotations

import random
from typing import List

from .agent import Agent


class MultiAgentSystem:
    """Manage multiple agents and update them collectively."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the system."""
        self.agents.append(agent)

    def update_all_agents(self) -> None:
        """Randomly adjust emotions and perform transitions for all agents."""
        for agent in self.agents:
            agent.update_emotion(random.uniform(0, 1))
            agent.transition()
