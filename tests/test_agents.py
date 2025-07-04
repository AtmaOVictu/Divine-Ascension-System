import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dialogue_custom_increment(self):
        a1 = Agent("B1")
        a2 = Agent("B2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, inc1=0.4, inc2=0.3)
        # With increments below thresholds, states should not change
        self.assertFalse(any("Enotnost" in line for line in lines))
        self.assertEqual(a1.state, "Ego")
        self.assertEqual(a2.state, "Jaz")


if __name__ == '__main__':
    unittest.main()
