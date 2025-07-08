import time
from typing import List, Dict


class WritingAgent:
    """Record events with emotional and philosophical reflections."""

    def __init__(self, name: str):
        self.name = name
        self.history: List[Dict[str, str]] = []

    def write_event(self, event: str, emotion: str, reflection: str) -> None:
        entry = {
            "event": event,
            "emotion": emotion,
            "reflection": reflection,
            "timestamp": time.time(),
        }
        self.history.append(entry)

    def summarize(self) -> str:
        summary = []
        for item in self.history:
            summary.append(
                f"Event: {item['event']}, Emotion: {item['emotion']}, Reflection: {item['reflection']}"
            )
        return "\n".join(summary)
