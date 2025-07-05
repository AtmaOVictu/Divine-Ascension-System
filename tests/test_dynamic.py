import unittest
from divine_agents.dynamic import DynamicAgent, MultiAgentSystem, biological_transition


class TestDynamicAgent(unittest.TestCase):
    def test_logistic_range(self):
        value = biological_transition(0.5, 1.0, 0.5)
        self.assertGreaterEqual(value, 0)
        self.assertLessEqual(value, 1)

    def test_agent_evolution(self):
        agent = DynamicAgent(1)
        agent.update_emotion(0.8)
        agent.evolve()
        self.assertIn(agent.state, agent.STATES)
        self.assertNotEqual(agent.state, "Ego")


class TestMultiAgentSystem(unittest.TestCase):
    def test_system_step(self):
        system = MultiAgentSystem(num_agents=2)
        system.step([0.9, 0.6], [0.0, 0.0])
        states = system.states()
        self.assertEqual(len(states), 2)
        self.assertTrue(any(s[2] != "Ego" for s in states))


if __name__ == "__main__":
    unittest.main()
