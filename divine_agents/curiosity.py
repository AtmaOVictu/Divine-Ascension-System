"""Curiosity module modeling multi-dimensional exploration."""
from .agent import Agent

class CuriousAgent(Agent):
    """Agent that explores different dimensions while transitioning states."""
    DIMENSIONS = ["fizična", "psihološka", "ontološka", "filozofska"]

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.phase = 0

    def explore(self) -> str:
        """Advance through a dimension and potentially transition state."""
        dimension = self.DIMENSIONS[self.phase]
        self.update_emotion(0.3)
        new_state = self.transition()
        self.phase = (self.phase + 1) % len(self.DIMENSIONS)
        return f"Raziskujem {dimension} dimenzijo, stanje: {new_state}"
