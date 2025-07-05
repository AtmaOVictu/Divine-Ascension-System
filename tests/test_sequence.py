import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.sequence import LogicalSequenceAgent


class TestLogicalSequenceAgent(unittest.TestCase):
    def test_sequence_transitions(self):
        agent = LogicalSequenceAgent("Seq")
        agent.execute_sequence(tension=0.6, emotion=0.6)
        self.assertEqual(agent.state, "Jaz")
        agent.execute_sequence(tension=0.8, emotion=0.6)
        self.assertEqual(agent.state, "Enotnost")

    def test_perform_action(self):
        agent = LogicalSequenceAgent("Seq")
        agent.execute_sequence(tension=0.7, emotion=0.6)
        response = agent.perform_action()
        self.assertIsInstance(response, str)
        self.assertIn("Resnica", response)


if __name__ == "__main__":
    unittest.main()
