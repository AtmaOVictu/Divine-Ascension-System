from __future__ import annotations

from typing import List, Sequence

from .agent import Agent


class Discourse:
    """Handle dynamic philosophical dialogue between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.lines: List[str] = []

    def step(self, emotion1: float, emotion2: float, question: str) -> None:
        """Run a single step of the discourse."""
        self.agent1.update_emotion(emotion1)
        self.agent2.update_emotion(emotion2)

        self.lines.append(
            f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond(question)}"
        )
        self.lines.append(
            f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond(question)}"
        )

        self.lines.append(f"{self.agent1.name} transition: {self.agent1.transition()}")
        self.lines.append(f"{self.agent2.name} transition: {self.agent2.transition()}")

    def run(
        self,
        question: str,
        emotions1: Sequence[float],
        emotions2: Sequence[float],
    ) -> List[str]:
        """Execute the discourse over multiple steps."""
        for e1, e2 in zip(emotions1, emotions2):
            self.step(e1, e2, question)
        return self.lines
