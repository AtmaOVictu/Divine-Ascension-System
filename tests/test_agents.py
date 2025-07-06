import os
import sys
import unittest

# Ensure package root is on the path when tests are executed directly
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.debate import ontological_debate


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

    def test_debate_triggers_enotnost(self):
        a1 = Agent("Debater1")
        a2 = Agent("Debater2", state="Jaz")
        transcript = ontological_debate(a1, a2, rounds=3)
        # At least one agent should reach Enotnost after debate
        self.assertIn("Enotnost", [a1.state, a2.state])
        # Ensure transcript captured state transitions
        self.assertTrue(any("preide" in line or "preide" in line.lower() for line in transcript))


if __name__ == '__main__':
    unittest.main()
