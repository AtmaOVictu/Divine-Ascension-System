import time
from typing import Optional

class Krak:
    """Represents a task that activates based on agent state or emotion."""

    def __init__(self, name: str, condition: str):
        self.name = name
        self.condition = condition
        self.timestamp: Optional[float] = None
        self.completed = False

    def check_condition(self, agent) -> bool:
        """Return True if the krak should activate for the given agent."""
        if self.condition == "high_emotion":
            return agent.emotion > 0.7
        if self.condition == "state_transition":
            return agent.state == "Jaz"
        return False

    def activate(self) -> str:
        """Mark the krak as completed and timestamp activation."""
        self.completed = True
        self.timestamp = time.time()
        return f"Krak {self.name} activated"
