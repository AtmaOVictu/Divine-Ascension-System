import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(2.0)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_triggered_transition(self):
        agent = Agent("B", state="Jaz")
        agent.update_emotion(0.6)
        new_state = agent.transition()
        self.assertEqual(new_state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # Ensure emotional tone is reflected
        self.assertTrue(any("Strastno".lower() in line.lower() or "Mirno".lower() in line.lower() for line in lines))


if __name__ == '__main__':
    unittest.main()
