import unittest
from divine_agents.agent import Agent
from divine_agents.learning import tension_decay, continuous_learning_cycle


class TestLearningUtilities(unittest.TestCase):
    def test_tension_decay(self):
        self.assertLess(tension_decay(1.0, 0.3, 1.0), 1.0)

    def test_continuous_cycle_transition(self):
        a1 = Agent('A1')
        a2 = Agent('A2')
        tension = 1.0
        for _ in range(2):
            a1, a2, tension = continuous_learning_cycle(a1, a2, tension, 1.0)
        self.assertIn(a1.state, Agent.STATES)
        self.assertIn(a2.state, Agent.STATES)


if __name__ == '__main__':
    unittest.main()

