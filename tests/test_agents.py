import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
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

    def test_no_transition_below_threshold(self):
        agent = Agent("B")
        agent.update_tension(0.5)
        agent.update_emotion(0.2)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_emotion_triggers_transition(self):
        agent = Agent("C")
        agent.update_emotion(0.6)
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

    def test_o_state_potential(self):
        agent = Agent("X", state="O")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Ego")


if __name__ == '__main__':
    unittest.main()
