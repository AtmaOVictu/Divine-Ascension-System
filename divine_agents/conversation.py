from __future__ import annotations
from typing import List, Tuple

from .agent import Agent


class Conversation:
    """Manage a dialogue between two agents based on emotion and tension."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.transcript: List[str] = []

    def step(self, emotion1: float, emotion2: float) -> None:
        """Perform a single conversational step.

        Each agent updates emotion, possibly transitions state, and responds.
        The transcript is extended with both agents' replies.
        """
        self.agent1.update_emotion(emotion1)
        self.agent1.transition()
        self.agent2.update_emotion(emotion2)
        self.agent2.transition()

        self.transcript.append(
            f"{self.agent1.name} ({self.agent1.state}): "
            f"{self.agent1.respond('Kaj je resnica?')}"
        )
        self.transcript.append(
            f"{self.agent2.name} ({self.agent2.state}): "
            f"{self.agent2.respond('Kaj je resnica?')}"
        )

    def run(self, emotions: List[Tuple[float, float]]) -> List[str]:
        """Run multiple conversational steps given emotion pairs."""
        for e1, e2 in emotions:
            self.step(e1, e2)
        return self.transcript
