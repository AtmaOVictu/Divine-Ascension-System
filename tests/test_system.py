import unittest

from divine_agents.agent import Agent
from divine_agents.modular_unit import ModularUnit
from divine_agents.system import RealitySystem


class TestRealitySystem(unittest.TestCase):
    def test_unit_activation(self):
        u1 = ModularUnit("U1")
        u2 = ModularUnit("U2")
        u1.connect_unit(u2)
        outputs = u1.activate()
        self.assertIn("U2 activated.", outputs)

    def test_simulate(self):
        system = RealitySystem()
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        system.add_agent(a1)
        system.add_agent(a2)
        unit = ModularUnit("Core")
        system.add_unit(unit)
        lines = system.simulate()
        self.assertTrue(any("activated" in line for line in lines))
        self.assertTrue(any("Enotnost" in line or "Jaz" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
