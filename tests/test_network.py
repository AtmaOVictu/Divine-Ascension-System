import unittest
from unittest.mock import patch
from divine_agents.agent import Agent


class TestNetworkIntegration(unittest.TestCase):
    def test_sync_with(self):
        a1 = Agent("A1", tension=0.6, emotion=0.6)
        a2 = Agent("A2", tension=0.2, emotion=0.2)
        a1.connect()
        a2.connect()
        success = a1.sync_with(a2)
        self.assertTrue(success)
        self.assertAlmostEqual(a1.tension, 0.4)
        self.assertAlmostEqual(a2.tension, 0.4)
        self.assertAlmostEqual(a1.emotion, 0.4)
        self.assertAlmostEqual(a2.emotion, 0.4)

    @patch('subprocess.run')
    def test_commit_to_github(self, mock_run):
        a = Agent("A")
        a.commit_to_github("test")
        self.assertTrue(mock_run.called)


if __name__ == '__main__':
    unittest.main()
