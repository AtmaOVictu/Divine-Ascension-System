"""Management of agents and philosophical debates."""
from __future__ import annotations

from typing import List

from .agent import Agent
from .dialogue import dynamic_dialogue


class Codex:
    """Central manager for agent debates and transitions."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []
        self.history: List[str] = []

    def add_agent(self, agent: Agent) -> None:
        """Register a new agent."""
        self.agents.append(agent)

    def run_debate(self, agent1: Agent, agent2: Agent) -> List[str]:
        """Run a debate between two agents and store the transcript."""
        lines = dynamic_dialogue(agent1, agent2)
        self.history.extend(lines)
        return lines
