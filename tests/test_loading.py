import unittest
from divine_agents.loading import LoadingScreen


class TestLoadingScreen(unittest.TestCase):
    def test_progress_calculation(self):
        times = [0.0]

        def fake_time():
            return times[0]

        screen = LoadingScreen(root=None, time_func=fake_time)
        times[0] = 0.5
        self.assertEqual(screen.get_progress(), 1)
        times[0] = 1.0
        self.assertEqual(screen.get_progress(), 2)
        times[0] = 50.0
        self.assertEqual(screen.get_progress(), 0)


if __name__ == "__main__":
    unittest.main()
