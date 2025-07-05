"""Utility classes for managing and comparing versioned agents."""
from __future__ import annotations
from typing import List
from .agent import Agent


class MetaModule:
    """Maintain a collection of agents and provide comparison utilities."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def compare_agents(self, agent1: Agent, agent2: Agent) -> bool:
        """Return True if agents share the same name, version and state."""
        return (
            agent1.name == agent2.name
            and agent1.version == agent2.version
            and agent1.state == agent2.state
        )

    def show_all(self) -> List[str]:
        return [f"{a.name} ({a.version}) - {a.state}" for a in self.agents]
