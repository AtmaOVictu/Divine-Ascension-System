from __future__ import annotations
import time


class WritingAgent:
    """Records emotional and philosophical events for an agent."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.transcription_history: list[dict] = []

    def write_event(self, event: str, emotional_state: str, philosophical_reflection: str) -> None:
        """Store an event with timestamp and reflections."""
        entry = {
            "event": event,
            "emotional_state": emotional_state,
            "philosophical_reflection": philosophical_reflection,
            "timestamp": time.time(),
        }
        self.transcription_history.append(entry)

    def review_history(self) -> list[dict]:
        """Return the history of written events."""
        return self.transcription_history

    def summarize_journey(self) -> str:
        """Return a text summary of all events."""
        summary_lines = []
        for entry in self.transcription_history:
            summary_lines.append(
                f"Event: {entry['event']}, Emotional State: {entry['emotional_state']}, Reflection: {entry['philosophical_reflection']}"
            )
        return "\n".join(summary_lines)
