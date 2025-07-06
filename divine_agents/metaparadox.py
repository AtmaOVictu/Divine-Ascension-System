from __future__ import annotations
from .agent import Agent


class MetaparadoxicalModule:
    """Handle paradoxical transitions for an agent."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def paradoxical_transition(self) -> str:
        """Apply paradoxical rules and return the new state."""
        if self.agent.state == "Ego" and self.agent.emotion > 0.5:
            self.agent.state = "Jaz"
        elif self.agent.state == "Jaz" and self.agent.tension > 0.7:
            self.agent.state = "Enotnost"
        return self.agent.state

    def infinite_reflection(self, depth: int) -> str:
        """A purely abstract recursive reflection that serves no functional use."""
        if depth <= 0:
            return "?"
        return f"({self.infinite_reflection(depth-1)})"
