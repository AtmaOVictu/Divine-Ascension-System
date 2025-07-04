import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.security_agents import (
    EncryptionAgent,
    AnonymizationAgent,
    AccessControlAgent,
    PrivacyProtectionAgent,
    DataDeletionAgent,
)


class TestSecurityAgents(unittest.TestCase):
    def test_encryption_cycle(self):
        enc = EncryptionAgent("key")
        original = "secret"
        encrypted = enc.encrypt_data(original)
        decrypted = enc.decrypt_data(encrypted)
        self.assertEqual(original, decrypted)

    def test_access_control(self):
        access = AccessControlAgent(user_role=2)
        self.assertTrue(access.has_access(1))
        self.assertFalse(access.has_access(3))

    def test_privacy_preference(self):
        agent = PrivacyProtectionAgent({"opt_in_training": False})
        message = agent.respect_user_choice()
        self.assertIn("opted out", message)

    def test_data_deletion(self):
        storage = {"a": 1, "b": 2}
        deleter = DataDeletionAgent(storage)
        deleter.delete_data("a")
        self.assertNotIn("a", storage)


if __name__ == "__main__":
    unittest.main()
