import unittest
from divine_agents.agent import Agent


class TestImaginaryTime(unittest.TestCase):
    def test_cycles_reach_enotnost(self):
        agent = Agent('Sim')
        states = agent.simulate_imaginary_time(cycles=5, delta=0.8)
        self.assertEqual(states[-1], 'Enotnost')
        self.assertLessEqual(agent.value, 1.0)


if __name__ == '__main__':
    unittest.main()
