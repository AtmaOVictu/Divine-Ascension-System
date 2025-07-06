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

    def test_transition_by_emotion(self):
        agent = Agent("A")
        agent.update_emotion(0.6, "fear")
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Jaz", emotion_kind="joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("relativna", reply)
        self.assertIn("vesel", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # Agent1 should transition to Jaz due to emotion update
        self.assertEqual(a1.state, "Jaz")
        self.assertTrue(any("prestrašen" in line or "vesel" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
