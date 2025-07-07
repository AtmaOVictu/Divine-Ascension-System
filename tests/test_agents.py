import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import (
    Agent,
    MembershipAgent,
    InterpretiveAgent,
)
from divine_agents.dialogue import philosophical_dialogue, dynamic_dialogue


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

    def test_membership_transition(self):
        a1 = MembershipAgent("M1")
        a2 = MembershipAgent("M2", group="G2")
        a1.update_tension(0.9)
        a1.ionize_environment(a2)
        state = a1.transition()
        self.assertEqual(state, "Jaz")
        self.assertEqual(a1.group, "G2")

    def test_interpretive_dialogue(self):
        a1 = MembershipAgent("M1")
        a2 = InterpretiveAgent("I1", state="Jaz")
        lines = dynamic_dialogue(a1, a2)
        self.assertTrue(any("interpretira" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
