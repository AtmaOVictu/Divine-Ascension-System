"""Sub-agent responsible for managing agent logs and histories."""
from __future__ import annotations

from typing import Dict, List

from .agent import Agent


class SubAgent:
    """Manage multiple agents and organise their log files."""

    def __init__(self) -> None:
        self.agents: Dict[str, Agent] = {}

    def add_agent(self, agent: Agent) -> None:
        """Register an agent with the manager."""
        self.agents[agent.name] = agent

    def sort_logs_by_version(self) -> List[Agent]:
        """Return agents sorted by their version timestamp."""
        return sorted(self.agents.values(), key=lambda a: a.version)

    def save_all_logs(self) -> None:
        """Save state histories for all managed agents."""
        for agent in self.agents.values():
            agent.save_history()
            print(f"Log saved for {agent.name} with version {agent.version}")
