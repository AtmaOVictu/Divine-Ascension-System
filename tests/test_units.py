import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.system import ModularUnit, AgentSystem
from divine_agents.agent import Agent


class TestUnits(unittest.TestCase):
    def test_unit_activation(self):
        u1 = ModularUnit("U1")
        u2 = ModularUnit("U2")
        u1.connect_unit(u2)
        self.assertEqual(u1.activate(), ["U1", "U2"])

    def test_system_simulation(self):
        system = AgentSystem()
        a = Agent("A")
        a.update_emotion(0.6, "joy")
        u = ModularUnit("U")
        system.add_agent(a)
        system.add_unit(u)
        result = system.simulate()
        self.assertIn("Jaz", result["transitions"])
        self.assertIn("U", result["activations"])


if __name__ == "__main__":
    unittest.main()
