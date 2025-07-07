import unittest
from divine_agents import Agent, Simulation


class TestSimulation(unittest.TestCase):
    def test_simulation_results(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        sim = Simulation(a1, a2, rounds=2)
        lines = sim.run()
        self.assertGreater(len(lines), 0)
        self.assertEqual(a1.state, "Enotnost")
        self.assertEqual(a2.state, "Enotnost")
        self.assertTrue(any("Enotnost" in line for line in lines))


if __name__ == '__main__':
    unittest.main()
