from __future__ import annotations

import random
from typing import List, Optional

from .agent import Agent


class MultiAgentSystem:
    """Manage multiple agents and orchestrate their updates."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the system."""
        self.agents.append(agent)

    def update_all_agents(self, emotions: Optional[List[float]] = None) -> None:
        """Update emotions and trigger transitions for all agents."""
        for idx, agent in enumerate(self.agents):
            if emotions and idx < len(emotions):
                agent.update_emotion(emotions[idx])
            else:
                agent.update_emotion(random.uniform(0, 1))
            agent.transition()
