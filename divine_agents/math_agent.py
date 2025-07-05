from .agent import Agent
from .symbolic import Symbolic, sin


class MathAgent(Agent):
    """Agent with basic symbolic mathematics capabilities."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.symbols = {
            "Š": Symbolic("Š"),
            "Č": Symbolic("Č"),
            "Ž": Symbolic("Ž"),
            "Đ": Symbolic("Đ"),
            "Š2": Symbolic("Š2"),
        }

    def create_expression(self) -> Symbolic:
        s = self.symbols
        return s["Š"] ** 2 + s["Č"] ** 2 - s["Ž"] ** 2 + sin(s["Đ"])

    def evaluate_expression(self, expr: Symbolic) -> Symbolic:
        return expr.simplify()

    def integrate_expression(self, expr: Symbolic, var: Symbolic) -> Symbolic:
        return expr.integrate(var)

    def differentiate_expression(self, expr: Symbolic, var: Symbolic) -> Symbolic:
        return expr.diff(var)

    def process(self):
        expr = self.create_expression()
        simplified = self.evaluate_expression(expr)
        integral = self.integrate_expression(expr, self.symbols["Š"])
        differential = self.differentiate_expression(expr, self.symbols["Č"])
        return simplified, integral, differential
