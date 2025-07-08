import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import DialogueManager


class TestMonologue(unittest.TestCase):
    def test_agent_monologue_transition(self):
        agent = Agent("Solo")
        manager = DialogueManager(agent)
        questions = ["Kaj je resnica?", "Kaj se naucim?"]
        emotions = [0.6, 0.6]
        lines = manager.monologue(agent, questions, emotions)

        self.assertIn("absolutna", lines[0])
        self.assertIn("relativna", lines[1])
        self.assertEqual(agent.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
