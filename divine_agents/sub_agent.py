import time
from typing import List

class SubAgent:
    """Assistant entity that logs actions for a parent agent."""

    def __init__(self, name: str):
        self.name = name
        self.logs: List[str] = []

    def log_action(self, action: str) -> None:
        """Record an action with a timestamp."""
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        entry = f"{timestamp} - {self.name}: {action}"
        self.logs.append(entry)

    def sort_logs(self) -> List[str]:
        """Return logs sorted by timestamp."""
        return sorted(self.logs, key=lambda x: x.split(' - ')[0])
