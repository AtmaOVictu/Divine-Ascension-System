import unittest
import math

from divine_agents import DynamicAgent, logistic_function, logarithmic_function


class TestDynamicAgent(unittest.TestCase):
    def test_functions(self):
        self.assertAlmostEqual(logistic_function(0.5, 1.0, 0.5), 0.5, places=2)
        self.assertAlmostEqual(
            logarithmic_function(1.0, 1.0, 1.0),
            math.log(2.0),
            places=5,
        )

    def test_evolve_and_transition(self):
        agent = DynamicAgent("DA", emotion_type="positive")
        agent.update_emotion(0.8)
        agent.evolve()
        state = agent.transition()
        self.assertIn(state, ["Jaz", "Enotnost"])

    def test_emotion_types(self):
        pos_agent = DynamicAgent("pos", emotion_type="positive")
        neg_agent = DynamicAgent("neg", emotion_type="negative")
        neu_agent = DynamicAgent("neu")
        pos_agent.update_emotion(0.4)
        neg_agent.update_emotion(0.4)
        neu_agent.update_emotion(0.4)
        self.assertGreater(pos_agent.tension, neu_agent.tension)
        self.assertLess(neg_agent.tension, pos_agent.tension)


if __name__ == "__main__":
    unittest.main()
