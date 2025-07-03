from __future__ import annotations
from typing import List
from .agent import Agent


class MultiAgentLearningSystem:
    """Manage a collection of agents and their copies for comparison."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents
        self.agent_copies: List[Agent] = []

    def generate_copies(self) -> None:
        """Create copies of the current agents."""
        self.agent_copies = [agent.copy() for agent in self.agents]

    def compare_histories(self) -> List[str]:
        """Compare agent histories and return differences."""
        diffs = []
        for i in range(len(self.agent_copies) - 1):
            a1 = self.agent_copies[i]
            a2 = self.agent_copies[i + 1]
            if a1.history != a2.history:
                diffs.append(f"Razlike med {a1.name} in {a2.name}: {a1.history} vs {a2.history}")
        return diffs

    def learn(self) -> None:
        """Adjust emotions slightly to simulate learning from experiences."""
        for agent in self.agent_copies:
            agent.update_emotion(agent.emotion + 0.1)
            agent.transition()
