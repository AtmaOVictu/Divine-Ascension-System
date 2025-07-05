"""Conversation logic for philosophical agents."""
from __future__ import annotations

from typing import List

from .agent import Agent


class Conversation:
    """Manage dialogue and emotional dynamics between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.history: List[str] = []

    def step(self) -> None:
        """Run a single step of conversation and possible transitions."""
        self.history.append(
            f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}"
        )
        self.history.append(
            f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}"
        )

        # escalate emotional intensity
        self.agent1.update_emotion(self.agent1.emotion + 0.3)
        self.agent2.update_emotion(self.agent2.emotion + 0.3)

        self.history.append(f"{self.agent1.name} prehaja v stanje: {self.agent1.transition()}")
        self.history.append(f"{self.agent2.name} prehaja v stanje: {self.agent2.transition()}")

    def run(self, steps: int = 1) -> List[str]:
        """Run the conversation for a number of steps."""
        for _ in range(steps):
            self.step()
        return self.history
