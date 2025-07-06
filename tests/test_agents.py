import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent, GradualAgent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = GradualAgent("A1")
        a2 = GradualAgent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Jaz" in line for line in lines))
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_emotion_trigger(self):
        agent = GradualAgent("T")
        agent.update_emotion("anger", 0.8)
        self.assertEqual(agent.state, "Jaz")

    def test_gradual_transition(self):
        agent = GradualAgent("T")
        agent.update_emotion("joy", 0.6)
        self.assertEqual(agent.state, "Jaz")
        agent.update_emotion("anger", 0.6)
        self.assertEqual(agent.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
