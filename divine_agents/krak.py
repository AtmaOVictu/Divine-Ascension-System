import time
from typing import Callable

class Krak:
    """Represents a task that activates when its condition is met."""

    def __init__(self, name: str, condition: Callable[["Agent"], bool]):
        self.name = name
        self.condition = condition
        self.completed = False
        self.timestamp = None

    def check_and_activate(self, agent: "Agent") -> bool:
        """Activate the krak if its condition is satisfied."""
        if not self.completed and self.condition(agent):
            self.timestamp = time.time()
            self.completed = True
            return True
        return False
