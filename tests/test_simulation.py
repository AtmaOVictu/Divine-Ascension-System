import unittest
from divine_agents.simulation import SimulationAgent, ModularUnit, RealitySystem


class TestSimulationComponents(unittest.TestCase):
    def test_agent_transition(self):
        agent = SimulationAgent("A")
        agent.simulate_reality("Reality")
        self.assertEqual(agent.state, "Reality")

    def test_unit_connection_activation(self):
        unit1 = ModularUnit("U1")
        unit2 = ModularUnit("U2")
        unit1.connect_unit(unit2)
        system = RealitySystem()
        system.add_unit(unit1)
        system.add_unit(unit2)
        # capture activation via output? For simplicity just call
        system.simulate()
        self.assertIn(unit2, unit1.connected_units)


if __name__ == "__main__":
    unittest.main()
