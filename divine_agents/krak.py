import time
from typing import Any

class Krak:
    """Represents a task that activates when conditions are met."""

    def __init__(self, name: str, condition: str) -> None:
        self.name = name
        self.condition = condition
        self.timestamp = time.time()
        self.completed = False

    def activate(self) -> str:
        """Mark the task as completed and set activation time."""
        self.timestamp = time.time()
        self.completed = True
        print(
            f"Krak {self.name} activated at {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))}"
        )
        return f"Krak {self.name} completed."

    def check_condition(self, agent: Any) -> bool:
        """Return True if the activation condition is satisfied."""
        if self.condition == "high_emotion" and agent.emotion > 0.7:
            return True
        if self.condition == "state_transition" and agent.state == "Jaz":
            return True
        return False
