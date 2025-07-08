"""Simple writing agent used for tracking events and reflections."""

from typing import List, Dict, Any
import time


class WritingAgent:
    """Record events with emotional context and philosophical reflection."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.transcription_history: List[Dict[str, Any]] = []

    def write_event(
        self,
        event: str,
        emotional_state: str,
        philosophical_reflection: str,
        emotional_intensity: float,
    ) -> None:
        """Store an event entry in the history."""
        entry = {
            "event": event,
            "emotional_state": emotional_state,
            "philosophical_reflection": philosophical_reflection,
            "emotional_intensity": emotional_intensity,
            "timestamp": time.time(),
        }
        self.transcription_history.append(entry)

    def review_history(self) -> List[Dict[str, Any]]:
        """Return the stored history."""
        return self.transcription_history

    def summarize_journey(self) -> str:
        """Create a simple textual summary of all entries."""
        summary_lines = []
        for entry in self.transcription_history:
            summary_lines.append(
                f"Event: {entry['event']}, Emotional State: {entry['emotional_state']}, Reflection: {entry['philosophical_reflection']}"
            )
        return "\n".join(summary_lines)
