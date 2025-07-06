import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, dynamic_debate


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

    def test_dynamic_debate(self):
        a1 = Agent("Debater1")
        a2 = Agent("Debater2", state="Jaz")
        steps1 = [("anger", 0.6), ("joy", 0.2)]
        steps2 = [("fear", 0.4), ("anger", 0.8)]
        transcript = dynamic_debate(a1, a2, steps1, steps2)
        self.assertEqual(a1.state, "Enotnost")
        self.assertEqual(a2.state, "Enotnost")
        self.assertTrue(any("anger" in line or "fear" in line for line in transcript))


if __name__ == '__main__':
    unittest.main()
