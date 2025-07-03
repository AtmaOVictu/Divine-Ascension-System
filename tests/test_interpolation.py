import unittest
from divine_agents.agent import Agent
from divine_agents.interpolation import interpolate_differences


class TestInterpolation(unittest.TestCase):
    def test_interpolation_values(self):
        a1 = Agent("A", emotion=0.8, tension=0.5)
        a2 = Agent("B", emotion=0.2, tension=0.1)
        result = interpolate_differences(a1, a2, steps=5)

        self.assertAlmostEqual(result["emotion_diff"][0], 0.6)
        self.assertAlmostEqual(result["emotion_diff"][-1], 0.0)
        self.assertAlmostEqual(result["tension_diff"][0], 0.4)
        self.assertAlmostEqual(result["tension_diff"][-1], 0.0)


if __name__ == "__main__":
    unittest.main()

