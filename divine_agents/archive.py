from dataclasses import dataclass
from typing import List

@dataclass
class Contact:
    """Store a contact between two agents with an associated event."""
    agent1: str
    agent2: str
    event: str
    timestamp: str


class Archive:
    """Archive that keeps track of all noteworthy contacts."""

    def __init__(self) -> None:
        self.contacts: List[Contact] = []

    def add_contact(self, contact: Contact) -> None:
        self.contacts.append(contact)

    def reorganize(self) -> None:
        """Sort contacts by timestamp to reorganize the archive."""
        self.contacts.sort(key=lambda c: c.timestamp)

    def __iter__(self):
        return iter(self.contacts)
