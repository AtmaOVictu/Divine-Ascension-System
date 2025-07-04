import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, interactive_debate


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

    def test_interactive_debate(self):
        a1 = Agent("Debater1")
        a2 = Agent("Debater2", state="Jaz")
        transcript = interactive_debate(a1, a2, rounds=2)
        self.assertTrue(a1.state in Agent.STATES)
        self.assertTrue(a2.state in Agent.STATES)
        self.assertTrue(len(transcript) > 0)


if __name__ == '__main__':
    unittest.main()
