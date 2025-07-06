from dataclasses import dataclass
from datetime import datetime
from typing import List, Iterable


@dataclass
class Contact:
    """Represents a single interaction between two agents."""
    agent1: str
    agent2: str
    event: str
    timestamp: datetime


class Archive:
    """Archive for storing and reorganizing agent contacts."""

    def __init__(self) -> None:
        self.contacts: List[Contact] = []

    def add_contact(self, contact: Contact) -> None:
        """Store a new contact in the archive."""
        self.contacts.append(contact)

    def reorganize(self) -> None:
        """Reorganize archive by sorting contacts chronologically."""
        self.contacts.sort(key=lambda c: c.timestamp)

    def __iter__(self) -> Iterable[Contact]:
        return iter(self.contacts)

    def __len__(self) -> int:
        return len(self.contacts)
