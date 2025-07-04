"""Security and privacy related agents for the Divine Ascension System."""

import base64
from typing import Any, Dict


class EncryptionAgent:
    """Agent responsible for basic data encryption and decryption."""

    def __init__(self, encryption_key: str) -> None:
        self.encryption_key = encryption_key

    def encrypt_data(self, data: str) -> str:
        encoded = base64.b64encode(data.encode()).decode()
        return encoded

    def decrypt_data(self, encrypted_data: str) -> str:
        decoded = base64.b64decode(encrypted_data.encode()).decode()
        return decoded


class AnonymizationAgent:
    """Agent that removes simple personal information from text."""

    def anonymize_data(self, data: str) -> str:
        # This placeholder removes digits as a simple anonymization step
        return ''.join(ch for ch in data if not ch.isdigit())


class AccessControlAgent:
    """Agent that checks if a user has sufficient privileges."""

    def __init__(self, user_role: int) -> None:
        self.user_role = user_role

    def has_access(self, required_role: int) -> bool:
        return self.user_role >= required_role


class PrivacyProtectionAgent:
    """Agent honoring user preferences for data training."""

    def __init__(self, user_preferences: Dict[str, Any]) -> None:
        self.user_preferences = user_preferences

    def respect_user_choice(self) -> str:
        if not self.user_preferences.get("opt_in_training", True):
            return "User opted out of data training."
        return "User data will be used for training."


class DataDeletionAgent:
    """Agent that permanently deletes data from storage."""

    def __init__(self, data_storage: Dict[str, Any]) -> None:
        self.data_storage = data_storage

    def delete_data(self, data_id: str) -> str:
        self.data_storage.pop(data_id, None)
        return f"Data {data_id} has been permanently deleted."

