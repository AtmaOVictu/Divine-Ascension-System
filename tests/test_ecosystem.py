import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.agent import Agent
from divine_agents.ecosystem import simulate_ecosystem


class TestEcosystem(unittest.TestCase):
    def test_simulation_shapes(self):
        agents = [Agent("A"), Agent("B", state="Jaz")]
        energy, tension, states = simulate_ecosystem(agents, steps=3)
        self.assertEqual(len(energy), 3)
        self.assertEqual(len(tension), 3)
        self.assertEqual(len(energy[0]), 2)
        self.assertEqual(len(states), 3)

    def test_emotional_transition(self):
        agent = Agent("X")
        agent.apply_emotion("fear", 0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")
        self.assertEqual(agent.emotion_label, "fear")


if __name__ == "__main__":
    unittest.main()
