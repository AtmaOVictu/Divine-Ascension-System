import time
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .agent import Agent


class SubAgent:
    """Assistant to an :class:`Agent` that records actions."""

    def __init__(self, name: str, associated_agent: 'Agent') -> None:
        self.name = name
        self.associated_agent = associated_agent
        self.logs: List[str] = []

    def log_action(self, action: str) -> None:
        """Record an action with a timestamp."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        entry = f"{timestamp} - {self.name}: {action}"
        self.logs.append(entry)

    def sort_logs(self) -> List[str]:
        """Return logs sorted by timestamp."""
        return sorted(self.logs)
