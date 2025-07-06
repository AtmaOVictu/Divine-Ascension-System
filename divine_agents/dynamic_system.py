"""Multi-agent system for coordinating dialogues and state transitions."""
from typing import List

from .agent import Agent
from .dialogue import philosophical_dialogue


class DynamicAgentSystem:
    """Manage multiple agents and simulate dialogues between them."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Register a new agent in the system."""
        self.agents.append(agent)

    def run_simulation(self) -> List[str]:
        """Run a simple simulation where each adjacent pair of agents dialog."""
        lines: List[str] = []
        for i in range(len(self.agents) - 1):
            a1 = self.agents[i]
            a2 = self.agents[i + 1]
            lines.extend(philosophical_dialogue(a1, a2))
        return lines
