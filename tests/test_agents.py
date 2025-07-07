import os
import sys
import unittest

# Ensure package import works when tests are executed from the tests directory
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost", emotion_name="joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("veseljem", reply)

    def test_emotion_triggered_transition(self):
        agent = Agent("A")
        agent.update_emotion(0.6, "fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, rounds=3)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # ensure emotions influenced transitions
        self.assertIn("prehaja v stanje", " ".join(lines))


if __name__ == '__main__':
    unittest.main()
