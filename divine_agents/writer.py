import time
from typing import List, Dict


class WritingAgent:
    """Records events with emotional and philosophical reflection."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.transcription_history: List[Dict[str, str | float]] = []

    def write_event(self, event: str, emotional_state: str, philosophical_reflection: str) -> None:
        """Log an event and reflections with a timestamp."""
        self.transcription_history.append(
            {
                "event": event,
                "emotional_state": emotional_state,
                "philosophical_reflection": philosophical_reflection,
                "timestamp": time.time(),
            }
        )

    def review_history(self) -> List[Dict[str, str | float]]:
        """Return the recorded history."""
        return self.transcription_history
