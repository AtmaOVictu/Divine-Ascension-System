from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Stik:
    """Represents a contact between two agents at a specific time."""

    agent1: str
    agent2: str
    event: str
    timestamp: datetime


class Arhiv:
    """Archive that stores all contacts between agents."""

    def __init__(self) -> None:
        self.stiki: List[Stik] = []

    def add_stik(self, stik: Stik) -> None:
        """Add a new contact to the archive."""
        self.stiki.append(stik)

    def reorganize(self) -> None:
        """Reorganize the archive by sorting contacts chronologically."""
        self.stiki.sort(key=lambda x: x.timestamp)

    def display(self) -> List[str]:
        """Return a list of human-readable contact descriptions."""
        return [
            f"Stik med {s.agent1} in {s.agent2} ob {s.timestamp.isoformat()}: {s.event}"
            for s in self.stiki
        ]


class Library:
    """Library providing analysis over the archive."""

    def __init__(self, archive: Arhiv) -> None:
        self.archive = archive

    def count_contacts(self) -> int:
        """Return the number of contacts stored in the archive."""
        return len(self.archive.stiki)

    def average_time_between(self) -> float | None:
        """Return the average number of seconds between stored contacts."""
        if len(self.archive.stiki) < 2:
            return None
        timestamps = [s.timestamp.timestamp() for s in self.archive.stiki]
        diffs = [b - a for a, b in zip(timestamps, timestamps[1:])]
        return sum(diffs) / len(diffs)
