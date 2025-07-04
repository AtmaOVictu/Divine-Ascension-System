import unittest
from divine_agents.security_agents import (
    EncryptionAgent,
    AnonymizationAgent,
    AccessControlAgent,
    PrivacyProtectionAgent,
    DataDeletionAgent,
)


class TestSecurityAgents(unittest.TestCase):
    def test_encryption_cycle(self):
        agent = EncryptionAgent(key=b'key')
        text = "secret"
        cipher = agent.encrypt_data(text)
        self.assertNotEqual(cipher, text)
        plain = agent.decrypt_data(cipher)
        self.assertEqual(plain, text)

    def test_anonymization(self):
        anonymized = AnonymizationAgent.anonymize_data("User123")
        self.assertNotIn("1", anonymized)
        self.assertNotIn("2", anonymized)
        self.assertNotIn("3", anonymized)

    def test_access_control(self):
        agent = AccessControlAgent("user")
        self.assertTrue(agent.has_access("guest"))
        self.assertFalse(agent.has_access("admin"))

    def test_privacy_choice(self):
        agent = PrivacyProtectionAgent(opt_in_training=False)
        self.assertIn("opted out", agent.respect_user_choice())

    def test_data_deletion(self):
        storage = {"id1": "data"}
        agent = DataDeletionAgent(storage)
        msg = agent.delete_data("id1")
        self.assertNotIn("id1", storage)
        self.assertIn("permanently deleted", msg)


if __name__ == "__main__":
    unittest.main()
