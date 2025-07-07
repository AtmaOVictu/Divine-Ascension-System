from __future__ import annotations

import time
from typing import List

from .agent import Agent


class SubAgent:
    """Helper entity that logs actions performed by its associated agent."""

    def __init__(self, name: str, associated_agent: Agent):
        self.name = name
        self.associated_agent = associated_agent
        self.logs: List[str] = []

    def log_action(self, action: str) -> None:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        self.logs.append(f"{timestamp} - {self.name}: {action}")


class ManagerAgent:
    """Coordinates and oversees the state transitions of other agents."""

    def __init__(self, name: str):
        self.name = name
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def manage_transitions(self) -> None:
        for agent in self.agents:
            agent.transition()
