from typing import List
from .agent import Agent


class Modul:
    """Group of agents performing a shared task."""

    def __init__(self, name: str, task: str):
        self.name = name
        self.task = task
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def run(self) -> None:
        """Execute the task for all agents in this module."""
        for agent in self.agents:
            agent.update_emotion(0.3)
            agent.transition()
