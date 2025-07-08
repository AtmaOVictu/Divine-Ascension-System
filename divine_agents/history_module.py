import time
from typing import List, Dict, Any


class HistoryModule:
    """Record and review historical events for agents."""

    def __init__(self):
        self.history: List[Dict[str, Any]] = []

    def record_event(self, event: str, emotional_state: float, moral_code: str) -> None:
        """Store a historical event with associated metadata."""
        self.history.append(
            {
                "event": event,
                "emotional_state": emotional_state,
                "moral_code": moral_code,
                "timestamp": time.time(),
            }
        )

    def review_history(self) -> List[Dict[str, Any]]:
        """Return the list of recorded events."""
        return self.history

    def learn_from_history(self) -> str:
        """Return a new moral code based on past conflict events."""
        conflicts = [h for h in self.history if "conflict" in h["event"]]
        return "relativist" if len(conflicts) > 3 else "utilitarian"
