from __future__ import annotations
from typing import Dict, List

from .agent import Agent


class SubAgentManager:
    """Manage multiple agents and their logs."""

    def __init__(self) -> None:
        self.agents: Dict[str, Agent] = {}

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the manager."""
        self.agents[agent.name] = agent

    def sort_logs_by_version(self) -> List[Agent]:
        """Return agents sorted by their timestamp/version."""
        return sorted(self.agents.values(), key=lambda a: a.timestamp)

    def save_all_histories(self) -> None:
        """Save state histories for all managed agents."""
        for agent in self.agents.values():
            agent.save_history()
            print(f"Log saved for {agent.name} with version {agent.version}")
