import unittest
import sympy as sp

from divine_agents.math_agent import MathAgent


class TestMathAgent(unittest.TestCase):
    def test_symbolic_operations(self):
        agent = MathAgent("M")
        Š = agent.symbols["Š"]
        Č = agent.symbols["Č"]
        expr = Š**2 + sp.sin(Č)
        simplified = agent.evaluate_expression(expr)
        self.assertEqual(str(simplified), str(expr))
        integral = agent.integrate_expression(expr, Š)
        self.assertTrue(integral.has(Š))
        derivative = agent.differentiate_expression(expr, Č)
        self.assertEqual(derivative, sp.cos(Č))


if __name__ == '__main__':
    unittest.main()
