import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import (
    Agent,
    TRANSITION_EMOTION_THRESHOLD,
    TRANSITION_TENSION_THRESHOLD,
)
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(TRANSITION_TENSION_THRESHOLD + 0.1)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotion_based_transition(self):
        agent = Agent("B")
        agent.update_emotion("fear", TRANSITION_EMOTION_THRESHOLD + 0.1)
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
        # ensure each agent transitioned once
        self.assertEqual(a1.history.count("Jaz"), 1)
        self.assertEqual(a2.history.count("Enotnost"), 1)


if __name__ == '__main__':
    unittest.main()
