import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import (
    Agent,
    TENSION_THRESHOLD,
    EMOTION_THRESHOLD,
)
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(TENSION_THRESHOLD + 0.1)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_custom_thresholds(self):
        agent = Agent("B", tension_threshold=0.9, emotion_threshold=0.9)
        agent.update_tension(0.8)
        # Should not transition yet
        state = agent.transition()
        self.assertEqual(state, "Ego")

        agent.update_emotion(0.95)
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


if __name__ == '__main__':
    unittest.main()
