import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from divine_agents import (
    Agent,
    compute_differences,
    linear_interpolation,
    quadratic_interpolation,
)


class TestInterpolation(unittest.TestCase):
    def test_compute_differences(self):
        a1 = Agent("A", emotion=0.6, tension=0.4)
        a2 = Agent("B", emotion=0.2, tension=0.5)
        diffs = compute_differences(a1, a2)
        self.assertAlmostEqual(diffs["emotion_diff"], 0.4)
        self.assertAlmostEqual(diffs["tension_diff"], -0.1)

    def test_linear_interpolation(self):
        x = [0, 1]
        y = [0, 2]
        new_x = [0, 0.5, 1]
        result = linear_interpolation(x, y, new_x)
        self.assertEqual(result, [0, 1, 2])

    def test_quadratic_interpolation(self):
        x = [0, 1, 2]
        y = [0, 1, 4]
        new_x = [1.5]
        result = quadratic_interpolation(x, y, new_x)
        self.assertAlmostEqual(result[0], 2.25)


if __name__ == "__main__":
    unittest.main()
