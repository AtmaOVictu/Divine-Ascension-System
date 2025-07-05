from typing import List
from .agent import Agent

class MultiAgentSystem:
    """Manage multiple agents and their interactions."""

    def __init__(self):
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def update_all_agents(self) -> None:
        """Update emotions randomly to trigger transitions."""
        for agent in self.agents:
            agent.update_emotion(0.8)  # simplified deterministic update
            agent.transition()
