import time
from typing import List, Tuple


class SpeedInsights:
    """Simple tracker for agent performance events."""

    def __init__(self) -> None:
        self.events: List[Tuple[str, float]] = []

    def log_event(self, event: str) -> None:
        """Record an event with a timestamp."""
        self.events.append((event, time.time()))

    def get_events(self) -> List[Tuple[str, float]]:
        return list(self.events)
