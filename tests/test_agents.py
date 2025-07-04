import unittest
import random
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents import Agent, philosophical_dialogue, Simulation, SpeculativeAgent


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

    def test_simulation_future_state(self):
        random.seed(0)
        agent = Agent("Sim", tension=0.7)
        sim = Simulation()
        state = sim.simulate_future_state(agent)
        self.assertEqual(state, "Jaz")

    def test_speculative_agent(self):
        agent = SpeculativeAgent("Spec")
        text = agent.speculate("resnica je subjektivna")
        self.assertIn("absolutna", text)


if __name__ == '__main__':
    unittest.main()
