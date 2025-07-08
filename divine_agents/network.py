from __future__ import annotations
from typing import List
from .agent import Agent
from .shared_memory import SharedMemory


class AgentNetwork:
    """Network handling a collection of agents and shared reflections."""

    def __init__(self, shared_memory: SharedMemory | None = None) -> None:
        self.agents: List[Agent] = []
        self.shared_memory = shared_memory or SharedMemory()

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the network."""
        self.agents.append(agent)

    def share_reflections(self) -> List[str]:
        """Collect reflections from all agents and store them."""
        reflections = []
        for agent in self.agents:
            r = agent.reflect()
            reflections.append(r)
            self.shared_memory.record_event(r)
        return reflections

    def evolve_agents(self) -> None:
        """Allow agents to learn from each other's reflections."""
        reflections = self.share_reflections()
        for agent in self.agents:
            agent.learn_from_reflections(reflections)
