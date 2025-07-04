"""Multi-color agent implementation with visibility toggling."""
from __future__ import annotations

import random

from .agent import Agent


class MultiColorAgent(Agent):
    """Agent with color representation and visibility state."""

    COLOR_MAP = {
        "Ego": "Red",
        "Jaz": "Blue",
        "Enotnost": "Gold",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, visible: bool = True):
        super().__init__(name, state, tension, emotion)
        self.color = self.COLOR_MAP.get(state, "Gray")
        self.visibility = "Visible" if visible else "Hidden"

    def transition(self) -> str:
        """Perform state transition, update color and visibility."""
        state = super().transition()
        self.color = self.COLOR_MAP.get(self.state, "Gray")
        self.toggle_visibility()
        return state

    def toggle_visibility(self) -> None:
        """Randomly toggle visibility between Visible and Hidden."""
        self.visibility = "Visible" if random.random() > 0.5 else "Hidden"

    def current_color(self) -> str:
        return self.color

    def current_visibility(self) -> str:
        return self.visibility
