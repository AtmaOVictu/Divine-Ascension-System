import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, advanced_dialogue


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

    def test_regulation(self):
        agent = Agent("A", emotion=0.9)
        agent.regulate()
        self.assertLess(agent.emotion, 0.9)

    def test_advanced_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2")
        lines = advanced_dialogue(a1, a2)
        self.assertGreaterEqual(len(lines), 4)


if __name__ == '__main__':
    unittest.main()
