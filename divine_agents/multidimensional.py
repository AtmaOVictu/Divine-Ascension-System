from typing import List
from .agent import Agent


class MultidimensionalAgent(Agent):
    """Agent operating across multiple dimensions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.dimensions = ["Fizicna", "Custvena", "Mentalna"]

    def act_across_dimensions(self) -> List[str]:
        """Return actions across all dimensions."""
        return [f"Agent {self.name} deluje v dimenziji: {d}" for d in self.dimensions]
