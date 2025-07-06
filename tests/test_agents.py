import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_on_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

    def test_transition_on_emotion(self):
        agent = Agent("B")
        agent.apply_emotion(0.6)
        self.assertEqual(agent.transition(), "Jaz")

    def test_no_transition_below_threshold(self):
        agent = Agent("C")
        agent.update_tension(0.6)
        agent.emotion = 0.4
        self.assertEqual(agent.transition(), "Ego")

    def test_responses(self):
        self.assertIn("absolutna", Agent("A", state="Ego").respond("Kaj je resnica?"))
        self.assertIn("relativna", Agent("B", state="Jaz").respond("Kaj je resnica?"))
        self.assertIn("eno", Agent("C", state="Enotnost").respond("Kaj je resnica?"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # ensure transitions occurred and final state lines present
        self.assertTrue(any("prehaja v stanje" in line for line in lines))
        self.assertIn("Enotnost", "".join(lines))


if __name__ == '__main__':
    unittest.main()
