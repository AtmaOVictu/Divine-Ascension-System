import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_debate


class TestAgentTransitions(unittest.TestCase):
    def test_transition_by_tension(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_transition_by_emotion(self):
        agent = Agent("B")
        agent.set_emotion("fear", 0.6)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

    def test_emotional_response(self):
        agent = Agent("A", state="Jaz")
        agent.set_emotion("joy", 0.4)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("relativna", reply)
        self.assertIn("Veselim", reply)

    def test_debate(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_debate(a1, a2)
        self.assertTrue(any("prehaja v stanje" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
