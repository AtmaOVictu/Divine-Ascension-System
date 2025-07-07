import time
from typing import List


class Log:
    """Simple timestamped event logger."""

    def __init__(self) -> None:
        self.entries: List[str] = []

    def add_entry(self, message: str) -> None:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        self.entries.append(f"{timestamp} - {message}")

    def __iter__(self):
        return iter(self.entries)

    def last(self) -> str:
        return self.entries[-1] if self.entries else ""


class Flow:
    """Track ordered state transitions for an agent."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.history: List[str] = [state]

    def update_state(self, new_state: str) -> None:
        self.state = new_state
        self.history.append(new_state)

    def __repr__(self) -> str:
        return f"{self.name}: {' -> '.join(self.history)}"
