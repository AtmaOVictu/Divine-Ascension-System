import os
import sys
import unittest

# Ensure the package root is on the path so tests can be executed directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.godbook import Godbook, ParadoxicalAgent


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

    def test_godbook_logging(self):
        godbook = Godbook()
        agent = ParadoxicalAgent("P", godbook=godbook)
        agent.update_emotion(0.8)
        agent.transition()
        self.assertEqual(len(godbook.entries), 1)

    def test_paradoxical_response(self):
        agent = ParadoxicalAgent("P", state="Enotnost")
        reply = agent.ask_paradox()
        self.assertIn("Vse resnice so enotne", reply)


if __name__ == '__main__':
    unittest.main()
