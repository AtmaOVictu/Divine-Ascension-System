"""Manage a collection of agents engaged in philosophical dialogue."""
from typing import List

from .agent import Agent
from .dialogue import philosophical_dialogue


class Cluster:
    """A cluster coordinating multiple agents."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def run(self, rounds: int = 1) -> List[str]:
        """Run several rounds of dialogue among all agents."""
        transcript: List[str] = []
        for _ in range(rounds):
            if len(self.agents) < 2:
                break
            a1, a2 = self.agents[0], self.agents[1]
            transcript.extend(philosophical_dialogue(a1, a2))
        return transcript
