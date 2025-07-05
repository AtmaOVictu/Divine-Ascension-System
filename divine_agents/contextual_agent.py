"""Agent implementation with context-driven transitions and dialogue."""
from __future__ import annotations

from typing import Optional

from .agent import Agent


class ContextualAgent(Agent):
    """Agent extended with internal and external context information."""

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
    ) -> None:
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.internal_context: Optional[str] = None
        self.external_context: Optional[str] = None

    def set_contexts(self, internal: Optional[str], external: Optional[str]) -> None:
        """Set internal and external context for the agent."""
        self.internal_context = internal
        self.external_context = external

    def transition_by_context(self) -> str:
        """Transition based on current contexts."""
        if (
            self.internal_context == "visoka napetost"
            and self.external_context == "stresno okolje"
        ):
            self.update_tension(0.8)
        elif self.internal_context == "mirno" and self.external_context == "podpora":
            self.update_tension(1.0)
            self.update_emotion(1.0)
        return self.transition()
