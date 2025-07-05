import random
import unittest
from divine_agents.test_loop import TestSuite

class TestLearningLoop(unittest.TestCase):
    def test_versions_expand(self):
        rng = random.Random(0)
        suite = TestSuite(['v1', 'v2'], rng=rng)
        suite.loop_tests(iterations=2)
        # initial versions + one new version per iteration
        self.assertEqual(len(suite.test_versions), 4)
        # at least one improved version should exist
        self.assertTrue(any(v.endswith('_Improved') for v in suite.test_versions))

if __name__ == '__main__':
    unittest.main()
