import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent, EtnegA
from divine_agents.dialogue import philosophical_dialogue, reflective_dialogue


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


class TestEtnegA(unittest.TestCase):
    def test_mirror_response(self):
        agent = Agent("A")
        mirror = EtnegA(agent)
        self.assertIn("relativna", mirror.respond("Kaj je resnica?"))

    def test_reflective_dialogue(self):
        agent = Agent("B")
        lines = reflective_dialogue(agent)
        self.assertEqual(len(lines), 6)


if __name__ == '__main__':
    unittest.main()
