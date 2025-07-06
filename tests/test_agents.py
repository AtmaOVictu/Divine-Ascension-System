import unittest
import os
import sys

# Ensure package is importable when tests are executed directly
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.update_emotion(0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("eno", reply)

    def test_emotional_response(self):
        agent = Agent("C")
        agent.update_emotion(0.7)
        agent.transition()
        reply = agent.respond("Kaj je resnica?")
        self.assertTrue(reply.startswith("Z močnimi čustvi"))

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        # After the dialogue at least one agent should reach Enotnost
        self.assertTrue(any("Enotnost" in line for line in lines))
        # Dialogue should contain emotional prefix when emotions are high
        self.assertTrue(any(line.startswith("A2") and "Z močnimi" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
