from typing import List
from .agent import Agent


class Modul:
    """Connects agents with a specific task."""

    def __init__(self, name: str, task: str):
        self.name = name
        self.task = task
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def execute(self) -> None:
        for agent in self.agents:
            agent.ontoznano.transition(self.task)
