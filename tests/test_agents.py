import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


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

    def test_emotional_response(self):
        agent = Agent("B", emotion=0.6)
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("čustva", reply.lower())

    def test_unity_loading(self):
        agent = Agent("C")
        for _ in range(120):
            agent.update_unity(0.05)
        self.assertAlmostEqual(agent.unity_progress, 0.01, places=2)


if __name__ == '__main__':
    unittest.main()
