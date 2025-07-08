import time
from typing import List, Dict


class WritingAgent:
    """Agent responsible for recording events with emotional context."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.transcription_history: List[Dict[str, str]] = []

    def write_event(self, event: str, emotional_state: str, philosophical_reflection: str) -> None:
        """Record an event with emotional and philosophical reflection."""
        self.transcription_history.append(
            {
                "event": event,
                "emotional_state": emotional_state,
                "philosophical_reflection": philosophical_reflection,
                "timestamp": time.time(),
            }
        )

    def review_history(self) -> List[Dict[str, str]]:
        """Return the written history."""
        return self.transcription_history
