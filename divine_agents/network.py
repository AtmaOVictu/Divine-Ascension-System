from __future__ import annotations
from typing import List

from .agent import Agent


class SharedMemory:
    """Store reflections from all agents for historical reference."""

    def __init__(self) -> None:
        self.log: List[str] = []

    def record(self, reflection: str) -> None:
        self.log.append(reflection)

    def history(self) -> List[str]:
        return list(self.log)


class AgentNetwork:
    """Manage multiple agents and facilitate shared reflections."""

    def __init__(self, memory: SharedMemory | None = None) -> None:
        self.agents: List[Agent] = []
        self.memory = memory or SharedMemory()

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def share_reflections(self) -> List[str]:
        reflections: List[str] = []
        for agent in self.agents:
            reflection = agent.reflect()
            reflections.append(reflection)
            self.memory.record(reflection)
        return reflections

    def evolve(self) -> None:
        reflections = self.share_reflections()
        for agent in self.agents:
            agent.learn_from_others(reflections)
