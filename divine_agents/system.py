"""Dynamic agent system for multi-agent interactions."""
from __future__ import annotations

from typing import List

from .agent import Agent


class DynamicAgentSystem:
    """Manage multiple agents and their interactions."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the system."""
        self.agents.append(agent)

    def step(self, question: str) -> List[str]:
        """Run a single interaction step for all agents."""
        logs: List[str] = []
        for agent in self.agents:
            logs.append(f"{agent.name} ({agent.state}): {agent.respond(question)}")
            agent.update_emotion(0.6)
            logs.append(f"{agent.name} prehaja v stanje: {agent.transition()}")
        return logs

    def run_simulation(self, question: str, steps: int = 1) -> List[str]:
        """Execute several interaction steps and return the log."""
        history: List[str] = []
        for _ in range(steps):
            history.extend(self.step(question))
        return history
