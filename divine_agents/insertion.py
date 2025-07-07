"""Utilities for dynamically inserting states and data into agents."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List

from .agent import Agent


@dataclass
class InsertionAgent:
    """Agent responsible for modifying other agents at runtime."""

    agent: Agent
    inserted_states: List[str] = field(default_factory=list)

    def insert_state(self, new_state: str) -> None:
        """Add a new state to the agent if it's not already present."""
        if new_state not in self.agent.STATES:
            self.agent.STATES = self.agent.STATES + (new_state,)
            self.inserted_states.append(new_state)

    def insert_data(self, data: Dict[str, Any]) -> None:
        """Insert new knowledge data into the agent."""
        if not hasattr(self.agent, "knowledge"):
            self.agent.knowledge = {}
        self.agent.knowledge.update(data)

    def modify_behavior(self, behavior: str) -> None:
        """Append a new behavior description to the agent."""
        if not hasattr(self.agent, "behaviors"):
            self.agent.behaviors = []
        self.agent.behaviors.append(behavior)

