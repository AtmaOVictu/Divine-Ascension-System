import unittest
import os
import sys

# Ensure the package root is on sys.path so imports work when running tests
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, philosophical_debate


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

    def test_emotion_transition(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        new_state = agent.transition()
        self.assertEqual(new_state, "Jaz")

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))

    def test_debate_rounds(self):
        a1 = Agent("X")
        a2 = Agent("Y", state="Jaz")
        philosophical_debate(a1, a2, rounds=2)
        # After multiple rounds both agents should progress to the highest state
        self.assertEqual(a1.state, "Enotnost")
        self.assertEqual(a2.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
