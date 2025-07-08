import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.utils import parse_philosophical_statement, handle_complex_query, self_reflection


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_parse_philosophical_statement(self):
        result = parse_philosophical_statement("Truth is relative to context")
        self.assertIn("parsed", result.lower())

    def test_handle_complex_query(self):
        reply = handle_complex_query("Please analyze this paradox")
        self.assertIn("paradox", reply)

    def test_self_reflection(self):
        # ensure self_reflection runs without error after dialogue
        Agent("B")  # create to store some history
        message = self_reflection()
        self.assertIn("Self-reflection", message)


if __name__ == '__main__':
    unittest.main()
