import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_no_transition_below_threshold(self):
        agent = Agent("A")
        agent.update_tension(0.2)
        agent.update_emotion(0.1)
        state = agent.transition()
        self.assertEqual(state, "Ego")

    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)
        self.assertIn("čustvo", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        # ensure emotional information is present in replies
        dialogue_lines = [l for l in lines if "Kaj je resnica?" in l]
        self.assertTrue(all("čustvo" in l for l in dialogue_lines))


if __name__ == '__main__':
    unittest.main()
