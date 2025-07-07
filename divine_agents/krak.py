from __future__ import annotations

import time
from typing import Callable


class Krak:
    """Represents a task activated when certain conditions are met."""

    def __init__(self, name: str, condition: Callable[["Agent"], bool]):
        self.name = name
        self.condition = condition
        self.completed = False
        self.timestamp = 0.0

    def check_and_activate(self, agent: "Agent") -> bool:
        """Check condition and activate the task if required."""
        if not self.completed and self.condition(agent):
            self.completed = True
            self.timestamp = time.time()
            return True
        return False

    def __repr__(self) -> str:  # pragma: no cover - simple debug
        status = "completed" if self.completed else "pending"
        return f"Krak(name={self.name}, status={status})"

