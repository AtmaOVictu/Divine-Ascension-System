"""Utility for managing philosophical dialogue between agents."""

from __future__ import annotations

from typing import List

from .agent import Agent


class DialogueManager:
    """Orchestrates conversations and handles emotional escalation."""

    def __init__(self, agent1: Agent, agent2: Agent):
        self.agent1 = agent1
        self.agent2 = agent2

    def step(self) -> List[str]:
        """Execute a single dialogue exchange and update agent states."""
        a1, a2 = self.agent1, self.agent2
        lines = [
            f"{a1.name} ({a1.state}): {a1.speak()}",
            f"{a2.name} ({a2.state}): {a2.speak()}",
        ]

        # increase emotional intensity for both agents
        a1.update_emotion(a1.emotion + 0.3)
        lines.append(f"{a1.name} prehaja v stanje: {a1.transition()}")

        a2.update_emotion(a2.emotion + 0.3)
        lines.append(f"{a2.name} prehaja v stanje: {a2.transition()}")

        return lines

    def run(self, steps: int = 1) -> List[str]:
        """Run multiple dialogue steps and return the transcript."""
        transcript: List[str] = []
        for _ in range(steps):
            transcript.extend(self.step())
        return transcript
