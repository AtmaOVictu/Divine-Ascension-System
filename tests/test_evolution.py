import unittest
from divine_agents.evolution import biological_transition, social_transition, EvolvingAgent


class TestEvolution(unittest.TestCase):
    def test_transition_functions_bounds(self):
        self.assertGreaterEqual(biological_transition(0.0, 1.0, 0.5), 0.0)
        self.assertLessEqual(biological_transition(0.0, 1.0, 0.5), 1.0)
        self.assertGreaterEqual(social_transition(0.0, 1.0, 0.5), 0.0)
        self.assertLessEqual(social_transition(0.0, 1.0, 0.5), 1.0)

    def test_agent_evolution(self):
        agent = EvolvingAgent("tester")
        initial_state = agent.get_state()
        agent.evolve()
        evolved_state = agent.get_state()
        self.assertNotEqual(initial_state, evolved_state)


if __name__ == "__main__":
    unittest.main()
