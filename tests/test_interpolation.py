import unittest
from divine_agents import Agent, interpolate_differences


class TestInterpolation(unittest.TestCase):
    def test_interpolate_differences(self):
        a1 = Agent("A1", emotion=0.8, tension=0.3)
        a2 = Agent("A2", emotion=0.2, tension=0.7)
        times = [0, 2.5, 5, 7.5, 10]
        emotion, tension = interpolate_differences(a1, a2, times)
        self.assertEqual(len(emotion), len(times))
        self.assertEqual(len(tension), len(times))
        # check starting difference
        self.assertAlmostEqual(emotion[0], a1.emotion - a2.emotion)
        self.assertAlmostEqual(tension[0], a1.tension - a2.tension)


if __name__ == '__main__':
    unittest.main()
