from __future__ import annotations
from typing import Optional

from .agent import Agent


class MembershipAgent(Agent):
    """Agent capable of joining groups and adapting based on environment."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, group: Optional[str] = None):
        super().__init__(name, state, tension, emotion)
        self.group = group

    def ionize_environment(self, other: "MembershipAgent") -> bool:
        """Simulate environmental influence and join other's group if stressed."""
        if self.tension > 0.8 or self.emotion > 0.7:
            self.group = other.group or other.name
            return True
        return False

    def transition(self, other: Optional["MembershipAgent"] = None) -> str:
        """Transition states after evaluating environmental conditions."""
        if other is not None:
            self.ionize_environment(other)
        return super().transition()


class InterpretiveAgent(MembershipAgent):
    """Agent interpreting changes of others and adapting accordingly."""

    def interpret_change(self, other: MembershipAgent) -> str:
        if other.state == "Enotnost":
            self.state = "Enotnost"
        elif other.state == "Jaz" and self.state == "Ego":
            self.state = "Jaz"
        self.history.append(self.state)
        return self.state
