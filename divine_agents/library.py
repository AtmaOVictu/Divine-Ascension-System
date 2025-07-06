from typing import List
from .archive import Archive, Contact


class Library:
    """Provides analytical operations for the archive."""

    def __init__(self, archive: Archive) -> None:
        self.archive = archive

    def average_contact_interval(self) -> float:
        """Return the average numeric timestamp difference."""
        if len(self.archive.contacts) < 2:
            return 0.0
        timestamps = sorted(float(c.timestamp) for c in self.archive.contacts)
        diffs = [b - a for a, b in zip(timestamps, timestamps[1:])]
        return sum(diffs) / len(diffs)
