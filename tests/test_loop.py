import unittest
from learning_loop import LearningSuite


class TestLearningLoop(unittest.TestCase):
    def test_new_versions_added(self):
        suite = LearningSuite(["v1", "v2"])
        suite.loop_tests(iterations=2)
        # After two iterations there should be at least one improved version
        self.assertTrue(any(v.endswith("_Improved") for v in suite.test_versions))


if __name__ == "__main__":
    unittest.main()
