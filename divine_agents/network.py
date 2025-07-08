from __future__ import annotations
from typing import List
from .agent import Agent

class SharedMemory:
    """Central memory storing reflections from all agents."""

    def __init__(self) -> None:
        self.log: List[str] = []

    def record(self, entry: str) -> None:
        self.log.append(entry)

    def history(self) -> List[str]:
        return list(self.log)

class AgentNetwork:
    """A simple network orchestrating agent interactions."""

    def __init__(self, memory: SharedMemory | None = None) -> None:
        self.agents: List[Agent] = []
        self.memory = memory or SharedMemory()

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def share_reflections(self) -> List[str]:
        reflections = [agent.reflect() for agent in self.agents]
        for entry in reflections:
            self.memory.record(entry)
        return reflections

    def evolve_agents(self) -> None:
        reflections = self.share_reflections()
        for agent in self.agents:
            agent.learn_from_others(reflections)
            agent.transition()

