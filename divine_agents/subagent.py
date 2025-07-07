from __future__ import annotations
from typing import Dict, List

from .agent import Agent


class SubAgent:
    """Manage multiple agents and their logs."""

    def __init__(self) -> None:
        self.agents_logs: Dict[str, Agent] = {}

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the manager."""
        self.agents_logs[agent.name] = agent

    def sort_logs_by_version(self) -> List[Agent]:
        """Return agents sorted by their timestamp/version."""
        return sorted(self.agents_logs.values(), key=lambda a: a.timestamp)

    def save_all_logs(self) -> None:
        """Persist histories for all agents."""
        for agent in self.agents_logs.values():
            agent.save_history()
            print(f"Log saved for {agent.name} with version {agent.version}")

