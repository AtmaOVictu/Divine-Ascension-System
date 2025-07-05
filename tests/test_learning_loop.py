import unittest
from divine_agents.test_loop import LearningTestLoop


class TestLearningTestLoop(unittest.TestCase):
    def test_loop_adds_versions(self):
        versions = ['v1', 'v2']
        loop = LearningTestLoop(versions)
        loop.loop(iterations=1)
        self.assertGreater(len(loop.versions), 2)

    def test_evaluate_returns_best(self):
        versions = ['v1', 'v2']
        loop = LearningTestLoop(versions)
        loop.run_test('v1')
        loop.run_test('v2')
        best_version, score = loop.evaluate()
        self.assertIn(best_version, versions)
        self.assertIsInstance(score, float)


if __name__ == '__main__':
    unittest.main()
