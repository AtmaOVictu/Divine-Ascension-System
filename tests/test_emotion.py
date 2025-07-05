import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from divine_agents.emotion_transformer import EmotionTransformer
from divine_agents.agent import Agent


class TestEmotionTransformer(unittest.TestCase):
    def test_positive_transformation(self):
        transformer = EmotionTransformer(0.5)
        result = transformer.transform_positive()
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 1)

    def test_negative_transformation(self):
        transformer = EmotionTransformer(-0.5)
        result = transformer.transform_negative()
        self.assertLessEqual(result, 0)
        self.assertGreaterEqual(result, -1)

    def test_agent_mutate_updates_tension(self):
        agent = Agent("A", tension=0.0, emotion=0.5)
        mutated = agent.mutate_emotion()
        self.assertEqual(agent.emotion, mutated)
        self.assertAlmostEqual(agent.tension, 0.0 + mutated)


if __name__ == '__main__':
    unittest.main()
