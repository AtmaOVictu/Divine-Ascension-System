import time
from typing import List


class SubAgent:
    """Helper entity that logs actions for an agent."""

    def __init__(self, name: str, associated_agent: 'Agent'):
        self.name = name
        self.associated_agent = associated_agent
        self.logs: List[str] = []

    def log_action(self, action: str) -> None:
        """Record an action with a timestamp."""
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        entry = f"{timestamp} - {self.name}: {action}"
        self.logs.append(entry)

    def sort_logs(self) -> List[str]:
        """Return logs sorted by timestamp."""
        return sorted(self.logs, key=lambda x: x.split(' - ')[0])
