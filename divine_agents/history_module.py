import time
from typing import List, Dict

class HistoryModule:
    """Store and review significant events."""

    def __init__(self) -> None:
        self.history: List[Dict[str, float | str]] = []

    def record_event(self, agent_name: str, state: str, emotion: float) -> None:
        """Record an agent event with timestamp."""
        self.history.append({
            "agent": agent_name,
            "state": state,
            "emotion": emotion,
            "timestamp": time.time(),
        })

    def last_event(self) -> Dict[str, float | str] | None:
        """Return the most recent event."""
        if self.history:
            return self.history[-1]
        return None
