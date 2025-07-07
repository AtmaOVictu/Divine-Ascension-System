import os
import sys
import unittest

# Ensure the project root is on the path so "divine_agents" can be imported
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

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

    def test_emotion_prefix(self):
        agent = Agent("B", emotion_type="fear")
        agent.update_emotion(0.6)
        response = agent.respond("Kaj je resnica?")
        self.assertIn("fear", response)

    def test_transition_by_emotion(self):
        agent = Agent("C")
        agent.update_emotion(0.6)
        new_state = agent.transition()
        self.assertEqual(new_state, "Jaz")


if __name__ == '__main__':
    unittest.main()
