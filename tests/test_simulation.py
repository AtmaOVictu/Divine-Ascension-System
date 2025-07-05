import unittest
from divine_agents.simulation import OntologicalAgent, simulate


class TestSimulation(unittest.TestCase):
    def test_simulation_transitions(self):
        agent = OntologicalAgent("Sim")
        tensions, emotions = simulate(agent, steps=5)
        # agent should reach at least state Jaz during simulation
        self.assertIn("Jaz", agent.history)
        self.assertTrue(len(agent.history) >= 2)
        # final state expected to be Enotnost
        self.assertEqual(agent.state, "Enotnost")
        self.assertEqual(len(tensions), 5)
        self.assertEqual(len(emotions), 5)


if __name__ == "__main__":
    unittest.main()
