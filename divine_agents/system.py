from __future__ import annotations
from typing import List
from .agent import Agent
from .krak import Krak

class CodexSystem:
    """Manage agents and kraki in the system."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []
        self.kraks: List[Krak] = []

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def add_krak(self, krak: Krak) -> None:
        self.kraks.append(krak)

    def update(self) -> None:
        for agent in self.agents:
            agent.transition()
        for krak in self.kraks:
            krak.transition()
