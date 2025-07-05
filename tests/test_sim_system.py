import unittest
from divine_agents.sim_system import SimulationAgent, ModularUnit, RealitySystem


class TestSimulationAgent(unittest.TestCase):
    def test_simulate_reality_transition(self):
        agent = SimulationAgent("Sim")
        agent.update_emotion(0.8)
        state = agent.transition()
        self.assertEqual(state, "Jaz")


class TestRealitySystem(unittest.TestCase):
    def test_system_simulation(self):
        system = RealitySystem()
        agent = SimulationAgent("A1")
        unit1 = ModularUnit("U1")
        unit2 = ModularUnit("U2")
        unit1.connect_unit(unit2)
        system.add_agent(agent)
        system.add_unit(unit1)
        lines = system.simulate()
        self.assertTrue(any("activated" in line for line in lines))
        self.assertIn(agent.state, ("Jaz", "Enotnost"))


if __name__ == "__main__":
    unittest.main()
