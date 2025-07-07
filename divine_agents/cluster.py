from __future__ import annotations

from typing import List

from .agent import Agent
from .dialogue import philosophical_dialogue


class AgentCluster:
    """Manage multiple agents and coordinate their debates."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def debate(self, rounds: int = 1) -> List[str]:
        """Run a debate among all agents and return dialogue lines."""
        lines: List[str] = []
        if len(self.agents) < 2:
            return lines

        a1, a2 = self.agents[0], self.agents[1]
        lines.extend(philosophical_dialogue(a1, a2, rounds=rounds))
        return lines
