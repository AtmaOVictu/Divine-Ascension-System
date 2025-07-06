import os
import sys
import unittest

# Ensure the project root is on sys.path so imports work when tests are run
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, debate


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

    def test_debate_transitions(self):
        """Ensure debate causes agents to change states."""
        a1 = Agent("Debater1")
        a2 = Agent("Debater2")
        log = debate(a1, a2, turns=2)
        # After the debate both agents should have transitioned at least once
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)
        self.assertTrue(any("prehaja v stanje" in line for line in log))


if __name__ == '__main__':
    unittest.main()
