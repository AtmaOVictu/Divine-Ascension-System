from __future__ import annotations

import random
from .agent import Agent


class MultiColorAgent(Agent):
    """Agent with color representation and visibility toggle."""

    COLORS = {
        "Ego": "Gray",
        "Jaz": "Blue",
        "Enotnost": "Gold",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.color = self.COLORS.get(state, "Gray")
        self.visibility = "Hidden"

    def transition(self) -> str:
        prev_state = self.state
        new_state = super().transition()
        if new_state != prev_state:
            self.color = self.COLORS.get(new_state, self.color)
        self.toggle_visibility()
        return new_state

    def toggle_visibility(self) -> None:
        self.visibility = "Visible" if random.random() > 0.5 else "Hidden"

    def current_color(self) -> str:
        return self.color

    def current_visibility(self) -> str:
        return self.visibility
