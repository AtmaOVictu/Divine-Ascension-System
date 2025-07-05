import sympy as sp
from .agent import Agent

class MathAgent(Agent):
    """Agent with symbolic mathematics capabilities using special characters."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        # Define special symbols
        self.Š, self.Č, self.Ž, self.Đ = sp.symbols('Š Č Ž Đ')

    def expression(self):
        """Return a sample symbolic expression using special symbols."""
        return self.Š**2 + self.Č**2 - self.Ž**2 + sp.sin(self.Đ)

    def integrate_expression(self):
        """Integrate the expression with respect to Š."""
        return sp.integrate(self.expression(), self.Š)

    def differentiate_expression(self):
        """Differentiate the expression with respect to Č."""
        return sp.diff(self.expression(), self.Č)

