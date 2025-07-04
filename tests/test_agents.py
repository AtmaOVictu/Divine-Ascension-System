import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.evolve import evolve_to_unity


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
        lines = philosophical_dialogue(a1, a2, rounds=3)
        self.assertTrue(any("prehaja" in line for line in lines))

    def test_evolve_to_unity(self):
        agent = Agent("B")
        evolve_to_unity(agent)
        self.assertEqual(agent.state, "Enotnost")


if __name__ == '__main__':
    unittest.main()
