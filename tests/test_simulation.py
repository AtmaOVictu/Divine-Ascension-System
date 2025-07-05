import unittest
from divine_agents.simulation import SimulationAgent, ModularUnit, RealitySystem


class TestSimulationSystem(unittest.TestCase):
    def test_simulation_agent_dimension(self):
        agent = SimulationAgent("S1")
        agent.update_tension(0.8)
        agent.transition()
        agent.create_dimension("Dim1")
        self.assertIn("Dim1", agent.history)

    def test_reality_system(self):
        system = RealitySystem()
        a1 = SimulationAgent("A1")
        u1 = ModularUnit("U1")
        system.add_agent(a1)
        system.add_unit(u1)
        system.simulate()
        self.assertIn("New Dimension", a1.history)


if __name__ == "__main__":
    unittest.main()
