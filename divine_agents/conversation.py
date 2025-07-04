"""Conversation simulation between ontological agents."""
from typing import List

from .agent import Agent


class Conversation:
    """Manage philosophical dialogue and emotional dynamics between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.history: List[str] = []

    def step(self) -> None:
        """Execute a single dialogue step with state updates."""
        self.history.append(
            f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}"
        )
        self.history.append(
            f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}"
        )

        # Increase emotional intensity to drive tension and transitions
        self.agent1.update_emotion(self.agent1.emotion + 0.3)
        self.history.append(
            f"{self.agent1.name} prehaja v stanje: {self.agent1.transition()}"
        )

        self.agent2.update_emotion(self.agent2.emotion + 0.3)
        self.history.append(
            f"{self.agent2.name} prehaja v stanje: {self.agent2.transition()}"
        )

    def run(self, steps: int = 1) -> List[str]:
        """Run multiple dialogue steps and return the transcript."""
        for _ in range(steps):
            self.step()
        return self.history
