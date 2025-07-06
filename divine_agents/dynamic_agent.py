from __future__ import annotations
from typing import Optional
from .agent import Agent

class DynamicAgent(Agent):
    """Agent with key-based activation in addition to emotion and tension."""

    activation_map = {
        "truth": "Ego",
        "negation": "Jaz",
        "wisdom": "Enotnost",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, key: Optional[str] = None) -> None:
        super().__init__(name, state, tension, emotion)
        self.key = key

    def set_key(self, key: Optional[str]) -> str:
        """Set activation key and update state if the key maps to a state."""
        self.key = key
        if key in self.activation_map:
            self.state = self.activation_map[key]
            self.history.append(self.state)
        return self.state

    def transition(self) -> str:
        """Override transition to include key-based activation."""
        state = super().transition()
        if self.key in self.activation_map and self.activation_map[self.key] != state:
            self.state = self.activation_map[self.key]
            self.history.append(self.state)
        return self.state
