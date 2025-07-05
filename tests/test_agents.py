import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

    def test_emotion_in_response(self):
        agent = Agent("B", emotion_type="fear")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("fear", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dialogue_state_change(self):
        a1 = Agent("C1")
        a2 = Agent("C2")
        lines = philosophical_dialogue(a1, a2)
        self.assertNotEqual(a1.state, "Ego")


if __name__ == '__main__':
    unittest.main()
