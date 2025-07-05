import unittest

from divine_agents.dynamic import (
    DynamicAgent,
    MultiAgentSystem,
    biological_transition,
    social_transition,
)


class TestDynamicFunctions(unittest.TestCase):
    def test_logistic_functions(self):
        self.assertGreater(biological_transition(1.0, 1.0, 0.5), 0)
        self.assertLessEqual(biological_transition(1.0, 1.0, 0.5), 1)
        self.assertGreater(social_transition(1.0, 1.0, 0.5), 0)
        self.assertLessEqual(social_transition(1.0, 1.0, 0.5), 1)


class TestDynamicAgent(unittest.TestCase):
    def test_dynamic_transition(self):
        agent = DynamicAgent("D")
        agent.update_emotion(0.8)
        agent.evolve()
        self.assertEqual(agent.state, "Jaz")


class TestMultiAgentSystem(unittest.TestCase):
    def test_system_evolution(self):
        system = MultiAgentSystem(num_agents=2)
        emotions = [0.9, 0.1]
        shadows = [0.0, 0.0]
        system.update_agents_emotion(emotions, shadows)
        system.evolve_agents()
        states = [agent.state for agent in system.agents]
        self.assertIn("Jaz", states)


if __name__ == "__main__":
    unittest.main()
