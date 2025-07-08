import time
from typing import List, Dict

class HistoryModule:
    """Maintain a history of agent events."""

    def __init__(self) -> None:
        self.history: List[Dict[str, object]] = []

    def record_event(self, event: str, emotional_state: str, moral_code: str) -> None:
        """Record a significant event with context."""
        self.history.append(
            {
                "event": event,
                "emotional_state": emotional_state,
                "moral_code": moral_code,
                "timestamp": time.time(),
            }
        )

    def review_history(self) -> List[Dict[str, object]]:
        """Return the list of recorded events."""
        return self.history

    def learn_from_history(self) -> str:
        """Return an adapted moral code based on past conflicts."""
        conflicts = [h for h in self.history if "conflict" in h["event"]]
        if len(conflicts) > 3:
            return "relativist"
        return "utilitarian"
