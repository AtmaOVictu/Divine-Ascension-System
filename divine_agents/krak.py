import time
from typing import Optional

class Krak:
    """Represents a task that activates under specific agent conditions."""

    def __init__(self, name: str, condition: str) -> None:
        self.name = name
        self.condition = condition
        self.timestamp: Optional[float] = None
        self.completed = False

    def check_condition(self, agent: 'Agent') -> bool:
        """Return True if the activation condition is met."""
        if self.condition == "high_emotion" and agent.emotion > 0.7:
            return True
        if self.condition == "state_transition" and agent.state == "Jaz":
            return True
        return False

    def activate(self) -> str:
        """Mark the krak as completed and log activation time."""
        self.timestamp = time.time()
        self.completed = True
        return f"Krak {self.name} completed."
