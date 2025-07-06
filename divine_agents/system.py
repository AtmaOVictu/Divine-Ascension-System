"""Dynamic system for multiple ontological agents."""
from __future__ import annotations

from typing import List

from .agent import Agent


class DynamicAgentSystem:
    """Manage multiple agents and simulate their interactions."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Add a new agent to the system."""
        self.agents.append(agent)

    def run_simulation(self, question: str) -> List[str]:
        """Run a single interaction round among all agents."""
        lines: List[str] = []
        for agent in self.agents:
            lines.append(f"{agent.name} ({agent.state}): {agent.respond(question)}")
            agent.update_emotion(0.6)
            new_state = agent.transition()
            lines.append(f"{agent.name} prehaja v stanje: {new_state}")
        return lines
