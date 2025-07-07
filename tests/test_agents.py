import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


class TestAgentTransitions(unittest.TestCase):
    def test_transition_thresholds(self):
        agent = Agent("A")
        agent.update_tension(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")

        agent2 = Agent("B", state="Jaz")
        agent2.update_emotion(0.6, "strah")
        state2 = agent2.transition()
        self.assertEqual(state2, "Enotnost")

    def test_responses(self):
        agent = Agent("A", state="Enotnost")
        agent.update_emotion(0.7, "veselje")
        reply = agent.respond("Kaj je resnica?")
        self.assertIn("veselje", reply.lower())

    def test_dialogue(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        lines = philosophical_dialogue(a1, a2)
        self.assertTrue(any("Enotnost" in line for line in lines))
        self.assertTrue(any("jeza" in line.lower() or "veselje" in line.lower() for line in lines))


if __name__ == '__main__':
    unittest.main()
