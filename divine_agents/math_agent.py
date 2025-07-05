import sympy as sp

from .agent import Agent


class MathAgent(Agent):
    """Agent capable of symbolic mathematics with special characters."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        # Define special symbols used in expressions
        self.symbols = {
            "Š": sp.symbols('Š'),
            "Č": sp.symbols('Č'),
            "Ž": sp.symbols('Ž'),
            "Đ": sp.symbols('Đ'),
        }

    def evaluate_expression(self, expr: sp.Expr) -> sp.Expr:
        """Simplify the given expression."""
        return sp.simplify(expr)

    def integrate_expression(self, expr: sp.Expr, var: sp.Symbol) -> sp.Expr:
        """Compute the integral of an expression with respect to a variable."""
        return sp.integrate(expr, var)

    def differentiate_expression(self, expr: sp.Expr, var: sp.Symbol) -> sp.Expr:
        """Differentiate an expression with respect to a variable."""
        return sp.diff(expr, var)
