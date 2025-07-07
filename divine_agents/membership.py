from __future__ import annotations
from typing import Optional

from .agent import Agent


class MembershipAgent(Agent):
    """Agent that can join groups based on emotional and tension thresholds."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.group: Optional[str] = None

    def ionize_environment(self, other_agent: 'MembershipAgent') -> bool:
        """Join the other agent's group if thresholds are exceeded."""
        if self.tension > 0.8 or self.emotion > 0.7:
            self.group = other_agent.group or other_agent.name
            return True
        return False


class InterpretiveAgent(MembershipAgent):
    """Agent that interprets another agent's state and adapts accordingly."""

    def interpret_change(self, other_agent: Agent) -> str:
        """Align this agent's state with the other agent's state."""
        if other_agent.state == "Enotnost":
            self.state = "Enotnost"
        elif other_agent.state == "Jaz":
            self.state = "Jaz"
        return self.state

