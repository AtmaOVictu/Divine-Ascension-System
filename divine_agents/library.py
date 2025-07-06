from __future__ import annotations

from datetime import datetime
from typing import Optional

from .archive import Archive, Contact


class Library:
    """Utility class for analyzing contacts stored in an Archive."""

    def __init__(self, archive: Archive) -> None:
        self.archive = archive

    def record_contact(
        self, agent1: str, agent2: str, event: str, timestamp: datetime
    ) -> None:
        """Convenience wrapper to create and store a contact."""
        self.archive.add_contact(Contact(agent1, agent2, event, timestamp))

    def average_time_between_contacts(self) -> Optional[float]:
        """Return average time in seconds between contacts, if possible."""
        if len(self.archive) < 2:
            return None

        timestamps = [c.timestamp for c in self.archive]
        timestamps.sort()
        diffs = [
            (t2 - t1).total_seconds() for t1, t2 in zip(timestamps, timestamps[1:])
        ]
        return sum(diffs) / len(diffs)
