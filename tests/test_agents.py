import os
import sys
import unittest

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
        # After transitions, final responses should match their new states
        self.assertIn("relativna", lines[-2])
        self.assertIn("eno", lines[-1])

    def test_transition_jaz_to_enotnost(self):
        agent = Agent("B", state="Jaz")
        agent.update_tension(0.9)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_no_transition_when_below_thresholds(self):
        agent = Agent("C")
        agent.update_tension(0.4)
        agent.update_emotion(0.3)
        state = agent.transition()
        self.assertEqual(state, "Ego")


if __name__ == '__main__':
    unittest.main()
