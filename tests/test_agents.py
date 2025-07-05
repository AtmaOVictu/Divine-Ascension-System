import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.emotion import logistic


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

    def test_logistic_function(self):
        self.assertAlmostEqual(logistic(0, 1, 0), 0.5, places=2)

    def test_emotion_curve_transition(self):
        agent = Agent("A")
        agent.apply_emotion_curve(t=5, k=1.0, c=0.0)
        state = agent.transition()
        self.assertEqual(state, "Jaz")


if __name__ == '__main__':
    unittest.main()
