import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(
            a1,
            a2,
            adjustments=[{"a1_emotion": 0.8, "a2_emotion": 0.6}],
        )
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_dialogue_with_adjustments(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        adjustments = [
            {"a1_emotion": 0.8, "a2_emotion": 0.6},
            {"a1_emotion": 0.9, "a2_emotion": 0.9},
        ]
        philosophical_dialogue(a1, a2, turns=2, adjustments=adjustments)
        self.assertEqual(a1.state, "Enotnost")
        self.assertEqual(a2.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
