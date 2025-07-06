import unittest
import os
import sys
from math import isclose

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.math_music import evaluate_expression, generate_scale


class TestMathMusic(unittest.TestCase):
    def test_evaluate_expression(self):
        result = evaluate_expression('sin(pi / 2)')
        self.assertTrue(isclose(result, 1.0, rel_tol=1e-5))

    def test_generate_scale(self):
        scale = generate_scale('C', 3)
        self.assertEqual(scale, ['C', 'D', 'E'])


if __name__ == '__main__':
    unittest.main()
