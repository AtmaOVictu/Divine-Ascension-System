import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.feel("fear", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses_include_emotion(self):
        agent = Agent("C", state="Enotnost", emotion_label="joy")
        agent.emotion = 0.6
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("joy", reply)
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # At least one agent should transition
        self.assertTrue(any("Jaz" in line or "Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

