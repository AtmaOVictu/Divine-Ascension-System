import unittest
from divine_agents.loading import calculate_progress


class TestLoadingScreen(unittest.TestCase):
    def test_calculate_progress(self):
        start = 0.0
        self.assertEqual(calculate_progress(start, 10.0), 10)
        self.assertEqual(calculate_progress(start, 105.0), 5)


if __name__ == "__main__":
    unittest.main()
