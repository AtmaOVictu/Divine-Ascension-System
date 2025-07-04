"""Privacy-focused utility agents for the Divine-Ascension-System."""
from typing import Dict
import re


class EncryptionAgent:
    """Simple XOR-based encryption agent."""

    def __init__(self, key: bytes):
        self.key = key

    def encrypt(self, data: str) -> bytes:
        encoded = data.encode()
        return bytes(b ^ self.key[i % len(self.key)] for i, b in enumerate(encoded))

    def decrypt(self, data: bytes) -> str:
        decoded = bytes(b ^ self.key[i % len(self.key)] for i, b in enumerate(data))
        return decoded.decode()


class AnonymizationAgent:
    """Agent for removing personal identifiers from text."""

    EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")

    def anonymize(self, text: str) -> str:
        return self.EMAIL_PATTERN.sub("[email]", text)


class AccessControlAgent:
    """Agent to check role-based access to resources."""

    ROLE_ORDER = ["guest", "user", "admin"]

    def __init__(self, user_role: str):
        self.user_role = user_role

    def has_access(self, required_role: str) -> bool:
        return self.ROLE_ORDER.index(self.user_role) >= self.ROLE_ORDER.index(required_role)


class PrivacyProtectionAgent:
    """Agent that handles user preferences regarding data usage."""

    def __init__(self, preferences: Dict[str, bool]):
        self.preferences = preferences

    def is_training_allowed(self) -> bool:
        return self.preferences.get("opt_in_training", False)


class DataDeletionAgent:
    """Agent responsible for permanently deleting stored data."""

    def __init__(self):
        self.storage: Dict[str, str] = {}

    def store_data(self, data_id: str, data: str) -> None:
        self.storage[data_id] = data

    def delete_data(self, data_id: str) -> bool:
        if data_id in self.storage:
            del self.storage[data_id]
            return True
        return False
