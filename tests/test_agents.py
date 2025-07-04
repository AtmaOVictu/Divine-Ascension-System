import unittest
import os
import sys

# Ensure package is importable when tests are run from any location
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Ego")
        self.assertIn("absolutna", agent.respond("Kaj je resnica?"))

        agent.state = "Jaz"
        self.assertIn("relativna", agent.respond("Kaj je resnica?"))

        agent.state = "Enotnost"
        self.assertIn("eno", agent.respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("absolutna" in line or "relativna" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

