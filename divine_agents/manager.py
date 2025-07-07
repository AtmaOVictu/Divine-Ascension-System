"""Utility classes for coordinating agents and recording their actions."""
from __future__ import annotations

import time
from typing import List

from .agent import Agent


class SubAgent:
    """Helper entity that logs actions for an associated agent."""

    def __init__(self, name: str, associated_agent: Agent) -> None:
        self.name = name
        self.associated_agent = associated_agent
        self.logs: List[str] = []

    def log_action(self, action: str) -> None:
        """Record an action with a timestamp."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        entry = f"{timestamp} - {self.name}: {action}"
        self.logs.append(entry)

    def sort_logs(self) -> List[str]:
        """Return logs sorted by timestamp."""
        return sorted(self.logs)


class ManagerAgent:
    """Coordinates a group of agents and triggers their transitions."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Register an agent under this manager's control."""
        self.agents.append(agent)

    def manage_transitions(self) -> None:
        """Call transition on all managed agents."""
        for agent in self.agents:
            previous = agent.state
            agent.transition()
            if previous != agent.state:
                # optional print or log
                pass
