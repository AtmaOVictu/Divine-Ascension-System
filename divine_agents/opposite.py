from __future__ import annotations
from typing import List

from .agent import Agent

class OppositeAgent:
    """Represents an opposing concept for an Agent."""

    def __init__(self, name: str, concept: str):
        self.name = name
        self.concept = concept

    def activate_opposite(self, agent: Agent) -> List[str]:
        """Activate the opposite, causing the agent to debate and potentially transition."""
        agent.define_opposite(self)
        lines = [f"{self.name} aktivira nasprotje do agenta {agent.name}."]
        lines.extend(agent.debate())
        return lines
