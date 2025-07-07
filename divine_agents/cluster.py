from __future__ import annotations

from typing import List
import random

from .agent import Agent


class Cluster:
    """Group of agents that can synchronize their transitions."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents
        self.history: List[str] = []

    def synchronize(self) -> None:
        """Synchronize transitions across all agents."""
        for agent in self.agents:
            # Randomly update emotions to emulate conversation dynamics
            mood = random.choice(["joy", "fear", "anger", "neutral"])
            agent.update_emotion(mood, random.uniform(0, 1))
            agent.update_tension(random.uniform(0, 1))
            agent.transition()
            self.history.append(agent.state)
