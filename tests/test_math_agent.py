import unittest
import sympy as sp
from divine_agents.math_agent import MathAgent

class TestMathAgent(unittest.TestCase):
    def setUp(self):
        self.agent = MathAgent("M")

    def test_integral(self):
        expr = self.agent.expression()
        integral = self.agent.integrate_expression()
        expected = sp.integrate(expr, self.agent.Š)
        self.assertEqual(integral, expected)

    def test_derivative(self):
        expr = self.agent.expression()
        derivative = self.agent.differentiate_expression()
        expected = sp.diff(expr, self.agent.Č)
        self.assertEqual(derivative, expected)

if __name__ == '__main__':
    unittest.main()

