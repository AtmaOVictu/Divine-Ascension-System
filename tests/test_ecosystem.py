import unittest
from divine_agents import Agent, Ecosystem


class TestEcosystem(unittest.TestCase):
    def test_run_shape(self):
        agents = [Agent("A"), Agent("B")]
        eco = Ecosystem(agents)
        energy, voltage = eco.run(steps=5)
        self.assertEqual(len(energy), 5)
        self.assertEqual(len(voltage), 5)
        self.assertEqual(len(energy[0]), 2)
        self.assertEqual(len(voltage[0]), 2)

    def test_state_progression(self):
        agents = [Agent("A"), Agent("B", state="Jaz")]
        eco = Ecosystem(agents)
        eco.run(steps=5)
        states = [agent.state for agent in agents]
        self.assertTrue(any(state in ("Jaz", "Enotnost") for state in states))


if __name__ == '__main__':
    unittest.main()
