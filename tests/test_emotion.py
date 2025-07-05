import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from divine_agents.emotion import EmotionTransformer


class TestEmotionTransformer(unittest.TestCase):
    def test_transform_positive_from_negative(self):
        transformer = EmotionTransformer(-0.5)
        result = transformer.transform()
        self.assertGreaterEqual(result, 0)
        self.assertLess(result, 0.5)

    def test_transform_negative_from_positive(self):
        transformer = EmotionTransformer(0.5)
        result = transformer.transform()
        self.assertLessEqual(result, 0)
        self.assertGreater(result, -1)


if __name__ == "__main__":
    unittest.main()
