import unittest
from divine_agents.emotion_dimension import EmotionDimensionAgent


class TestEmotionDimensionAgent(unittest.TestCase):
    def test_process_emotion(self):
        agent = EmotionDimensionAgent("Jeza", 80, 3)
        influence = agent.process_emotion()
        self.assertAlmostEqual(influence, 2.4)
        self.assertEqual(agent.senses["touch"], 40.0)
        self.assertEqual(agent.senses["sight"], 32.0)


if __name__ == "__main__":
    unittest.main()
