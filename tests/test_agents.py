import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue
from divine_agents.evolution import evolution_function, transition_res


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

    def test_evolve(self):
        agent = Agent("B")
        state = agent.evolve(1.0)
        self.assertEqual(state, "Jaz")
        state = agent.evolve(2.5)
        self.assertEqual(state, "Enotnost")

    def test_res_phase(self):
        progress = evolution_function(1.0)
        phase = transition_res(progress)
        self.assertTrue(phase.startswith("RES"))


if __name__ == '__main__':
    unittest.main()
