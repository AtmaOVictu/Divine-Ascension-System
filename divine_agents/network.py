from typing import List

from .agent import Agent


class SharedMemory:
    """A simple shared memory for agents to record events."""

    def __init__(self) -> None:
        self.memory_log: List[str] = []

    def record_event(self, event: str) -> None:
        self.memory_log.append(event)

    def retrieve_history(self) -> List[str]:
        return list(self.memory_log)


class AgentNetwork:
    """Network allowing agents to share reflections and evolve."""

    def __init__(self, memory: SharedMemory) -> None:
        self.agents: List[Agent] = []
        self.memory = memory

    def add_agent(self, agent: Agent) -> None:
        agent.shared_memory = self.memory
        self.agents.append(agent)

    def share_reflections(self) -> List[str]:
        reflections = []
        for agent in self.agents:
            reflections.append(agent.reflect())
        return reflections

    def evolve_agents(self) -> None:
        history = self.memory.retrieve_history()
        for agent in self.agents:
            agent.learn_from_memory(history)
