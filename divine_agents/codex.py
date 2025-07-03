from typing import List
from .agent import Agent
from .dialogue import philosophical_debate


class Codex:
    """Manage a collection of agents and run debates."""

    def __init__(self, num_agents: int = 2):
        self.agents: List[Agent] = [Agent(f"Agent{i+1}") for i in range(num_agents)]

    def run(self) -> List[str]:
        if len(self.agents) >= 2:
            return philosophical_debate(self.agents[0], self.agents[1])
        return []
