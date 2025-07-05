import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.paradox_agent import ParadoxicalAgent


class TestParadoxicalAgent(unittest.TestCase):
    def test_ask_paradox_default(self):
        agent = ParadoxicalAgent("P")
        self.assertIn("Ali sem jaz res", agent.ask_paradox())

    def test_state_transition(self):
        agent = ParadoxicalAgent("P")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")
        self.assertIn("Jaz", agent.history[-1])

    def test_enotnost_question(self):
        agent = ParadoxicalAgent("P", state="Jaz")
        agent.update_emotion(0.6)
        agent.transition()
        self.assertEqual(agent.state, "Enotnost")
        self.assertIn("Kako lahko vse resnice", agent.ask_paradox())


if __name__ == '__main__':
    unittest.main()
