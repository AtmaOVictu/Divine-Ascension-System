"""Agent cluster monitoring utilities."""
from __future__ import annotations

from typing import Iterable, Dict

from .agent import Agent


class AgentCluster:
    """Represents a group of agents that can be monitored collectively."""

    def __init__(self, agents: Iterable[Agent]):
        self.agents = list(agents)

    def check_states(self) -> Dict[str, str]:
        """Return current states of all agents."""
        return {agent.name: agent.state for agent in self.agents}

    def update(self) -> Dict[str, str]:
        """Update each agent by triggering state transitions if thresholds are met."""
        updated = {}
        for agent in self.agents:
            agent.transition()
            updated[agent.name] = agent.state
        return updated

