"""Security-focused agents for data protection."""

import base64
from typing import Dict

class EncryptionAgent:
    """Symmetric encryption agent using a simple XOR algorithm."""

    def __init__(self, key: bytes):
        self.key = key

    def _xor(self, data: bytes) -> bytes:
        key_repeated = (self.key * (len(data) // len(self.key) + 1))[: len(data)]
        return bytes(a ^ b for a, b in zip(data, key_repeated))

    def encrypt_data(self, text: str) -> str:
        encoded = text.encode("utf-8")
        encrypted = self._xor(encoded)
        return base64.b64encode(encrypted).decode("utf-8")

    def decrypt_data(self, cipher: str) -> str:
        encrypted = base64.b64decode(cipher)
        decrypted = self._xor(encrypted)
        return decrypted.decode("utf-8")


class AnonymizationAgent:
    """Agent responsible for anonymizing text data."""

    @staticmethod
    def anonymize_data(text: str) -> str:
        return "".join("X" if ch.isdigit() else ch for ch in text)


class AccessControlAgent:
    """Simple role-based access control agent."""

    ROLES = {"guest": 0, "user": 1, "admin": 2}

    def __init__(self, user_role: str):
        self.user_role = user_role

    def has_access(self, required_role: str) -> bool:
        return self.ROLES.get(self.user_role, 0) >= self.ROLES.get(required_role, 0)


class PrivacyProtectionAgent:
    """Agent enforcing user's privacy preferences."""

    def __init__(self, opt_in_training: bool):
        self.opt_in_training = opt_in_training

    def respect_user_choice(self) -> str:
        if not self.opt_in_training:
            return "User opted out of data training."
        return "User data will be used for training."


class DataDeletionAgent:
    """Agent that can delete stored data by identifier."""

    def __init__(self, storage: Dict[str, str]):
        self.storage = storage

    def delete_data(self, data_id: str) -> str:
        if data_id in self.storage:
            del self.storage[data_id]
            return f"Data {data_id} has been permanently deleted."
        return f"Data {data_id} not found."
