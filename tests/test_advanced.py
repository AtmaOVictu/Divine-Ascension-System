import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.advanced import SelfRegulation, EmotionalDynamics
from divine_agents.agent import MultiDimensionalAgent


class TestAdvancedComponents(unittest.TestCase):
    def test_self_regulation_high_tension(self):
        reg = SelfRegulation(energy=1.0, tension=0.9)
        reg.adjust()
        self.assertAlmostEqual(reg.energy, 0.5)

    def test_multidimensional_agent_movement(self):
        agent = MultiDimensionalAgent("B")
        dim = agent.move_dimension()
        self.assertEqual(dim, 2)

    def test_emotional_warning(self):
        emo = EmotionalDynamics("tesnoba")
        self.assertIn("Etika", emo.ethical_warning())


if __name__ == '__main__':
    unittest.main()
