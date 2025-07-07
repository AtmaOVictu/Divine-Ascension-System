from __future__ import annotations
from datetime import datetime
from typing import Optional, List
from .agent import Agent

class SubAgent(Agent):
    """Agent associated with a parent agent."""

    def __init__(self, name: str, associated_agent: Optional[Agent] = None, **kwargs):
        super().__init__(name, **kwargs)
        self.associated_agent = associated_agent

    def log_action(self, message: str) -> None:
        """Log an action performed by the sub-agent."""
        self.log(message)
        if self.associated_agent is not None:
            self.associated_agent.log(message)

    def sort_logs(self) -> List[str]:
        """Return logs sorted by timestamp."""
        return sorted(self.logs, key=lambda x: x.split(" | ")[0])
