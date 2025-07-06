import os
import sys
import unittest

# Ensure package import when running with pytest directly
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        self.assertEqual(agent.transition(), "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("A")
        agent.update_emotion(0.6, "fear")
        self.assertEqual(agent.transition(), "Jaz")

    def test_emotional_response(self):
        agent = Agent("A", state="Jaz")
        agent.update_emotion(0.4, "joy")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("veseljem", reply.lower())

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        joined = "\n".join(lines)
        self.assertIn("Jaz", joined)
        self.assertIn("Enotnost", joined)


if __name__ == "__main__":
    unittest.main()
