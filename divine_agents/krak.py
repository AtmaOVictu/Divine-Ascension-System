"""Utility classes for agent tasks (kraki)."""

from __future__ import annotations

import time
from typing import Callable


class Krak:
    """Represents a task triggered by agent state or emotion."""

    def __init__(self, name: str, condition: Callable[["Agent"], bool]):
        self.name = name
        self.condition = condition
        self.completed = False
        self.timestamp: float | None = None

    def check_and_activate(self, agent: "Agent") -> bool:
        """Activate this krak if the condition evaluates to True."""
        if not self.completed and self.condition(agent):
            self.completed = True
            self.timestamp = time.time()
            return True
        return False
