import unittest

from divine_agents.agent import Agent
from divine_agents.simulation import ImaginaryTimeSimulation


class TestImaginaryTimeSimulation(unittest.TestCase):
    def test_simulation_reaches_enotnost(self):
        agent = Agent("Sim")
        sim = ImaginaryTimeSimulation(agent)
        sim.run(cycles=8)
        self.assertEqual(agent.state, "Enotnost")
        self.assertEqual(len(sim.history), 8)


if __name__ == "__main__":
    unittest.main()
