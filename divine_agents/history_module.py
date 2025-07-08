import time
from typing import List, Dict

class HistoryModule:
    """Record and review historical events for an agent."""

    def __init__(self) -> None:
        self.history: List[Dict[str, object]] = []

    def record_event(self, event: str, emotional_state: float, moral_code: str) -> None:
        """Store an event with emotional state and moral code."""
        self.history.append({
            'event': event,
            'emotional_state': emotional_state,
            'moral_code': moral_code,
            'timestamp': time.time()
        })

    def review_history(self) -> List[Dict[str, object]]:
        """Return a copy of the history."""
        return list(self.history)

    def learn_from_history(self) -> str:
        """Simple learning logic returning a moral stance."""
        conflicts = [h for h in self.history if 'conflict' in h['event']]
        if len(conflicts) > 3:
            return 'relativist'
        return 'utilitarian'
