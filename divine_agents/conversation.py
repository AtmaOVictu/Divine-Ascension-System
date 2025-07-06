from __future__ import annotations

from typing import List, Tuple

from .agent import Agent


class Conversation:
    """Manage philosophical dialogue between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent):
        self.agent1 = agent1
        self.agent2 = agent2
        self.log: List[str] = []

    def step(self, emotion1: float, emotion2: float) -> Tuple[str, str]:
        """Perform one exchange with updated emotions."""
        self.agent1.update_emotion(emotion1)
        self.agent2.update_emotion(emotion2)

        self.agent1.transition()
        self.agent2.transition()

        line1 = f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}"
        line2 = f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}"
        self.log.extend([line1, line2])
        return line1, line2

    def run(self, steps: List[Tuple[float, float]]) -> List[str]:
        """Run conversation for a sequence of emotion updates."""
        for e1, e2 in steps:
            self.step(e1, e2)
        return self.log
