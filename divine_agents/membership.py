from __future__ import annotations
from typing import Optional
from .agent import Agent


class MembershipAgent(Agent):
    """Agent capable of joining groups and adapting through ionization."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.group: Optional[str] = None

    def ionize_environment(self, other: "MembershipAgent") -> bool:
        """Join the other agent's group if emotion or tension is high."""
        if self.tension > 0.8 or self.emotion > 0.7:
            self.group = other.group or other.name
            return True
        return False

    def transition(self) -> str:
        """Transition using base logic after possible ionization."""
        self.ionize_environment(self)
        return super().transition()


class InterpretiveAgent(MembershipAgent):
    """Agent that interprets another agent's state and aligns with it."""

    def interpret_change(self, other: MembershipAgent) -> str:
        """Align state with another agent's state."""
        if other.state == "Enotnost":
            self.state = "Enotnost"
        elif other.state == "Jaz":
            self.state = "Jaz"
        return self.state

