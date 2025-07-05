import unittest
from divine_agents import SimulationAgent, ModularUnit, RealitySystem


class TestRealitySystem(unittest.TestCase):
    def test_unit_connections(self):
        u1 = ModularUnit("Unit1")
        u2 = ModularUnit("Unit2")
        u1.connect_unit(u2)
        self.assertIn(u2, u1.connected_units)

    def test_system_simulation(self):
        system = RealitySystem()
        a1 = SimulationAgent("A1")
        system.add_agent(a1)
        u1 = ModularUnit("Unit1")
        system.add_unit(u1)
        lines = system.simulate()
        self.assertIn("A1's new state", lines[1])
        self.assertTrue(any("activated" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
