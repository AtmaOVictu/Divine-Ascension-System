import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        state = agent.transition(tension=0.8)
        self.assertEqual(state, "Jaz")

        agent = Agent("B")
        state = agent.transition(tension=0.6, tension_threshold=0.5)
        self.assertEqual(state, "Jaz")

        agent = Agent("C")
        state = agent.transition(emotion=0.4, emotion_threshold=0.3)
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, a1_emotion=0.9, a2_emotion=0.7)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
