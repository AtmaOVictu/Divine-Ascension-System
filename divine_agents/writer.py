import time
from typing import List, Dict


class WritingAgent:
    """Capture events and reflections for an agent."""

    def __init__(self, name: str):
        self.name = name
        self.transcription_history: List[Dict[str, str]] = []

    def write_event(self, event: str, emotional_state: str, philosophical_reflection: str) -> None:
        """Record an event with emotional and philosophical context."""
        entry = {
            "event": event,
            "emotional_state": emotional_state,
            "philosophical_reflection": philosophical_reflection,
            "timestamp": time.time(),
        }
        self.transcription_history.append(entry)

    def review_history(self) -> List[Dict[str, str]]:
        """Return the recorded history."""
        return self.transcription_history

    def summarize_journey(self) -> str:
        """Summarize the agent's journey."""
        summary = []
        for entry in self.transcription_history:
            summary.append(
                f"Event: {entry['event']}, Emotional State: {entry['emotional_state']}, Reflection: {entry['philosophical_reflection']}"
            )
        return "\n".join(summary)
