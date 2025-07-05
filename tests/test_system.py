import unittest

from divine_agents import Agent, MultiAgentSystem, logistic


class TestMultiAgentSystem(unittest.TestCase):
    def test_logistic_transition(self):
        self.assertAlmostEqual(logistic(0, k=1.0, c=0.5), logistic(0))
        value = logistic(1, k=10, c=0.1)
        self.assertGreater(value, 0.5)

    def test_system_evolution(self):
        a1 = Agent("A1")
        a2 = Agent("A2", state="Jaz")
        system = MultiAgentSystem([a1, a2])
        system.evolve(t=1.0, k_emotion=10, c_emotion=0.1)
        states = system.get_states()
        self.assertEqual(states[0], "Jaz")
        self.assertEqual(states[1], "Enotnost")


if __name__ == "__main__":
    unittest.main()
