import unittest
from divine_agents.advanced_agent import AdvancedAgent, logistic_function, logarithmic_function


class TestAdvancedAgent(unittest.TestCase):
    def test_logistic_function(self):
        self.assertAlmostEqual(logistic_function(0.0, 1.0, 0.0), 0.5, places=2)

    def test_emotion_update_negative(self):
        agent = AdvancedAgent("A", emotion_type="negative")
        agent.update_emotion(0.8)
        self.assertLess(agent.tension, 0)

    def test_evolve_and_transition(self):
        agent = AdvancedAgent("B", emotion_type="positive")
        agent.update_emotion(1.0)
        agent.evolve()
        self.assertEqual(agent.state, "Jaz")


if __name__ == "__main__":
    unittest.main()
