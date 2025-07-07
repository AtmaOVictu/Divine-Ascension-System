from __future__ import annotations
import time
from typing import List

class Log:
    """Collect log entries with timestamps for system events."""

    def __init__(self) -> None:
        self.entries: List[str] = []

    def add_entry(self, message: str) -> None:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        self.entries.append(f"{timestamp} - {message}")

    def display_log(self) -> List[str]:
        """Return all logged entries."""
        return self.entries

class Kot:
    """Represent a flow of state transitions for an agent."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.history: List[str] = [state]
        self.timestamp = time.time()

    def activate_flow(self) -> str:
        self.history.append(self.state)
        return f"Kot {self.name} activated at state {self.state}."

    def update_flow(self, new_state: str) -> str:
        self.state = new_state
        self.timestamp = time.time()
        self.history.append(self.state)
        return f"Flow updated: {self.state}"

    def log(self) -> str:
        timestamp_str = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))
        return f"{timestamp_str} - Kot {self.name}: {self.state}"
