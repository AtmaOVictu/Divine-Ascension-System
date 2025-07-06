from dataclasses import dataclass
from typing import List, Optional
import statistics


@dataclass
class Contact:
    """Represents a contact between two agents."""
    agent1: str
    agent2: str
    event: str
    timestamp: float


class Archive:
    """Archive storing all contacts between agents."""

    def __init__(self) -> None:
        self.contacts: List[Contact] = []

    def add_contact(self, contact: Contact) -> None:
        """Add a contact to the archive."""
        self.contacts.append(contact)

    def reorganize(self) -> None:
        """Reorganize the archive by sorting contacts by timestamp."""
        self.contacts.sort(key=lambda c: c.timestamp)

    def get_contacts(self) -> List[Contact]:
        """Return all stored contacts."""
        return self.contacts


class Library:
    """Simple library for analyzing contacts in the archive."""

    def __init__(self, archive: Archive) -> None:
        self.archive = archive

    def average_timestamp(self) -> Optional[float]:
        """Return average timestamp of all contacts, if any."""
        if not self.archive.contacts:
            return None
        return statistics.mean(c.timestamp for c in self.archive.contacts)
