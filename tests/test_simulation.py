import unittest
from divine_agents.simulation import SimulationAgent, ModularUnit, RealitySystem


class TestSimulation(unittest.TestCase):
    def test_agent_transition(self):
        agent = SimulationAgent("S1", state="Potential")
        agent.simulate_reality("Actual")
        self.assertEqual(agent.state, "Actual")

    def test_unit_connection_and_activation(self):
        u1 = ModularUnit("U1")
        u2 = ModularUnit("U2")
        u1.connect_unit(u2)
        self.assertIn(u2, u1.connected_units)

    def test_reality_system(self):
        system = RealitySystem()
        agent = SimulationAgent("S2")
        unit = ModularUnit("U3")
        system.add_agent(agent)
        system.add_unit(unit)
        system.simulate()
        self.assertEqual(agent.state, "New Dimension")


if __name__ == '__main__':
    unittest.main()
