from __future__ import annotations

from typing import List

from .agent import Agent


class MetaModule:
    """Manage a collection of agents by their unique IDs."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Add a new agent to the module."""
        self.agents.append(agent)

    def compare_agents(self, agent1: Agent, agent2: Agent) -> bool:
        """Compare agents by name, version and state."""
        return (
            agent1.name == agent2.name
            and agent1.state == agent2.state
            and agent1.agent_id == agent2.agent_id
        )

    def execute_agent_equation(self, agent: Agent, x_value: float) -> float:
        """Execute the agent's equation."""
        return agent.evaluate_equation(x_value)

