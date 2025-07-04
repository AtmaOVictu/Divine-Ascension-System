import unittest
from divine_agents.privacy_agents import (
    EncryptionAgent,
    AnonymizationAgent,
    AccessControlAgent,
    PrivacyProtectionAgent,
    DataDeletionAgent,
)


class TestPrivacyAgents(unittest.TestCase):
    def test_encryption_roundtrip(self):
        agent = EncryptionAgent(b'k')
        message = 'secret'
        enc = agent.encrypt(message)
        dec = agent.decrypt(enc)
        self.assertEqual(message, dec)

    def test_anonymization(self):
        agent = AnonymizationAgent()
        text = 'Contact me at foo@example.com'
        self.assertNotIn('foo@example.com', agent.anonymize(text))

    def test_access_control(self):
        agent = AccessControlAgent('user')
        self.assertTrue(agent.has_access('guest'))
        self.assertFalse(agent.has_access('admin'))

    def test_privacy_preference(self):
        agent = PrivacyProtectionAgent({'opt_in_training': False})
        self.assertFalse(agent.is_training_allowed())

    def test_data_deletion(self):
        agent = DataDeletionAgent()
        agent.store_data('id1', 'data')
        self.assertTrue(agent.delete_data('id1'))
        self.assertFalse(agent.delete_data('id1'))


if __name__ == '__main__':
    unittest.main()
