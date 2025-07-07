import time
from typing import List

class Log:
    """Store timestamped log entries."""

    def __init__(self) -> None:
        self.entries: List[str] = []

    def add_entry(self, message: str) -> None:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        self.entries.append(f"{timestamp} - {message}")

    def display(self) -> List[str]:
        """Return the list of log entries."""
        return self.entries.copy()

class Kot:
    """Track the flow of state transitions for an agent."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.history: List[str] = [state]
        self.timestamp = time.time()

    def update(self, new_state: str) -> str:
        """Update the current state and record it in the history."""
        self.state = new_state
        self.timestamp = time.time()
        self.history.append(new_state)
        return f"Flow updated: {new_state}"

    def log(self) -> str:
        """Return a description of the current state with timestamp."""
        ts = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))
        return f"{ts} - Kot {self.name}: {self.state}"
