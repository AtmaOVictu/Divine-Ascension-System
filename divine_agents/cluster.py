from __future__ import annotations

from typing import Iterable, List

from .agent import Agent


class AgentCluster:
    """Group of agents that can be evaluated together."""

    def __init__(self, agents: Iterable[Agent]):
        self.agents: List[Agent] = list(agents)

    def evaluate(self) -> None:
        """Evaluate each agent and trigger transitions if needed."""
        for agent in self.agents:
            agent.transition()
