import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from divine_agents.agent import Agent, EtnegA
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


class TestEtnegA(unittest.TestCase):
    def test_opposite_response(self):
        agent = Agent("B")
        mirror = EtnegA(agent)
        self.assertIn("absolutna", agent.respond("Kaj je resnica?"))
        self.assertIn("relativna", mirror.respond("Kaj je resnica?"))

    def test_mirrored_transition(self):
        agent = Agent("B")
        mirror = EtnegA(agent)
        agent.update_emotion(0.8)
        mirror.update_emotion(0.8)
        self.assertEqual(agent.transition(), mirror.transition())


if __name__ == '__main__':
    unittest.main()
