"""Manager and sub-agent classes for coordinating agent activities."""
from __future__ import annotations

import time
from typing import List

from .agent import Agent


class SubAgent:
    """Helper agent that logs actions of a main agent."""

    def __init__(self, name: str, associated_agent: Agent):
        self.name = name
        self.associated_agent = associated_agent
        self.logs: List[str] = []
        self.timestamp = time.time()

    def log_action(self, action: str) -> None:
        """Record an action with a timestamp."""
        timestamp_str = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))
        entry = f"{timestamp_str} - {self.name}: {action}"
        self.logs.append(entry)

    def sort_logs(self) -> List[str]:
        """Return logs sorted by timestamp."""
        self.logs.sort(key=lambda x: x.split(' - ')[0])
        return self.logs


class ManagerAgent:
    """Manager that oversees multiple agents and coordinates transitions."""

    def __init__(self, name: str):
        self.name = name
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Register an agent under management."""
        self.agents.append(agent)

    def manage_transitions(self) -> None:
        """Invoke transitions on all managed agents."""
        for agent in self.agents:
            agent.transition()
