"""Module providing a simple writing agent for event transcription."""
from __future__ import annotations

import time
from typing import Dict, List


class WritingAgent:
    """Agent that records events with emotional and philosophical context."""

    def __init__(self, name: str):
        self.name = name
        self.transcription_history: List[Dict[str, object]] = []

    def write_event(self, event: str, emotional_state: str, reflection: str) -> None:
        """Store an event description with associated meta information."""
        entry = {
            "event": event,
            "emotional_state": emotional_state,
            "philosophical_reflection": reflection,
            "timestamp": time.time(),
        }
        self.transcription_history.append(entry)

    def review_history(self) -> List[Dict[str, object]]:
        """Return all logged events."""
        return self.transcription_history
