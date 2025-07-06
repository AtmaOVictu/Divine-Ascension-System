import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_responses_include_tone(self):
        agent = Agent("C", state="Enotnost", emotion=0.8)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("strastno", reply)
        self.assertIn("eno", reply)

    def test_dialogue_progression(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2, rounds=3)
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
