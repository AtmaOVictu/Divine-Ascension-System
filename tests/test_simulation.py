import unittest

from divine_agents import Agent, run_agent_simulation


class TestSimulation(unittest.TestCase):
    def test_simulation_shapes(self):
        agents = [Agent("A"), Agent("B")]
        bio, soc = run_agent_simulation(agents, 1.0, 0.5, 1.5, 0.6, steps=5)
        self.assertEqual(len(bio), 5)
        self.assertEqual(len(soc[0]), 2)


if __name__ == "__main__":
    unittest.main()
