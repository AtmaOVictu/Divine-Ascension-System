from typing import List
from .agent import Agent
from .dialogue import philosophical_dialogue


class Codex:
    """Simple coordinator for agent dialogue."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def run(self, emotion1: float = 0.8, emotion2: float = 0.6) -> List[str]:
        """Run a single dialogue round between the first two agents."""
        if len(self.agents) < 2:
            raise ValueError("At least two agents are required")
        a1, a2 = self.agents[:2]
        return philosophical_dialogue(a1, a2, emotion1, emotion2)
