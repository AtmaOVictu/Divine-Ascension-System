import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.conversation import dynamic_conversation


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

    def test_dynamic_conversation(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = dynamic_conversation(a1, a2, rounds=2)
        # After conversation at least one agent should have transitioned
        self.assertTrue(a1.state != "Ego" or a2.state != "Jaz")
        # Responses should mention emotion influence
        self.assertTrue(any("Jeza" in line or "veselje" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
